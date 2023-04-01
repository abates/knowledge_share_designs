from nautobot.extras.jobs import IntegerVar
from design_builder.base import DesignJob

from .initial_context import InitialDevicesContext


class InitialDevices(DesignJob):
    shard = IntegerVar(label="Device Shard", min_value=0, max_value=9)

    class Meta:
        name = "Initial Devices"
        commit_default = False
        design_file = "templates/initial_devices.yaml.j2"
        context_class = InitialDevicesContext
        soft_time_limit = 3600

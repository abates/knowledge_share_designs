from nautobot.extras.jobs import ChoiceVar
from design_builder.base import DesignJob

from .initial_context import InitialDesignContext, countries


class InitialDesign(DesignJob):
    country = ChoiceVar(label="Country", choices=tuple((iso, country) for iso,country in countries().items()))

    class Meta:
        name = "Initial Data"
        commit_default = False
        design_file = "templates/initial_design.yaml.j2"
        context_class = InitialDesignContext
        soft_time_limit = 3600

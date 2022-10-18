from nautobot.dcim.models import Region, Site

from netaddr import IPNetwork

from design_builder.errors import DesignValidationError
from design_builder.context import Context, context_file


class KSInitialDesignContext(Context):
    """Render context for basic design"""


from design_builder.context import Context, context_file
from design_builder.errors import DesignValidationError
from nautobot.dcim.models import Region, Site
from netaddr import IPNetwork


class KSInitialDesignContext(Context):
    """Render context for basic design"""

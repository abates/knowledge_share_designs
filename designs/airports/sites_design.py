from design_builder.base import DesignJob

from nautobot.dcim.models import Region
from nautobot.extras.jobs import ObjectVar

from .sites_context import SitesContext


class SitesDesign(DesignJob):
    region = ObjectVar(model=Region)

    class Meta:
        name = "Sites Design"
        description = "Pre-populate site data"
        commit_default = True
        design_file = "templates/sites_design.yaml.j2"
        context_class = SitesContext

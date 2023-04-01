from nautobot.tenancy.models import Tenant
from nautobot.extras.jobs import ObjectVar

from design_builder.base import DesignJob

from .initial_context import SitesContext, countries


class SitesDesign(DesignJob):
    tenant = ObjectVar(Tenant)

    class Meta:
        name = "Sites Design"
        commit_default = True
        design_file = "templates/sites_design.yaml.j2"
        context_class = SitesContext
        soft_time_limit = 3600

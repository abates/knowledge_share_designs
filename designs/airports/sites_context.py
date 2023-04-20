from design_builder.context import Context, context_file
from design_builder.errors import DesignValidationError
from nautobot.dcim.models import Region

@context_file("sites_context.yaml")
class SitesContext(Context):
    """Render context for sites"""

    region: Region

    def validate_region(self):
        self.sites = [site for site in self.all_sites.values() if self.region.slug == site["region__slug"]]
        if not self.sites:
            raise DesignValidationError(f"No matching sites for region {self.region.name}")
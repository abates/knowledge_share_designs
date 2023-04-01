from design_builder.context import Context, context_file
from design_builder.errors import DesignValidationError


@context_file("initial_context.yaml")
@context_file("regions_context.yaml")
@context_file("sites_context.yaml")
class SitesContext(Context):
    """Render context for sites"""

    continent: str

    def validate_continent(self):
        try:
            self.regions = self.all_regions[self.continent]
        except KeyError:
            raise DesignValidationError(f"Non-existent region {self.continent}")

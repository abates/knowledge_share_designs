from design_builder.context import Context, context_file
from design_builder.errors import DesignValidationError


@context_file("initial_context.yaml")
@context_file("regions_context.yaml")
class InitialContext(Context):
    """Render context for initial data."""

    continent: str

    def validate_continent(self):
        try:
            self.regions = {self.continent: self.all_regions[self.continent]}
        except KeyError:
            raise DesignValidationError(f"Non-existent region {self.continent}")

from design_builder.context import Context, context_file
from design_builder.errors import DesignValidationError


@context_file("context.yaml")
class DesignContext(Context):
    """Render context for {{ design_name }} design"""

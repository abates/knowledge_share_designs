from design_builder.design_builder import DesignJob

from .context import DesignContext

class BasicDesign(DesignJob):
    class Meta:
        name = "Basic Design"
        commit_default = False
        design_file = "templates/basic_design.yaml.j2"
        context_class = DesignContext
        report = "templates/basic_design_report.md.j2"

from design_builder.design_builder import DesignJob

from .ks_initial_context import KSInitialDesignContext

class KSInitialDesign(DesignJob):
    class Meta:
        name = "Initial Data"
        commit_default = False
        design_file = "templates/ks_initial_design.yaml.j2"
        context_class = KSInitialDesignContext

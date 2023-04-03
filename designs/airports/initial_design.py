from design_builder.base import DesignJob
from nautobot.extras.jobs import ChoiceVar

from .initial_context import InitialContext


class InitialDesign(DesignJob):
    continent = ChoiceVar(
        choices=(
            ("continent-as", "Asia"),
            ("continent-sa", "South America"),
            ("continent-eu", "Europe"),
            ("continent-an", "Antarctica"),
            ("continent-na", "North America"),
            ("continent-oc", "Oceania"),
            ("continent-ac", "Africa"),
        )
    )

    class Meta:
        name = "Initial Design"
        description = "Pre-populate design data including regions for a given continent"
        commit_default = True
        design_file = "templates/initial_design.yaml.j2"
        context_class = InitialContext

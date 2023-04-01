from nautobot.extras.jobs import ChoiceVar

from design_builder.base import DesignJob

from .sites_context import SitesContext


class SitesDesign(DesignJob):
    continent = ChoiceVar(
        ("continent-as", "Asia"),
        ("continent-sa", "South America"),
        ("continent-eu", "Europe"),
        ("continent-an", "Antarctica"),
        ("continent-na", "North America"),
        ("continent-oc", "Oceania"),
        ("continent-ac", "Africa"),
    )

    class Meta:
        name = "Sites Design"
        commit_default = True
        design_file = "templates/initial_design.yaml.j2"
        context_class = SitesContext
        soft_time_limit = 3600

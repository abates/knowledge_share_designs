"""Unit tests for designs"""
"""Unit tests for designs"""

from design_builder.tests import DesignTestCase
from nautobot.dcim.models import Region, Site

from ..sites_design import SitesDesign
from ..sites_context import SitesContext

class TestInitialDesign(DesignTestCase):
    def test_design(self):
        job = self.get_mocked_job(SitesDesign)
        region = Region(name="region-us-ca", slug="region-us-ca")
        context = SitesContext({"region": region})
        context.validate()
        print(job.render(context, "templates/sites_design.yaml.j2"))
        self.assertTrue(False)

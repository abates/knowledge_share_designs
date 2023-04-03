"""Unit tests for designs"""

from design_builder.tests import DesignTestCase
from nautobot.dcim.models import Region, Site

from ..ks_initial_design import KSInitialDesign


class TestInitialDesign(DesignTestCase):
    def test_design(self):
        job = self.get_mocked_job(KSInitialDesign)
        job.run({}, True)

        americas = Region.objects.get(name="Americas")
        us = americas.children.get(name="United States")
        for region_name in ["US-East-1", "US-West-1"]:
            region = us.children.get(name=region_name)
            # each region should have two sites
            self.assertEqual(2, region.sites.count())

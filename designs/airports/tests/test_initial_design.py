from nautobot.dcim.models import Region

from design_builder.tests import DesignTestCase

from ..initial_design import InitialDesign

class TestInitialContext(DesignTestCase):
    def test_context(self):
        job = self.get_mocked_job(InitialDesign)
        job.run({"country": "US"}, True)

        region = Region.objects.get(slug="continent-na")
        self.assertEqual(1, region.children.count())
        country = region.children.first()
        self.assertEqual(51, country.children.count())

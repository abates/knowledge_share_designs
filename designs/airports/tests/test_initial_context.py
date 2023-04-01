from design_builder.tests import DesignTestCase

from ..initial_context import InitialDesignContext

class TestInitialContext(DesignTestCase):
    def test_context(self):
        context = InitialDesignContext(data={"country": "US"})
        self.assertEqual(23252, len(context.sites))
        for site in context.sites.values():
            self.assertIsInstance(site["name"], str)

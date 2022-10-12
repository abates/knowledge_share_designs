"""Unit tests for designs"""

from design_builder.tests import DesignTestCase

from unittest import mock

from .. import BasicDesign


class TestFabricPod(DesignTestCase):
    def test_design(self):
        input = {}

        job = BasicDesign()
        job.request = mock.Mock()
        job.job_result = mock.Mock()
        job.run(input, True)

        self.assertTrue(True)

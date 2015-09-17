from django.test import TestCase

__all__ = [
    'InteractionFieldsTestCase'
]


class InteractionFieldsTestCase(TestCase):

    def setUp(self):
        super(InteractionFieldsTestCase, self).setUp()

    def test_fail(self):
        self.assertTrue(True)

from django.test import TestCase

class SmokeTest(TestCase):

    def test_bad_maths(self):
        self.assertionEqual(1 + 1, 3)

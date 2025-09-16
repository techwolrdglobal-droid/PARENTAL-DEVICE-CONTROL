import unittest
from services.location_service import LocationService

class TestPrivacyEnforcement(unittest.TestCase):
    def test_location_requires_consent(self):
        ls = LocationService()
        ls.consent_given = False
        with self.assertRaises(PermissionError):
            ls.start_location()
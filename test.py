import unittest
from unittest import mock
from dvla_api import vehicle_data


class TestLicensePlate(unittest.TestCase):

    def incorrect_license(self):
        with mock.patch('builtins.input', side_effect=['MJ59 LVZ']):
            self.assertRaises(ValueError)

    def correct_license(self):
        with mock.patch('builtins.input', side_effect=['MJ59LVZ']):
            self.assertTrue(self)


class TestIsPrivate(unittest.TestCase):

    def incorrect_private(self):
        with mock.patch('builtins.input', side_effect=['s']):
            self.assertRaises(ValueError)

    def correct_private(self):
        with mock.patch('builtins.input', sideeffect=['Y']):
            self.assertTrue(self)


if __name__ == '__main__':
    unittest.main()




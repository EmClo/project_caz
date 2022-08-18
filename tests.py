

import unittest
from unittest import mock
from bath_caz import get_bath_caz_status

class TestVehicle(unittest.TestCase):

    def test_vehicle_reg(self):
        with mock.patch('builtins.input', side_effect=['Your electric car is exempt and can drive through the CAZ with no charge.']):
            reg_number = 'YS15EZX'
            self.assertEqual('Your electric car is exempt and can drive through the CAZ with no charge.', get_bath_caz_status(reg_number))


    if __name__ == '__main__':
        unittest2.main()

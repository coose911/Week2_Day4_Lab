import unittest
from src.phone_number import phonenumber

class TestPhoneNumber(unittest.TestCase):
    def setUp(self):
        self.phonenumber1 = phonenumber(1234567890)


    def test_phone_number(self):
        self.assertEqual("(123) 456-7890", phonenumber(self.phonenumber1))
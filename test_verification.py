import unittest
from verification_logic import verify_pan_format, calculate_checksum, verify_pan_details

class TestVerificationLogic(unittest.TestCase):
    def test_verify_pan_format_valid(self):
        valid_pan = "ABCDE1234F"
        self.assertTrue(verify_pan_format(valid_pan))

    def test_verify_pan_format_invalid(self):
        invalid_pan = "123456789"  # Incorrect length
        self.assertFalse(verify_pan_format(invalid_pan))

    def test_calculate_checksum_valid(self):
        valid_pan = "ABCDE1234F"
        self.assertTrue(calculate_checksum(valid_pan))

    def test_calculate_checksum_invalid(self):
        invalid_pan = "ABCDE12345"  # Incorrect PAN number for checksum (simplified)
        self.assertFalse(calculate_checksum(invalid_pan))

    # You can write more test cases for verify_pan_details() function, covering various scenarios

if __name__ == '__main__':
    unittest.main()

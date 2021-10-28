import unittest
from main import convert_to_cm

class MyTestCase(unittest.TestCase):
    def test_inch_to_cm(self):
        self.assertEqual(convert_to_cm('american','inch',5), 12.7)

    def test_foot_to_cm(self):
        self.assertEqual(convert_to_cm('american', 'foot', 5), 152.4)
if __name__ == '__main__':
    unittest.main()

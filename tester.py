import unittest
from main import convert_to_cm

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(convert_to_cm('american','inch',5), 12.7)


if __name__ == '__main__':
    unittest.main()

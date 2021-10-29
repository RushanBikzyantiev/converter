import unittest
from main import convert_to_cm
from main import convert_from_cm

class MyTestCase(unittest.TestCase):
    def test_inch_to_cm(self):
        self.assertEqual(convert_to_cm('american','inch',5), 12.7)

    def test_foot_to_cm(self):
        self.assertEqual(convert_to_cm('american', 'foot', 5), 152.4)
    def test_milya_to_cm(self):
        self.assertEqual(convert_to_cm('american', 'mi', 5), 804672.0)

    def test_Elbow_to_cm(self):
        self.assertEqual(convert_to_cm('oldrussian', 'Elbow', 5), 296.89)
    def test_span_to_cm(self):
        self.assertEqual(convert_to_cm('oldrussian', 'span', 5), 88.9)
    def test_fathom_to_cm(self):
        self.assertEqual(convert_to_cm('oldrussian', 'fathom', 5), 1066.8)

    def test_cm_to_hand(self):
        self.assertEqual(convert_from_cm('american', 'hand', 100), 9.84)

    def test_cm_to_yard(self):
        self.assertEqual(convert_from_cm('american', 'yard', 50), 0.55)

    def test_cm_to_rod(self):
        self.assertEqual(convert_from_cm('american', 'rod', 300), 0.6)
        
    def test_cm_to_verst(self):
        self.assertEqual(convert_from_cm('american', 'verst', 266700), 2.5)

if __name__ == '__main__':
    unittest.main()

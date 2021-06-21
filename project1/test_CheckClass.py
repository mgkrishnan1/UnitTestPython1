import unittest
from CheckClass import CheckClass


class Test1(unittest.TestCase):
    def test_checkValue(self):
        v1 = CheckClass()

        # Test for positive case.
        val = v1.checkValue(3.2)
        self.assertEqual(val, 1)

        # Test for zero case.
        val = v1.checkValue(0)
        self.assertEqual(val, 0)

        # Test for negative case.
        val = v1.checkValue(-5)
        self.assertEqual(val, -1)

        # Test for TypeError
        with self.assertRaises(TypeError):
            v1.checkValue(True)
            v1.checkValue("Hello")


if __name__ == "__main__":
    unittest.main()

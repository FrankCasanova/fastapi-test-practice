import unittest

from introduction import add

#Unittest version.

class TestIntroduction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(1, -2), -1)
        self.assertEqual(add(1, 3.5), 4.5)
        self.assertEqual(add(1, -3.5), -2.5)
        self.assertEqual(add(1, 0), 1)
        self.assertEqual(add(1, -0), 1)
        self.assertEqual(add(1, 0.0), 1)
        self.assertEqual(add(1, -0.0), 1)
        self.assertEqual(add(1, 0.5), 1.5)
        self.assertEqual(add(1, -0.5), 0.5)

#Pytest version, more shorter.

def test_add():
    assert add(1, 2) == 3
    assert add(1, -2) == -1
    assert add(1, 3.5) == 4.5
    assert add(1, -3.5) == -2.5
    assert add(1, 0) == 1
    assert add(1, -0) == 1
    assert add(1, 0.0) == 1
    assert add(1, -0.0) == 1
    assert add(1, 0.5) == 1.5
    assert add(1, -0.5) == 0.5        
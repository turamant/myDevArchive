import unittest


class SimpleTest(unittest.TestCase):

    def test1(self):
        a = 'a'
        b = 'a'
        self.assertEqual(a, b)

    def test2(self):
        self.assertEqual(1, 5 - 4)

    def test3(self):
        self.assertNotEqual(2, 8-3)


import unittest


class Calculator:
    def add(self, n1,n2):
        n3=n1+n2
        return n3

    def mul(self, n1,n2):
        n3=n1*n2
        return n3


class SimplisticTest(unittest.TestCase):

    def test_add(self):
        c=Calculator()
        self.assertEqual(30,c.add(5,25))

    def test_mul(self):
        c=Calculator()
        self.assertEqual(125,c.mul(5,25))



if __name__ == '__main__':
    unittest.main()

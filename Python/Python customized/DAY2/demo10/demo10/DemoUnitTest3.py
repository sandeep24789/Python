import unittest

class Calculator:
    def add(self, n1,n2):
        n3=n1+n2
        return n3

    def mul(self, n1,n2):
        n3=n1*n2
        return n3

class FixturesTest(unittest.TestCase):

    def setUp(self):
        print('In setUp()')
        self.c = Calculator()

    def tearDown(self):
        print('In tearDown()')
        del self.c

    def test(self):
        print('in test()')
        self.assertEqual(self.c.add(10,20),30)

if __name__ == '__main__':
    unittest.main()

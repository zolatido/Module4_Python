import unittest

def check(x):

    return x>=100

class myTest(unittest.TestCase):

    def test(self):

        self.assertTrue(check(99))

if __name__ == '__main__':
    unittest.main()
import unittest

def squared(n):
    return n**2

class TestStringMethods(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(squared(0), 0)
    def test_five(self):
        self.assertEqual(squared(5), 25)
        
if __name__ == '__main__':
    unittest.main()
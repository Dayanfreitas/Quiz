import unittest

class TestHelper(unittest.TestCase):

    def test_name(self):
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()
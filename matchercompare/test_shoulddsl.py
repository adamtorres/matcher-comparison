import unittest

class Examples(unittest.TestCase):
    def test_boolean(self):
        # c = True
        # c == True
        pass

    def test_numbers(self):
        # e = 4.2
        # e == 4.2
        # e+1 == 5.2
        # e > 4
        # e >= 4.2
        # e < 5
        # e <= 4.2
        # e != 4
        pass

    def test_strings(self):
        # d = "this"
        # d == "this"
        # InString = "this" in "this is a test"
        # StartsWith
        # EndsWith
        pass


    def test_lists(self):
        # a = [1, 2, 3]
        # a == [1, 2, 3]
        # a contains 3
        # a does not contain 42
        # Count of items/length
        pass

    def test_dicts(self):
        # b = {'a':1, 'b':2}
        # b == {'a':1, 'b':2}
        # b contains 'b'
        # b does not contain 'q'
        # Count of items/length
        pass


    def test_objects(self):
        # IsInstance
        # has attribute
        # attribute has value
        pass

    def test_existance(self):
        # Empty/None
        pass

    def test_functions(self):
        # Call function with no params
        # Call function with params
        pass


    def test_errors(self):
        # KeyError
        # {}[123]
        # ZeroDivisionError
        # lambda: 1/0 == throws
        # lambda: 1/0.000001 == works
        pass


    def test_custom(self):
        # A couple hinted at custom tests
        pass

    def test_other(self):
        # Anything not fitting the other categories
        # should-dsl: change
        pass

if __name__ == '__main__':
    unittest.main()

import unittest
from should_dsl import should, should_not

class TestShoulddslExamples(unittest.TestCase):
    """
    A couple links which helped in writing these examples.
    http://www.should-dsl.info/
    http://pythonhosted.org/should_dsl/available_matchers.html
    """
    def test_boolean(self):
        c = True
        c |should| be(True)

    def test_numbers(self):
        e = 4.2
        e |should| be(4.2)
        (e+1) |should| be(5.2)
        e |should| be_greater_than(4)
        e |should| be_greater_than_or_equal_to(4.2)
        e |should| be_less_than(5)
        e |should| be_less_than_or_equal_to(4.2)
        e |should_not| be(4)

    def test_strings(self):
        d = "this"
        e = "this is a test"
        d |should| be("this")
        e |should| include("is a")
        e |should| start_with("this")
        e |should| end_with("test")

    def test_lists(self):
        a = [1, 2, 3]
        a |should| include_all_of([1, 2, 3])
        a |should| include(3)
        a |should_not| include(42)
        a |should| have(3).items

    def test_dicts(self):
        b = {'a':1, 'b':2}
        b |should| include_all_of({'a':1, 'b':2})
        b |should| include_keys('b')
        b |should_not| include_keys('Q')
        b |should| have(2).whatsits # Note: the .whatsits is syntactic sugar and can be anything.
        #have_at_most, have_at_least

    def test_objects(self):
        class Box(object):
            def __init__(self, name=None):
                self.name = name
        b = Box("hello world")
        b |should| be_kind_of(Box)
        b |should| be_instance_of(Box)
        b |should| respond_to("name")
        b.name |should| be("hello world")

    def test_existance(self):
        b = None
        b |should| be(None)
        b = "bob"
        b |should_not| be(None)

    def test_functions(self):
        def no_params(): return 42
        def yes_params(x, y): return x+y

        no_params() |should| be(42)
        yes_params(4,5) |should| be(9)

    def test_errors(self):
        KeyError |should| be_thrown_by(lambda: {}[123])
        ZeroDivisionError |should| be_thrown_by(lambda: 1/0)

    def test_custom(self):
        pass

    def test_other(self):
        # Anything not fitting the other categories
        class Thing(object):
            def __init__(self, name=None):
                self.name = name
            def reset(self):
                self.name = None
            def get_name(self):
                return self.name

        b = Thing("Billy")
        b.reset |should| change(b.get_name)     # Note: change() requires a callable.  Simple variables
        b.reset |should_not| change(b.get_name) # cannot be used.

if __name__ == '__main__':
    unittest.main()

import unittest
from hamcrest import *
import datetime

#Used for custom matcher class
from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.helpers.hasmethod import hasmethod

class TestHamcrestExamples(unittest.TestCase):
    """
    Various links which helped in writing these examples.
    https://github.com/hamcrest/PyHamcrest
    https://code.google.com/p/hamcrest/wiki/TutorialPython
    http://pythonhosted.org/PyHamcrest/tutorial.html
    https://pypi.python.org/pypi/PyHamcrest
    """
    def test_boolean(self):
        c = True
        # Note: _is() is syntactic sugar
        assert_that(c, is_(True))
        assert_that(c, True)
        assert_that(c, equal_to(True))

    def test_numbers(self):
        e = 4.2
        assert_that(e, 4.2)
        assert_that(e + 1, 5.2)
        assert_that(e, greater_than(4))
        assert_that(e, greater_than_or_equal_to(4.2))
        assert_that(e, less_than(5))
        assert_that(e, less_than_or_equal_to(4.2))
        assert_that(e, is_not(equal_to(4)))

    def test_strings(self):
        d = "this is a test"
        assert_that(d, contains_string("is"))
        assert_that(d, starts_with("this is"))
        assert_that(d, ends_with("a test"))

    def test_lists(self):
        a = [1, 2, 3]
        assert_that(a, contains(1, 2, 3)) #contains == exact match of all elements
        assert_that(a, has_item(3))
        assert_that(a, has_items(3, 1))
        assert_that(a, is_not(has_item(42)))
        assert_that(a, has_length(3))

    def test_dicts(self):
        b = {'a':1, 'b':2}
        assert_that(b, has_entries({'a':1, 'b':2}))
        assert_that(b, has_key('b'))
        assert_that(b, is_not(has_key('q')))
        assert_that(b, has_length(2))


    def test_objects(self):
        class Box(object):
            def __init__(self, name=None):
                self.name = name
        b = Box("hello world")
        assert_that(b, instance_of(Box))
        assert_that(b, has_property("name"))
        assert_that(b, has_property("name", "hello world"))

    def test_existance(self):
        b = None
        assert_that(b, none())
        b = "bob"
        assert_that(b, not_none())

    def test_functions(self):
        # Call function with no params
        # Call function with params
        pass


    def test_errors(self):
        # calling/raises was added a month ago to 1.8 but 1.7.1 is what pip install gets.
        # assert_that(calling({}[123]), raises(KeyError))
        # assert_that(calling(lambda: 1/0), raises(ZeroDivisionError))
        pass

    def test_custom(self):
        assert_that(datetime.date(2008, 4, 5), is_(on_a_saturday()))

    def test_other(self):
        # Anything not fitting the other categories
        # should-dsl: change
        pass

# Custom matcher code #################################################################

class IsGivenDayOfWeek(BaseMatcher):
    def __init__(self, day):
        self.day = day # Monday == 0, Sunday == 6

    def _matches(self, item):
        if not hasmethod(item, "weekday"):
            return False
        return item.weekday() == self.day

    def describe_to(self, description):
        day_as_string = ["Monday", "Tuesday", "Wednesday", "Thursday", 
                         "Friday", "Saturday", "Sunday"]
        description.append_text("calenday date falling on ") \
                   .append_text(day_as_string[self.day])

def on_a_saturday():
    return IsGivenDayOfWeek(5)

# End custom matcher code #############################################################

if __name__ == '__main__':
    unittest.main()

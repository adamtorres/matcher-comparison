import unittest
import sure
from sure import expect

class TestSureExamples(unittest.TestCase):
    """
    A couple links which helped in writing these examples.
    https://github.com/gabrielfalcao/sure
    """
    def test_boolean(self):
        c = True
        c.should.be.ok
        False.shouldnt.be.ok
        False.should_not.be.ok

    def test_numbers(self):
        e = 4.2
        e.should.equal(4.2)
        e.should.be.equal(4.2) # 'be' is optional
        (e+1).should.equal(5.2)
        e.should.be.greater_than(4)
        e.should.be.above(4)
        e.should.be.greater_than_or_equal_to(4.2)
        e.should.be.lower_than(5)
        e.should.be.below(5)
        e.should.be.lower_than_or_equal_to(4.2)
        e.shouldnt.equal(2)

    def test_strings(self):
        d = "this"
        e = "this is a test"
        d.should.equal("this")
        e.should.contain("is a")
        # StartsWith and EndsWith do not exist
        # But, there is a regex match() which can do the same thing with ^ and $
        import re
        e.should.match(r'^this', re.I)
        e.should.match(r'test$', re.I)

    def test_lists(self):
        a = [1, 2, 3]
        a.should.equal([1, 2, 3])
        a.should.contain(3)
        a.shouldnt.contain(42)
        a.should.have.length_of(3)

    def test_dicts(self):
        b = {'a':1, 'b':2}
        b.should.equal({'a':1, 'b':2})
        b.should.have.key('b')
        b.should_not.have.key('q')
        b.should.have.length_of(2)

        # Bonus: verify key exists and check its value
        b.should.have.key('b').being.equal(2)

    def test_objects(self):
        class Box(object):
            def __init__(self, name=None):
                self.name = name
        b = Box("hello world")
        b.should.be.a(Box) # Note: "be.a(" can also be "be.an("
        b.should.have.property('name')
        b.should.have.property('name').being.equal("hello world")

    def test_existance(self):
        b = None
        b.should.be.none
        b = "bob"
        b.should.be.equal("bob")

    def test_functions(self):
        def no_params(): return 42
        def yes_params(x, y): return x+y

        no_params.when.called_with().should.return_value(42)
        yes_params.when.called_with(5, 4).should.return_value(9)

    def test_errors(self):
        (lambda: {}[123]).when.called_with().should.throw(KeyError)
        (lambda: 1/0).when.called_with().should.throw(ZeroDivisionError)

    def test_custom(self):
        # A couple hinted at custom tests
        pass

    def test_other(self):
        # Anything not fitting the other categories
        pass

if __name__ == '__main__':
    unittest.main()

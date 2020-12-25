import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_mult_positive(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_div_positive(self):
        assert self.calc.division(self, 4, 2) == 2

    def test_sub_positive(self):
        assert self.calc.subtraction(self, 5, 2) == 3

    def test_add_positive(self):
        assert self.calc.adding(self, 3, 2) == 5

    # def test_multiply_fail(self):
    #     assert self.calc.multiply(self, 2, 2) == 5
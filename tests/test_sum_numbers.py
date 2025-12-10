import importlib

student = importlib.import_module("sum_numbers")

def test_simple_sum():
    assert student.sum_numbers(1, 2, 3) == 6

def test_with_negative_values():
    assert student.sum_numbers(10, -3, -7) == 0

def test_with_zero():
    assert student.sum_numbers(0, 0, 0) == 0

def test_with_floats():
    assert student.sum_numbers(1.5, 2.5, 3.0) == 7.0

def test_large_input():
    nums = list(range(1, 101))
    assert student.sum_numbers(*nums) == sum(nums)

def test_no_arguments():
    assert student.sum_numbers() == 0

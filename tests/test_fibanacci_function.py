import pytest
import application.testapp


def test_0_as_function_input(iteration_number=0):
    expected_series=[0]
    test_result = application.testapp.generate_fibonacci(iteration_number)
    assert test_result == expected_series, \
        "Generated Fibonacci sequence {0} is not equal to the expected one {1}".format(test_result, expected_series)


def test_1_as_function_input(iteration_number=1):
    expected_series=[0, 1]
    test_result = application.testapp.generate_fibonacci(iteration_number)
    assert test_result == expected_series, \
        "Generated Fibonacci sequence {0} is not equal to the expected one {1}".format(test_result, expected_series)


@pytest.mark.parametrize("iteration_number, expected_series", [
    (5, [0, 1, 1, 2, 3]),
    (9, [0, 1, 1, 2, 3, 5, 8, 13, 21]),
    (12, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
    ])
def test_various_function_input(iteration_number, expected_series):
    test_result = application.testapp.generate_fibonacci(iteration_number)
    assert test_result == expected_series, \
        "Generated Fibonacci sequence {0} is not equal to the expected one {1}".format(test_result, expected_series)

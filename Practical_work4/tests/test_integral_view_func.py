
from Practical_work4.Variant5 import integral_view
import pytest


@pytest.mark.parametrize("image, integral_matrix", [([[1, 1], [1, 1]], [[1, 2], [2, 4]]),
                                                    ([[0, 0], [0, 1]], [[0, 0], [0, 1]]),
                                                    ([[1, 2], [1, 2], [1, 2]], [[1, 3], [2, 6], [3, 9]]),
                                                    ([[1, 2, 3], [4, 5, 6]], [[1, 3, 6], [5, 12, 21]]),
                                                    ([[1, 0], [0, 0]], [[1, 1], [1, 1]])])
def test_good(image, integral_matrix):
    assert integral_view(image) == integral_matrix


@pytest.mark.parametrize("image, expected_exception", [('a', TypeError),
                                                       (42, TypeError),
                                                       ([1, 1], TypeError),
                                                       ([[1, 2], ["a", "b"]], TypeError),
                                                       ([[1, 2], 3], TypeError),
                                                       ([[1, 3], [1, [1]]], TypeError),
                                                       ([[1, 3], [1]], IndexError)])
def test_with_error(image, expected_exception):
    with pytest.raises(expected_exception):
        integral_view(image)





from Practical_work4.Variant5 import rect_sum
import pytest


@pytest.mark.parametrize("image, x1, y1, x2, y2, output_sum", [([[1, 1], [1, 1]], 1, 1, 1, 1, 0),
                                                               ([[1, 2], [3, 4]], 0, 0, 1, 1, 1),
                                                               ([[1, 0], [0, 1]], 0, 0, 2, 2, 2),
                                                               ([[1, 3], [2, 4]], 1, 1, 1, 2, 0),
                                                               ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 1, 1, 2, 3, 2),
                                                               ([[1, 2], [3, 2]], 1, 1, 0, 2, 0),
                                                               ([[1, 2], [3, 4]], -4, -7, 10, 9, 0)])
def test_good(image, x1, y1, x2, y2, output_sum):
    assert rect_sum(image, x1, y1, x2, y2) == output_sum


@pytest.mark.parametrize("image, x1, y1, x2, y2, expected_exception", [([[1, 2], [3, 4]], 1, 1, "10", 9, TypeError),
                                                                       ([[1, 4], [4, 10]], 1, 0, 1.8, 1, TypeError),
                                                                       ([[1, 2], [2, 4]], 0, 1, 1.0, 2, TypeError),
                                                                       ([[4, 'a'], [0, 7]], 0, 0, 2, 2, TypeError),
                                                                       ([[1, 2], [2, 4]], 0, 0, 1, 10, IndexError),
                                                                       ([[1, 3], [[1]]], 1, 1, 2, 2, IndexError)
                                                                       ])
def test_with_error(image, x1, y1, x2, y2, expected_exception):
    with pytest.raises(expected_exception):
        rect_sum(image, x1, y1, x2, y2)

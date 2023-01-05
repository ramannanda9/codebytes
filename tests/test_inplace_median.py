import pytest

from codebytes import inplace_median


@pytest.mark.parametrize("numbers, window_size, expected", [([3,1,2,5,4,6],3,[2,2,4,5]),
                                                            ([3,1,2,5,4,6,7],2,[2,1.5,3.5,4.5,5.0,6.5]),(None,2,[]),([2,3,4,5],5,[])])
def test_inplace_median(numbers, window_size, expected):
    assert inplace_median.inplace_median(numbers, window_size) == expected

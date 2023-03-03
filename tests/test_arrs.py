import pytest
from utils import arrs


@pytest.fixture
def test_data():
    # return [[], [1, 2, 3], [1, 2, 3, 4]]
    return [], [1, 2, 3], [1, 2, 3, 4]


def test_get(test_data):
    list_0, list_1, list_2 = test_data
    assert arrs.get(list_1, 1, "test") == 2
    assert arrs.get(list_0, 0, "test") == "test"


def test_slice(test_data):
    list_0, list_1, list_2 = test_data
    assert arrs.my_slice(list_2, 1, 3) == [2, 3]
    assert arrs.my_slice(list_1, 1) == [2, 3]
    assert arrs.my_slice(list_1, -4) == [1, 2, 3]
    assert arrs.my_slice(list_1, -2) == [2, 3]
    assert arrs.my_slice(list_0, 1) == []

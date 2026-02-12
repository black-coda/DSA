from dsa.searching.binary_search import binary_search, find_first, find_last


def test_binary_search():
    assert binary_search([1, 3, 5, 7, 9], 5) == 2
    assert binary_search([1, 3, 5, 7, 9], 10) == -1
    assert binary_search([1], 1) == 0


def test_find_first():
    arr = [1, 2, 2, 2, 2, 3, 4, 5]
    assert find_first(arr, 2) == 1
    assert find_first(arr, 1) == 0
    assert find_first(arr, 5) == 7
    assert find_first(arr, 6) == -1


def test_find_last():
    arr = [1, 2, 2, 2, 2, 3, 4, 5]
    assert find_last(arr, 2) == 4
    assert find_last(arr, 1) == 0
    assert find_last(arr, 5) == 7
    assert find_last(arr, 6) == -1

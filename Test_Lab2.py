import Lab2

#def test_get_user_input():
#    result = Lab2.get_user_input()
#    assert (result == [1, 2, 3, 4, 5])

def test_calc_average():
    result = Lab2.calc_average([1, 2, 3, 4, 5])
    assert (result == 3)

def test_find_min_max():
    result = Lab2.find_min_max([1, 2, 3, 4, 5])
    assert (result == [1, 5])

def test_sort_temperature():
    result = Lab2.sort_temperature([1, 2, 3, 4, 5])
    assert (result == [1, 2, 3, 4, 5])

def test_calc_median_temperature():
    result = Lab2.calc_median_temperature([1, 2, 3, 4, 5])
    assert (result == 3)
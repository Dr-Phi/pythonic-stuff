from city_functions import get_information

def test_med_col():
    """Does Medellin Colombia works?"""
    result = get_information('medellin', 'colombia')
    assert result == 'Medellin, Colombia'

def test_city_country_population():
    result = get_information('santiago', 'chile', 5000000)
    assert result == 'Santiago, Chile - population 5000000'

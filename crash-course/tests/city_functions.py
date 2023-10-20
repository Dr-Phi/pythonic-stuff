
def get_information(city, country, population=0):
    if population:
        result = f'{city.title()}, {country.title()} - population {population}'
    else:
        result = f'{city.title()}, {country.title()}'
    return result

def get_rainfall():
    rainfall = {}

# We don’t know what cities the user will enter, so we create an empty
# dict, ready to be filled.

    while True:
        city_name = input('Enter city name: ')
        if not city_name:
            break

        mm_rain = input('Enter mm rain: ')
# If you’re from the United States, then you might be surprised to
# hear that other countries measure rainfall in millimeters.

        rainfall[city_name] = rainfall.get(city_name,
                        0) + int(mm_rain)
# The first time we encounter a city, we’ll add 0 to its current rainfall.
# Any subsequent time, we’ll add the current rainfall to the previously
# stored rainfall. dict.get makes this possible.

    for city, rain in rainfall.items():
        print(f'{city}: {rain}')

get_rainfall()
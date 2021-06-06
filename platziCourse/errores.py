countries = {
    'mexico': 122,
    'colombia': 49,
    'argentina': 43,
    'chile': 18,
    'peru': 31,
}


while True:
    country = str( input( "type the name of the country: " ) ).lower()
    try:
        print("la poblacion de {} es {} millones".format(country, countries[country]))
    except KeyError:
        print("The country {}, is not defined".format(country))
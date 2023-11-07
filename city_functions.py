#try it 11-1
def thing(city, country, population=None):
    if population == None:
        return (f"{city}, {country}")
    else:
        return (f"{city}, {country}, population - {population}") 
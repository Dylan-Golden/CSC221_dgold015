import city_functions as cf

def test_city_country():
    try:
        assert cf.thing('santiago', 'chile') == "santiago, chile"
    except:
        print ("failed")
    else:
        print ("passed")

def test_city_country_population():
    try:
        assert cf.thing('santiago', 'chile', 5000000) == "santiago, chile, population - 5000000"
    except:
        print ("failed")
    else:
        print ("passed")
    
        
test_city_country()
test_city_country_population()
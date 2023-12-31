
destinations = [
    "Paris, France",
    "Shanghai, China",
    "Los Angeles, USA",
    "São Paulo, Brazil",
    "Cairo, Egypt"
]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]


def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index


print(get_destination_index("Los Angeles, USA"))
# print(get_destination_index("Hyderabad, India"))


def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index


test_destination_index = get_traveler_location(traveler=test_traveler)
print(test_destination_index)

# Visiting Interesting Places
attractions = [[] for i in range(5)]
print(attractions)


def add_attraction(destination, attraction):
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index]
    attractions_for_destination.append(attraction)
    return


add_attraction(destinations[2], ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
print(attractions)

# Finding the Best Places to Go

def find_attractions(destination, interests):
    '''
    params:
        destination that is a string describing city, country
        interests is a list of strings describing places
        
    returns:
        attractions in the city that include at least one of the interests
    '''
    destination_index = get_destination_index(destination)
    
    # These the available attractions
    attractions_in_city = attractions[destination_index]
    
    attractions_with_interest = []
        
    for attraction in attractions_in_city:
        # The first element in attraction is the name of the attraction
        # And the second is an interest
        attraction_tags = attraction[1]   
        for interest in interests:
            if interest in attraction_tags:
                attractions_with_interest.append(attraction[0])

    return attractions_with_interest
    
la_arts = find_attractions("Los Angeles, USA",['art'])
print(la_arts)

# See The Parts of a City You want to See

def get_attractions_for_traveler(traveler):
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]
    
    traveler_attractions = find_attractions(traveler_destination,
                                            traveler_interests)
    
    reply = f"Hi {traveler[0]}, we think you'll like these places around {traveler_destination}: "
    for attraction in traveler_attractions:
        if attraction != traveler_attractions[-1]:
            reply += attraction + ", "
        else:
            reply += attraction
    reply += "."
    return reply
    
derek = ['Dereck Smill', 'Paris, France', ['monument']]
smills_france = get_attractions_for_traveler(derek)
print(smills_france)
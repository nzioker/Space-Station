import urllib.request, geocoder, json

url = " http://api.open-notify.org/astros.json"

def extract_information(url):
    return json.loads(urllib.request.urlopen(url).read())
    


def write_to_txt_file(astronauts_data):
    new_file = open("station.txt", "w")
    #write number of astronauts
    new_file.write("We have " + str(astronauts_data["number"]) + " astronauts on board. \n")
    people = astronauts_data["people"]

    # write names of astronauts
    for person in people:
        new_file.write("Name: " + person['name'] + " " + "Craft: " + person['craft'] + "\n")

    #write the coordinates of the iss
    coordinates = str(get_coordinates())

    new_file.write("\nYour current coordinates are, " + coordinates)

def get_coordinates():
    coordinates = geocoder.ip("me").latlng
    return coordinates


astronauts_data = extract_information(url)
write_to_txt_file(astronauts_data)
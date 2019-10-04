# Photo Album Technical Showcase
# This program retreives JSON data from a web service and displays it
# using console output.
# Author: Thomas Staudt

import requests
import json
import re

album_id = "0"
# Get the album ID from the user. If the input is not a whole number
# between 1 and 100, repeat the prompt.
while album_id.isdigit() == False or (album_id.isdigit() == True and (int(album_id) < 1 or int(album_id) > 100)):
    album_id = input("Select an album id between 1 and 100: ")
# Get the url for the specified album.
url = "https://jsonplaceholder.typicode.com/photos?albumId=" + album_id
# Get the JSON objects from the URL.
json_request = requests.get(url)
# Get a list of every json from the url.
json_list = json_request.json()
# Loop through the list and print out every photo's ID and Title.
for one_json in json_list:
    # Modify the json so that it will works with json.loads().
    modified_json = re.sub("\'", "\"", str(one_json))
    # Parse the modified json.
    parsed_json = json.loads(modified_json)
    # Print the ID and title of the parsed json.
    print("Photo ID: " + str(parsed_json['id']) + ", Title: " +str(parsed_json['title']))
'''
Analyze JSON
1. get the file
2. Analyze the resulting JSON file to display, for all entries : director, title,
district, start date, end date, and geographic coordinates.
3. Display for each film (there may be several entries for the same film) the director,
the shooting dates, and the locations.
4. Display for each district its number of shooting.
'''

import json
from socket import *

with open('film.json') as infile :
    json_data = json.load(infile)
    print("director, title, district, start date, end date, and arrondissement")
    print('='*80)

    for p in json_data :
        try:
            print(p["fields"]["nom_realisateur"],",",p["fields"]["nom_tournage"],",",
                  p["fields"]["date_debut"],",",p["fields"]["date_fin"],",",p["fields"]["ardt_lieu"])
        except TypeError:
            print("this data does not seem serializable with JSON")
        except KeyError:
            print("this data has a key error")

    print('='*80)

    dist = []

    for p in json_data :
        try:
            dist.append(int(p["fields"]["ardt_lieu"]))
        except TypeError:
            print(".")
        except KeyError:
            print(".")
    district = list(set(dist))
    #print(district)
    for i in range (0,len(district)) :
        count = 0
        for j in range (0, len(dist)) :
            if dist[j] == district[i] :
                count += 1
            else :
                continue
        print(district[i],":" ,count,"shootings")

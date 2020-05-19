#sort by is the number of cities that begin with the letter ‘S’.
states = {"Minnesota": ["St. Paul", "Minneapolis", "Saint Cloud", "Stillwater"],
          "Michigan": ["Ann Arbor", "Traverse City", "Lansing", "Kalamazoo"],
          "Washington": ["Seattle", "Tacoma", "Olympia", "Vancouver"]}
def city_with_s(city):
    ct=0
    for s in city:
        if s[0]=="S":
            ct=ct+1
    return ct

print(sorted(states, key=lambda state: city_with_s(states[state])))

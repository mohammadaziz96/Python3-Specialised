placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."
d={}
for c in placement:
    if c not in d:
        d[c]=0
    d[c]=d[c]+1
print(d)
keys=list(d.keys())
min_value=keys[0]
print(keys)
for key in keys:
    if d[key] < d[min_value]:
        min_value=key
print(min_value)

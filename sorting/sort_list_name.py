"""The dictionary, medals, shows the medal count for six countries during the Rio Olympics. Sort the country names so they appear alphabetically. Save this list to the variable alphabetical."""

alphabetical=[]
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
for i in sorted(medals.keys()):
    alphabetical.append(i)
print(alphabetical)

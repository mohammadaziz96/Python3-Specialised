olympics=[("John", 31, "Cross Country"),
        ("Milano", 38, "Sailing"),
        ("Winni", 54, "Art"),
        ("Makaru", 60, "Cyclying")]
outfile=open("reduce_olympics.csv", "w")
outfile.write("Name, Age, Sports")
outfile.write("\n")
for line in olympics:
    row_string="{},{},{}".format(line[0], line[1], line[2])
    outfile.write(row_string)
    outfile.write("\n")
outfile.close()


student=[("Modassir",1010,"Kerela"),
        ("Mojammil",1014,"Kota"),
        ("Aziz",1044,"England"),
        ("Shamima",1123,"Mughalsarai"),
        ("Tamanna", 1001,"Patna")]
record=open("Student_rec.csv", "w")
record.write("Name,Code,City")
record.write("\n")
for line in student:
    r=line[0] + "," + str(line[1])+ "," +line[2]
    record.write(r)
    record.write("\n")
record.close()

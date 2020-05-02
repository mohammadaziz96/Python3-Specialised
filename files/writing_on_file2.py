record=[("A",101,"Actor"),
        ("B",102,"Musician"),
        ("C",103,"Singer"),
        ("D",104,"Director"),
        ("E",105,"Producer")]
final_rec=open("bollywood.csv", "w")
final_rec.write("Name,Code,Occupation")
final_rec.write("\n")
for line in record:
    f=",".join([line[0],str(line[1]),line[2]])
    final_rec.write(f)
    final_rec.write("\n")
final_rec.close()

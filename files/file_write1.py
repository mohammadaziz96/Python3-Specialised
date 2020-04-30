file_obj=open("square.txt", "w")
for i in range(13):
    square=i*i
    file_obj.write(str(square))
    file_obj.write("\n")
file_obj.close()
new_file_obj=open("square.txt", "r")
print(new_file_obj.read()[:8])


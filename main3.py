file=open("Codingal.txt", "r")
counter=0


# Reading from file
Content=file.read()
# splitting content into lines
# and storing them ina list
colist=Content.split("\n")

for i in colist:
    if i:

        counter +=1

print("this is the number of lines in the file")
print(counter)


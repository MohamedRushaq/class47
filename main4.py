# entering the file names
firstfile=input("enter the name of first file ")
secondfile=input("enter the name of second file ")

# opening both files in read only mode to read initial contents
f1=open(firstfile, 'r')
f2=open(secondfile, 'r')

# printing the contents of the file before appending 
print('contents of first file before appending -\n', f1.read())
print('content of second file before appending - \n', f2.read())

# closing the files 
f1.close()
f2.close()
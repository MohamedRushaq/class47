# open the file in read mode
file_read=open('Codingal.txt','r')
print("file in Read Mode -")
print(file_read.read())
file_read.close()

# open the file in write mode
file_write=open('Codingal.txt', 'w')
# write in the file 
file_write.write(" file in write mode ...")
file_write.write("Hi! I am penguin. I am 1 year.old ")
file_write.close()

# open the file in append mode
file_append=open('Codingal.txt', 'a')
# append in the file
file_append.write("\n file in append mode ...")
file_append.write("Hi! I am penguin. I am 1 year. old")
file_append.close()
#reading text file
file_reader = open("file.txt")
#print(file_reader.read()) # reads entire file, return content as string

# print(file_reader.read(3))

# print(file_reader.readline(2))
print(file_reader.readlines())
file_reader.close()



file_reader = open("file.txt")
for line in file_reader:
    print(line)
file_reader.close()

with open("file.txt") as file_reader:
    for line in file_reader:
        print(line)
print("file closed")



#===========WRITE+++++
#overright
file_writer = open("file2.txt","w") # w is for overright the file
file_writer.write("my conetnt\n")
file_writer.close()


file_writer = open("file2.txt","a") # a is for append the file
file_writer.write("WHy conetnt\n")
file_writer.write("WHeretnt\n")
file_writer.close()

file_writer = open("file2.txt","w") # w is for overright the file
file_writer.write("have orverrighte\n")
file_writer.close()

my_list = ["line1\n", "Line2\n", "Line3\n", "Line4\n","Line5\n"]
file_writer = open("text3.txt", "w")
file_writer.writelines(my_list) # for list
file_writer.close()

# read file without empyt lines
with open("text3.txt") as file_reader:
    for line in file_reader:
        # print(line[:-1])
        print(line, end="")

# write list to file in seprate lines
my_list = ["sdf","sdfg","sfg","sdfg","sfdgsde"]
file_writer = open("text4.txt", "w")
file_writer.write("\n".join(my_list))
file_writer.close()


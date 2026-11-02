#===========================LISTS==============================
#Basic type of collection
list_empty = []
print(list_empty)
list1 = ["Marek", "John", "Tom", 123, 567, True, False]
print(list1)

firstnames = ["Marek", "John", "Tom", "Jim", "Anna", "Mike"]
print(firstnames)

#Get by index
print(firstnames[0])
print(firstnames[1])

startname_index = 2
print(firstnames[startname_index])
print(firstnames[startname_index + 1])
print(firstnames[startname_index + 2])

print(firstnames[-1])
print(firstnames[-2])

print(len(firstnames))


#Iterating over list

for index in range(6):
    print(index)

for index in [0, 1, 2, 3, 4, 5]:
    print(index)

#for element  in collection
for firstname in firstnames:
    print("Name: {}".format(firstname))

#append to the end
firstnames.append("Jack")
print(firstnames)

#insert inside list
firstnames.insert(4, "Peter")
print(firstnames)

#add list to list
firstnames_female = ["Eva", "Anna"]
print(firstnames_female)
firstnames_male = ["Mark", "Peter", "Tom", "Jack"]
print(firstnames_male)
firstnames = firstnames_female + firstnames_male
print(firstnames)

#Remove by index
del firstnames[2]
print(firstnames)

#Remove by content
firstnames.remove("Tom")
print(firstnames)

firstnames = ["Mark", "John", "Tom", "Jim", "Tom", "Anna", "Mike", "Tom"]
firstnames.remove("Tom") #Remove first occurrence
print(firstnames)

#searching in collection

print(firstnames.index("Tom")) #Returns index of first occurrence
print(firstnames.index("Tom", 4))


firstnames = ["Mark", "John", "Tom", "Jim", "Tom", "Anna", "Mike", "Tom"]
print(firstnames)
print(firstnames.index("Tom"))
print(firstnames.index("Tom", 3))
print(firstnames.index("Tom", 5))


if "Jacob" in firstnames:
    print("Name Jacob is in firstnames")
else:
    print("Name Jacob is not in firstnames")


if "John" in firstnames:
    print("Name John is in firstnames")
else:
    print("Name John is not in firstnames")


#Lists in bool context
sample_list = []
print(bool(sample_list)) #False
sample_list = ["a", "b"]
print(bool(sample_list)) #True
sample_list = [""]
print(bool(sample_list)) #True!

# if len(sample_list) > 0:
if sample_list:
    print("List has elements")
else:
    print("List is empty")


#==========================TUPLES=============================================
#Tuple are faster, but you cannot modify it
sample_tuple = ("a", 123, 456, "qqqq", False, True)
print(sample_tuple)

print(sample_tuple[3])
print(sample_tuple.index("a"))
print("a" in sample_tuple)

# sample_tuple[0] = "qweqwe" #Forbidden

#Convert tuple to list, and list to tuple
sample_list = list(sample_tuple)
sample_list.append("something")
sample_tuple = tuple(sample_list)
print(sample_tuple)


#assingning multiple variables in one line using tuples
a, b = 1, 2
# a = 1
# b = 2
print(a)
print(b)

fullnames = [
    ("John", "Doe"),
    ("Marek", "Wisniewski"),
    ("Jan", "Kowalski")
]

for firstname, lastname in fullnames: #firstname, lastname = ("John", "Doe")
    print(f"{firstname} {lastname}")


firstnames = ["Mark", "John", "Tom", "Jim", "Tom", "Anna", "Mike", "Tom"]
for index, firstname in enumerate(firstnames):
    print("Firstname {}: {}".format(index + 1, firstname))



#Hashable and id
a = 1
print(id(a)) #Address in memory
a = 2
print(id(a)) #Id is different, because we "redeclare" variable

b = True
print(id(b))
b = False
print(id(b))

#Hashable (immutable): int, float, string, boolean, tuple (only when contains immutable types)

#=================================SETS========================================
#Every value is unique, values have to be hashable, not guaranteed the order
sample_set = {"a", "b", "sample_string", 1, 2, 3, False, ("a", "b", "c")}
print(sample_set)

#Add to set
sample_set.add("d")
print(sample_set)

#Remove from set
sample_set.remove("b")
print(sample_set)

#Check if element is in the set
print("a" in sample_set)
print("a" not in sample_set)

# print(sample_set[0]) <- prohibited due to set is not holding order

sample_set_2 = {"a", "b", "c", "d"}
print(sample_set_2)
sample_set_2.add("d") #Will not raise error, duplicated object is skipped

lst1 = list(sample_set_2)
print(lst1)

#===============================DICTIONARIES===================================
#Storing pairs -> key-value (key have to be unique)
sample_dict = {
    "a": 1,
    "b": 2,
    "c": 123,
    2: False,
    10: "sample string"
}

print(sample_dict)

print(sample_dict["c"])
sample_dict["c"] = 456
print(sample_dict)

# print(sample_dict["x"]) #<_ when key not exists interpreter raise an error

print(sample_dict.get("c"))

#check if key exists in dictionary

print("a" in sample_dict)
print("a" not in sample_dict)

#remove values
del sample_dict["c"]
print(sample_dict)

print()

#iterate over dictionary

for k in sample_dict:
    print("{}: {}".format(k, sample_dict[k]))

print()

for k, v in sample_dict.items():
    print("{}: {}".format(k, v))

print("Workshop Lesson 3")
# declare list of names
# iterate through the collection and print all the names


names =["Joe", "Mark", "Luke", "Tom", "Peter"]
for name in names:
    print(name)

# declare list of set (firstname, lastname)
# iterate through collection and pritn all full names

fullnames = [
    ("Joe", "Doe"),
    ("Mark", "Wnsniewski"),
    ("Luke", "Adams"),
    ("Tom","Sibin"),
    ("Peter", "Thompson"),
]


for firstname, lastname in fullnames: #firstname, lastname = ("John", "Doe")
    print(f"{firstname} {lastname}")

#define list wtih duplicates (names)
#check if list contain duplicatges (conver list to set)
#dedupliation the list & print deduplicated collection
cars = [
    "BMW",
    "Honda",
    "Tesla",
    "BMW",
    "Hyundai",
    "Audi",
    "BMW",
]
for car in cars:
    print(car)


car_set = set(cars)
len(car_set)
print(len(cars))
print(len(car_set))
if len(car_set)<len(cars):
    print("List contains duplicates")
    print(f"List contains {len(cars) - len(car_set)} duplicates")
else:
    print("List does NOT contains duplicates")



# declare list with 8 elements
# print only elements with 4 char or longer

drink_list = [
    "Fanta",
    "Coke",
    "Spirte",
    "Pepsi",
    "MountainDue",
    "DrPepper",
    "RedBull",
    "Mirinda",
]
print()
for drink in drink_list:
    if len(drink) >= 6:
        print(drink)

print()
# find all Johns
my_list = ["John", "mark", "Will", "John", "John", "angle","jack", "jim", "John"]
print(my_list)
print(my_list.index("John",1))
print(my_list.index("John",4))
print(my_list.index("John",5))
print()
print()

idx = my_list.index("John")
print(idx)
print()
while idx < len(my_list) - 1:
    idx = my_list.index("John", idx + 1)
    print(idx)
    print("end")






print("Hello world")

#Variables - like a box with some content, and with 'label'

message = "Hello world"
print(message)

message = message +  " World"
print(message)

message = "aaaaaa"
print(message)

#==========================Basic data types=========================
print()
print("Basic data types")

#Integer (number)
counter = 2
print(counter)

#Floating-point (number)
weight_sum = 10.5
print(weight_sum)

#String (text)
message = "Future Collars"
print(message)

#Multiline string
message2 = """
line1
line2
line3
"""
print(message2)

#Boolean value - True/False
always_true = True
print(always_true)

always_false = False
print(always_false)

#None - nothing
nothing_here = None
print(nothing_here)


#=================================Math operators==========================
print()
print("Math operators")



a = 2
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(b % a) #Remainder from divide 11 % 2 -> 2 + 2 + 2 + 2 + 2 + 1
print(a ** b) #To the power of (2 * 2 * 2)


#==============================Logical operators=========================
print()
print("Logical operators")

print(a == b) #Equals
print(a != b) #Different
print(a < b) #Less
print(a <= b) #Less or eq
print(a > b) #Grater
print(a >= b) #Greater or eq


#=======================AND, OR, NOT operators========================
print()
print("AND, OR, NOT operators")

#AND - both are True
print(False and False) #False
print(False and True) #False
print(True and False) #False
print(True and True) #True

#OR - at least one is true
print(False or False) #False
print(False or True) #True
print(True or False) #True
print(True or True) #True

#NOT - negation
print(not True) #False
print(not False) #True


#=============================Variables in boolean context====================
print()
print("Variables in boolean context")

print(bool(-1)) #True
print(bool(0)) #False
print(bool(1)) #True
print(bool(2)) #True
print(bool(0.1)) #True
print(bool("")) #False
print(bool("something")) #True
print(bool(" ")) #True
print(bool(None)) #False


#==============================Checking variable type=========================
print()
print("Checking variable type")

a = "Text"
print(type(a)) #Check variable type

print(type(a) is str)
print(type(a) == str) #Not recommended
print(type(a) is int)
print(type(a) is not int)


print(1 + 2) # no addition
print("1" + "2") # since it is a text


print(int("2") +int("2"))
print(str("2")+str("5"))

# === Text operations===
print("Hello" + " " + "World")
print ("hello" *4) # multipy a string

print("text for %s formatting %i" % ("a", 2)) # deprecated
###1 st method
a = "Fijo"
b = "doing"
print("My program prints hello {}".format(a))
print("My program prints hello {} in line {}".format(a, 130))
#== 2nd method
print (f"Hello {a} what are you {b}")


#===getting user input==
print("your name?")
user = input()
print("hello {}" .format(user))

age = int(input("how old are you?"))
print("your age is {}". format(age))
print("in ten years you will be {} years old".format(age + 10))




#==== additional text formatting
print("1\n2\n3\n4\n5") # to enter in next line

print("My favourite book is \"The Alchemist\" author Paul")
print("My favourite book is 'The Alchemist' author Paul")









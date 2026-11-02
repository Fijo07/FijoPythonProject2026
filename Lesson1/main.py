import sys

print ("  3). Fizzbuzz v2")
number = 11
if number % 5 == 0 or number % 3 == 0:
    result = ""
    if number % 5 == 0:
        result = result + "Fizz"
    if number % 3 == 0:
        result = result + "buzz"
        print(result)
else:
    print(number)


# Tap Ctrl twice, the second time you have to hold
# and then press arrow down key to get multiple cursor

# elif (condtion)
print ("  4). ELIF   ~ FizzBuzz V3")
if number % 15 ==0:
    print("Fizzbuzz")
elif number % 5 == 0:
    print ("Fizz")
elif number % 3 == 0:
    print ("Buzz")
else:
    print (number)

print ("  5). While Condiotn")
i = 0
while i < 10:
    print(f"iteratoin {i}")
    i = i + 1

# prime no V1
print ("  6). Prime no V1")
number = 23
x = number // 2
factor = 0

while x > 1:
    if number % x == 0:
        print (f"{number} has factor {x}")
        factor = x
    x = x - 1

if not factor:
    print(f"{number} is prime")
else:
    print(f"{number} is not prime")

    # factorial no V1
print("  7). Factorial no V1")
counter = 0
product = 1
while counter < 10:
    counter += 1 # shorter verstion of counter = counter +1
    product *= counter # product = product * counter
    print("{}:{}".format(counter, product))


counter = 0
product = 1
while counter < 10:
    counter += 1
    print ("I am calc {}".format(counter))
    product *= counter
    if product > 1000:
        break # stopping and exiting loop
    print ("{}: {}".format(counter, product))



# Prime V2
number = 24
x = number // 2
factor = 0

while x > 1:
    if number % x == 0:
        print(f"{number} is not primt has {x}")
        break
    x -= 1
else:
    print(f"{number} is prime")



# For Loop
print ("FOr LOOP- code execute givne numner of times")
# for variable in range():
        #line1
        #line2
        #line3
print()
print()

for i in range(10): # coz it is less than /equal 10
    print(i)

print()
print()
for i in range(5, 10): #start, stop
    print(i)

print()
print()
for i in range(0, 10, 2): #start, stop, step
    print(i)


print()
print()
print("reverse")

for i in range(10, 0, -1):
    print(i)

print()
print("skipping a numnber form loop")
for i in range(0, 10):
    if i == 5:
        continue # skipping that no
    if i == 7:
        continue
    print(i)


print(sys.argv[0]) # reserve for program name
print(sys.argv[1])
print(sys.argv[2])









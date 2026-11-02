

# a single progme age of all passger fight
# The cost of a child's ticket is PLN 200, the cost of an adult ticket is PLN 400.
# If the passenger is an adult, he can also order alcohol (maximum 3 glasses of wine, each for PLN 10).
# There can be a maximum of 20 passengers. The program calculates the total revenue from tickets.
# If the age of the passenger is 0 or the maximum number of passengers has been reached,
# the program exits printing the summary:
# Total revenue, Number of Adult Passengers, Number of Children, Number of Wine Glasses.



wine_count = 0
child_count = 0
adult_count = 0
passenger_count = 0

while passenger_count < 20:
    print("enter passenger age")
    age = int(input())
    if age == 0:
        break
    elif age < 18:
        child_count += 1
        passenger_count += 1
        continue

    print("enter the number of glasses of wine")
    wine_current = int(input())
    if wine_current < 0 or wine_current > 3:
        print("invalid no of glasses of wine")
        continue

    wine_count += wine_current
    adult_count += 1
    passenger_count += 1
revenue = adult_count * 400 + child_count * 200 + wine_count * 10
print(f"No of adult {adult_count} , no of children {child_count} and no of wine glasses {wine_count}, so revenue is {revenue}")
print("Adult: {}, Children: {}, Glasses of wine: {}, Revenue: {}".format(
    adult_count,
    child_count,
    wine_count,
    adult_count * 400 + child_count * 200 + wine_count * 10
))




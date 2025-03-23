#Programming often involves examining a set of conditions and deciding which action to take based on those conditions. Python’s if statement allows you to examine the current state of a program and respond appro-priately to that state. 
 
cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

# Testing for equality is case sensitive in python.
carr = "Hyundai"
carr.lower() == "hyundai"
#resolves True.


#Checking for inequality
requested_topping = "mushrooms"

if requested_topping != "anchovies":
    print(("Hold the anchovies!"))
#This code compares the value of requested_topping to the value "anchovies". if the values dont match, python returns True and executes the code following the if statement.
 
#Numerical Comparisons
age = 19
age < 21 #True
age > 21 #False

#Checking multiple conditions

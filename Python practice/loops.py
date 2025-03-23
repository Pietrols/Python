#looping through an entire list
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(f"{magician.title()}, that was an amazing performance.")
print("Thank you, everyone. That was a great magic performance")

#using the range() function
for value in range(1, 5):
    print(value)

for value in range(6):
    print(value)

#using range() to make a list of numbers
numbers = list(range(1, 6))
print(numbers)

#using a third arguement as a step size when generating numbers.
even_numbers = list(range(2, 25, 2))
print(even_numbers)

#create a seperate list and populate it with arguements made in the loop
squares = []
for value in range(1, 22):
    square = value ** 2
    squares.append(square)

print(squares)

#simple statistics with a list of numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

#list comprehensions
#allows us to generate a list in just one line
squares1 = [value**2 for value in range(1, 22)]
print(squares1)

# million = []
# for value in range(1, 1000000):
#     million.append(value)

# print(million)

# print(sum(million))

odd_numbers = list(range(1, 20, 2))
print(odd_numbers)

three_multiples = [value*3 for value in range(3, 30)]
print(three_multiples)

cubes = []
for value in range(3, 30):
    cube = value ** 3
    cubes.append(cube)

print(cubes)

# Slicing a list
#This code prints a slice of the list,  the output retains the structure of the list and includes the first three players in the list.
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3])

#you can generate any subset of a list. Eg, second to to fourth item in a list, you would start the slice at index 1 and end at index 4:
print(players[1:4])

#ommiting first index in a slice, automatically starts at the beginning of the list
print(players[:4])

#similarly, to start at a point till end of the list
print(players[2:])

print(players[:-3])


#Copying a list
# To copy a list, you can make a slice that includes the entire original list by omitting the first index and the second index ([:]). This tells Python to make a slice that starts at the first item and ends with the last item, producing a copy of the entire list.

my_foods = ["pizza", 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append("Chicken curry")
friend_foods.append("Ice cream")
print(my_foods)
print(friend_foods)

#exercise
artists = ["Kendrick", "Tyler", "Kanye", "Daniel", "Black", "John", "SZA"]
print(f"The first three items in the list are: {artists[:3]}")
print(f"The three artists in the middle are: {artists[2:5]}")
print(f"The last three artists on the list are: {artists[-3:]}")


#Tuples
#A tuple looks like a list, except you use parenthesis instead of square brackets. Tuples are immutable lists. meaning thath you cannot change the list. You can access individual elements using item's index, like lists.

#For example, if we have a rectangle that should always be a certain size, we can ensure that its size doesn’t change by putting the dimensions into a tuple:

dimensions = (200, 5)
print(dimensions[0])
print(dimensions[1])

#dimensions[0] = 250 // trying to change a value results in an error message.

#Looping through all values in a tuple
for dimension in dimensions:
    print(dimension)
    
#Writing over a Tuple
#although you cant modify, you can assign a new value to a variable that represents a tuple.
dimensions = (400, 100)
print(dimensions[0])
print(dimensions[1])
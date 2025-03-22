#looping through an entire list
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(f"{magician.title()}, that was an amazing performance.")
print("Thank you, everyone. That was a great magic performance")

#using the reang() function
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


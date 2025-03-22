#a list is a collection of items in a particular order.
bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)

#accessing elements in a list
print(bicycles[0])
print(bicycles[1].title())

#accessing last element
print(bicycles[-1].title())

#using individual values from a list
message = f"My first bicycle was a {bicycles[0].title()}"
print(message)

#modifying elements in a list
motorcycles = ["honda", "yamaha", "suzuki"]

#adding elements to a list
#aapending elements to the end of a list
motorcycles.append("ducati")
print(motorcycles)

#inserting elements into a list at any position
motorcycles.insert(0, "toyota")
print(motorcycles)

#removing element from a list
del motorcycles[0]
print(motorcycles)

#removing using pop() method
#the pop() method removes the last item in a list, but it lets you work with that item after removing it.
#this is useful when accessing a list stored in chronological order
last_bike = motorcycles.pop()
print(motorcycles)
print(last_bike)
print(f"The last motorcycle i owned was a {last_bike.title()}.")


#popping items from any position in a list
first_bike = motorcycles.pop(0)
print(f"The first motorcycle i owned was a {first_bike.title()}.")

#removing an item by value
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)

motorcycles.remove("ducati")
print(motorcycles)

#organizing a list
#sorting a list permanently with a sort() method to sort alphabetically
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()
print(cars)

#reversing aphabetical order
cars.sort(reverse=True)
print(cars)

#sorting a list temporarily with the sorted(function)
cars = ["bmw", "audi", "toyota", "subaru"]
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

#printing a list in reverse order
cars.reverse()
print(cars)

#find length of a list
print(len(cars))


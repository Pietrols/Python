print("hello world!")

message = "Hello Python world!"
print(message)

name_0f_py = "The language 'Python' is named after Monty Python, not the snake"

#changing case
#capitalize first letter
name = "ada lovelace"
print(name.title())

#upper and lower case
name1 = "eliano david"
print(name1.upper())
name2 = "HANNAH GEORGE"
print(name2.lower())

#using variables in strings
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name.title())
print(f"Hello, {full_name.title()}")

#adding whitespace to strings with tabs or newlines
#to add a tab to your text /t
print("python")
print("\tpython")

#to add a newline in a string
print(" i\n love\n python")

#stripping whitespace
favorite_language = "python "

#stripping whitespace on right side
print(favorite_language.rstrip())

#to remove whitespace permanently
favorite_language = favorite_language.rstrip()

#to remove whitespace on left side
fav_language = " javascript"
print(fav_language.lstrip())

#removing prefixes
nostarch_url = "https://nostarch.com"
print(nostarch_url.removeprefix("https://"))

suffremove = "python_notes.txt"
print(suffremove.removesuffix(".txt"))

#numbers
numbers = 0.3 + 0.3
print(numbers)

#numbers and floats
#dividing any two numbers always returns a float
num1 = 4 / 2
print(num1)

#underscores in numbers
universe_age = 14_000_000_000
print(universe_age)

#multiple assigns
x, y, z = 0, 1, 2
print(x, y, z)

#constants
#python has no built-in constant types, it uses all caps
MAX_CONNECTIONS = 5000

#the zen if python
import this

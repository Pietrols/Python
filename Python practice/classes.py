# class Car: 
#     '''A simple attempt to represent a car.'''
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()

#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it.")

#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer.")

#     def increment_odometer(self, miles):
#         self.odometer_reading += miles
    
# my_new_car = Car('audi', 'A4', 2024)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()

# class ElectricCar(Car):

#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery_size = 40

#     def describe_battery(self):
#         print(f"This car has a {self.battery_size}-kWh battery.")

# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())
# my_leaf.describe_battery()

class Restaurant:
    """A simple restaurant class."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describe the restaurant"""
        print(f"The restaurant is called {self.restaurant_name}")
        print(f"The cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is open.")

    def restaurant(self):
        print(f"{self.restaurant_name} takes {self.number_served} customers at a time.")

    def set_number_served(self, guests):
        self.number_served = guests

    def increment_number_served(self, increment):
        self.number_served += increment

french_restaurant = Restaurant("Bonjoir Bakery", "French Toast")
italy_restaurant = Restaurant("Pizza Hut 🍕", "Peperroni Pizza 🍕")
zambian_restaurant = Restaurant("Matebeto", "Chicken Nshima")

restaurant = Restaurant("Home", "Jollof Rice")
print(f"Number served: {restaurant.number_served}")
restaurant.number_served = 50
print(f"Number served: {restaurant.number_served}")

french_restaurant.describe_restaurant()
french_restaurant.restaurant()
print("----")
italy_restaurant.describe_restaurant()
french_restaurant.restaurant()
print("----")
zambian_restaurant.describe_restaurant()
french_restaurant.restaurant()
print("----")


class User:
    '''A user account'''
    def __init__(self, first_name, last_name, age, height):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.login_attempts = 0

    def describe_user(self):
        """user description"""
        print(f"This is {self.first_name} {self.last_name}, age {self.age}, and height {self.height}m.")

    def greet_user(self):
        """user greeting"""
        print(f"Hello {self.first_name} {self.last_name}, How are you doing?")

    def increment_login_attempts(self):
            self.login_attempts += 1

    def reset_login_attempts(self):
            self.login_attempts = 0
    
user1 = User("Eliano", "David", 2, 0.8)
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"Login attempts: {user1.login_attempts}")

user1.reset_login_attempts()
print(f"Login attempts: {user1.login_attempts}")

user2 = User("Katalina", "George", 0, 0.4)

user1.describe_user()
user2.describe_user()
print("----")
user1.greet_user()
user2.greet_user()


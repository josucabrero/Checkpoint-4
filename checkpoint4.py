from decimal import Decimal
import math

# Exercise 1

my_list = ["Soprano", "Tenor", "Baritono"]

my_tuple = ("My", "awesome", "tuple")

my_float = 16.1

my_decimal = Decimal(16.10)

my_dictionary = {
    "SO": "Soprano",
    "TE": "Tenor",
    "BA": "Baritono"
}

# Exercise 2

print(math.ceil(my_float))

# Exercise 3

print(math.sqrt(my_float))

# Exercise 4

first_element = my_dictionary ["SO"]

print(first_element)

# Exercise 5

one, two, three = my_tuple

print(two)

# Exercise 6

my_list = my_list + ["Bajo"]

print(my_list)

# Exercise 7

my_list[0] = "Alto"

print(my_list)

# Exercise 8

my_list.sort()

print(my_list)

# Exercise 9

my_tuple += ("shines",)

print(my_tuple)
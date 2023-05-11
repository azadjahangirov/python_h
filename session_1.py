## 1. Interaction with the user

# Exercise 1.1 | Interaction with the user and simple calculations
# Ask user (using `input()` function) to provide the number of kilograms of potatoes he'd like to buy and how much 1-kilogram costs.
# The program should display how much user have to pay.

"""
kg = float(input('Please provide the kg you want to buy: '))
cost = 15
payment = cost * kg
print(f'You should pay {payment} zloty.')
"""

# Exercise 1.2 | Shoemaker
# Ask the user to provide a number of days of the week (Monday=1, Sunday=7) when he left his shoes at the shoemaker shop for a repair.
# Ask him also how many days the repair will take. As an output, inform the user at which day of the week he should get back his shoes.
# For example, leaving shoes on Tuesday with 3 days needed for the repair, should output Friday.

"""
days = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday', 7:'Sunday'}
left_repair = int(input('Please write which day have you put your shoes for repair: '))
long = int(input('How many days will it take? '))
ready = left_repair + long


print(f'Please come on {days[ready]}')
"""

# Exercise 1.3 | BMI
# Write a program that will ask the user for his height (in cm) and body weight, and as a result will present his BMI and recommendations.
# Take a look at BMI definition in wikipedia.

"""
height = float(input('Please provide your height: '))
weight = float(input('Please provide your weight: '))
bmi = weight / (height * height)
print(f'Your BMI is {bmi:.1f}')
"""

# Exercise 1.4 | Hotel fee
"""
Write a program, where the user provides his age and the number of nights he wants to stay at the hotel.
Based on that values calculate the fee for his stay. The rules are:

- minor (below 18 years old) will pay 100 PLN per night
- adults (of age 18 but less than 65) will pay:
    - 200 PLN if they are staying for one night
    - 180 PLN if they are staying for at least 2 nights but less than 5
    - 150 PLN if they are staying for 5 and more nights
- pensioners (65 and older) will pay the same rate as adults but with a 10% discount

For example, if a user is 70 years old and will spend 10 nights at the hotel, he will pay 150 PLN - 10% discount = 135 PLN per night,
so for the whole stay, he will pay 1350 PLN.
"""

# age = int(input('Please provide your age: '))
# nights = int(input('Please provide days you will stay: '))
# discount = 0.9
#
# if age < 18:
#     payment = 100 * nights
# elif 18 <= age <= 65:
#     if nights == 1:
#         payment = 200 * nights
#     elif 2 <= nights < 5:
#         payment = 180 * nights
#     elif nights >= 5:
#         payment = 150 * nights
# else:
#     if nights == 1:
#         payment = (200 * nights) * discount
#     elif 2 <= nights < 5:
#         payment = (180 * nights) * discount
#     elif nights >= 5:
#         payment = (150 * nights) * discount
#
#
# if nights == 1:
#     day = 'a night'
# else:
#     day = str(nights) + ' nights'
#
# print(f'Your bill for {day} will be {payment}')


### Exercise 1.5 | Triangle area
"""
Write a program that will ask a user for the lengths of the sides of a triangle.
Check if it's possible to create a triangle from those lengths and if so, calculate the area of the triangle.

To calculate square root use:

import math

x = math.sqrt(10)
"""

# a = float(input('Please provide the a length of the side of a triangle: '))
# c = float(input('Please provide the c length of the side of a triangle: '))
#
# import math
#
# b = math.sqrt((c ** 2) - (a ** 2))
#
# if b >= 1:
#     # calculating the area
#     area = a * b / 2
#
# print(f'The area of the triangle is {area}')

# Exercise 1.6 | Tickets
"""
Assumptions:
	- 0-6   - kindergarten - ticket price: 0
	- 7-17  - school       - ticket price: 2.28
	- 18-64 - adult        - ticket price: 3.80
	- +65   - pensioner    - ticket price: 1.90

Write a program that will ask a user for his age and a number of tickets he'd like to buy.

Based on the assumptions above calculate the price he should pay for the tickets.

"""

# age = int(input('Please provide your age: '))
# tickets = int(input('How many tickets: '))
#
# kindergarden_price = 0
# school_price = 2.28
# adult_price = 3.80
# pensioner_price = 1.90
#
# if age <= 6:
#     price = kindergarden_price
# elif 7 <= age <= 17:
#     price = school_price
# elif 18 <= age < 65:
#     price = adult_price
# else:
#     price = pensioner_price
#
# payment = price * tickets
# print(payment)


### Exercise 1.7 | Counting prices
"""
Ask a user for a product he'd like to byt, its quantity and price. Based on that display proper information.

Example:
What would you like to buy? - tomatoes
Provide a price - 5
Provide quantity - 10

For tomatoes, you'd like to buy, you have to pay 50 PLN.
"""

# Option I

"""
tomatoes = 10
eggplant = 12
potatoes = 6

what = input('What would you like to buy? ')
quantity = float(input('How many kg? '))

payment = 0
if what == 'tomatoes':
  payment = tomatoes * quantity
elif what == 'potatoes':
  payment = potatoes * quantity
elif what == 'eggplant':
  payment = eggplant * quantity
else:
    print(f'We are not selling {what}')

print(f'You should pay {payment}')
"""

# Option II
"""
vegetables = {'tomato': 10, 'potato': 6, 'eggplant': 12}
what = input('What would you like to buy? ')

payment = 0

if what in vegetables:
    quantity = float(input('How many kg? '))
    payment = quantity * vegetables[f'{what}']
    print(f'You should pay {payment}')
else:
    print(f'We are not selling {what}')
"""

# Exercise 1.8 | Dog age calculator
"""
Let's assume that 1 dog year equals 5 human years.

Ask a user what is the name of his dog and how old is he and calculate dogs age, if he would be a human. 

Example:
Provide name of the dog - Lassie
Provide dogs age - 3

If Lassie was a human, would have 15 years.
"""

# name = input('What is the name of the dog? ')
# age = float(input('How old is he? '))
#
# human_age = age * 5
# print(f'If {name} was a human, would have {human_age:.0f} years')


# Exercise 1.9 FizzBuzz
"""
Write a Python program which iterates the integers from 1 to 100.
For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".
"""

# for number in range(1, 18):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

# Exercise 2.1 | Math quiz
"""
Write a program that will draw two numbers from the range from 0 do 99. Display those numbers and ask the user what is the
sum of them (do not display the result). Ask user for a correct answer till he provides a correct one.
"""

# from math import sqrt
# print(sqrt(16))


"""
from random import randint
first = randint(0, 99)
second = randint(0, 99)
result = first + second

print(first)
print(second)

while True is True:
    summary = int(input("Please provide the sum of the two given numbers: "))
    if summary == result:
        print("Good job")
        break
    else:
        print("Please calculate correctly!")

print("After loop")
"""

# Exercise 2.2 | Christmas tree
"""
Write a program that reads from the user an integer and then displays a Christmas tree with that many levels with provided
number of levels.
For example, for 3 display:

    *
  * * *
* * * * *
"""

star = '*'
integer = int(input('Please provide and integer: '))
number = 1
start = 1
space = integer
while number <= integer:
    print((space * ' '),(start * star),(space * ' '))
    start += 2
    number += 1
    space -= 1


# Exercise 2.3
"""
Write a program that will read numbers from the user, use `STOP` as a command to stop reading numbers.
Then, display the following stats:
- number of provided numbers, how many
- sum, 
- average, 
- minimum
- maximum

In one version use build-in functions in the other not.
"""

# my_list = []
# while True is True:
#     data = input("Please provide a number: ")
#     if data == 'STOP':
#         break
#
#     try:
#         my_list.append(int(data))   # adding numbers to my_list list
#     except ValueError:
#         # in case there will be not a <number>(eg 10qw, 8ty) or 'STOP' will give us error
#         print('Please provide a valid number!')
#         # continue means go up and continue while loops
#         continue
#
# if len(my_list) == 0:
#     # we write stop in the first attempt means there is no number for displaying and other calculations
#     print('You did not provide any number!')
# else:
#     average = sum(my_list) / len(my_list)
#     print(f'Provided numbers: {my_list}')
#     print(f'Count - {len(my_list)}')
#     print(f'Sum  - {sum(my_list)}')
#     print(f'Average - {average}')
#     print(f'Minimum - {min(my_list)}')
#     print(f'Maximum - {max(my_list)}')


# Exercise 2.4 | Guess a number
"""
Write a program that will draw a number from a range from 0 to 999. The users task is to guess that number.
When the user provides wrong number, give him a hint, whether the number he is looking for is bigger or smaller from the one he gave.
"""

# from random import randint
#
# secret_number = (randint(0, 999))
# print(secret_number)
#
# while True:
#     guessed = int(input("Guess the number: "))
#     if guessed == secret_number:
#         break
#     elif guessed > secret_number:
#         print('Go down')
#     elif guessed < secret_number:
#         print('Go up')
#     continue
#
# print(f'You rock, {guessed} is the correct number!')

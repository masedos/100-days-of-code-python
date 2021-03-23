#!/usr/bin/env python

__version__ = '0.0.2'
__author__ = 'Fernandes Macedo'
__email__ = 'masedos@gmail.com'

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print('Yu can ride the rollercoaster')
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print(f"Your tickets are ${bill}.")
  elif age <= 18:
    bill = 7
    print(f"Your tickets are ${bill}.")
  elif age < 22:
    bill = 11
    print(f"Your tickets are ${bill}.")
  else:
    bill = 15
    print(f"Adult tickets are ${bill}.")
  photo = input("Do you want a photo taken? (Y/N) ")
  if photo == 'Y' or 'y':
    bill += 3 
    print(f"You final bill is ${bill}")
else:
  print("Sorry, you have to grow taller before you can ride")

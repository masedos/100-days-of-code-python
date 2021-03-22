#!/usr/bin/env python

__version__ = '0.0.1'
__author__ = 'Fernandes Macedo'
__email__ = 'masedos@gmail.com'

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print('Yu can ride the rollercoaster')
  age = int(input("What is your age? "))
  if age < 12:
    print("Please pay $5.")
  elif age <= 18:
    print("Please pay $7.")
  elif age < 22:
    print("Please pay $15.")
  else:
    print("Please pay $17.")
else:
  print("Sorry, you have to grow taller before you can ride")

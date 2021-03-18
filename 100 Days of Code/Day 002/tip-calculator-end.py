#!/usr/bin/env python

__version__ = '0.0.1'
__author__ = 'Fernandes Macedo'
__email__ = 'masedos@gmail.com'

print("Welcome to the tip calculator")
bill = float(input('What was the total bill? $'))
people = int(input('How many people to split the bill? '))
tip = float(input('What the percentage tip would you like to give? 10, 12, or 15? '))

each = ((bill  * tip / 100) + bill) / people

print(f"Each person should pay: ${each:.1f}")
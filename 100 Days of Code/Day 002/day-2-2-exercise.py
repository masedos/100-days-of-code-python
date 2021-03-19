#!/usr/bin/env python

__version__ = '0.0.1'
__author__ = 'Fernandes Macedo'
__email__ = 'masedos@gmail.com'

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

print(int(weight / (height * height)))

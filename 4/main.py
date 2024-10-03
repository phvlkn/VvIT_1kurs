import math
import datetime
from modules.module import sumTwoNums
from modules.module1 import *

a = int(input("Enter a number: "))
print(math.sqrt(a))
print(datetime.datetime.now())
a, b = splitBySpaces(input("Enter two numbers:"))
print(sumTwoNums(a, b))
s = str(input("Enter a string: "))
print(splitBySpaces(s))
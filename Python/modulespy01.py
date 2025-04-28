# built in modules in python

import random
import math
import datetime
import os
import sys
import time


random_number = random.randint(1, 10)
print(f"Random number is : {random_number}")

# maths

print(f"Square root of 529065 is {math.sqrt(529065)}")
print(f"Pi is {math.pi}")
print(f"Floor of 5.7 is {math.floor(5.7)}")

# dates
current_time = datetime.datetime.now()
print(f"Current time is : {current_time}")
print(f"Todays date : {datetime.date.today()}")
print(f"Current year : {datetime.date.today().year}")

# os
current_directory = os.getcwd()
print(f"Current directory : {current_directory}")
print(f"List of files : {os.listdir('.')}")


# time
print("waiting for 3 seconds...")
time.sleep(3)
print("done !! ")

# sys
print(f"python version : {sys.version}")
print(f"Platform : {sys.platform}")

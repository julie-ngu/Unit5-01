# Created by: Julie Nguyen
# Created on: Nov 2017
# Created for: ICS3U
# This program makes an array of 10 random number from 1 to 100 then calculates the average of these 
# numbers

from numpy import random

# input
counter = 0
random_numbers = []

# process
while counter < 10:
    single_number = random.randint(1, 100 + 1)
    print(single_number)
    random_numbers.append(single_number)
    counter = counter + 1

total = 0

for single_number in random_numbers:
    total = total + single_number

average = total / len(random_numbers)

# output
print("\nThe average of the array is " + str(average) + ".")

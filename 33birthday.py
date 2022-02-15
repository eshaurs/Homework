#!/usr/bin/env python3

# You are probably well aware of the 'birthday paradox'
# https://en.wikipedia.org/wiki/Birthday_problem
# Let's try simulating it

# You will need a list for the 365 day calendar
# You will need a set number of people (e.g. 25)
# During each 'trial' you do the following
#	Choose a person
#	Git them a random birthday
#	Store it in the calendar
# Once you have stored all birthdays, check to see if any have the same day
# Do this for many trials to see what the probability of sharing a birthday is

import random
trials = 10000
days = 365
people = 22
matches = 0

# Making the calendar
for t in range(trials):
	calendar = [] # supposed to hold the number of birthdays on a date
	for i in range(days):
		calendar.append(0)

	for j in range(people):
		calendar[random.randint(0, days-1)] += 1
		
	for item in calendar:
		if item > 1: 
			matches += 1
			break

print(matches/trials)

"""
python3 33birthday.py
0.571
"""


# This is just a practice exercise for Jan 27. We're trying to make sure that FizzBuzz
# is divisible by 4 or 8
"""
for i in range(1, 45):
	if i % 3 == 0 and i % 8 == 0:
		print('FizzBuzz')  # one liners don't have to be "tabbed" like this. 
	elif i % 3 == 0:
		print('Buzz')
	elif i % 8 == 0:
		print('Fizz')
	else: 
		print(i)
"""	
# Another Exercise: double running sum
runningSum = 0
factorial = 1

for i in range(6):
	v = i*2
	runningSum += v
	print(i, v,runningSum)

	
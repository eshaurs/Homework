import random

trials = 100000
limit = 6

for dc in range(1, 20):

	adv = 0   # max of d1 and d2
	dis = 0
	plus = [0]*limit # fill with zeros

	for i in range(trials):
		d1 = random.randint(1,20)
		d2 = random.randint(1,20)
		if max(d1, d2) >= dc: adv += 1
		if min(d1, d2) >= dc: dis += 1
		for bonus in range(limit):
			if d1 + bonus >= dc: plus[bonus] += 1
	# print(dc, adv, dis, plus)	
	print(f'{dc}\t{adv/trials:.4f}\t{dis/trials:.4f}',end='')
	for v in plus:
		print(f'\t{v/trials:.4f}', end='')
	print()
# reversed ages

# age, age, reversals, pairs
# looking for 8 reversals total then eyeball the pairs

diffs = {}

# assume having child between 14 and 60
for diff in range(14, 60):
	pairs = []
	son = 0
	mom = diff
	while mom < 120:
		# assuming different birthdays, there are 2 chances each year for a reversal
		if str(son).zfill(2)[::-1] == str(mom) or str(son).zfill(2)[::-1] == str(mom+1):
			pairs.append([son, mom])
		mom += 1
		son += 1
	diffs[diff] = pairs

#print(diffs)

for pairs in diffs.values():
	if len(pairs) == 8:
		print(pairs)
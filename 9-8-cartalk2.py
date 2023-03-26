# palendromic odometer

# 6 digit numbers
# last 4 palendrome
# add 1, last 5 palendrome
# add 2, middle 4 panendrome
# add 3, all panendrome

def is_palindrome(word):
	return word == word[::-1]

for miles in range(99999, 1000000):
	milage = str(miles)
	if is_palindrome(milage[-4:]):
		if is_palindrome(str(miles+1)[-5:]):
			if is_palindrome(str(miles+2)[1:-1]):
				if is_palindrome(str(miles+3)):
					print(miles, miles+1, miles+2, miles+3)
"""Exercises from chapter 5 of Think Python"""

import time

"""5-1: checking epoch time"""

epoch = time.time()

# current hour is the number of seconds in the current day divided by the number of seconds each hour
print(f'The current hour is {epoch % (24 * 60 * 60) // (60*60)}')

# current minutes
print(f'The current minute in the day is {epoch % (24 * 60 * 60) // (60)}')

print(f'The current seconds in the day is {epoch % (24 * 60 * 60)}')

print(f'The number of days since the epoch is {epoch // (24 * 60 * 60)}')

""" 
5-2: Fermat's last theorem 
"""

def check_fermat(a, b, c, n):
	if n > 2 and a**n + b**n == c**n:
		return 'Holy shit Fermat was wrong!'
	else:
		return 'Nope, that didn\'t work'

a = input('enter value for a: ')
b = input('enter value for b: ')
c = input('enter value for c: ')
n = input('enter value for n: ')

a,b,c,n = int(a),int(b),int(c),int(n)

print(check_fermat(a,b,c,n))
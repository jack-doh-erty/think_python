""" 16-2 birthdays """

from datetime import datetime

def current_day():
	today = datetime.today()
	print(f'current time is {today}')
	print(today.strftime('%A'))

def next_birthday(birthday):
	"""
	Takes a birthday as input
	print the user's current age and the time until their next birthday
	"""

	today = datetime.today()

	age = today - birthday
	print(f'age in years is {round(age.days/365, 1)}')

	this_year_bday = birthday.replace(year = today.year)

	if this_year_bday < today:
		next_bday = birthday.replace(year = today.year +1)
	else:
		next_bday = this_year_bday

	time_until_next_birthday = next_bday - today
	print(f'next birthday in {time_until_next_birthday}')


def double_day(d1, d2):
	"""
	returns the "double day" of 2 birthdays, when the oldest is double the age of the youngest
	"""
	first = min(d1, d2)
	last = max(d1, d2)
	return last + (last - first)


if __name__ == '__main__':
	current_day()

	birthday = datetime(year=1994, month=1, day=10)
	birthday2 = datetime(year=1996, month=10, day=13)

	next_birthday(birthday)
	print(double_day(birthday, birthday2))
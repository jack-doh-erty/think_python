x = y = 1

print(x,y)
print(x,y);
print(x,y)

print(x*y)

# volume of a sphere
r = 5
pi = 3.142
vol = (4/3) * pi * r**3
print(vol)

# price of books
n = 60

unit_price = 24.95 * 0.6
shipping = 3 + (n - 1) * 0.75

# total cost
print((unit_price * n) + shipping)

# running time 

from datetime import datetime, time
from datetime import timedelta

total_time = 2 * (8 * 60 + 15) + 3 * (7 * 60 + 12)

total_time_2 = 2 * timedelta(minutes = 8, seconds = 15) + 3 * timedelta(minutes = 7, seconds = 12)

start_time = datetime(2023, 1, 1 , 6, 52, 0)
start_time_2 = time(6,52,0)
end_time = start_time + timedelta(seconds = total_time)

print(start_time, end_time)
print(end_time.second)    

print(start_time + total_time_2)

import time
from math import floor

def day_of_week(year, month, day):
 
    d = day
    m = (month - 3) % 12 + 1
    if m &gt; 10: Y = year - 1
    else: Y = year
    y = Y % 100
    c = (Y - (Y % 100)) / 100
 
    w = (d + floor(2.6 * m - 0.2) + y + floor(y/4) + floor(c/4) - 2*c) % 7
 
    return int(w)
 
"""
Compute the number of months starting on a given day of the week in a century
"""
def months_start_range(day,year_start,year_end):
    total = 0
    for year in range(year_start, year_end + 1):
        for month in range(1,13):
            if day_of_week(year, month, 1) == day: total += 1
    return total
 
start = time.time()
 
total = months_start_range(0,1901,2000)
 
elapsed = time.time() - start
 
print("%s found in %s seconds") % (total,elapsed)

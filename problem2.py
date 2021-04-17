"""
-------------------------------------------------------------------------------
Name:   main.py
Purpose:  distance per day 

Author: me

Created:  date in today
------------------------------------------------------------------------------
"""
print("travel log")

###starts the thing###
time = 0
dist = 0
travelled = 0
###does the math###
while travelled < 100:
  dist = float(input("Enter the distance travelled for the day: "))
  travelled = travelled + dist
  time = time + 1

average = travelled // time

average = round(average,0)
print ("The average distance driven per day is " + str(average))
print("It took", str(time) ,"days to surpass 100km driven.")
###final statemets###
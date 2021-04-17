"""
-------------------------------------------------------------------------------
Name:   main.py
Purpose:  count wins or smth idk

Author: me

Created:  date in today
------------------------------------------------------------------------------
"""
###the range  and counter###
print("tournament log")
for x in range(1,7):
  result = str(input("W or L: "))
  if result == "W": 
     win = win + 1
###supposed to track what bracket you are in###
if result == 5 or result == 6:
  print("Your team is in Group 1")
elif result == result == 3 or result == 4:
  print("Your team is in Group 2")
elif result == result == 1 or result == 2:
  print("Your team is in Group 3")
else:
  print("Your team is eliminated from the tournament")
###it does not even work ###
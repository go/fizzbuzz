#!/usr/bin/env python

import sys

"""
check provided number
"""
def check_num(num):
  for x in range(1,num+1):
    if (x%15 == 0):
      sys.stdout.write("FizzBuzz\n")
    elif (x%3 == 0):
      sys.stdout.write("Fizz\n")
    elif (x%5 == 0):
      sys.stdout.write("Buzz\n")
    else:
      sys.stdout.write("%i\n" % (x,))

"""
Main funtion
"""
if __name__ == "__main__":
  try:
    end = int(sys.argv[1])
    check_num(end)
  except ValueError:
    sys.stdout.write("Please try with Interger argument\n")


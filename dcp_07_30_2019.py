"""
Daily Coding Problem - 07/30/2019

This problem was recently asked by Google.

Given a list of numbers and a number k, 
return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""
import sys
from input_conversor import string_to_list
import pdb

# Time Complexity O(n + nlog(n)) => O(nlog(n)), where n is the list size
def check_list(l,k):
  if len(l) > 1:
    l.sort() # timsort O(nlog(n))
    j = len(l)-1
    i = 0
    while i < j: # O(n)
      r = l[i] + l[j]
      if r == k:
        return True
      elif r > k:
        j = j - 1
      else:
        i = i + 1
  return False

if __name__ == "__main__":
  if len(sys.argv) == 3:
    l = string_to_list(sys.argv[1])
    k = int(sys.argv[2])
    if l != None:
      if check_list(l,k):
        print("Two numbers add up to k")
      else:
        print("There aren't two numbers that add up to k")
    else:
        print("Error processing list")
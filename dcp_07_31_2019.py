"""
Daily Coding Problem - 07/31/2019

This problem was asked by Uber.

Given an array of integers, return a new array such that each 
element at index i of the new array is the product of all the numbers 
in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be 
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""
from functools import reduce
import sys
from input_conversor import string_to_list
import pdb

# Time Complexity: O(n) + O(n) => O(n), where n is the list size
def special_product_with_division(l):
  total_mult = reduce(lambda x, y: x*y, l, 1)
  new_l = map(lambda x: total_mult/x, l)
  return list(new_l)

# Time Complexity: O(n²/2), where n is the list size
# Uses an accumulator to keep values already multiplicated,
# so the multiplication from the numbers before i don't need to be done again
def special_product_without_division(l):
  size = len(l)
  if size == 0:
    return []
  if size < 2:
    return [1]

  multiplication_accumulator = 1 
  new_list = []

  for i in range(0,size):
    i_value = multiplication_accumulator
    for j in range(i+1, size):
      i_value = i_value * l[j]

    new_list.append(i_value)
    multiplication_accumulator = multiplication_accumulator * l[i]
  
  return new_list

if __name__ == "__main__":
  if len(sys.argv) == 2:
    l = string_to_list(sys.argv[1])
    if l != None:
      print("New array using division: {}".format(special_product_with_division(l)))
      print("New array not using division: {}".format(special_product_without_division(l)))
    else:
      print("Invalid number list {}".format(sys.argv[1]))
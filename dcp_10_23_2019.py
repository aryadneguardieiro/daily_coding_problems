"""
Daily Coding Problem - 10/23/2019 - Medium
This problem was asked by Google.

Given a string of parentheses, write a function to compute the minimum number of parentheses to be removed to make the string valid (i.e. each open parenthesis is eventually closed).

For example, given the string "()())()", you should return 1. Given the string ")(", you should return 2, since we must remove all of them.
"""

#Time complexity O(N), where N is the string size
def spare_parenthesis_counter(input_string):
  spare = 0
  openning = 0
  for c in input_string:
    if c != '(' and c !=')':
      raise Exception("Invalid char '{}' found, input should contain just ')' or '('. ".format(c))
    if c == '(':
      spare = spare + 1
      openning = openning + 1
    elif c == ')' and openning > 0:
      spare = spare - 1
      openning = openning - 1
    else:
      spare = spare + 1
  return spare

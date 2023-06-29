""" 
Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on
a separate line, except backwards.
"""

my_string = "En algun lugar de un gran pais"

index = -1
length = len(my_string)
neg_len = length * -1
while index >= neg_len:
  print(my_string[length + index])
  index -= 1
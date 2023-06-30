"""
def count(lett, stri):
  count = 0
  letter = lett.lower()
  string = stri.lower()
  for char in string:
    if char == letter:
      count = count + 1
  print(count)

  READ DOCUMENTATION, SEARCH FOR BUILT-IN FN
  instead of reinventing the wheel
"""

letter = input("Letter you want to count: ").lower()
string = input("Text you want to analyze: ").lower()

print(string.count(letter))

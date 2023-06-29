# read numbers until the user input “done”.

# Once “done” is entered, print out the total, count, and average of the numbers

def output(arr):
  print(sum(arr), len(arr), (sum(arr)/len(arr)))


nums = []
while True:
    try:
      user_input = input("Enter number: ")
      if user_input == 'done':
        output(nums)
        break      
      nums.append(float(user_input))
    except:
      print("Invalid input")
      continue

def output(arr):
  print(max(arr), min(arr))


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

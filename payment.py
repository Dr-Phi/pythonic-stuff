def computepay(hours, rate):
  if hours > 40:
    extra = hours - 40
    pay = (40 * rate) + (extra * (rate + rate/2))
    print("Pay: " + str(pay))
  else:
    print("Pay: " + str(hours * rate))


try:
  hours = float(input("Enter Hours: "))
  rate = float(input("Enter Rate: "))
  computepay(hours, rate)
except:
  print("Error, please enter a number")


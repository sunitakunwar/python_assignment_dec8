
'''Define a function to determine whether the user's integer input is a even number or an odd number.'''


number = int(input("Enter a number: "))

if (number % 2) == 0:
     print("{0} is an Even Number".format(number))

else:
     print("{0} is an Odd Number".format(number))

# Prompt the user to enter an integer number
x = int(input("Enter an integer number: "))


# Determine if the number is even or odd
#   If it is even print (e.g.) "4 is even."
#   If it is odd, print (e.g.) "7 is odd."

if x % 2 == 0:
    print(f"{x} is even.")
else:
    print(f"{x} is odd.")

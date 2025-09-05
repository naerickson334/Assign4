# Prompt the user to enter the number of hours worked
# Convert the input to a float to handle decimal hours
hours = float(input("How many hours did you work this week? "))
if hours < 0:
    print("Hours and rate should be positive.")
    sys.exit
# Prompt the user to enter the hourly rate
# Convert the input to a float to handle decimal hours
rate = float(input("How much do you get paid per hour? "))
if rate < 0:
    print("Hours and rate should be positive.")
    sys.exit

# If either is negative Print an error
# message if either hours or rate is negative "Hours and rate should be
# positive"


# Otherwise, if the number of hours worked is greater than 40 you need to
# calculate pay + overtime
    # Calculate the number of overtime hours.
    # Calculate and print the gross pay including overtime pay using the format:
    #   `Your gross pay is $AMOUNT`
    # Don't forget about order of operations!!
if hours <= 40:
    pay = hours * rate
else:
    normal_pay = rate * 40
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * (rate * 1.5)
    pay = normal_pay + overtime_pay

# Otherwise the number of hours worked is 40 or less, so calculate regular pay
    # Calculate and print the gross pay using the format:
    #   `Your gross pay is $AMOUNT`
print(f"Your gross pay is ${pay:.2f}")


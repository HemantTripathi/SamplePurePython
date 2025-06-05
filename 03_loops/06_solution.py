# Factorial Calculator
# Problem : Compute the factorial of a number using a while loop

user_input = int(input("Enter a int value: "))
factorial = 1

while user_input > 0:
    factorial *= user_input
    user_input -= 1
print(factorial)




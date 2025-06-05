# Prime Number Checker
# Problem : Check if number id prime

user_input = int(input("Enter a number: "))
is_prime = True

if user_input > 1:
    for i in range(2, user_input):
        if (user_input % i) == 0:
            is_prime = False
            break
    print(is_prime)



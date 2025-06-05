# Multiplication table printer
# Problem : Print the multiplication table for a given number upto 10, but skip the fifth iteration

user_input = int(input("Enter a given number: "))
sum_even = 0
for i in range(1, 11):
    #if i != 5:
    if i == 5:
        continue
    print(user_input, ' X ', i, '=', user_input * i)



# Sum of even numbers
# Problem : Calculate the sum of the even numbers upto a given numbers n

user_input = int(input("Enter a given number: "))
sum_even = 0
for i in range(1, user_input + 1):
    if i % 2 == 0:
        sum_even += i
print(f"Sum of even numbers is: {sum_even}")


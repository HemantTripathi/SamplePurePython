# Reverse a String
# Problem : Reverse a String using loop

user_input = input("Enter a String value: ")
string_reverse = ""

for value in user_input:
    string_reverse = value + string_reverse
print(string_reverse)




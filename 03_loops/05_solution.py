# Find the First Non-Repeated Character
# Problem : Given a  String, find the first non-repeated character

user_input = input("Enter a String value: ")
string_reverse = ""

for value in user_input:
    print(value)
    if user_input.count(value) == 1:
        print("Char is: ", value)
        break




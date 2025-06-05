# List Uniqueness Checker
# Problem : check if all the elements in list are unique. If a duplicate is found, exit the loop and print the duplicate
# items = ["apple","banana","orange","apple","mango"]

items = ["apple","banana","orange","apple","mango"]
unique_items = set()

for item in items:
    # print(item)
    if item in unique_items:
        print("Duplicate: {}".format(item))
        break
    else:
        unique_items.add(item)
        print("Add: {}".format(item))



# Fruit Ripeness Checker Problem:
# Determine if a fruit is ripe, overripe, or unripe based on its color.(e.g., Banana: Green-Unripe, Yellow-Ripe, Brown-Overripe)

fruit_name = "Banana"
fruit_color = "Yellow"

if fruit_name == "Banana":
    if fruit_color == "Green":
        print("Unripe")
    elif fruit_color == "Yellow":
        print("Ripe")
    else:
        print("Overripe")
else:print("Please enter the correct fruit")

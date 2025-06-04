# Movie ticket pricing problem : Movie tickets are priced based on age: $12 for adults(18 and over), $8 for children.
# Everyone get a $2 discount on Wednesday

from datetime import datetime
day_name = datetime.today().strftime('%A')

print("Today is :", day_name)
age = 19
price_child = 8
price_adult = 12
discount_rate = 2

if day_name == "Wednesday":
    price_child = price_child - discount_rate
    price_adult = price_adult - discount_rate

if age < 18:
    print("Movie ticket price for children is ${}".format(price_child))
else:
    print("Movie ticket price for Adult is ${}".format(price_adult))

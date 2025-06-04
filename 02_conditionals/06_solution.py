# Transportation Mode Selection :
# Problem : Choose a mode of transportation based on the distance(e.g., <3km : Walk, 3-15km: Bike, >15km: Car)

no_of_kilometers = 60

if no_of_kilometers < 3:
    mode = "Walk"
elif no_of_kilometers <= 15:
    mode = "Bike"
else:
    mode = "Car"

print(mode)



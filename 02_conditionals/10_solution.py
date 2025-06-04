# Pet Food recommendation
# Problem : Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2years - Puppy food, Cat: > 5 years - Senior cat food)

pet_species = input("Enter Pet Species: ")
pet_age = int(input("Enter Pet's Age: "))

if pet_species == "Dog":
    if pet_age < 2:
        print("Puppy food")
    else:
        print("Adult food")
elif pet_species == "Cat":
    if pet_age > 5:
        print("Senior cat food")
    else:
        print("Junior cat food")
else:
    print("Sorry, Mentioned Pet is Not defined.")






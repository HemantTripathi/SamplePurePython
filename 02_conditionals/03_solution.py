# Grade Calculator Problem : Assign a letter grade based on a student's score: A(90-100), B(80-89), C(70-79), D(60-69), F(below 60)

score = 60

if score > 100:
    print("Please check your score again and enter it correctly.")
    exit()

if score > 89:
    print("A")
elif score > 79:
    print("B")
elif score > 69:
    print("C")
elif score > 59:
    print("D")
else:
    print("F")

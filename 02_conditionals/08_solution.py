# Password strength checker
# Problem : Check if password is "Weak","Medium, or "Strong". Criteria: < 6 chars(Weak), 6-10 chars(Medium), >10 chars(Strong)

entered_password = "sdasdh234"
pwd_length = len(entered_password)
print(pwd_length)

if pwd_length < 6:
    strength = "Weak"
elif pwd_length <= 10:
    strength = "Medium"
elif pwd_length > 10:
    strength = "Strong"

print(strength)




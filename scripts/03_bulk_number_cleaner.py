import phonenumbers

numbers = [
    "+91900000000",
    "+911234567890",
    "12345",
    "+447911123456"
]

valid_numbers = []

for n in numbers:
    try:
        p = phonenumbers.parse(n)
        if phonenumbers.is_valid_number(p):
            valid_numbers.append(n)
    except:
        pass

print("Valid numbers:", valid_numbers)

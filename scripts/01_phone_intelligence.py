import phonenumbers
from phonenumbers import carrier, geocoder

number = "+91900000000"  # dummy example number

p = phonenumbers.parse(number)

print("Valid:", phonenumbers.is_valid_number(p))
print("Country:", geocoder.description_for_number(p, "en"))
print("Carrier:", carrier.name_for_number(p, "en"))


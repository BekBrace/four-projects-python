# pipenv shell
# pipenv install phonenumbers

import phonenumbers
from phonenumbers import timezone, geocoder, carrier

number = input('Enter the phone number 📱 >>> ')
phonenumber = phonenumbers.parse(number)

timezone = timezone.time_zones_for_number(phonenumber)

carrier = carrier.name_for_number(phonenumber, 'en')

region = geocoder.description_for_number(phonenumber, 'en')


if __name__ == "__main__":
    print(phonenumber)
    print("Time Zone : " + str(timezone))
    print("Carrier : " + carrier)
    print("Region : " + region)

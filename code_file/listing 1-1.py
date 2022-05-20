from geopy.geocoders import Nominatim

if __name__ == '__main__':
    address = 'taj mahal'
    user_agent = 'Network Programming in Python: The Basics.py'
    location = Nominatim(user_agent=user_agent).geocode(address)
    print(location.latitude, location.longitude)

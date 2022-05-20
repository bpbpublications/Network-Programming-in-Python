import requests

def geocode(address):
    base = 'https://nominatim.openstreetmap.org/ui/search.html'
    parameters = {'q': address, 'format': 'json'}
    user_agent = ' Client-Server Networking: An Overview search2.py'
    headers = {'User-Agent': user_agent}
    response = requests.get(base, params=parameters, headers=headers)
    reply = response.json()
    print(reply[0]['lat'], reply[0]['lon'])

if __name__ == '__main__':
    geocode('taj mahal.agra,uttar pradesh')

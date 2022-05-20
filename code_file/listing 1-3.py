import http.client
import json
from urllib.parse import quote_plus

base = '/search'

def geocode(address):
    path = '{}?q={}&format=json'.format(base, quote_plus(address))
    user_agent = b'Client-Server Networking: An Overview.py'
    headers = {b'User-Agent': user_agent}
    connection = http.client.HTTPSConnection('nominatim.openstreetmap.org')
    connection.request('GET', path, None, headers)
    rawreply = connection.getresponse().read()
    reply = json.loads(rawreply.decode('utf-8'))
    print(reply[0]['lat'], reply[0]['lon'])

if __name__ == '__main__':
    geocode('taj mahal')
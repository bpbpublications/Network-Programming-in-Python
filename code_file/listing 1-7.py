import socket

if __name__ == '__main__':
    hostname = 'maps.google.com'
    addr = socket.gethostbyname(hostname)
    print('The IP address of {} is {}'.format(hostname, addr))
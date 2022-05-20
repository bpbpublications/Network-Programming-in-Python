import socket, sys, zen_utils

if __name__ == '__main__':
    listener = socket.fromfd(0, socket.AF_INET, socket.SOCK_STREAM)
    sys.stdin = open('/dev/null', 'r')
    sys.stdout = sys.stderr = open('/tmp/zen.log', 'a', buffering=1)
    listener.settimeout(8.0)
    try:
        zen_utils.accept_connections_forever(listener)
    except socket.timeout:
        print('Waited 8 seconds with no further connections; shutting down')
import socket, sys, zen_utils

if __name__ == '__main__':
    sock = socket.fromfd(0, socket.AF_INET, socket.SOCK_STREAM)
    sys.stdin = open('/dev/null', 'r')
    sys.stdout = sys.stderr = open('/tmp/zen.log', 'a', buffering=1)
    address = sock.getpeername()
    print('Accepted connection from {}'.format(address))
    zen_utils.handle_conversation(sock, address)
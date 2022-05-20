from socketserver import BaseRequestHandler, TCPServer, ThreadingMixIn
import zen_utils

class ZenHandler(BaseRequestHandler):
    def handle(self):
        zen_utils.handle_conversation(self.request, self.client_address)

class ZenServer(ThreadingMixIn, TCPServer):
    allow_reuse_address = 1
    # address_family = socket.AF_INET6  # uncomment if you need IPv6

if __name__ == '__main__':
    address = zen_utils.parse_command_line('legacy "SocketServer" server')
    server = ZenServer(address, ZenHandler)
    server.serve_forever()
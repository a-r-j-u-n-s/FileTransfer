import socket
import argparse
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import functools

# ADD GUI

PORT = 8080
DIRECTORY = "media"
parser = argparse.ArgumentParser(description='Serve files from the media \
                                 directory.')

host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)

parser.add_argument('--host', default=ip, type=str, required=False,
                    help='Specify the ip address to listen on.')

parser.add_argument('--port', default=PORT, type=int, required=False,
                    help='Specify the port to listen on.')

args = parser.parse_args()

handler = functools.partial(SimpleHTTPRequestHandler, directory=DIRECTORY)

with TCPServer((args.host, args.port), handler) as httpd:
    print(f'Server is listening on {args.host} on port {args.port}.')
    httpd.serve_forever()
import socket
import argparse
import http.server
import socketserver

# ADD GUI

parser = argparse.ArgumentParser(description='Serve files from the current \
                                 directory.')

host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)

parser.add_argument('--host', default=ip, type=str, required=False,
                    help='Specify the ip address to listen on.')

parser.add_argument('--port', default=8080, type=int, required=False,
                    help='Specify the port to listen on.')

args = parser.parse_args()

handler = http.server.SimpleHTTPRequestHandler


with socketserver.TCPServer((args.host, args.port), handler) as httpd:
    print(f'Server is listening on {args.host} on port {args.port}.')
    httpd.serve_forever()
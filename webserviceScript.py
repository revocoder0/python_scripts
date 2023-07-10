import socketserver
import http.server

PORT = 1998

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT),Handler) as httpd:
    print("Serving at prot ", PORT)
    httpd.serve_forever()
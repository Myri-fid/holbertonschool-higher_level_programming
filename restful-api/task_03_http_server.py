import http.server
import json

class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        if self.path == '/':
            self.wfile.write(b'Hello, this is a simple API!')
        elif self.path == '/data':
            response = json.dumps({"name": "John", "age": 30, "city": "New York"})
            self.wfile.write(response.encode('utf-8'))
        elif self.path == '/info':
            response = json.dumps({"version": "1.0", "description": "A simple API built with http.server"})
            self.wfile.write(response.encode('utf-8'))
        elif self.path == '/status':
            self.wfile.write(b'OK')
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Endpoint not found')

if __name__ == '__main__':
    httpd = http.server.HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    print('Le serveur démarre sur le port 8000...')
    httpd.serve_forever()


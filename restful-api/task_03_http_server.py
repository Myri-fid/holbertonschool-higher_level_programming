import http.server
import json
"""
basic web server using the http.server module
"""


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """
    basic web server using the http.server module
    """

    def do_GET(self):
        """
        server class to serve a sample JSON data when the endpoint
        """

        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = json.dumps({"name": "John",
                                   "age": 30, "city": "New York"})
            self.wfile.write(response.encode('utf-8'))
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = json.dumps({"version": "1.0",
                                   "description":
                                   "A simple API built with http.server"})
            self.wfile.write(response.encode('utf-8'))
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
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

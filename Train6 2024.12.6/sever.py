from http.server import BaseHTTPRequestHandler,HTTPServer

PORT_NUMBER = 8080

# This class will handle any incoming request from a browser
class MyHandler(BaseHTTPRequestHandler):
    # Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write("Hello World!".encode())
        return


try:
    # Create a web server and define the handler to manage the incoming request
    server = HTTPServer(('localhost', PORT_NUMBER), MyHandler)
    print ('Started httpserver on port ' , PORT_NUMBER)
    # Wait forever for incoming http requests
    server.serve_forever()

except KeyboardInterrupt:
    print ('^C received, shutting down the web server')
    server.socket.close()
    
    
    




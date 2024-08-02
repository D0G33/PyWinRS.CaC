import base64
from http.server import *
import atexit


encoded = base64.encode("temp")
server = HTTPServer

def exitFunc():
    server.server_close()


def runServer(self,file,port=27555):

    f = open(file,'rb')
    content = f.read()
    encoded = base64.encode(content)

    class createClass(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(encoded)

    server_address = ('', port)
    self.server = HTTPServer(server_address,createClass)
    atexit.register(exitFunc)


import base64
from http.server import *
import atexit

class exit:
    def __init__(self,server):
        self.server = server

    def exitFunc(self):
        self.server.server_exit()
def runServer(file,port=27555):

    f = open(file,'rb')
    content = f.read()
    encoded = base64.b64encode(content)

    class createClass(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(encoded)

    server_address = ('', port)
    server = HTTPServer(server_address,createClass)
    ex = exit(server)
    atexit.register(ex.exitFunc)
    server.serve_forever()

if __name__ == "__main__":
    runServer("olli-the-polite-cat.jpg")
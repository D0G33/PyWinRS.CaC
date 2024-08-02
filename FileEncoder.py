import base64
from http.server import *
import atexit


class exit:
    def __init__(self,server):
        self.server = server

    def exitFunc(self):
        try:
            self.server.server_exit()
        except:
            print('"At Exit" Detected Server is Already Closed')
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
    try:
        server.serve_forever()
    except:
        print("Server Now Closing")

def singleGetServer(file,port=27555):

    f = open(file,'rb')
    content = f.read()
    encoded = base64.b64encode(content)

    class createClass(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(encoded)
            self.server.server_close()


    server_address = ('', port)
    server = HTTPServer(server_address,createClass)
    ex = exit(server)
    atexit.register(ex.exitFunc)
    try:
        server.serve_forever()
    except:
        print("Server Now Closing")

if __name__ == "__main__":
    runServer("olli-the-polite-cat.jpg")
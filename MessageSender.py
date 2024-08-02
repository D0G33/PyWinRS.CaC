import base64
from http.server import *
import atexit
import rsa
import CustomCrypto as cc

class exit:
    def __init__(self,server):
        self.server = server

    def exitFunc(self):
        try:
            self.server.server_exit()
        except:
            print('"At Exit" Detected Server is Already Closed')
def sendMessageEncoded(message,key="veryEpicKey",port=27556):

    secret = cc.encode(message,key)
    encoded = base64.b64encode(secret.encode())
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
    sendMessageEncoded("hello!")
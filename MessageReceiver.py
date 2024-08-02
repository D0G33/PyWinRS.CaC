import base64
import urllib.request
import time
import CustomCrypto as cc

def getMessageEncoded(ip,port,key="veryEpicKey"):
    respone = urllib.request.urlopen("http://"+ip+":"+str(port))
    encoded = respone.read()
    secret = base64.b64decode(encoded).decode()
    content = cc.decode(secret,key)
    return content

if __name__ == "__main__":
    print(getMessageEncoded("10.0.0.144",27556))



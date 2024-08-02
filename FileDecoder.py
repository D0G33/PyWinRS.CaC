import base64
import urllib.request

def decodeFile(ip,port,filetype,filename="output"):
    respone = urllib.request.urlopen("http://"+ip+":"+port)
    encoded = respone.read()
    content = base64.b64decode(encoded)
    f = open(filename+"."+filetype,'wb')
    f.write(content)
    f.close()


if __name__ == "__main__":
    decodeFile("10.0.0.144","27555","jpg")



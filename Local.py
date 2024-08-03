import FileEncoder as fe
import MessageSender as ms
import MessageReceiver as mr
import CustomCrypto as cc
import SevenZip as z7
import socket
from multiprocessing import Process


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


class fileProcess:
    def __init__(self,file):
        self.process = Process(target=fe.runServer, args=(file,))
        self.process.start()

    def stopServer(self):
        self.process.kill()
        #self.process.close()

def sendScreenApp():
    z7.zip("sc.exe")
    fileServer = fileProcess("package.7z")
    ms.sendMessageEncoded("setup")

    fin = mr.getMessageEncoded("10.0.0.153",27557)

    while fin != "finished":
        fin = mr.getMessageEncoded("10.0.0.153",27557)
        pass

    fileServer.stopServer()

if __name__ == "__main__":
    sendScreenApp()

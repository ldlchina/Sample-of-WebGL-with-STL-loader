from threading import Thread
import webbrowser, http.server, socketserver
import time;

port_number = 8000

server = None
def startServer(port):
    Handler = http.server.SimpleHTTPRequestHandler
    global server
    server = socketserver.TCPServer(("", port), Handler)

    print("Start server at port", port)
    server.serve_forever()
   
def start(port):
    thread = Thread(target=startServer, args=[port])
    thread.start()
    
    startTime = int(time.time())
    while not server:
        if int(time.time()) > startTime + 60:
            print("Time out")
            break
    return server

def stop():
    if server:
        server.shutdown()
        
def openUrl():
    url = "http://localhost:" + str(port_number)
    webbrowser.open(url)
    print(url + " is opened in browser")

if __name__ == "__main__":
    start(port_number)
    openUrl()

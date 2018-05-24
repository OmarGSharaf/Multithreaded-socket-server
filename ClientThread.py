import socket, threading, sys
threadLimiter = threading.BoundedSemaphore(5)

class ClientThread(threading.Thread):

    def __init__(self, client_socket, addr, THREAD_INDEX ,BUFFER_SIZE = 20):
        self.THREAD_INDEX = THREAD_INDEX
        threading.Thread.__init__(self)
        self.client_socket = client_socket
        self.addr = addr
        self.BUFFER_SIZE = BUFFER_SIZE
        print "[INFO] connection received from: ", addr[1]

    def run(self):
            threadLimiter.acquire()
            try:
                for x in range (0,1024):
                    data = self.client_socket.recv(self.BUFFER_SIZE)
                    print "[THREAD#%s] %s \n" % (self.THREAD_INDEX, data)

                    self.client_socket.send(data) #echo

                self.client_socket.close()
                print "[INFO] Socket is closed\n"
            except socket.error, e: 
                print "[ERROR] ", e
                sys.exit(True)
            finally:
                threadLimiter.release()

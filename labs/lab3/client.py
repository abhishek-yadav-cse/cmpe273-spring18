import zmq
import sys
from threading import Thread


def sendMessage():
        context_object = zmq.Context()
        socket_object = context_object.socket(zmq.REQ)
        socket_object.connect("tcp://127.0.0.1:6789")
        while True:
        # Send a "message" using the socket
                socket_object.send_string("["+str(sys.argv[1])+"]: " + input("["+str(sys.argv[1])+"]>"))
                sent_message = (socket_object.recv().decode())


def receiveMessage():
        context = zmq.Context()

        # Define the socket using the "Context"
        sock = context.socket(zmq.SUB)

        # Define subscription and messages with prefix to accept.
        sock.setsockopt_string(zmq.SUBSCRIBE, "")
        sock.connect("tcp://127.0.0.1:5432")
        while True:
            message= sock.recv().decode()
            if message.find("["+str(sys.argv[1])+"]: "):
                print("\n"+message+"\n["+str(sys.argv[1])+"] ")        


print("User["+str(sys.argv[1])+"] Connection to chat server is established")
sending_input = (Thread(target=receiveMessage,args=( )))
sending_input.start()

sending_message = (Thread(target=sendMessage,args=( )))
sending_message.start()



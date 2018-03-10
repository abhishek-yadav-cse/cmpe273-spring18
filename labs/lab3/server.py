import zmq
from threading import Thread
message_storage = []


def binding(message_storage):
    context_object = zmq.Context()
    sock_object = context_object.socket(zmq.REP)
    sock_object.bind("tcp://127.0.0.1:6789")
    while True:
        binding_message = str(sock_object.recv().decode())
        sock_object.send_string("Echo: " + binding_message)
        message_storage.append(binding_message)
        #q.put(binding_message)
def unbinding(message_storage):
    context_object1 = zmq.Context()
    sock_object1 = context_object1.socket(zmq.PUB)
    sock_object1.bind("tcp://127.0.0.1:5432")
    while True:
         while len(message_storage) != 0:
            unbinding_message = message_storage.pop()
            sock_object1.send_string(unbinding_message)

unbinding_start = (Thread(target=unbinding,args=(message_storage, )))
unbinding_start.start()

binding_start = (Thread(target=binding,args=(message_storage, )))
binding_start.start()

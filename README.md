# 361
Algo CLI

![fig2](https://user-images.githubusercontent.com/72105939/236315963-1a2a0163-1f3a-4b45-9f74-121163b7c671.png)

Picture source: https://zguide.zeromq.org/docs/chapter1/#Why-We-Needed-ZeroMQ
^ THIS link is a good source to understand whats going on. 

The server is structured like this:


#  Hello World server in Python
   Binds REP socket to tcp://*:5555
   Expects b"Hello" from client, replies with b"World"


    import time
    import zmq

    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")



    while True:
         / Wait for next request from client
      message = socket.recv()
      print(f"Received request: {message}")Do some 'work'
      time.sleep(1)

        / Send reply back to client
      socket.send_string("World")

----------------------------------------------------------------------

The client is like this: 


#   Hello World client in Python
   Connects REQ socket to tcp://localhost:5555
   Sends "Hello" to server, expects "World" back


    import zmq

    context = zmq.Context()

    / Socket to talk to server
 
    print("Connecting to hello world server...")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    / Do 10 requests, waiting each time for a response
 
    for request in range(10):
       print(f"Sending request {request} ...")
       socket.send_string("Hello")

    /  Get the reply.
       message = socket.recv()
       print(f"Received reply {request} [ {message} ]")





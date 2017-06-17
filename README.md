# ServerSocketMultiClienAndInstance
 This program implements a socket server of multiple clients and multiple instances
 
 # Description
 
 This program implements a socket server of multiple clients and multiple
instances.Allows multiple simultaneous connections (thread socket) configured
to start one instances.
    In this example you are configured to listen on ports 3000, 3001, 3002, 3003,
and 3004 allowing for 1000 concurrent connections per instance.


 # Exemple

For RUN server open terminal and type it:
$ python main.py 

If success on initiating the message will be as below:

Server Tests
Server launched on socket: ('0.0.0.0', 3000)
Server launched on socket: ('0.0.0.0', 3001)
Server launched on socket: ('0.0.0.0', 3002)
Server launched on socket: ('0.0.0.0', 3003)
Server launched on socket: ('0.0.0.0', 3004)
Server running ... 2017-06-17 18:06:55.223839
Server running ... 2017-06-17 18:07:05.233936
Server running ... 2017-06-17 18:07:15.244094
Server running ... 2017-06-17 18:07:25.254251

To simulate sockets clients you can use the Netcat tool as in the example:
For exemple port 3000

$ nc 127.0.0.1 3000

#ENJOY

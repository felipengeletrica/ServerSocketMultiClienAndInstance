# ServerSocketMultiClienAndInstance
 This program implements a socket server of multiple clients and multiple instances
 
 # Description
 
 This program implements a socket server of multiple clients and multiple
instances.Allows multiple simultaneous connections (thread socket) configured
to start one instances.
    In this example you are configured to listen on ports 3000, 3001, 3002, 3003,
and 3004 allowing for 1000 concurrent connections per instance.


Exemple:

    To simulate sockets clients you can use the Netcat tool as in the example:
For exemple port 3000

$ nc 127.0.0.1 3000

# ServerSocketMultiClienAndInstance
 This program implements a socket server of multiple clients and multiple instances
 
 # Description
 
 This program implements a socket server of multiple clients and multiple
instances.Allows multiple simultaneous connections (thread socket) configured
to start one instances.<br/>
    <t/>In this example you are configured to listen on ports 3000, 3001, 3002, 3003,
and 3004 allowing for 1000 concurrent connections per instance.


 # Exemple

For RUN server open terminal and type it:<br/>
<<<<<<< HEAD

$ python main.py 


If success on initiating the message will be as below:

Server Tests
=======
$ python main.py 

If success on initiating the message will be as below:<br/>

Server Tests<br/>
>>>>>>> 30624b05bcf2ca96d8d03a7515cf88b24c94deb4
Server launched on socket: ('0.0.0.0', 3000)<br/>
Server launched on socket: ('0.0.0.0', 3001)<br/>
Server launched on socket: ('0.0.0.0', 3002)<br/>
Server launched on socket: ('0.0.0.0', 3003)<br/>
Server launched on socket: ('0.0.0.0', 3004)<br/>
Server running ... 2017-06-17 18:06:55.223839<br/>
Server running ... 2017-06-17 18:07:05.233936<br/>
Server running ... 2017-06-17 18:07:15.244094<br/>
Server running ... 2017-06-17 18:07:25.254251<br/>

To simulate sockets clients you can use the Netcat tool as in the example:<br/>
<<<<<<< HEAD
Exemple port 3000
=======
For exemple port 3000:<br/>
>>>>>>> 30624b05bcf2ca96d8d03a7515cf88b24c94deb4

$ nc 127.0.0.1 3000<br/>

#ENJOY

# Server  Socket  Multi Cliente and multiple instances

 This program implements a socket server of multiple clients and multiple instances
 
 # Description
 
 This program implements a socket server of multiple clients and multiple
instances.Allows multiple simultaneous connections (thread socket) configured
to start one instances.<br/>
    <t/>In this example you are configured to listen on ports 3000, 3001, 3002, 3003,
and 3004 allowing for 1000 concurrent connections per instance.


 # Exemple running server:

For RUN server open terminal and type it:<br/>


$ python main.py 


If success on initiating the message will be as below:

Server Tests

$ python main.py 

If success on initiating the message will be as below:<br/>

Server Tests<br/>

Server launched on socket: ('0.0.0.0', 3000)<br/>
Server launched on socket: ('0.0.0.0', 3001)<br/>
Server launched on socket: ('0.0.0.0', 3002)<br/>
Server launched on socket: ('0.0.0.0', 3003)<br/>
Server launched on socket: ('0.0.0.0', 3004)<br/>
Server running ... 2017-06-17 18:06:55.223839<br/>
Server running ... 2017-06-17 18:07:05.233936<br/>
Server running ... 2017-06-17 18:07:15.244094<br/>
Server running ... 2017-06-17 18:07:25.254251<br/>


 # Exemple cliente connect port 3000:<br/>

   To simulate sockets clients you can use the Netcat tool as in the example:<br/>
   
$ nc 127.0.0.1 3000<br/>

#ENJOY

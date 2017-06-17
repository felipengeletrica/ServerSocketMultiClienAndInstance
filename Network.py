#!/usr/bin/env python
#Copyright (c) 2017, Felipe Vargas <felipeng.eletrica@gmail.com>
#All rights reserved.
#
#Redistribution and use in source and binary forms, with or without
#modification, are permitted provided that the following conditions are met:
#
#1. Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#2. Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
#ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
#ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
#The views and conclusions contained in the software and documentation are those
#of the authors and should not be interpreted as representing official policies,
#either expressed or implied, of the FreeBSD Project.

import socket
import threading

class ThreadedServer(threading.Thread):
    def __init__(self, host, port, timeout, buffer, maxconection):

        """
        :type host: ip from host use 0.0.0.0  for local address
        :type port: listen port number
        :type timeout: timeout connection
        :type buffer: buffer data
        :type maxconection : maximum simultaneous connections 
        """

        try:
            threading.Thread.__init__(self)
            self.iterations = 0
            self.daemon = True  # OK for main to exit even if instance is still running
            self.paused = True  # start out paused
            self.state = threading.Condition()

            self.host = host
            self.port = port
            self.buffer = buffer
            self.maxconection = maxconection
            self.timeout = timeout
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.sock.bind((self.host, self.port))
            socket_address = self.sock.getsockname()
            print ('Server launched on socket: {!s}'.format(str(socket_address)))
        except:
            raise

    def run(self):

        #print "Starting " + self.name
        self.process = p = threading.Thread(target=self.listen)
        p.daemon = True
        p.start()

    def stop(self):
        #TODO: Function error not stop
        #print "Trying to stop thread "
        self.process.join(self)

    def listen(self):

        self.sock.listen(self.maxconection)
        while True:
            client, address = self.sock.accept()
            print 'Client connected IP: ' + str(address)
            client.settimeout(self.timeout)
            threading.Thread(target=self.listenToClient, args=(client, address)).start()

    def listenToClient(self, client, address):

        while True:
            try:
                data = client.recv(self.buffer)

                if data:
                    # Set the response to echo back the recieved data
                    print "Data", data
                    response = data
                    client.send(response)
                else:
                    print 'Client disconnected'
                    raise
            except:
                client.close()
                return False



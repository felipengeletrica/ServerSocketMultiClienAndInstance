#!/usr/bin/env python
#-*- coding: latin-1 -*-

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

import time
import datetime

import Network


if __name__ == "__main__":
    
    
    print "Server Tests"

    #Start server tests
    
    

    p = Network.ThreadedServer("0.0.0.0", 3000, 60, 1024, 1000)
    q = Network.ThreadedServer("0.0.0.0", 3001, 60, 1024, 1000)
    r = Network.ThreadedServer("0.0.0.0", 3002, 60, 1024, 1000)
    s = Network.ThreadedServer("0.0.0.0", 3003, 60, 1024, 1000)
    t = Network.ThreadedServer("0.0.0.0", 3004, 60, 1024, 1000)

    p.run()
    q.run()
    r.run()
    s.run()
    t.run()

    print "Running test... " + str(datetime.datetime.now())

    #process secondary funtions
    #bacup indexation
    #statistics
    while True:
    #if True:
        
        try:
            print "Server running ... " + str(datetime.datetime.now())
            time.sleep(10)
        except Exception as error:
            
            print "Erro " + str(error)
            
            
            

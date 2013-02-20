#!/usr/bin/python

import time
import sys
from struct import pack, unpack
import logging

from icehms import Holon, run_holon, hms, Message

class Server(Holon):
    def __init__(self):
        Holon.__init__(self, "MyMsgPublisher", logLevel=logging.INFO )

    def run(self):
        #pub = self._get_publisher("MyTopic", hms.GenericEventInterfacePrx)
        pub = self._get_event_publisher("MyTopic")
        counter = 0
        while not self._stop:
            counter +=1
            #pub.put_message(Message(header="myHeader", arguments=dict(counter=counter, data=pack("=i", counter) )))
            pub.put_message(Message(header="myHeader", arguments=dict(counter=counter, other="MyOther" )))
            time.sleep(0.5)
    
    def getState(self, current):
        return ["Running and publishing", str(counter)]



if __name__ == "__main__":
    import logging
    s = Server()
    run_holon(s)

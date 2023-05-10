#!/usr/bin/python3

# KAIST CS341 SDN Lab POX controller
# 
# 

import json
import sys

from pox.core import core

sys.path.append('/home/vagrant')
import route # /home/vagrant/route.py

log = core.getLogger()

net = None
switchcnt = 0
def init():
    global net
    net = json.load(open('/tmp/net.json'))
    route.init(net)

def connectionUp(event):
    global net
    global switchcnt
    if switchcnt == 0:
        # This is the first switch
        init()
    switchname = str(event.connection.ports[65534]).split(':',2)[0]
    route.addrule(switchname, event.connection)
    # Switch will send unhandled packets to the controller
    # For debugging, print out such packets
    
    def handle_packetin(event):
        packet = event.parsed
        if not packet.parsed:
            log.warning('Ignoring incomplete packet')
            return
        packet_in = event.ofp
        # Many ICMPv6, ARPv6 packets will be printed
        print('unhandled packet :'+str(packet.dump()))
    
    event.connection.addListenerByName('PacketIn', handle_packetin)
    switchcnt += 1
    if switchcnt == len(net['switches']):
        # This was the last switch
        switchcnt = 0

def launch():
    """
    Starts the component
    """
    # Initialize when mininet is set
    core.openflow.addListenerByName("ConnectionUp", connectionUp)

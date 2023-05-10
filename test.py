#!/usr/bin/python3

# KAIST CS341 SDN Lab Test script

import time
import argparse

from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel

from topology import Topology
from graph import gen_graph
from dump import dump_clear, dump_net

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='CS341 SDN Lab Tester')
    parser.add_argument('--task', metavar='T', type=int, nargs='?', default=1,
                        help='task to test', required=True, choices=range(1,6))
    args = parser.parse_args()
    # Uncomment below to see verbose log
    #setLogLevel('debug')
    
    switches, hosts, links = gen_graph(args.task)
    t = Topology(switches, hosts, links)
    net = None
    if args.task == 1:
        net = Mininet(topo=t)
    else:
        net = Mininet(topo=t, controller=RemoteController, listenPort=6633)
        dump_net(net, links)

    net.start()
    net.waitConnected()
    time.sleep(1)
    CLI(net)
    net.stop()


import pox.openflow.libopenflow_01 as of

# KAIST CS341 SDN Lab Task 2, 3, 4
#
# Task 2: Getting familiarized with POX 
#   - Let switches "flood" packets
# 
# Task 3: Implementing a Simple Routing Protocol
#   - Let switches route via Dijkstra
#   - Match ARP and IPv4 packets
#
# Task 4: Implementing a Custom Routing Protocol 
#   - Let switches route via Fog routing
#   - Keep routing ARP packets with Dijkstra, and use Fog routing on IPv4 only

###
# If you want, define global variables
###

def init(net):
    #
    # net argument has following structure:
    # 
    # net = {
    #    'hosts': {
    #         'h1': {
    #             'name': 'h1',
    #             'IP': '10.0.0.1',
    #             'links': [
    #                 # (node1, port1, node2, port2, link cost)
    #                 ('h1', 1, 's1', 2, 3)
    #             ],
    #         },
    #         ...
    #     },
    #     'switches': {
    #         's1': {
    #             'name': 's1',
    #             'links': [
    #                 # (node1, port1, node2, port2, link cost)
    #                 ('s1', 2, 'h1', 1, 3)
    #             ]
    #         },
    #         ...
    #     }
    # }
    #
    ###
    # YOUR CODE HERE
    ###
    pass

def addrule(switch, connection):
    #
    # This function is invoked when a new switch is connected to controller
    # Install table entry to the switch's routing table
    #
    # For more information about POX openflow API,
    # Refer to [POX official document](https://noxrepo.github.io/pox-doc/html/),
    # Especially [ofp_flow_mod - Flow table modification](https://noxrepo.github.io/pox-doc/html/#ofp-flow-mod-flow-table-modification)
    # and [Match Structure](https://noxrepo.github.io/pox-doc/html/#match-structure)
    #
    # your code will be look like:
    # msg = ....
    # connection.send(msg)
    ###
    # YOUR CODE HERE
    ###
    pass
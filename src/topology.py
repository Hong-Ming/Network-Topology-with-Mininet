#!/usr/bin/python   

from mininet.cli import CLI
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSController
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class mytopo(Topo):

    def build(self):
        # Create switch 1 ~ 9
        switch1 = self.addSwitch('s1')
        switch2 = self.addSwitch('s2')
        switch3 = self.addSwitch('s3')
        switch4 = self.addSwitch('s4')
        switch5 = self.addSwitch('s5')
        switch6 = self.addSwitch('s6')
        switch7 = self.addSwitch('s7')
        switch8 = self.addSwitch('s8')
        switch9 = self.addSwitch('s9')

        # Create host 1 ~ 9
        host1 = self.addHost('h1')
        host2 = self.addHost('h2')
        host3 = self.addHost('h3')
        host4 = self.addHost('h4')
        host5 = self.addHost('h5')
        host6 = self.addHost('h6')

        # Link s9 - s7, s9 - s8
        self.addLink(switch9, switch7, bw = 40, delay = '5ms',  loss = 2 )
        self.addLink(switch9, switch8, bw = 50, delay = '4ms',  loss = 3 )

        # Link s7 - s1, s7 - s2, s7 - s3
        self.addLink(switch7, switch1, bw = 23, delay = '1ms',  loss = 8 )
        self.addLink(switch7, switch2, bw = 18, delay = '2ms',  loss = 9 )
        self.addLink(switch7, switch3, bw = 15, delay = '3ms',  loss = 5 )

        # Link s8 - s4, s8 - s5, s8 - s6
        self.addLink(switch8, switch4, bw = 19, delay = '80us', loss = 7 )
        self.addLink(switch8, switch5, bw = 30, delay = '95us', loss = 2 )
        self.addLink(switch8, switch6, bw = 20, delay = '60us', loss = 6 )

        # Link s1 - h1, s2 - h2, s3 - h3, s4 - h4, s5 - h5, s6 - h6
        self.addLink(switch1, host1,   bw = 10, delay = '50us', loss = 12)
        self.addLink(switch2, host2,   bw = 5,  delay = '2ms',  loss = 3 )
        self.addLink(switch3, host3,   bw = 7,  delay = '63us', loss = 9 )
        self.addLink(switch4, host4,   bw = 12, delay = '40us', loss = 14)
        self.addLink(switch5, host5,   bw = 15, delay = '30us', loss = 18)
        self.addLink(switch6, host6,   bw = 3,  delay = '5ms',  loss = 2 )

# create topology
topo = mytopo()
# Create and manage a network with a OvS controller and use TCLink
net = Mininet(
    topo = topo, 
    controller = OVSController,
    link = TCLink)
# Start a network
net.start()
# Dump information of hosts and switchs
dumpNodeConnections(net.hosts)
dumpNodeConnections(net.switches)
# Enter CLI
CLI(net)
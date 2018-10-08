# /usr/bin/env python2
"""
mini-fw-topo.py: A custom FlowVisor WAN topology
"""

#__author__      = "Seshagiri Prabhu"
#__copyright__   = "MIT License"

from mininet.topo import Topo

class FVTopo(Topo):

    def __init__(self):
        # Initialize topology
        Topo.__init__(self)
        
        # Creates switches
        for i in xrange(4):
            self.addSwitch('s%d' % (i+1), dpid="%016x" %(i+1))
        
        # Creates hosts
        for i in xrange(4):
            self.addHost('h%d' % (i+1), inNamespace=True)
        
        # Add link between switches
        self.addLink('s1', 's2', bw=1)
        self.addLink('s2', 's4', bw=1)
        self.addLink('s1', 's3', bw=10)
        self.addLink('s3', 's4', bw=10)
        
        # Add link between hosts and switches
        self.addLink('h1', 's1')
        self.addLink('h2', 's1')
        self.addLink('h3', 's4')
        self.addLink('h4', 's4')

topos = { 'fvtopo': ( lambda: FVTopo() ) }



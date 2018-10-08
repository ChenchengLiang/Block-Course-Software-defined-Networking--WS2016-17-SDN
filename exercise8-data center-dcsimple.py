"""Custom topology example

######### works with notree data center
sudo mn --custom dcsimple.py --topo simple
or

sudo mn --custom dcsimple.py --topo simple --controller remote
and
./pox.py samples.spanning_tree

########

"""

from mininet.topo import Topo 

class Simple( Topo ):
    "Simple topology of depth 3 "

    def __init__( self ):
        "Create custom topo."

        # Add default members to class.
        super( Simple, self ).__init__()

        # Create hosts
        hostlist = []
	h1=self.addHost('h1')
	h2=self.addHost('h2')
	h3=self.addHost('h3')
	h4=self.addHost('h4')
	h5=self.addHost('h5')
	h6=self.addHost('h6')
	h7=self.addHost('h7')
	h8=self.addHost('h8')

        # Create switches
        switchlist = []
	s1=self.addSwitch('s1')
	s2=self.addSwitch('s2')
	s3=self.addSwitch('s3')
	s4=self.addSwitch('s4')
	s5=self.addSwitch('s5')
	s6=self.addSwitch('s6')
	s7=self.addSwitch('s7')

        # Connect hosts to switches 
        # Connect switches to switches
	self.addLink(s1,s2)
	self.addLink(s1,s3)
	self.addLink(s2,s4)
	self.addLink(s2,s5)
	self.addLink(s3,s6)
	self.addLink(s3,s7)

	self.addLink(s4,h1)
	self.addLink(s4,h2)
	self.addLink(s5,h3)
	self.addLink(s5,h4)
	self.addLink(s6,h5)
	self.addLink(s6,h6)
	self.addLink(s7,h7)
	self.addLink(s7,h8)



topos = { 'simple': ( lambda: Simple() ) }
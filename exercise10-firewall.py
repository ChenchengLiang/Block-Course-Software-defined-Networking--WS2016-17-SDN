
"""
Do the following to test this code
sudo /home/mininet/mininet/custom/firewall_start.py


Do the follwoing to quickly debug part of the code
./pox.py --verbose forwarding.l2_learning misc.firewall
 sudo mn --topo single,3 --controller remote --mac
dpctl dump-flows tcp:127.0.0.1:6634

"""


from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.util import dpidToStr
from pox.lib.addresses import EthAddr
from collections import namedtuple
import os


log = core.getLogger()
#policyFile = "%s/pox/pox/misc/firewall-policies.csv" % os.environ[ 'HOME' ]  
policyFile = "%s/pox/pox/misc/firewall-policies_small.csv" % os.environ[ 'HOME' ]  

''' Add your global variables here ... '''


class Firewall (EventMixin):

    def __init__ (self):
        self.listenTo(core.openflow)
        log.debug("Enabling Firewall Module")

    def _handle_ConnectionUp (self, event):    
        ''' Add your logic here ... '''

	msg = of.ofp_flow_mod()

	match =of.ofp_match()
	match.dl_src = EthAddr("00:00:00:00:00:01")
	match.dl_dst = EthAddr("00:00:00:00:00:02")
	msg.match = match
	action = of.ofp_action_output(port = of.OFPP_NONE)
	msg.actions.append(action)
	event.connection.send(msg)
	
	

        log.debug("Firewall rules installed on %s", dpidToStr(event.dpid))

def launch ():
    '''
    Starting the Firewall module
    '''
    core.registerNew(Firewall)
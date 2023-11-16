from pox.pox.core import core
import pox.pox.openflow.libopenflow_01 as of
from pox.pox.lib.revent import * 
from pox.pox.lib.util import dpidToStr 
from pox.pox.lib.addresses import EthAddr 
from collections import namedtuple 
import os 
import yaml

log = core.getLogger() 

class Firewall(EventMixin):
    def __init__(self):
        self.listenTo(core.openflow)
        
        with open('rules.yml', 'r') as f:
            rules = yaml.safe_load(f)

        self.firewall_switch = rules['firewall_switch']
        self.firewall_rules = rules['rules']
        
        log.debug("Firewall Module Enabled")
            
   
    def _handle_connection_up(self, event):
        if event.dpid == self.firewall_switch:
            log.debug("Firewall Switch Connected: %s", dpidToStr(event.dpid))
            for rule in self.firewall_rules:
                self._install_rule(event, rule)
    
    def _install_rule(self, event, rule):
        # TODO: Implement the function that installs the given rule in the switch
        block_match = of.ofp_match() # It’s used to create a match object that defines the criteria for OpenFlow rules.
        
        msg = of.ofp_flow_mod()
        msg.match = block_match # Assigns the customized block_match to the match field of a flow mode message.
                                #  This message is then sent to the switch to update its flow table.
        event.connection.send(msg)
        pass

    
    def launch(): 
        # Starting the Firewall module
        core.registerNew(Firewall)
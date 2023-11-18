from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.util import dpidToStr
from pox.lib.addresses import EthAddr
from collections import namedtuple
import os
import yaml

from pox.lib.addresses import IPAddr
import pox.lib.packet as pkt

log = core.getLogger()

class Firewall(EventMixin):
    def __init__(self):
        self.listenTo(core.openflow)
        
        with open('rules.yml', 'r') as f:
            rules = yaml.safe_load(f)

        self.firewall_switch = rules['firewall_switch']
        self.firewall_rules = rules['rules']
        
        log.debug("Firewall Module Enabled")

        self.switch = {
                'dst_port': self.handle_dst_src_port,
                'src_port': self.handle_dst_src_port,
                'net_protocol': self.handle_net_protocol,
                'src_mac': self.handle_dst_src_mac,
                'dst_mac': self.handle_dst_src_mac,
                'src_ip': self.handle_dst_src_ip,
        }
            
   
    def _handle_connection_up(self, event):
        print()
        if event.dpid == self.firewall_switch:
            log.debug("Firewall Switch Connected: %s", dpidToStr(event.dpid))
            for rule in self.firewall_rules:
                self._install_rule(event, rule)
    
    def _install_rule(self, event, rule):

        block_match = of.ofp_match() # It’s used to create a match object that defines the criteria for OpenFlow rules.
        self._add_rule(block_match, rule) # Adds the rule to the block_match object.
        
        block_match.dl_type = pkt.ethernet.IP_TYPE
        msg = of.ofp_flow_mod()
        msg.match = block_match 

        event.connection.send(msg)
    
    def _add_rule(self, block_match, rule):
        for key in rule.keys():
            self.switch.get(key, lambda x, block_match=None: print(f"Unhandled key: {x} with block_match: {block_match}"))(rule[key],key, block_match)


    def handle_dst_src_port(value,key, block_match):
        if "src_port" == key:
            block_match.tp_src = IPAddr(value)
        if "dst_port" == key:
            block_match.tp_dst = IPAddr(value)
        print(f"Handling dst_port: {value} with block_match: {block_match}")
    
    def handle_dst_src_ip(value,key, block_match):
        if "src_ip" == key:
            block_match.nw_src = value
        if "dst_ip" == key:
            block_match.nw_dst = value
        print(f"Handling dst_ip or src_ip with : {value} with block_match: {block_match}")
    
    def handle_net_protocol(value,key, block_match):
        protocols = {
                "TCP": pkt.ipv4.TCP_PROTOCOL,
                "UDP": pkt.ipv4.UDP_PROTOCOL,
                "ICMP": pkt.ipv4.ICMP_PROTOCOL,
            }
        block_match.nw_proto = protocols[value]


    def handle_dst_src_mac(value,key, block_match):

        if "src_mac" == key:
                block_match.dl_src = EthAddr(value)
        if "dst_mac" == key:
                block_match.dl_dst = EthAddr(value)
        print(f"Handling src_mac or dst_mac: {value} with block_match: {block_match}")
        # Your logic for 'src_mac'

        
    
def launch(): 
    # Starting the Firewall module
    core.registerNew(Firewall)

from mininet.topo import Topo

class MyTopology(Topo):
    
    def __init__(self, n):
        """
        Receives n, being n the number of switches to be created.
        If n <= 1, then the topology will be a simple switch with four hosts.
        """
        Topo.__init__(self)
        
        hostL1 = self.addHost('Left_1')
        hostL2 = self.addHost('Left_2')

        hostR1 = self.addHost('Right_1')
        hostR2 = self.addHost('Right_2')

        switch = self.addSwitch('Switch_0')

        self.addLink(hostL1, switch)
        self.addLink(hostL2, switch)

        for i in range(n - 1):
            switch2 = self.addSwitch('Switch_' + str(i + 1))
            self.addLink(switch, switch2)
            switch = switch2

        self.addLink(hostR1, switch)
        self.addLink(hostR2, switch)
    
    def neighbors(self, switch):
        """
        Returns the neighbors of a switch.
        """
        return list(self.g.adj[switch])

        
topos = {"MyTopo": MyTopology} 
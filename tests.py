import unittest
from topology import MyTopology

class TestTopology(unittest.TestCase):

    def test_quantity(self):
        for i in range(1, 10):
            topo = MyTopology(i)
            self.assertEqual(len(topo.hosts()), 4)
            self.assertEqual(len(topo.switches()), i)
            self.assertEqual(len(topo.links()), i + 3)
    

if __name__ == '__main__':
    unittest.main()
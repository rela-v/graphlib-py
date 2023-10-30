'''Test file for the node data structure.'''

#import libraries
import unittest
from src.node import Node

class TestNodeClass(unittest.TestCase):
    '''A test class for the Node data structure.'''
    def tearDown(self):
        '''Method for tearDown (cleaning up setUp) of all tests for the node data structure.'''
        if hasattr(self, 'node'):
            del self.node

    def test_node_creation(self):
        '''Testing the creation of nodes.'''
        self.node = Node('Name', {'LIKES': ['FOOD']})
        self.assertEqual(self.node.name, 'Name')
        self.assertEqual(self.node.props, {'LIKES': ['FOOD']})
        self.assertEqual(self.node.props['LIKES'], ['FOOD']) 
        self.assertEqual(self.node.props['LIKES'][0], 'FOOD')

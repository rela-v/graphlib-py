'''Source code file for the node structure.'''

#import libraries
from dataclasses import dataclass

@dataclass
class Node:
    '''Class defining the Node datastructure.'''
    name: str
    props: dict

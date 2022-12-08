import sys
import re
import math

class Solution:
    def __init__(self, *args, **kwargs):
        super(Solution, self).__init__(*args, **kwargs)
        self.n = int(input("Input your number of nodes: "))
        self.nodes_gen()
        self.nodes = dict(zip(self.list_nodes, [{} for n in range(len(self.list_nodes))]))
        print(self.nodes)
        self.nodes_connect()
        print(self.nodes)
        self.final()
    
    def nodes_gen(self):
        i=65
        self.list_nodes = []
        for node in range(self.n):
            self.list_nodes.append(chr(i))
            i+=1
            
        print(self.list_nodes)
        return self.list_nodes
    
    def nodes_connect(self):
        self.src_node,self.dest_node = str, str
        while True: 
            try:
                print(self.nodes)
                self.src_node = input(f"Please input the node you would like to create a connection for. The node has to be within '{self.list_nodes[0]} and {self.list_nodes[-1]}' followed by a : ")
                assert(self.src_node in self.list_nodes)
                self.dest_node = input("Enter the node you would like to traverse to: ")    
                self.edge_mag = int(input(f"Enter the magnitude of edge {self.src_node+self.dest_node} OR {self.dest_node+self.src_node}: "))          
                (self.nodes[self.dest_node])[self.src_node] = (self.nodes[self.src_node])[self.dest_node] = self.edge_mag
                self.src_node = str
            except:
                raise ValueError("Please input your data in the prescribed formats. [_Vertex_as_type_(str)_ <space> _Magnitude/Connection_as_type_(int)_]")
    
    def final(self):
        print(self.nodes)
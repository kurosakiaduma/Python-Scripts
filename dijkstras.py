import sys
import re
import math

class Solution:
    def __init__(self, *args, **kwargs):
        super(Solution, self).__init__(*args, **kwargs)
        self.n = int(input("Input your number of nodes: "))
        self.nodes_gen()
        self.nodes = dict(zip(self.list_nodes, [{} for n in range(len(self.list_nodes))]))
        self.node_connect()
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
    
    def node_connect(self):
        self.src_node = self.dest_node = str
        self.edge_mag = int
        try:
            print(self.nodes)
            self.src_node = input(f"Please input the node you would like to create a connection for. The node has to be within '{self.list_nodes[0]} and {self.list_nodes[-1]}' followed by a : ")
            self.dest_node = input("Enter the node you would like to traverse to: ")    
            assert(self.dest_node in self.list_nodes)
            if ("end" in [self.src_node, self.dest_node]):
                return self
            self.edge_mag = int(input(f"Enter the magnitude of edge {self.src_node+self.dest_node} OR {self.dest_node+self.src_node}: "))          
            (self.nodes[self.dest_node])[self.src_node] = (self.nodes[self.src_node])[self.dest_node] = self.edge_mag
        except: 
            raise ValueError("Please input your data in the prescribed formats. [_Vertex_as_type_(str)_ <space> _Magnitude/Connection_as_type_(int)_]")
    
    def traverse(self):

        self.verts = set()
        self.usr_path = input(f'Enter only two vertices to find their shortest path: ').upper()
        self.src_node = self.origin = self.usr_path[0]
        self.dest_node = self.usr_path[-1]
        
        try:
            while ((self.src_node and self.dest_node in self.nodes.keys())):
                if self.src_node == self.dest_node:
                    self.verts.add(self.dest_node)
                    break
                assert(self.src_node != self.dest_node and len(self.usr_path) == 2 and self.usr_path.isalpha() and self.src_node not in self.verts)
                if self.src_node != self.origin:    
                    self.verts.add(self.src_node)
                self.possibles = {k: v for k,v in self.nodes.get(self.src_node).items() if k not in self.verts and self.origin}
                print(self.possibles)
                self.possibles = {k for k,v in self.possibles.items() if v == min(self.possibles.values())}
                print(self.verts,self.possibles)
                self.src_node = list(self.possibles - self.verts)[0]
                print(self.src_node)
        except:
                raise("Please enter a valid path")
        
        print(self.verts)
        join = lambda p : "".join(str(i) for i in p)
        self.verts = join(self.verts)  
        print(self.verts)
        return (self.origin+self.verts)
     
    def final(self):
        return self.nodes
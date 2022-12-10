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
            self.src_node = input(f"Please input the node you would like to create a connection for. The node has to be within '{self.list_nodes[0]} and {self.list_nodes[-1]}: ").upper()
            self.dest_node = input("Enter the node you would like to traverse to: ").upper()    
            assert(self.dest_node in self.list_nodes)
            if ("end" in [self.src_node, self.dest_node]):
                return self
            self.edge_mag = int(input(f"Enter the magnitude of edge {self.src_node+self.dest_node} OR {self.dest_node+self.src_node}: "))          
            (self.nodes[self.dest_node])[self.src_node] = (self.nodes[self.src_node])[self.dest_node] = self.edge_mag
        except: 
            raise ValueError("Please input your data in the prescribed formats. [_Vertex_as_type_(str)_ <space> _Magnitude/Connection_as_type_(int)_]")
    
    def traverse(self):
        self.verts = set()
        self.possibles = set() 
        self.d_verts = set()
        self.connected = {}
        self.cost = self.d_cost = 0
        
        self.usr_path = input(f'Enter only two vertices to find their shortest path: ').upper()
        self.alt_path = self.d_path = None
        
        self.src_node = self.origin = self.usr_path[0]
        self.dest_node = self.usr_path[-1]
        
        try:
            while ((self.src_node and self.dest_node in self.nodes.keys())):

                assert(len(self.usr_path) == 2 and self.usr_path.isalpha())
                
                self.connected = {k: v for k,v in self.nodes.get(self.src_node).items() if k not in self.verts and k not in self.origin}
                print(self.connected)
                
                if self.dest_node in self.connected.keys() and self.src_node != self.origin and not self.d_verts:
                    self.d_verts.update(self.verts)
                    self.d_verts.add(self.src_node)
                    self.d_cost = self.connected.get(self.dest_node) + self.cost
                    print("I have verified I am traversing from a non-origin to the dest")
                    pass
                elif self.dest_node in self.connected.keys() and self.src_node == self.origin:
                    self.d_verts.add(self.src_node)
                    self.d_verts.add(self.dest_node)
                    self.d_cost = self.connected.get(self.dest_node)
                    print("I have verified I am travelling from the origin to the dest")
                    pass
                elif self.src_node == self.dest_node:
                    self.verts.add(self.src_node)
                    ("I have verified that I am at the destination node.")
                    break
                elif self.src_node != self.dest_node and self.dest_node not in self.connected.keys():
                    self.verts.add(self.src_node)
                    print("I have verified that I am traversing to a non-origin to a non-dest")
                    pass
                
                self.possibles = {k for k,v in self.connected.items() if v == min(self.connected.values())}
                
                self.edge_mag = min(self.connected.values())
                self.cost+=self.edge_mag
                print(self.cost,self.d_cost, self.verts,self.d_verts)                 
                
                self.verts.add(self.src_node)
                self.src_node = list(self.possibles - self.verts)[0]
                print(self.src_node)
        except:
                raise("Please enter a valid path")
        
        print(self.verts,self.d_verts)
        
        join = lambda p : "".join(str(i) for i in p)
        
        if self.verts:
            self.alt_path = (join(self.verts))
        else:
            pass
        
        if self.d_verts:
            self.d_path = (join(self.d_verts))
        else:
            pass
        
        self.paths = ((self.d_path, self.d_cost), (self.alt_path, self.cost))
        
        return self.optimizer()
    
    def optimizer(self):
        if self.paths[0][1] < self.paths[1][1]:
            return self.paths[0]
        elif self.paths[0][0] == self.paths[1][0]:
            return self.paths[0]
        elif self.paths[0][1] > self.paths[1][1]:
            return self.paths[1]
        elif self.paths[0][1] == self.paths[1][1]:
            return self.paths
        
    def final(self):
        return self.nodes
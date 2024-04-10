class Solution:
    def __init__(self, *args, **kwargs):
        super(Solution, self).__init__(*args, **kwargs)
        
        self.n = int(input("Input your number of nodes: "))

        self.nodes_gen()
        self.hello()

    
        self.nodes = dict(zip(self.list_nodes, self.list_mag_edges))
        
        self.final()
    
    def nodes_gen(self):
        i=65
        self.list_nodes = []
        for node in range(self.n):
            self.list_nodes.append(chr(i))
            i+=1
            
        print(self.list_nodes)
        return self.list_nodes
    
    def hello(self):
        self.verts = []
        self.edges = []   
        for node in range(self.n):
            try:
                self.usr_pick = input(f"Please enter a node between {self.list_nodes[0]} and {self.list_nodes[-1]} followed by a space and the number of connections you intend to create")
                self.desc_node, self.pick_conn = self.usr_pick.split()[0], self.usr_pick.split()[2:]
                assert(self.desc_node in self.list_nodes and 0<=int(self.pick_conn)<3)
                for vert in range(self.pick_conn):
                    self.verts.append(input("Enter connected vertex: "))
                    self.edges.append(int(input("Enter the edge magnitude: ")))
                self.list_mag_edges = list(zip(self.verts,self.edges))
            except:
                raise ValueError("Please input your data in the prescribed formats. [_Vertex_as_type_(str)_ <space> _Magnitude/Connection_as_type_(int)_]")
    
    def final(self):
        print(self.nodes)
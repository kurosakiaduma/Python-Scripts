'''
Program: MST//Dijkstra's Algorithm for Directed Graphs
Author: Tevin Aduma
Description: The intention is to create a program that solves Dijkstra's Greedy Algo problem
             by using inputs to determine the least costly path between source and destination
             vertices. 
'''

class Solution:
    def __init__(self, *args, **kwargs):
        super(Solution, self).__init__(*args, **kwargs)
        while True:
            self.start()
        
    def start(self):
        print("""Welcome to the\nVERTEX-TRAVERSAL OPTIMIZER\nPlease choose one of the following options\nto proceed with the program.\n
                1. Enter the number of vertices in your graph\n
                2. Connect a node/vertex to another\n
                3. Print out your graph in a dictionary\n
Contact: kurosakiaduma@gmail.com 🙋🏾‍♂️ 
                """)
        inp = int(input(":>"))
        print({inp})
        try:
            assert inp in range(0,5)
            if inp == 1:
                self.nodes_gen()
            elif inp == 2:
                self.node_connect()
            elif inp == 3:
                self.final()
            elif inp == 4:
                self.traverse()
            elif inp == 0:
                quit(0)
            pass
        except:
            raise ValueError("Please enter a value between 1 and 3")
            
    def nodes_gen(self):
        self.n = int(input("Input your number of nodes: "))
        i=65
        self.list_nodes = []

        for node in range(self.n):
            self.list_nodes.append(chr(i))
            i+=1            
        print(self.list_nodes)
        

        

        return self.list_nodes
    
    def node_connect(self):
        
        self.nodes = dict(zip(self.list_nodes, [{} for n in range(len(self.list_nodes))]))
        self.src = self.dest = str
        self.edge_mag = int

        try:
            print(self.nodes)
            
            self.src = input(f"Please input the node you would like to create a connection for. The node has to be within '{self.list_nodes[0]} and {self.list_nodes[-1]}: ").upper()
            self.dest = input("Enter the node you would like to traverse to: ").upper()    
            
            assert(self.dest in self.list_nodes)
            
            if ("end" in [self.src, self.dest]):
                return self
            self.edge_mag = int(input(f"Enter the magnitude of edge {self.src+self.dest} OR {self.dest+self.src}: "))          
            (self.nodes[self.dest])[self.src] = (self.nodes[self.src])[self.dest] = self.edge_mag
            
            print(self.nodes)
        
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
        
        self.src = self.origin = self.usr_path[0]
        self.dest = self.usr_path[-1]
        
        try:
            while ((self.src and self.dest in self.nodes.keys())):

                assert(len(self.usr_path) == 2 and self.usr_path.isalpha())
                
                self.connected = {k: v for k,v in self.nodes.get(self.src).items() if k not in self.verts and k not in self.origin}
                print(self.connected)
                
                if self.dest in self.connected.keys() and self.src != self.origin and not self.d_verts:
                    self.d_verts.update(self.verts)
                    self.d_verts.add(self.src)
                    self.d_verts.add(self.dest)
                    self.d_cost = self.connected.get(self.dest) + self.cost
                    print("I have verified I am traversing from a non-origin to the dest.")
                    pass
                elif self.dest in self.connected.keys() and self.src == self.origin:
                    self.d_verts.add(self.src)
                    self.d_verts.add(self.dest)
                    '''Look into time constraints between adding items into the set or iterating through a 
                    for loop with the both items in a list//tuple//set
                    '''
                    self.d_cost = self.connected.get(self.dest)
                    print("I have verified I am travelling from the origin to the dest.")
                    pass
                elif self.src == self.dest:
                    self.verts.add(self.src)
                    ("I have verified that I am at the destination node.")
                    break
                elif self.src != self.dest and self.dest not in self.connected.keys():
                    self.verts.add(self.src)
                    print("I have verified that I am traversing to a non-dest.")
                    pass
                
                self.possibles = {k for k,v in self.connected.items() if v == min(self.connected.values())}
                
                if self.possibles or self.dest in self.possibles and not(self.cost>self.d_cost):
                    self.edge_mag = min(self.connected.values())
                    self.cost+=self.edge_mag
                else:
                    break
                    
                print(self.cost,self.d_cost, self.verts,self.d_verts)                 
                
                self.verts.add(self.src)
                self.src = list(self.possibles - self.verts)[0]
                print(self.src)
        except:
                raise("Please enter a valid path")
        
        print(self.verts,self.d_verts)
        
        join = lambda p : "".join(str(i) for i in p)
        
        if self.dest in self.verts:
            self.alt_path = (join(self.verts))
        else:
            pass
        
        if self.dest in self.d_verts:
            self.d_path = (join(self.d_verts))
        else:
            pass
        
        self.paths = ((self.d_path, self.d_cost), (self.alt_path, self.cost))
        
        return self.optimizer()
    
    def optimizer(self):
        try:
            if self.paths[0][1] < self.paths[1][1]:
                return self.paths[0]
            elif self.paths[0][0] == self.paths[1][0]:
                return self.paths[0]
            elif self.paths[0][1] > self.paths[1][1]:
                return self.paths[1]
            elif self.paths[0][1] == self.paths[1][1]:
                    return self.paths
        except:
            if None in self.paths[0][0]:
                return self.paths[1]
            elif None in self.paths[1][0]:
                return self.paths[0]
            else:
                return f"There is no direct or indirect connection between {self.origin} and {self.dest}. \nPlease check your input."
    
    def final(self):
        return f'{self.nodes}'
    
    def clear(self):
        self.nodes.clear()
    
if __name__ == "__main__":
    Solution()
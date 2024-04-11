'''
Program: MST//Dijkstra's Algorithm for Directed Graphs
Author: Tevin Aduma
Description: This is a program that allows the following operations:
                * Graph generation 
                * Vertex and Edge CRUD operations
                * Dijkstras Traversal Algorithm
                * Kruskal's MST Algorithm
                * Prim's MST Algorithm
'''
from sys import exit
class Solution:
    def __init__(self, *args, **kwargs):
        super(Solution, self).__init__(*args, **kwargs)
        self.verts = self.possibles = self.d_verts= set()
        self.nodes = self.connected = {}
        self.edge_mag = self.n = self.cost = self.d_cost = int()
        self.list_nodes = list()
        self.src = self.dest = self.origin = str
        self.paths = tuple()
        while True:
            self.start()
        
    def start(self) -> None:
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
                exit(0)
        except ValueError as e:
            print(f"{e}: Please enter a value between 1 and 4")
            
    def nodes_gen(self) -> list:
        self.n = int(input("Input your number of nodes: "))
        i=65 # ASCII code for A
        self.list_nodes = []

        for _ in range(self.n):
            self.list_nodes.append(chr(i))
            i+=1
        print(self.list_nodes)
    
        return self.list_nodes
    
    def node_connect(self) -> None:
        """Connects existing nodes within a graph

        Raises:
            ValueError: If the input data is not in the prescribed formats.

        Returns:
            None
        """
        # Initialize the nodes dictionary with each node as a key and an empty dictionary as its value
        self.nodes = dict(zip(self.list_nodes, [{} for n in range(len(self.list_nodes))]))
        
        # Start an infinite loop to continuously ask for user input
        while True:
            try:
                # Print the current state of the nodes
                print(self.nodes)
                
                # Ask the user for the source node and convert it to uppercase
                self.src = input(f"Please input the node you would like to create a connection for. The node has to be within '{self.list_nodes[0]} and {self.list_nodes[-1]}: ").upper()
                # Ask the user for the destination node and convert it to uppercase
                self.dest = input("""
                                  Enter the node you would like to connect to\n
                                  Enter 'stop' to halt this operation\n
                                  :>
                                  """).strip().upper()
                
                # If the user inputs "end" for either the source or destination, return the current instance of the class
                if ("stop" in [self.src, self.dest]):
                    return self

                # Assert that the destination node is in the list of nodes
                assert(self.dest in self.list_nodes)

                # Ask the user for the magnitude of the edge and convert it to an integer
                # Inquire about the nature of the
                self.edge_mag = int(input(f"Enter the magnitude of edge {self.src+self.dest} OR {self.dest+self.src}: "))
                while True:
                    direction = int(input("Is the edge one-way or two-way? Use 1 or 2 for either choice"))
                    if direction in [1,2]:
                        break
                    print("""\nPlease enter 1 or 2 to create a single one-way node or\n
                          a single one-way edge or two edges of the same weight in different
                          directions.
                          """
                          )
                if direction == 1:
                    (self.nodes[self.src])[self.dest] = self.edge_mag
                else:
                    # Add the edge to the nodes dictionary for both the source and destination nodes
                    (self.nodes[self.dest])[self.src] = (self.nodes[self.src])[self.dest] = self.edge_mag
                # Print the updated state of the nodes
                print(self.nodes)
            # If any error occurs during the above process, raise a ValueError with a helpful message
            except ValueError as e:
                print(f"{e}: Please input your data in the prescribed formats. [_Vertex_as_type_(str)_ <space> _Magnitude/Connection_as_type_(int)_]")

    def traverse(self):
        self.verts = set()
        self.possibles = set()
        self.d_verts = set()
        self.connected = {}
        self.cost = self.d_cost = 0
        
        usr_path = input('Enter only two vertices to find their shortest path: ').strip().upper()
        alt_path = d_path = None
        
        self.src = self.origin = usr_path[0]
        self.dest = usr_path[-1]
        
        try:
            while ((self.src in self.nodes.keys() and self.dest in self.nodes.keys())):

                assert(len(usr_path) == 2 and usr_path.isalpha())
                
                self.connected = {k: v for k,v in self.nodes.get(self.src).items() if k not in self.verts and k not in self.origin}
                print(self.connected)
                
                if self.dest in self.connected.keys() and self.src != self.origin and not self.d_verts:
                    self.d_verts.update(self.verts)
                    self.d_verts.add(self.src)
                    self.d_verts.add(self.dest)
                    self.d_cost = self.connected.get(self.dest) + self.cost
                    print("I have verified I am traversing from a non-self.origin to the dest.")
                elif self.dest in self.connected.keys() and self.src == self.origin:
                    self.d_verts.add(self.src)
                    self.d_verts.add(self.dest)
                    # Look into time constraints between adding items into the set or iterating through a 
                    # for loop with the both items in a list//tuple//set
                    self.d_cost = self.connected.get(self.dest)
                    print("I have verified I am traveling from the self.origin to the dest.")
                elif self.src == self.dest:
                    self.verts.add(self.src)
                    print("\nI have verified that I am at the destination node.")
                    break
                elif self.src != self.dest and self.dest not in self.connected.keys():
                    self.verts.add(self.src)
                    print("I have verified that I am traversing to a non-dest.")
                
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
        except ValueError as e:
                print(f"{e}: Please enter a valid path")
        
        print(self.verts,self.d_verts)
        
        join = lambda p : "".join(str(i) for i in p)
        
        if self.dest in self.verts:
            alt_path = (join(self.verts))
        else:
            pass
        
        if self.dest in self.d_verts:
            d_path = (join(self.d_verts))
        else:
            pass
        
        self.paths = ((d_path, self.d_cost), (alt_path, self.cost))
        
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
        except Exception as e:
            if None in self.paths[0][0]:
                return self.paths[1]
            elif None in self.paths[1][0]:
                return self.paths[0]
            else:
                print(f"{e}\nThere is no direct or indirect connection between {self.origin} and {self.dest}. \nPlease check your input.")
    
    def final(self):
        return f'{self.nodes}'
    
    def clear(self):
        self.nodes.clear()
    
if __name__ == "__main__":
    Solution()
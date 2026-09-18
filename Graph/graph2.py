""" <<<<<<< HEAD

class Graph:
    def __init__(self):
        self.graph={}

    def create_graph(self):
        n=int(input("enter no.of nodes"))
        while n>0:
            node=input("enter node:")
            edges_number=int(input(f"enter number of nodes connected to {node}"))
            while edges_number>0:
                edges=input(f"enter nodes to connected to main {node}:")
                self.add_edge(node,edges)
                edges_number-=1
            n-=1
    def add_edge(self,node,edges):
        if node not in self.graph:
            self.graph[node]=[]
        self.graph[node].append(edges)
    def delete_node(self,node):
        if node in self.graph:
            del self.graph[node]
        for y in self.graph.values():
            if node in y:
                y.remove(node)
    def update_node(self,node,new_node):
        if node in self.graph:
            for z in self.graph.values():
                if node in z:
                    z.remove(node)
                    z.append(new_node)
            self.graph[new_node]=self.graph.pop(node)
    def display_graph(self):
        print(self.graph)
    def find_cycle(self):
        for n,m in self.graph.items():
            for n in m:
                if n in self.graph and m == self.graph[n]:
                    print(f"found the match {n} with {m}")
                else:
                    pass
=======
class Graph:
    def __init__(self):
        # This dictionary lives inside the object instance
        self.adj_list = {}

    def add_edge(self, node, edge):
        # Automatically initialize node if not present
        if node not in self.adj_list:
            self.adj_list[node] = []
        self.adj_list[node].append(edge)

    def create_graph(self):
        number = int(input("Enter number of nodes: "))
        while number > 0:
            node = input("Enter node: ")
            edges_number = int(input(f"Enter number of nodes connected to {node}: "))
            while edges_number > 0:
                edge = input(f"Enter node connected to {node}: ")
                self.add_edge(node, edge)
                edges_number -= 1
            number -= 1

    def display(self):
        print("\nFinal Graph Structure:")
        for node, neighbors in self.adj_list.items():
            print(f"{node} -> {neighbors}")


# --- Creating the Object and Running It ---
my_graph = Graph()       # 1. Create an object from the Graph class
my_graph.create_graph()  # 2. Call the method to build it via inputs
my_graph.display()       # 3. Call the method to print it
>>>>>>> b7b68bc9df63f4f2d69a37cd12dde8da81f26611
 """
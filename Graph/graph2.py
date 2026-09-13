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
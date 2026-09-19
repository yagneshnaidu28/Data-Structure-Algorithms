graph={}

number=int(input("enter number of nodes"))
while (number>0):
    node=input("enter node {i} :")
    edges_number=int(input(f"enter number of nodes connected to {node}"))
    while (edges_number>0):
        edges=input(f"enter nodes to connected to main {node}:")
        if node not in graph:
            graph[node]=[]
        graph[node].append(edges)
        edges_number-=1
    number-=1

print(graph)





""" ------------------------------------------------------------------------------------------- """
graph={
    "a":["b","c","a"],
    "b":["c","d"],
    "c":["d","a"],
    "d":["c"]
}

""" Delete  """

x=input("enter node to delete")
if x in graph:
    del graph[x]
for y in graph.values():
    if x in y:
        y.remove(x)

print(graph)


""" update """
x=input("enter node to update")
if x in graph:
    y=input("enter node to add to this node:")
    for z in graph.values():
        if x in z:
            z.remove(x)
            z.append(y)
    graph[y]=graph.pop(x)

            

print(graph)

""" Finding circular cycle in node """
for n,m in graph.items():
    for n in m:
        if n in graph and m == graph[n]:
            print(f"found the match {n} with {m}")
        else:
            pass



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

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
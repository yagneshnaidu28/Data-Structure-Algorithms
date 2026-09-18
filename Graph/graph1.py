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


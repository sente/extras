#from queue import Queue


class Queue(object):


    def __init__(self):
        self.data = []

    def enqueue(self, obj):
        self.data.append(obj)

    def dequeue(self):
        if len(self.data) > 0:
            res = self.data[0]
            self.data = self.data[1:]
            return res

    def isEmpty(self):
        if len(self.data) == 0:
            return True
        else:
            return False



def BFS(graph,root,target):
    q = Queue()
    checked = []
    q.enqueue(root)
    path = 0
    while not q.isEmpty():
        v = q.dequeue()
        print v
        if v == target:
           return True
        elif v not in checked:
            for edge in graph[v]:
                if v not in checked:
                    q.enqueue(edge)
            checked.append(v)
    return False

graph = {1: [2, 3],
         2: [1, 4, 5, 6],
         3: [1, 4],
         4: [2, 3, 5],
         5: [2, 4, 6, 7, 8],
         6: [2, 5],
         7: [1, 5],
         8: [7, 3]}


def print_graph(graph):

    import networkx as nx
    G=nx.DiGraph()

    for g in graph:
        G.add_node(g)
        for edge in graph[g]:
            G.add_edge(g,edge)

    print 'edges'
    print G.edges()

    print 'nodes'
    print G.nodes()

    nx.write_dot(G,'gg.dot')
    return G

print_graph(graph)


print BFS(graph, 1, 6) 


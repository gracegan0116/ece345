import numpy as np

def generate_graph (inputfile, graph):
    f = open(inputfile, "r")
    node = set()
    for row in f:
        item = row.split()
        graph[int(item[0])][int(item[1])] = float(item[2])
        node.add(int(item[0]))
    return node

def dijkstra_algo (graph, vertices, deadline):
    row = len(graph)
    col = len(graph[0])
    # initialize S_set for visited set
    S_set = set()
    # initialize Q_set for unvisited set
    Q_set = set()
    # use to count for the time and node number
    time = 0
    count = 0

    # a distance array to store the [time to reach to vertex, parent vertex]
    parent = -1
    distance = [[float("Inf"),parent]] * row
    # initial the first vertex to compute be vertices[0] as source
    u = list(vertices)[0]
    distance[u] = [0.-1]

    # Q_set is used to store the vertices that haven't been visited
    for item in vertices:
        Q_set.add(item)
    
    # while Q_set is not None:
    u = ExtractMin(distance, Q_set)
    Q_set.remove(u)
    S_set.add(u)
    i = 0
    for adjacent_v in graph[u]:
        # make sure it has edge between u and v in directed graph
        if (adjacent_v != 0):
            if distance[i][0] > (distance[u][0] + adjacent_v):
                distance[i] = [distance[u][0] + adjacent_v, u]
        i = i + 1

def ExtractMin(distance, Q_set):
    index = -1
    minimum = float("Inf")
    for i in range (0, len(distance)):
        if distance[i][0] < minimum:
            index = i
    return index


if __name__ == "__main__":
    inputfile = "facebook_small.txt"
    deadline = 10
    graph = np.zeros((500,500))
    vertices = generate_graph(inputfile, graph)
    dijkstra_algo(graph, vertices, deadline)
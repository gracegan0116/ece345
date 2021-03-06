#!/usr/bin/env python3
import numpy as np
import sys
import time

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
    spread = 0
    source_node = 0

    for vertex in vertices:
        # a distance array to store the [time to reach to vertex, parent vertex]
        parent = -1
        distance = [[float("Inf"),parent]] * row
        # initial the first vertex to compute be vertices[0] as source
        u = vertex
        distance[u] = [0,-1]

        # Q_set is used to store the vertices that haven't been visited
        for item in vertices:
            Q_set.add(item)
        
        while Q_set is not None:
            u = ExtractMin(distance, Q_set)
            if u == -1: break
            Q_set.remove(u)
            S_set.add(u)
            i = 0
            
            for adjacent_v in graph[u]:
                # make sure it has edge between u and v in directed graph
                if (adjacent_v != 0):
                    if distance[i][0] > (distance[u][0] + adjacent_v):
                        distance[i] = [distance[u][0] + adjacent_v, u] 
                i = i + 1
        
        # Top_1 Influencer
        j = 0
        count = 0
        
        while j < len(distance):
            if distance[j][0] <= deadline:
                count = count + 1
                if distance[j][0] > time:
                    time = distance[j][0]
            j = j + 1
    
        if count > spread:
            spread = count
            source_node = vertex
    return source_node, spread
    


def ExtractMin(distance, Q_set):
    index = -1
    minimum = float("Inf")
    for i in range (0, len(distance)):
        if distance[i][0] < minimum and i in Q_set:
            index = i
            minimum = distance[i][0]
    return index

# Wrong Influencer
def Top_1_Influencer(distance, j):
    spread = 1
    while j != -1:
        if distance[j][1] != -1:
            spread = spread + 1
        j = distance[j][1]
    return spread

if __name__ == "__main__":
    start = time.time()
    input_file = sys.argv[1]
    deadline = sys.argv[2]
    graph = np.zeros((500, 500))
    vertices = generate_graph(input_file, graph)
    source_node, spread = dijkstra_algo(graph, vertices, deadline)
    end = time.time()
    print("TOP-1 INFLUENCER: " + str(source_node) + " SPREAD:" + str(spread) + " TIME:" + str(end-start) + " sec")

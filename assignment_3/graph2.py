from collections import defaultdict
import sys
import time

class Node:
    def __init__(self, node_num, weight):
        self.node_num = node_num
        self.time = weight

def generate_graph (inputfile):
    f = open(inputfile, "r")
    G = defaultdict(list)
    for row in f:
        item = row.split()
        G[int(item[0])].append(Node(int(item[1]), float(item[2])))
    return G

def get_longest_path(G,v,deadline,top_1_path,seen=None,path=None):
    if seen is None: seen = []
    if path is None: path = [v]
    seen.append(v)
    paths = []
    for t in G[v]:
        if t.node_num not in seen and t.time <= deadline and t.node_num not in top_1_path:
            t_path = path + [t.node_num]
            paths.append(tuple(t_path))
            paths.extend(get_longest_path(G, t.node_num, deadline-t.time, top_1_path, seen[:], t_path))
    return paths

def Top_2_Influencer(graph, deadline):
    # key = starting node, vale = (max_len, path)
    paths = defaultdict(list)
    # finding the longest path
    top_one_len = -1
    top_one_path = []
    for node in list(graph.keys()):
        path = get_longest_path(graph, node, deadline, [])
        if path:
            max_len   = max(len(p) for p in path)
            max_paths = [p for p in path if len(p) == max_len]
            if len(max_paths)!=1:
                max_paths = max_paths[0]
            if max_len > top_one_len:
                top_one_len = max_len
                top_one_path = max_paths
            paths[node] = (max_len, max_paths)
    # finding top 2 influencer
    top_two_node = -1
    top_two_len = -1
    for node in list(paths.keys()):
        path = paths[node][1]
        result = [x for x in path if x not in top_one_path]
        if path and len(result)>top_two_len:
            top_two_node = node
            top_two_len = len(result)
    return top_two_node,top_two_len



if __name__ == '__main__':
    start = time.time()
    input_file = sys.argv[1]
    deadline = int(sys.argv[2])
    # Build graph dictionary
    graph = generate_graph(input_file)
    # Run DFS, compute longest path
    node, spread = Top_2_Influencer(graph, deadline)
    end = time.time()
    print("TOP-2 INFLUENCER: " + str(node) + " SPREAD:" + str(spread) + " TIME:" + str(end-start) + " sec")


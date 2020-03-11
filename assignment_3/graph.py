import numpy as np

def generate_graph (inputfile, graph):
    f = open(inputfile, "r")
    for row in f:
        item = row.split()
        graph[int(item[0])][int(item[1])] = float(item[2])
    print(graph)

if __name__ == "__main__":
    inputfile = "facebook_large.txt"
    graph = np.zeros((5000,5000))
    generate_graph(inputfile, graph)
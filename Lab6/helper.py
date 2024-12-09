GRAPH = [   # every row includes two arrays representing left and right nodes
    [3],
    [3, 4],
    [3, 4, 5],
]
DOLE_1 = []
DOLE_2 = []


def prepare_graph(graph, n):
    global GRAPH, DOLE_1, DOLE_2
    GRAPH = graph
    DOLE_1 = [i for i in range(n)]
    DOLE_2 = [i + n for i in range(n)]

    GRAPH.append( DOLE_1[:] )
    GRAPH.append([])
    
    for node in DOLE_2:
        GRAPH[node].append(len(GRAPH) - 1)


def find_node(from_node, to_node):
    if from_node == to_node:
        return [from_node]

    for node in GRAPH[from_node]:
        if find_node(node, to_node) is not None:
            return [from_node] + find_node(node, to_node)
    
    return None


def find_every_node(from_node):
    result = set()

    for node in GRAPH[from_node]:
        if find_every_node(node) is not None:
            result |= { node } | find_every_node(node)
    
    return result


def algo():
    arr_index = 1
    from_node = len(GRAPH) - 2
    to_node = len(GRAPH) - 1

    path = find_node(from_node, to_node)

    while path is not None:
        GRAPH[path[0]].remove(path[1])
        GRAPH[path[-2]].remove(path[-1])

        for node_index in range(1, len(path) - 2):
            GRAPH[path[node_index]].remove(path[node_index + 1])
            GRAPH[path[node_index + 1]].append(path[node_index])

        path = find_node(from_node, to_node)
    
    result = []
    for node in DOLE_2:
        for second_node in GRAPH[node]:
            if second_node != len(GRAPH) - 1:
                result.append((node, second_node))

    return result
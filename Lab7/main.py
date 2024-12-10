G = [ # network must be one-sided
    [1, 2, 3], 
    [2],
    [3],
    []
]

c_1 = [1, 2, 0, 0, 0] # weights foward
c_2 = [0, 0, 3, 2, 2] # weights backward

s = 3
t = 1

# initialize G_backward and prepare G
i = 0
G_backward = [ {} for _ in range(len(G)) ]
for k, row in enumerate(G):
    G[k] = {}
    for j, vertex in enumerate(row):
        G_backward[vertex][k] = i + j
        G[k][vertex] = i + j
    i += len(row)

f_1 = []
f_2 = []

cf_1 = []
cf_2 = []

fp_1 = []
fp_2 = []

path = []

min_weight = float('inf')


def references(vertex):
    queue = [vertex]

    while True:

        if not queue:
            return

        vertex = queue[0]
        queue = queue[1:]

        for forward_vertex, edge_index in G[vertex].items():
            if cf_1[edge_index] > 0 and path[forward_vertex] is None:
                path[forward_vertex] = vertex
                queue.append(forward_vertex)

        for forward_vertex, edge_index in G_backward[vertex].items():
            if cf_2[edge_index] > 0 and path[forward_vertex] is None:
                path[forward_vertex] = vertex
                queue.append(forward_vertex)


def step1():
    global f_1, f_2

    f_1 = [0] * len(c_1)
    f_2 = [0] * len(c_2)

    return step2()


def step2():
    global cf_1, cf_2

    cf_1 = [c_1[i] - f_1[i] + f_2[i] for i in range(len(c_1))]
    cf_2 = [c_2[i] - f_2[i] + f_1[i] for i in range(len(c_2))]

    return step3()


def step3():
    global path
    path = [None] * len(G)
    path[s] = 0

    references(s)
    if path[t] is None:
        return

    return step5()

def step5():
    global min_weight

    current = t
    min_weight = float('inf')
    
    while current != s:

        if current in G[path[current]]:
            new_weight = cf_1[G[path[current]][current]]
        else:
            new_weight = cf_2[G_backward[path[current]][current]]

        if min_weight > new_weight:
            min_weight = new_weight
        
        current = path[current]

    return step6()

def step6():
    global fp_1, fp_2

    fp_1 = [0] * len(c_1)
    fp_2 = [0] * len(c_2)

    current = t

    while current != s:

        if current in G[path[current]]:
            fp_1[G[path[current]][current]] = min_weight
        else:
            fp_2[G_backward[path[current]][current]] = min_weight

        current = path[current]

    return step7()


def step7():
    global f_1, f_2

    fn_1 = [max(0, f_1[i] - f_2[i] + fp_1[i] - fp_2[i]) for i in range(len(c_1))]
    fn_2 = [max(0, f_2[i] - f_1[i] + fp_2[i] - fp_1[i]) for i in range(len(c_2))]
    
    f_1 = fn_1
    f_2 = fn_2

    return step8()


def step8():
    global cf_1, cf_2

    current = t

    while current != s:

        if current in G[path[current]]:
            cf_1[G[path[current]][current]] -= min_weight
            cf_2[G_backward[current][path[current]]] += min_weight
        else:
            cf_2[G_backward[path[current]][current]] -= min_weight
            cf_1[G[current][path[current]]] += min_weight

        current = path[current]

    return step3()


def main():
    step1()

    i = 0
    for k, row in enumerate(G):
        for j, vertex in enumerate(row):
            print(f"Edge ({vertex}, {k}): {f_2[i + j]}")
            print(f"Edge ({k}, {vertex}): {f_1[i + j]}")
        i += len(row)


if __name__ == "__main__":
    main()
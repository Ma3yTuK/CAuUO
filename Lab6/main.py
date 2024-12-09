import helper

C = [
    [ 7, 2, 1, 9, 4 ],
    [ 9, 6, 9, 5, 5 ],
    [ 3, 8, 3, 1, 8 ],
    [ 7, 9, 4, 2, 2 ],
    [ 8, 4, 7, 4, 8 ]
]


n = len(C)
a = []
b = []
a_c = []
b_c = []
a_s = []
b_s = []
Jeq = []
Jlt = []
G = []
M = []
MARKED_VERTECES = []
MARKED_I = []
MARKED_J = []
TETTA = 0


def step1():
    global a, b
    a = [0] * n
    b = [min(list(zip(*C))[i]) for i in range(n)]

    return step2()


def step2():
    global Jeq, Jlt
    Jeq = []
    Jlt = []
    for i in range(n):
        for j in range(n):
            if a[i] + b[j] == C[i][j]:
                Jeq.append((i, j))
            if a[i] + b[j] < C[i][j]:
                Jlt.append((i, j))
    
    return step3()


def step3():
    global G
    G = []
    for i in range(n * 2):
        G.append([])

    for i, j in Jeq:
        G[i].append(n + j)
    
    return step4()


def step4():
    global M
    helper.prepare_graph(G, n)
    M = helper.algo() # changes G as well

    return step5()


def step5():
    if len(M) == n:
        result = []
        for vj, ui in M:
            result.append((ui, vj - n))
        return result
    
    return step6()


def step6():
    global MARKED_VERTECES
    MARKED_VERTECES = helper.find_every_node(len(G) - 2)

    return step7()


def step7():
    global MARKED_I, MARKED_J
    MARKED_I = []
    MARKED_J = []

    for vertex in MARKED_VERTECES:
        if vertex < n:
            MARKED_I.append(vertex)
        else:
            MARKED_J.append(vertex - n)
    
    return step8()


def step8():
    global a_c, b_c
    a_c = [1 if i in MARKED_I else -1 for i in range(n)]
    b_c = [-1 if j in MARKED_J else 1 for j in range(n)]

    return step9()


def step9():
    global TETTA
    values = []

    for i in range(n):
        if i in MARKED_I:
            for j in range(n):
                if j not in MARKED_J:
                    values.append((C[i][j] - a[i] - b[j]) / 2)
    
    TETTA = min(values)

    return step10()


def step10():
    global a_s, b_s

    a_s = [a[i] + TETTA * a_c[i] for i in range(n)]
    b_s = [b[i] + TETTA * b_c[i] for i in range(n)]

    return step11()


def step11():
    global a, b
    a = a_s
    b = b_s

    return step2()


def main():
    result = step1()
    r_sum = 0
    for i, j in result:
        r_sum += C[i][j]
    
    print(result)
    print(r_sum)


if __name__ == "__main__":
    main()
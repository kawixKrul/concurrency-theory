from graphviz import Digraph

def visualize_diekerts_graph(n, filename):
    A = []
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            A += [((i, j), f'A{i}{j}', '#ff0000')]

    B = []
    for i in range(1, n):
        for j in range(i, n + 2):
            for k in range(i + 1, n + 1):
                B += [((i, j, k), f'B{i}{j}{k}', '#00ff00')]

    C = []
    for i in range(1, n):
        for j in range(i, n + 2):
            for k in range(i + 1, n + 1):
                C += [((i, j, k), f'C{i}{j}{k}', '#0000ff')]

    G = Digraph(name='Diekerts graph')
    for (_, label, color) in (A+B+C):
        G.node(label, style='filled', fillcolor=color)

    for ((i, j), A_label, _) in A:
        for ((l, m, x), B_label, _) in B:
            if i == l and j == x:
                G.edge(A_label, B_label)

    for ((i, j, k), B_label, _) in B:
        for ((l, m, x), C_label, _) in C:
            if i == l and j == m and k == x:
                G.edge(B_label, C_label)
            
    for ((i, j, k), C_label, _) in C:
        for ((l, m), A_label, _) in A:
            if i == l - 1 and j == l and (k == l or k == m):
                G.edge(C_label, A_label)

    for ((i, j, k), C_label, _) in C:
        for ((l, m, x), B_label, _) in B:
            if l != m and i == l - 1 and j == m and k == l:
                G.edge(C_label, B_label)

    for ((i, j, k), C1_label, _) in C:
        for ((l, m, x), C2_label, _) in C:
            if l != m and i == l - 1 and j == m and k == x:
                G.edge(C1_label, C2_label)


    G.save(filename=f'{filename}.dot')
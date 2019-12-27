def build_time(source_files, transformations, target_file):
    """
    Return milliseconds needed to build the target file, assuming 
    files not dependent on each other can be processed simultaneously.
    Input:      source | list of source file names
            transforms | list of transformations of form
                       | ([input_files], output_file, transform_time)
                target | name of target file to build
    """
    A = {} # dict mapping file to a set of files
    w = {} # dict mapping file to dict of file: weight

    vert = set()
    for file in source_files:
        vert.add(file)
    for t in transformations:
        for in_file in t[0]:
            vert.add(in_file)
        vert.add(t[1])

    for v in vert:
        A[v] = set()
        w[v] = {}

    for trans in transformations:
        for file in trans[0]:
            if file in A:
                A[trans[1]].add(file)
                w[trans[1]][file] = -trans[2]
            else:
                A[trans[1]] = {file}
                w[trans[1]] = {file: -trans[2]}
    # print(A, w)
    d, parent = min_weight_path(A, w, target_file)

    min_path = float('inf')

    for v in d:
        if d[v] < min_path:
            min_path = d[v]

    # print(min_path)
    return abs(min_path)

def min_weight_path(A, w, s):
    _, order = DFS(A, s)
    order.reverse()

    d = {file: float('inf') for file in A}

    parent = {file: None for file in A}

    d[s], parent[s] = 0, s

    def relax(w, d, parent, u, v):
        if d[v] > d[u] + w[u][v]:
            d[v] = d[u] + w[u][v]
            parent[v] = u

    for u in order:
        if u is not None:
            for v in A[u]:
                relax(w, d, parent, u, v)
    return d, parent


def DFS(A, s, parent = None, order = []):
    if parent is None:
        parent = {v: None for v in A}
        parent[s] = s
    for v in A[s]:
        if parent[v] is None:
            parent[v] = s
            DFS(A, v, parent, order)
    order.append(s)
    return parent, order


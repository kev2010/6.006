def bidirectional_dijkstra(Adj, w, s, t):
    """
    Return a list of vertices forming a shortest path from s to t 
    Vertices are all integers in range(len(Adj))
    Input:  Adj: undirected graph, Adj[v] is list of vertices adjacent to v
              w: weight dictionary, w[(u,v)] is integer weight of edge (u,v)
              s: source vertex
              t: target vertex
    """
    d_s = [float('inf') for _ in Adj]
    d_t = [float('inf') for _ in Adj]
    parent_s = [None for _ in Adj]
    parent_t = [None for _ in Adj]

    d_s[s], parent_s[s] = 0, s
    d_t[t], parent_t[t] = 0, t
    Q_s = PriorityQueue()
    Q_t = PriorityQueue()

    D = float('inf')
    V = 0

    for v in range(len(Adj)):
        Q_s.insert(v, d_s[v])
        Q_t.insert(v, d_t[v])

    for _ in range(len(Adj)):
        checkers = False
        if Q_s.find_min() < Q_t.find_min():
            if d_s[Q_s.A[0].label] > D / 2:
                break
            u = Q_s.extract_min()
            vp = d_s[u] + d_t[u]

            checkers = True
        else:
            if d_t[Q_t.A[0].label] > D / 2:
                break
            u = Q_t.extract_min()
            vp = d_s[u] + d_t[u]

        for v in Adj[u]:
            if checkers:
                relax(Adj, w, d_s, parent_s, u, v)
                Q_s.decrease_key(v, d_s[v])
            else:
                relax(Adj, w, d_t, parent_t, u, v)
                Q_t.decrease_key(v, d_t[v])

        if vp < D:
            D = vp
            V = u

    path_s = []
    p_s = V
    if s != V and t != V:
        path_s.append(V)
    while parent_s[p_s] != s:
        path_s.append(parent_s[p_s])
        p_s = parent_s[p_s]

    path_s.append(s)

    path_t = []
    p_t = V
    while parent_t[p_t] != t:
        path_t.append(parent_t[p_t])
        p_t = parent_t[p_t]

    path_t.append(t)

    path = path_s[::-1] + path_t
    return path


def relax(A, w, d, parent, u, v):
    if d[v] > d[u] + w[(u, v)]:
        d[v] = d[u] + w[(u, v)]
        parent[v] = u

class Item:
    def __init__(self, label, key):
        self.label, self.key = label, key

class PriorityQueue:                      # Binary Heap Implementation
    def __init__(self):                   # stores keys with unique labels
        self.A = []
        self.label2idx = {}

    def min_heapify_up(self, c):            
        if c == 0: return
        p = (c - 1) // 2
        if self.A[p].key > self.A[c].key:   
            self.A[c], self.A[p] = self.A[p], self.A[c]         
            self.label2idx[self.A[c].label] = c
            self.label2idx[self.A[p].label] = p
            self.min_heapify_up(p)         

    def min_heapify_down(self, p):          
        if p >= len(self.A): return
        l = 2 * p + 1
        r = 2 * p + 2
        if l >= len(self.A): l = p
        if r >= len(self.A): r = p
        c = l if self.A[r].key > self.A[l].key else r 
        if self.A[p].key > self.A[c].key:             
            self.A[c], self.A[p] = self.A[p], self.A[c]         
            self.label2idx[self.A[c].label] = c
            self.label2idx[self.A[p].label] = p
            self.min_heapify_down(c)       

    def insert(self, label, key):         # insert labeled key
        self.A.append(Item(label, key))
        idx = len(self.A) - 1
        self.label2idx[self.A[idx].label] = idx
        self.min_heapify_up(idx)

    def find_min(self):                   # return minimum key
        return self.A[0].key

    def extract_min(self):                # remove a label with minimum key
        self.A[0], self.A[-1] = self.A[-1], self.A[0]
        self.label2idx[self.A[0].label] = 0
        del self.label2idx[self.A[-1].label]
        min_label = self.A.pop().label
        self.min_heapify_down(0)
        return min_label

    def decrease_key(self, label, key):   # decrease key of a given label
        if label in self.label2idx:
            idx = self.label2idx[label]
            if key < self.A[idx].key:
                self.A[idx].key = key
                self.min_heapify_up(idx)


A = [[1, 2, 3, 4], [0, 5, 6, 7], [0, 8, 9], [0], [0], [1], [1], [1], [2], [2]]
w = {(0, 1): 5, (1, 0): 5, (0, 2): 1, (2, 0): 1, (0, 3): 5, (3, 0): 5, (0, 4): 9, (4, 0): 9, (1, 5): 13, (5, 1): 13, (1, 6): 5, (6, 1): 5, (1, 7): 13, (7, 1): 13, (2, 8): 12, (8, 2): 12, (2, 9): 5, (9, 2): 5}

s = 0
t = 9

print(bidirectional_dijkstra(A, w, s, t))


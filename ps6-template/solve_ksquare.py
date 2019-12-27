def is_solved(config):
    "Return whether input config is solved"
    ##################
    # YOUR CODE HERE #
    ##################
    k = len(config)
    for i in range(1, k**2+1):
        y = (i-1)//k
        x = i - k*y - 1
        if config[y][x] != i:
            return False
    return True

def move(config, mv):
    "Return a new configuration made by moving config by move mv"
    k = len(config)
    (s, i) = mv         # s in ("row", "col") and i in range(k)

    if s == "row":
        flipped = tuple([-i for i in config[i][::-1]])
        config = config[:i] + (flipped,) + config[i+1:]
    if s == "col":
        copy = ()
        for a in range(len(config)):
            temp = ()
            for b in range(len(config)):
                if (a*k + b) % k == i:
                    temp += (-config[k-a-1][i],)
                else:
                    temp += (config[a][b],)
                # print(temp)
            copy += (temp,)
        config = copy[:]
    return tuple([tuple(row) for row in config])

def getAdjacent(config):
    adjacent = [None] * (2*len(config))
    moves = [None] * (2*len(config))
    k = len(config)
    for i in range(0, k):
        moves[i] = ("row", i)
        adjacent[i] = move(config, ("row", i))
        moves[i+k] = ("col", i)
        adjacent[i+k] = move(config, ("col", i))
    return (adjacent, moves)

def solve_ksquare(config):
    "Return a list of moves that solves config"
    ##################
    # YOUR CODE HERE #
    ##################
    if is_solved(config):
        return []

    parent = {config: None}
    prev = [config]
    level = 1
    while len(prev) > 0:
        next = []
        for u in prev:
            edges, moves = getAdjacent(u)
            for i in range(len(edges)):
                e = edges[i]
                if e not in parent:
                    parent[e] = moves[i], u
                    next.append(e)

                    if is_solved(e):
                        ans = []
                        current = e

                        for j in range(0,level):
                            p = parent[current]
                            ans.append(p[0])
                            current = p[1]

                        return ans[::-1]
        prev = next
        level += 1
    return []

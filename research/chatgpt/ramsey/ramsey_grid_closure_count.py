"""Count undirected Hamiltonian cycles of small step-count grids, without symmetry quotient."""
from functools import lru_cache


def cycles(a, b):
    width = a + 1
    size = width * (b + 1)
    if size % 2:
        return 0  # bipartite grid
    start, finish = 1, width  # a cycle must use both neighbors of corner 0
    adj = [[] for _ in range(size)]
    for v in range(size):
        for u in (v-1, v+1, v-width, v+width):
            if 0 <= u < size and abs(v % width-u % width)+abs(v//width-u//width)==1:
                adj[v].append(u)
    @lru_cache(None)
    def paths(v, remaining):
        if v == finish:
            return int(not remaining)
        return sum(paths(u, remaining ^ (1 << u)) for u in adj[v] if remaining >> u & 1)
    return paths(start, ((1 << size)-1) ^ 1 ^ (1 << start))

if __name__ == '__main__':
    for k in (3, 4, 7):
        print((3,k), cycles(3,k))

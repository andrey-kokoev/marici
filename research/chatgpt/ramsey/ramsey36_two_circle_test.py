"""Two-circle Ramsey(3,6) test; exact four-sector obstruction.

Every A edge of the two-circle model has angular separation >90 degrees
in each circle. A graph admits such a one-circle positioning iff some
proper 4-coloring has no directed cycle on edges moving clockwise one
color class, for one of the six cyclic orders of its color classes.

Data: Brendan McKay's seven 17-vertex R(3,6)-critical graphs (graph6).
Checks every canonical proper four-coloring, not a sample. This is only a
necessary condition for the full two-circle inequality, not sufficient.
"""
from itertools import permutations

G6 = [
    'P??GaOo`XMGsIcT?pSLaGuA?',
    'P?C?I_h`SDEQQcLAh`dU?tG?',
    'P@oGQA?`ACcdCtDYC]Ah?goC',
    'PG?OSAKccKGiGwJSI[@oWUA_',
    'PGD?OkeO_WAEGQobP_s`cgU?',
    'Ps`A?WIDGeCdGsQEKK?oLL_O',
    'Ps`A?_KChFCiBoQSKCOoXL_O',
]

def decode_graph6(s):
    n = ord(s[0]) - 63
    bits = [((ord(ch) - 63) >> p) & 1 for ch in s[1:] for p in range(5, -1, -1)]
    pairs = ((i, j) for j in range(1, n) for i in range(j))
    edges = [pair for pair, bit in zip(pairs, bits) if bit]
    assert n == 17
    return n, edges


def scan(s):
    n, edges = decode_graph6(s)
    nbr = [set() for _ in range(n)]
    for i, j in edges:
        nbr[i].add(j); nbr[j].add(i)
    order = sorted(range(n), key=lambda i: (-len(nbr[i]), i))
    color = [-1] * n
    orders = [(0, *p) for p in permutations((1, 2, 3))]
    total = 0
    admissible = 0
    witness = None

    def acyclic(perm):
        indeg = [0]*n
        out = [[] for _ in range(n)]
        for i, j in edges:
            gap = (perm[color[j]] - perm[color[i]]) % 4
            if gap == 1:
                out[i].append(j); indeg[j] += 1
            elif gap == 3:
                out[j].append(i); indeg[i] += 1
        stack = [v for v in range(n) if indeg[v] == 0]
        count = 0
        while stack:
            v = stack.pop(); count += 1
            for u in out[v]:
                indeg[u] -= 1
                if indeg[u] == 0:
                    stack.append(u)
        return count == n

    def visit(d, used):
        nonlocal total, admissible, witness
        if d == n:
            assert used == 4  # These graphs are 4-chromatic.
            total += 1
            good = [perm for perm in orders if acyclic(perm)]
            if good:
                admissible += 1
                if witness is None:
                    witness = (color.copy(), good[0])
            return
        v = order[d]
        taken = {color[u] for u in nbr[v] if color[u] != -1}
        for c in range(min(used + 1, 4)):
            if c not in taken:
                color[v] = c
                visit(d + 1, max(used, c + 1))
        color[v] = -1
    visit(0, 0)
    return len(edges), total, admissible, witness

if __name__ == '__main__':
    for index, graph in enumerate(G6, 1):
        nedges, counted, passed, witness = scan(graph)
        print(f'graph {index}: {nedges} edges; {counted} canonical 4-colorings; '
              f'{passed} admit a strict 90-degree single-circle realization')
        assert (passed > 0) == (index not in (2, 6))
    print('Verified: graphs 2 and 6 fail the necessary circle condition.')

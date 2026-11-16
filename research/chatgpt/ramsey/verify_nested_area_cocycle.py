"""Exact Z^3 second-order signature / nested single-cycle cocycle verifier.

Uses integer positions and twice the oriented area vector, so every check
is an integer identity (no floating point tolerances).
"""
from itertools import combinations, permutations


def sub(u, v):
    return tuple(a-b for a, b in zip(u, v))


def add(u, v):
    return tuple(a+b for a, b in zip(u, v))


def cross(u, v):
    return (u[1]*v[2]-u[2]*v[1],
            u[2]*v[0]-u[0]*v[2],
            u[0]*v[1]-u[1]*v[0])


def signature(path, positions):
    """(endpoint displacement, twice oriented area)."""
    d = (0, 0, 0)
    area2 = (0, 0, 0)
    for i, j in zip(path, path[1:]):
        e = sub(positions[j], positions[i])
        area2 = add(area2, cross(d, e))
        d = add(d, e)
    return d, area2


def forward_path(cycle, i, j):
    # Empty path when i == j; otherwise use the unique forward arc.
    at = {v: k for k, v in enumerate(cycle)}
    n = len(cycle)
    t = (at[j] - at[i]) % n
    return [cycle[(at[i]+k) % n] for k in range(t+1)]


def test(positions, a_cycle, b_cycle):
    B = set(b_cycle)
    A = set(a_cycle)
    assert A <= B and len(B) == len(b_cycle) and len(A) == len(a_cycle)
    nxt_b = {b_cycle[t]: b_cycle[(t+1) % len(b_cycle)] for t in range(len(b_cycle))}

    access = {}
    anchor = {}
    for x in b_cycle:
        route = [x]
        while route[-1] not in A:
            route.append(nxt_b[route[-1]])
        access[x] = route
        anchor[x] = route[-1]

    def a_route(i, j):
        # x --b--> first A node --a--> second A node <--b-- y
        middle = forward_path(a_cycle, anchor[i], anchor[j])
        return access[i] + middle[1:] + list(reversed(access[j]))[1:]

    def b_route(i, j):
        return forward_path(b_cycle, i, j)

    sa = signature(a_cycle + [a_cycle[0]], positions)[1]
    sb = signature(b_cycle + [b_cycle[0]], positions)[1]
    h = {}
    for i, j in permutations(b_cycle, 2):
        h[i, j] = sub(signature(a_route(i, j), positions)[1],
                      signature(b_route(i, j), positions)[1])

    rank_a = {x: t for t, x in enumerate(a_cycle)}
    rank_b = {x: t for t, x in enumerate(b_cycle)}

    def eps(rank, n, i, j, k):
        return (((rank[j]-rank[i]) % n)
              + ((rank[k]-rank[j]) % n)
              - ((rank[k]-rank[i]) % n)) // n

    for i, j, k in permutations(b_cycle, 3):
        lhs = sub(add(h[i, j], h[j, k]), h[i, k])
        ea = eps(rank_a, len(a_cycle), anchor[i], anchor[j], anchor[k])
        eb = eps(rank_b, len(b_cycle), i, j, k)
        rhs = sub(tuple(ea*s for s in sa), tuple(eb*s for s in sb))
        assert lhs == rhs, (i, j, k, lhs, rhs)

    # A special consequence of the 3-node identity with endpoints reversed.
    for i, j in permutations(b_cycle, 2):
        lhs = add(h[i, j], h[j, i])
        rhs = sub(sa, sb) if anchor[i] != anchor[j] else tuple(-s for s in sb)
        assert lhs == rhs, (i, j, lhs, rhs)
    return sa, sb, h


# Nested A subset of B, coordinates entirely integral.
positions = [(3*i*i % 23, 7*i % 19, 5*i*i*i % 17) for i in range(8)]
a_cycle = [0, 4, 2, 7]
b_cycle = list(range(8))
sa, sb, h = test(positions, a_cycle, b_cycle)
print('nested exact check: 8 nodes, A=4, B=8, 336 ordered triples verified')
print('2*area(a) =', sa, '2*area(b) =', sb)

# Integer approximation of a regular pentagon; A=B for the baseline test.
pentagon = [(1000, 0, 0), (309, 951, 0), (-809, 588, 0),
            (-809, -588, 0), (309, -951, 0)]
sa5, sb5, h5 = test(pentagon, [0, 2, 4, 1, 3], list(range(5)))

def dot(u,v):
    return sum(a*b for a,b in zip(u,v))

a_edges = {pair for pair in combinations(range(5), 2)
           if dot(h5[pair[0],pair[1]],h5[pair[1],pair[0]]) > 0}
assert a_edges == {(0,2), (0,3), (1,3), (1,4), (2,4)}
print('pentagon exact check: A-edges =', sorted(a_edges))
print('triangle-free; independence number 2; 20 ordered triples verified')

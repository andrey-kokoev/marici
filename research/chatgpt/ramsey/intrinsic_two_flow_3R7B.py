"""Coordinate-free 3R/7B two-flow construction on a genus-one theta ribbon graph.

States are oriented graph edges (darts).  A chosen local cyclic order
at each vertex determines relative clockwise/counterclockwise successor
permutations.  Colors belong to UNORIENTED edges.
"""
from collections import defaultdict
from itertools import combinations


def theta_graph(lengths=(2, 3, 5)):
    edges = []
    stars = defaultdict(list)
    branch_edges = []
    next_vertex = 2
    for length in lengths:
        vertices = [0] + list(range(next_vertex, next_vertex + length - 1)) + [1]
        next_vertex += length - 1
        branch = []
        for u, v in zip(vertices, vertices[1:]):
            edge = len(edges)
            edges.append((u, v))
            stars[u].append(2 * edge)
            stars[v].append(2 * edge + 1)
            branch.append(edge)
        branch_edges.append(branch)
    return edges, stars, branch_edges


def build_flows(lengths=(2, 3, 5)):
    edges, stars, branches = theta_graph(lengths)
    sigma = {}
    # At both trivalent vertices, port order is branch 0, branch 1, branch 2.
    # Degree-two vertices have their unique alternating port order.
    for v, darts in stars.items():
        if v in (0, 1):
            assert len(darts) == 3
        for a, b in zip(darts, darts[1:] + darts[:1]):
            sigma[a] = b
    inverse = {j: i for i, j in sigma.items()}
    right = {d: sigma[d ^ 1] for d in sigma}
    left = {d: inverse[d ^ 1] for d in sigma}
    return edges, branches, right, left


def cycles(permutation):
    seen = set()
    result = []
    for d in permutation:
        if d not in seen:
            out = []
            p = d
            while p not in seen:
                seen.add(p)
                out.append(p)
                p = permutation[p]
            assert p == d
            result.append(out)
    return result


def color_word(cycle, red_edges):
    return ''.join('R' if d // 2 in red_edges else 'B' for d in cycle)


def valid_word(word, window=10, red_count=3):
    assert len(word) % window == 0
    return all(sum(word[(i+j) % len(word)] == 'R' for j in range(window)) == red_count
               for i in range(len(word)))


def matmul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def product(word):
    U = ((1, -1), (0, 1))
    V = ((1, 0), (1, 1))
    m = ((1, 0), (0, 1))
    for letter in word:
        m = matmul(m, U if letter == 'R' else V)
    return m


def power(a, n):
    result = ((1, 0), (0, 1))
    for _ in range(n):
        result = matmul(result, a)
    return result


def residue_components(cycle):
    assert len(cycle) % 10 == 0
    position = {d: i for i, d in enumerate(cycle)}
    parent = list(range(10))
    def find(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(x, y):
        parent[find(x)] = find(y)
    for e in range(len(cycle) // 2):
        union(position[2*e] % 10, position[2*e+1] % 10)
    groups = defaultdict(list)
    for p in range(10):
        groups[find(p)].append(p)
    return sorted([tuple(group) for group in groups.values()], key=lambda c: c[0])


def run():
    edges, branches, right, left = build_flows()
    cycles_right = cycles(right)
    cycles_left = cycles(left)
    assert len(cycles_right) == len(cycles_left) == 1
    rr, ll = cycles_right[0], cycles_left[0]
    assert len(rr) == len(ll) == 20
    # F_left = alpha F_right^{-1} alpha
    inverse_right = {v: k for k, v in right.items()}
    for d in right:
        assert left[d] == (inverse_right[d^1] ^ 1)

    red_edges = {0, 1, 7}    # RR / BBB / BBRBB along the three branches
    wr = color_word(rr, red_edges)
    wl = color_word(ll, red_edges)
    assert valid_word(wr) and valid_word(wl)
    assert wr == 'RRBBBBBRBB' * 2
    assert wl == 'RRBBRBBBBB' * 2
    for w in (wr[:10], wl[:10]):
        assert power(product(w), 3) == ((-1, 0), (0, -1))
        assert power(product(w), 6) == ((1, 0), (0, 1))
        assert power(product(w), 2) != ((1, 0), (0, 1))
    valid = []
    for reds in combinations(range(10), 3):
        if all(valid_word(color_word(cyc, set(reds))) for cyc in (rr, ll)):
            valid.append(reds)
    assert len(valid) == 8

    n_vertices = len({u for e in edges for u in e})
    n_edges = len(edges)
    n_faces = len(cycles_right)
    genus = (2 - (n_vertices - n_edges + n_faces)) // 2
    assert (n_vertices, n_edges, n_faces, genus) == (9, 10, 1, 1)

    print('branches, edge IDs:', branches)
    print('vertices, edges, faces, genus:', n_vertices, n_edges, n_faces, genus)
    print('right tour darts:', rr)
    print('left tour darts: ', ll)
    print('right 10-window:', wr[:10])
    print('left 10-window: ', wl[:10])
    print('residue classes: ', residue_components(rr))
    print('compatible 3-red edge sets:', valid)
    print('right matrix after 10:', product(wr[:10]))
    print('left matrix after 10: ', product(wl[:10]))
    print('physical closure after 20; full matrix-frame closure after 60')

if __name__ == '__main__':
    run()

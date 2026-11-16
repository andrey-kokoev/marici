"""Exact constructive coverage of all seven 17-node Ramsey(3,6) types.

Run: python ramsey36_seven_types_representation.py

Standard library only. Reconstructs each graph from the 16-node Clebsch
carrier by existing square operations and one four-port vertex birth.
Checks both forbidden simplex conditions at every stage. Explicit A and B
Hamiltonian cycles certify the traversal requirements at every stage.
Final isomorphisms are checked against the complete published catalogue.

Catalogue source: Brendan D. McKay,
https://users.cecs.anu.edu.au/~bdm/data/r36_17.g6
https://users.cecs.anu.edu.au/~bdm/data/ramsey.html
McKay's data are CC BY 4.0. Catalogue ordering defines type numbers.

The seven-graph classification is an external input for COMPLETENESS ONLY.
The construction paths and admissibility tests do not use target graphs.
This is a finite representation theorem, not a general Ramsey formula.
"""
from itertools import combinations
from collections import Counter

CATALOGUE = ['P??GaOo`XMGsIcT?pSLaGuA?',
 'P?C?I_h`SDEQQcLAh`dU?tG?',
 'P@oGQA?`ACcdCtDYC]Ah?goC',
 'PG?OSAKccKGiGwJSI[@oWUA_',
 'PGD?OkeO_WAEGQobP_s`cgU?',
 'Ps`A?WIDGeCdGsQEKK?oLL_O',
 'Ps`A?_KChFCiBoQSKCOoXL_O']

RECORDS = [{'catalogue_type': 1,
  'moves': [{'kind': 'half', 'vertices': [0, 1, 2, 3], 'remove': [[0, 1], [2, 3]], 'add': [[0, 3]]},
            {'kind': 'half', 'vertices': [4, 5, 6, 7], 'remove': [[4, 6], [5, 7]], 'add': [[5, 6]]},
            {'kind': 'half', 'vertices': [8, 9, 12, 13], 'remove': [[8, 12], [9, 13]], 'add': [[8, 13]]}],
  'birth_ports': [1, 2, 4, 7],
  'catalogue_bijection': [4, 15, 14, 7, 16, 3, 8, 9, 12, 2, 6, 10, 1, 13, 11, 5, 0],
  'cycles': [{'A': [0, 1, 3, 2, 6, 4, 5, 7, 8, 9, 11, 10, 14, 12, 13, 15],
              'B': [0, 3, 5, 6, 8, 11, 13, 14, 2, 1, 4, 7, 9, 10, 15, 12]},
             {'A': [1, 3, 0, 2, 6, 4, 5, 7, 8, 10, 11, 15, 14, 12, 13, 9],
              'B': [0, 5, 6, 11, 12, 1, 7, 10, 13, 8, 14, 2, 3, 4, 15, 9]},
             {'A': [1, 3, 7, 6, 2, 0, 4, 5, 10, 8, 9, 11, 15, 13, 12, 14],
              'B': [0, 5, 9, 12, 7, 10, 15, 1, 2, 11, 6, 3, 4, 8, 13, 14]},
             {'A': [1, 9, 6, 2, 0, 3, 7, 8, 10, 5, 4, 11, 15, 13, 12, 14],
              'B': [0, 5, 11, 14, 7, 13, 9, 2, 3, 4, 8, 1, 6, 10, 15, 12]},
             {'A': [9, 1, 16, 2, 6, 5, 4, 0, 3, 7, 8, 10, 14, 12, 13, 15, 11],
              'B': [0, 1, 6, 10, 13, 4, 7, 11, 12, 2, 8, 14, 3, 5, 9, 15, 16]}]},
 {'catalogue_type': 2,
  'moves': [{'kind': 'switch', 'vertices': [0, 1, 2, 3], 'remove': [[0, 1], [2, 3]], 'add': [[0, 3], [1, 2]]},
            {'kind': 'half', 'vertices': [0, 1, 2, 3], 'remove': [[0, 3], [1, 2]], 'add': [[0, 1]]},
            {'kind': 'half', 'vertices': [0, 4, 8, 12], 'remove': [[0, 4], [8, 12]], 'add': [[0, 12]]},
            {'kind': 'half', 'vertices': [1, 5, 9, 13], 'remove': [[1, 9], [5, 13]], 'add': [[5, 9]]}],
  'birth_ports': [1, 4, 8, 13],
  'catalogue_bijection': [7, 15, 1, 2, 10, 6, 14, 11, 9, 5, 12, 13, 8, 16, 4, 3, 0],
  'cycles': [{'A': [0, 1, 3, 2, 6, 4, 5, 7, 8, 9, 11, 10, 14, 12, 13, 15],
              'B': [0, 3, 5, 6, 8, 11, 13, 14, 2, 1, 4, 7, 9, 10, 15, 12]},
             {'A': [0, 2, 1, 3, 7, 5, 4, 6, 9, 11, 10, 14, 15, 13, 12, 8],
              'B': [0, 1, 6, 10, 12, 7, 11, 13, 4, 8, 14, 2, 3, 5, 15, 9]},
             {'A': [2, 0, 1, 3, 7, 5, 4, 6, 9, 8, 10, 11, 15, 14, 12, 13],
              'B': [0, 5, 6, 11, 12, 1, 7, 10, 13, 8, 14, 2, 3, 4, 15, 9]},
             {'A': [2, 0, 8, 10, 5, 1, 3, 7, 6, 4, 12, 14, 15, 11, 9, 13],
              'B': [0, 5, 6, 11, 12, 1, 7, 10, 13, 8, 14, 2, 3, 4, 15, 9]},
             {'A': [1, 3, 7, 5, 4, 6, 2, 0, 12, 13, 9, 8, 10, 11, 15, 14],
              'B': [0, 5, 6, 11, 12, 7, 10, 13, 1, 8, 14, 2, 3, 4, 15, 9]},
             {'A': [2, 0, 1, 3, 12, 13, 16, 4, 5, 7, 6, 14, 15, 11, 9, 8, 10],
              'B': [0, 4, 7, 9, 10, 1, 13, 14, 3, 2, 8, 11, 5, 6, 12, 15, 16]}]},
 {'catalogue_type': 3,
  'moves': [{'kind': 'switch', 'vertices': [0, 1, 2, 3], 'remove': [[0, 1], [2, 3]], 'add': [[0, 3], [1, 2]]},
            {'kind': 'half', 'vertices': [0, 1, 2, 3], 'remove': [[0, 2], [1, 3]], 'add': [[0, 1]]},
            {'kind': 'half', 'vertices': [4, 6, 9, 11], 'remove': [[4, 11], [6, 9]], 'add': [[6, 11]]},
            {'kind': 'half', 'vertices': [4, 6, 12, 14], 'remove': [[4, 12], [6, 14]], 'add': [[6, 12]]},
            {'kind': 'half', 'vertices': [8, 10, 12, 14], 'remove': [[8, 12], [10, 14]], 'add': [[10, 12]]}],
  'birth_ports': [2, 3, 4, 14],
  'catalogue_bijection': [16, 15, 5, 6, 0, 8, 9, 14, 2, 3, 11, 12, 10, 13, 1, 7, 4],
  'cycles': [{'A': [0, 1, 3, 2, 6, 4, 5, 7, 8, 9, 11, 10, 14, 12, 13, 15],
              'B': [0, 3, 5, 6, 8, 11, 13, 14, 2, 1, 4, 7, 9, 10, 15, 12]},
             {'A': [0, 2, 1, 3, 7, 5, 4, 6, 9, 11, 10, 14, 15, 13, 12, 8],
              'B': [0, 1, 6, 10, 12, 7, 11, 13, 4, 8, 14, 2, 3, 5, 15, 9]},
             {'A': [2, 1, 0, 3, 7, 5, 4, 6, 9, 8, 10, 11, 15, 14, 12, 13],
              'B': [0, 5, 6, 11, 12, 1, 7, 10, 13, 8, 14, 2, 3, 4, 15, 9]},
             {'A': [2, 1, 9, 13, 5, 4, 0, 3, 12, 8, 7, 6, 11, 15, 14, 10],
              'B': [0, 5, 6, 12, 9, 10, 15, 1, 3, 2, 7, 4, 8, 11, 13, 14]},
             {'A': [4, 0, 3, 7, 5, 1, 2, 10, 8, 9, 13, 12, 14, 15, 11, 6],
              'B': [0, 5, 6, 8, 11, 13, 14, 2, 3, 1, 7, 4, 9, 10, 15, 12]},
             {'A': [4, 0, 3, 7, 8, 9, 1, 5, 10, 2, 13, 12, 14, 15, 11, 6],
              'B': [0, 5, 6, 9, 10, 15, 3, 1, 12, 2, 7, 4, 8, 11, 13, 14]},
             {'A': [4, 16, 14, 1, 0, 3, 12, 6, 2, 10, 8, 7, 15, 11, 9, 13, 5],
              'B': [0, 2, 5, 11, 12, 7, 9, 14, 4, 3, 8, 13, 1, 6, 10, 15, 16]}]},
 {'catalogue_type': 4,
  'moves': [{'kind': 'switch', 'vertices': [0, 1, 2, 3], 'remove': [[0, 1], [2, 3]], 'add': [[0, 3], [1, 2]]},
            {'kind': 'switch',
             'vertices': [4, 5, 10, 11],
             'remove': [[4, 11], [5, 10]],
             'add': [[4, 10], [5, 11]]},
            {'kind': 'half', 'vertices': [0, 1, 2, 3], 'remove': [[0, 2], [1, 3]], 'add': [[0, 1]]},
            {'kind': 'half', 'vertices': [0, 4, 8, 10], 'remove': [[0, 8], [4, 10]], 'add': [[0, 10]]},
            {'kind': 'half', 'vertices': [5, 7, 13, 15], 'remove': [[5, 13], [7, 15]], 'add': [[7, 13]]}],
  'birth_ports': [2, 3, 8, 15],
  'catalogue_bijection': [11, 15, 10, 7, 1, 2, 16, 12, 8, 4, 5, 13, 14, 6, 3, 9, 0],
  'cycles': [{'A': [0, 1, 3, 2, 6, 4, 5, 7, 8, 9, 11, 10, 14, 12, 13, 15],
              'B': [0, 3, 5, 6, 8, 11, 13, 14, 2, 1, 4, 7, 9, 10, 15, 12]},
             {'A': [0, 2, 1, 3, 7, 5, 4, 6, 9, 11, 10, 14, 15, 13, 12, 8],
              'B': [0, 1, 6, 10, 12, 7, 11, 13, 4, 8, 14, 2, 3, 5, 15, 9]},
             {'A': [0, 2, 1, 3, 7, 5, 4, 6, 9, 11, 10, 14, 15, 13, 12, 8],
              'B': [0, 1, 6, 10, 12, 5, 15, 9, 3, 2, 7, 4, 8, 11, 13, 14]},
             {'A': [2, 1, 0, 3, 7, 5, 4, 6, 9, 8, 10, 11, 15, 14, 12, 13],
              'B': [0, 5, 6, 10, 12, 9, 15, 1, 3, 2, 7, 4, 8, 11, 13, 14]},
             {'A': [2, 1, 0, 3, 7, 5, 4, 6, 9, 8, 10, 11, 15, 14, 12, 13],
              'B': [0, 5, 6, 12, 9, 10, 15, 1, 3, 2, 7, 4, 8, 11, 13, 14]},
             {'A': [2, 1, 5, 4, 0, 3, 7, 6, 9, 8, 10, 11, 15, 14, 12, 13],
              'B': [0, 6, 11, 12, 1, 7, 10, 13, 4, 8, 14, 2, 3, 5, 15, 9]},
             {'A': [4, 5, 1, 0, 3, 7, 6, 2, 16, 8, 9, 11, 10, 14, 15, 13, 12],
              'B': [0, 2, 7, 9, 12, 11, 14, 16, 4, 1, 8, 13, 3, 5, 10, 15, 6]}]},
 {'catalogue_type': 5,
  'moves': [{'kind': 'switch', 'vertices': [0, 1, 2, 3], 'remove': [[0, 1], [2, 3]], 'add': [[0, 3], [1, 2]]},
            {'kind': 'switch', 'vertices': [0, 2, 4, 6], 'remove': [[0, 2], [4, 6]], 'add': [[0, 6], [2, 4]]},
            {'kind': 'half', 'vertices': [5, 7, 8, 10], 'remove': [[5, 10], [7, 8]], 'add': [[5, 8]]},
            {'kind': 'half', 'vertices': [8, 10, 12, 14], 'remove': [[8, 12], [10, 14]], 'add': [[8, 14]]},
            {'kind': 'half', 'vertices': [5, 8, 9, 13], 'remove': [[5, 13], [8, 9]], 'add': [[8, 13]]},
            {'kind': 'half', 'vertices': [0, 6, 8, 14], 'remove': [[0, 6], [8, 14]], 'add': [[6, 8]]}],
  'birth_ports': [0, 7, 9, 10],
  'catalogue_bijection': [11, 16, 10, 9, 13, 0, 12, 15, 14, 7, 4, 6, 1, 5, 2, 8, 3],
  'cycles': [{'A': [0, 1, 3, 2, 6, 4, 5, 7, 8, 9, 11, 10, 14, 12, 13, 15],
              'B': [0, 3, 5, 6, 8, 11, 13, 14, 2, 1, 4, 7, 9, 10, 15, 12]},
             {'A': [0, 2, 1, 3, 7, 5, 4, 6, 9, 11, 10, 14, 15, 13, 12, 8],
              'B': [0, 1, 6, 10, 12, 7, 11, 13, 4, 8, 14, 2, 3, 5, 15, 9]},
             {'A': [0, 3, 1, 2, 4, 5, 7, 6, 9, 11, 10, 14, 15, 13, 12, 8],
              'B': [0, 1, 7, 10, 12, 9, 2, 11, 5, 14, 3, 15, 4, 6, 8, 13]},
             {'A': [7, 3, 0, 6, 2, 1, 5, 4, 11, 9, 8, 10, 14, 12, 13, 15],
              'B': [0, 1, 11, 12, 2, 5, 6, 15, 8, 3, 9, 10, 4, 7, 13, 14]},
             {'A': [10, 2, 1, 3, 7, 5, 4, 11, 9, 6, 0, 15, 13, 12, 14, 8],
              'B': [0, 1, 11, 13, 6, 8, 4, 7, 12, 2, 14, 3, 5, 9, 15, 10]},
             {'A': [10, 2, 1, 5, 4, 11, 9, 6, 7, 3, 0, 15, 13, 12, 14, 8],
              'B': [0, 1, 11, 13, 6, 4, 7, 8, 12, 2, 14, 3, 5, 9, 15, 10]},
             {'A': [10, 2, 1, 5, 4, 0, 8, 6, 7, 3, 12, 14, 15, 13, 9, 11],
              'B': [1, 4, 6, 13, 3, 15, 8, 11, 2, 5, 12, 0, 7, 9, 14, 10]},
             {'A': [5, 1, 14, 12, 3, 7, 6, 2, 4, 0, 15, 11, 10, 16, 9, 13, 8],
              'B': [0, 1, 6, 11, 13, 7, 4, 10, 12, 5, 9, 14, 3, 8, 15, 16, 2]}]},
 {'catalogue_type': 6,
  'moves': [{'kind': 'half', 'vertices': [0, 1, 2, 3], 'remove': [[0, 1], [2, 3]], 'add': [[0, 3]]},
            {'kind': 'half', 'vertices': [4, 5, 6, 7], 'remove': [[4, 6], [5, 7]], 'add': [[5, 6]]}],
  'birth_ports': [1, 2, 4, 7],
  'catalogue_bijection': [15, 1, 3, 14, 4, 13, 16, 2, 11, 5, 10, 7, 8, 9, 6, 12, 0],
  'cycles': [{'A': [0, 1, 3, 2, 6, 4, 5, 7, 8, 9, 11, 10, 14, 12, 13, 15],
              'B': [0, 3, 5, 6, 8, 11, 13, 14, 2, 1, 4, 7, 9, 10, 15, 12]},
             {'A': [1, 3, 0, 2, 6, 4, 5, 7, 8, 10, 11, 15, 14, 12, 13, 9],
              'B': [0, 5, 6, 11, 12, 1, 7, 10, 13, 8, 14, 2, 3, 4, 15, 9]},
             {'A': [1, 3, 7, 6, 2, 0, 4, 5, 10, 8, 9, 11, 15, 13, 12, 14],
              'B': [0, 5, 9, 12, 7, 10, 15, 1, 2, 11, 6, 3, 4, 8, 13, 14]},
             {'A': [16, 1, 3, 7, 6, 2, 0, 8, 9, 11, 10, 5, 13, 15, 14, 12, 4],
              'B': [0, 1, 6, 10, 12, 7, 11, 13, 4, 2, 8, 14, 3, 5, 9, 15, 16]}]},
 {'catalogue_type': 7,
  'moves': [{'kind': 'switch', 'vertices': [0, 1, 2, 3], 'remove': [[0, 1], [2, 3]], 'add': [[0, 3], [1, 2]]},
            {'kind': 'half', 'vertices': [4, 6, 9, 11], 'remove': [[4, 6], [9, 11]], 'add': [[4, 9]]},
            {'kind': 'half', 'vertices': [5, 7, 8, 10], 'remove': [[5, 10], [7, 8]], 'add': [[7, 10]]}],
  'birth_ports': [5, 6, 8, 11],
  'catalogue_bijection': [12, 11, 7, 5, 14, 2, 3, 16, 4, 15, 13, 1, 8, 10, 9, 6, 0],
  'cycles': [{'A': [0, 1, 3, 2, 6, 4, 5, 7, 8, 9, 11, 10, 14, 12, 13, 15],
              'B': [0, 3, 5, 6, 8, 11, 13, 14, 2, 1, 4, 7, 9, 10, 15, 12]},
             {'A': [0, 2, 1, 3, 7, 5, 4, 6, 9, 11, 10, 14, 15, 13, 12, 8],
              'B': [0, 1, 6, 10, 12, 7, 11, 13, 4, 8, 14, 2, 3, 5, 15, 9]},
             {'A': [6, 2, 0, 3, 1, 9, 4, 11, 10, 5, 7, 8, 12, 13, 15, 14],
              'B': [0, 1, 7, 10, 12, 9, 11, 13, 6, 4, 14, 2, 3, 8, 15, 5]},
             {'A': [5, 1, 2, 6, 7, 3, 0, 4, 9, 8, 10, 11, 15, 14, 12, 13],
              'B': [0, 1, 7, 12, 9, 10, 13, 11, 6, 4, 14, 2, 3, 8, 15, 5]},
             {'A': [16, 5, 1, 2, 6, 7, 3, 0, 4, 9, 8, 10, 14, 12, 13, 15, 11],
              'B': [0, 1, 6, 10, 12, 5, 11, 9, 15, 2, 3, 8, 4, 7, 13, 14, 16]}]}]

def edge(u, v):
    return (min(u, v), max(u, v))


def bits(n, edges):
    adj = [0] * n
    for u, v in edges:
        assert 0 <= u < v < n
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    return tuple(adj)


def independent_set(adj, size):
    """Return one independent set of the requested size, or None."""
    def search(candidates, need):
        if need == 0:
            return ()
        while candidates.bit_count() >= need:
            bit = candidates & -candidates
            candidates ^= bit
            v = bit.bit_length() - 1
            tail = search(candidates & ~adj[v], need - 1)
            if tail is not None:
                return (v,) + tail
        return None
    return search((1 << len(adj)) - 1, size)


def verify_admissible(n, edges):
    adj = bits(n, edges)
    assert not any(adj[u] & adj[v] for u, v in edges), "A triangle"
    assert independent_set(adj, 6) is None, "B group of six"
    assert independent_set(adj, 5) is not None, "Expected B maximum five"


def clebsch():
    return frozenset((i, j) for i, j in combinations(range(16), 2)
                     if (i ^ j).bit_count() in (1, 4))


def square_move(edges, move):
    S = tuple(move["vertices"])
    assert len(S) == len(set(S)) == 4
    inside = {edge(i, j) for i, j in combinations(S, 2)
              if edge(i, j) in edges}
    degree = Counter(v for e in inside for v in e)
    assert len(inside) == 4 and all(degree[v] == 2 for v in S)
    diagonals = {edge(i, j) for i, j in combinations(S, 2)} - inside
    removed = {edge(*p) for p in move["remove"]}
    added = {edge(*p) for p in move["add"]}
    assert len(removed) == 2 and removed <= inside
    assert len(set().union(*(set(p) for p in removed))) == 4
    if move["kind"] == "switch":
        assert added == diagonals and len(added) == 2
    elif move["kind"] == "half":
        assert len(added) == 1 and added <= diagonals
    else:
        raise AssertionError("Unknown operation")
    assert not (added & edges)
    return edges.difference(removed).union(added)


def birth(edges, ports):
    assert len(ports) == len(set(ports)) == 4
    assert all(0 <= v < 16 for v in ports)
    assert not any(edge(i, j) in edges for i, j in combinations(ports, 2))
    portset = set(ports)
    # Exact general birth condition: every old B-five is hit by a new A-port.
    for S in combinations(range(16), 5):
        if not any(edge(i, j) in edges for i, j in combinations(S, 2)):
            assert portset.intersection(S), ("Unhit B-five", S)
    return edges.union((v, 16) for v in ports)


def verify_cycles(n, edges, cycles):
    for name, is_A in (("A", True), ("B", False)):
        path = cycles[name]
        assert len(path) == n and set(path) == set(range(n))
        assert all((edge(path[i], path[(i + 1) % n]) in edges) == is_A
                   for i in range(n)), (name, "invalid cycle")


def decode_graph6(text):
    n = ord(text[0]) - 63
    encoded = [(ord(c) - 63 >> k) & 1
               for c in text[1:] for k in range(5, -1, -1)]
    pairs = ((i, j) for j in range(1, n) for i in range(j))
    return n, frozenset(e for e, bit in zip(pairs, encoded) if bit)


def main():
    seen = set()
    checked_states = 0
    print("Type | switches | half-squares | births | final A-edges")
    for record in RECORDS:
        E = clebsch()
        verify_admissible(16, E)
        verify_cycles(16, E, record["cycles"][0])
        checked_states += 1
        for step, move in enumerate(record["moves"], 1):
            E = square_move(E, move)
            verify_admissible(16, E)
            verify_cycles(16, E, record["cycles"][step])
            checked_states += 1
        E = birth(E, record["birth_ports"])
        verify_admissible(17, E)
        verify_cycles(17, E, record["cycles"][-1])
        checked_states += 1
        assert len(record["cycles"]) == len(record["moves"]) + 2

        # Only here is the catalogue used, to identify the finished construction.
        label = record["catalogue_type"]
        n, target = decode_graph6(CATALOGUE[label - 1])
        mapping = record["catalogue_bijection"]
        assert n == 17 and sorted(mapping) == list(range(17))
        assert frozenset(edge(mapping[i], mapping[j]) for i, j in E) == target
        seen.add(label)
        s = sum(m["kind"] == "switch" for m in record["moves"])
        h = sum(m["kind"] == "half" for m in record["moves"])
        assert s <= 2 and h <= 4
        assert len(E) == 40 - h + 4
        print(f"{label:4} | {s:8} | {h:12} | {1:6} | {len(E):13}")
    assert seen == set(range(1, 8))
    assert checked_states == 42
    print("CERTIFIED: all 7 published types have explicit constructions.")
    print("All 42 recorded states avoid A triangles and B-six groups.")
    print("Both A and B have certified single Hamiltonian cycles at every state.")
    print("No new primitive: degree-preserving square switches, half-square")
    print("recompositions, and one four-port birth suffice.")

if __name__ == "__main__":
    main()

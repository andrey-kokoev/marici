"""Exact exhaustive test of cyclic A/B Ramsey constructions.

For each undirected cyclic distance set D on N vertices, color an edge A
exactly if its cyclic distance lies in D; all other edges are B.
Tests (N,m)=(21,7) and (26,8), proves the lists of ALL admissible
C_N-invariant distance sets, and tests whether a new vertex can be
attached while keeping every existing ring edge fixed.

Does not assume any cyclic symmetry for the new vertex.
"""
from itertools import combinations


def has_clique_of_size(adj, wanted):
    N = len(adj)
    def go(cand, remain):
        if remain == 0:
            return True
        while cand.bit_count() >= remain:
            bit = cand & -cand
            cand ^= bit
            i = bit.bit_length() - 1
            if go(cand & adj[i], remain-1):
                return True
        return False
    return go((1 << N) - 1, wanted)


def cyclic_adj(N, distances):
    A = [0] * N
    for i in range(N):
        for d in distances:
            A[i] |= (1 << ((i+d) % N)) | (1 << ((i-d) % N))
    return A


def has_triangle(A):
    return any((A[i] & A[j]) != 0
               for i in range(len(A))
               for j in range(i+1, len(A)) if A[i] & (1 << j))


def admissible(A, m):
    N = len(A)
    if has_triangle(A):
        return False
    B = [((1 << N) - 1) ^ (1 << i) ^ A[i] for i in range(N)]
    return not has_clique_of_size(B, m)


def all_cyclic_witnesses(N, m):
    distances = range(1, N//2 + 1)
    answer = []
    for mask in range(1 << len(distances)):
        D = tuple(d for i,d in enumerate(distances) if mask & (1 << i))
        A = cyclic_adj(N, D)
        if admissible(A, m):
            answer.append(D)
    return answer


if __name__ == '__main__':
    for N, m in [(21, 7), (26, 8)]:
        witnesses = all_cyclic_witnesses(N, m)
        assert len(witnesses) == {21:9, 26:6}[N]
        assert witnesses
        for D in witnesses:
            A = cyclic_adj(N, D)
            degrees = {x.bit_count() for x in A}
            assert degrees == {m-1}, (D, degrees)
            # No extension may use any A-edge to the center: each original
            # vertex already has m-1 A-neighbors, which form a B-clique.
            # The only other extension connects the center by B to all
            # ring vertices; this completes an existing B_(m-1).
            assert has_clique_of_size([((1 << N)-1) ^ (1 << i) ^ A[i]
                                       for i in range(N)], m-1)
            assert not admissible(A + [0], m)  # all-B to the new vertex
        print(f'(N={N},m={m}): {len(witnesses)} cyclic distance sets, '
              f'all A-degree {m-1}, none extendible without recoloring')
        print('  sets:', witnesses)
    print('Every claim verified exhaustively with integer bit operations.')

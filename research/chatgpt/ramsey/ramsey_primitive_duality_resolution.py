#!/usr/bin/env python3
"""Exact finite audit: symplectic color duality and Ramsey witness resolution.

Mathematical distinction:
  - J exchanges R/B as operators (and swaps Ramsey clique parameters).
  - The clause system is the Ramsey task, not derived from R/B multiplication.
  - Binary branching compares BOTH color choices; it is not a unique color rule.
"""
from collections import Counter
from itertools import combinations


def mul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def check_primitive():
    R = ((0, -1), (0, 0))
    B = ((0, 0), (1, 0))
    J = ((0, -1), (1, 0))
    Jinverse = ((0, 1), (-1, 0))
    assert mul(J, J) == ((-1, 0), (0, -1))
    assert mul(mul(J, R), Jinverse) == B
    assert mul(mul(J, B), Jinverse) == R


def ramsey_clauses(n, s, t):
    """Positive literal means RED. Negative literal means BLUE."""
    edges = list(combinations(range(n), 2))
    edge_id = {edge: i + 1 for i, edge in enumerate(edges)}
    clauses = [tuple(-edge_id[e] for e in combinations(U, 2))
               for U in combinations(range(n), s)]
    clauses += [tuple(edge_id[e] for e in combinations(U, 2))
                for U in combinations(range(n), t)]
    return edges, tuple(clauses)


def satisfies(clauses, assignment):
    return all(any(assignment[abs(lit)] == (lit > 0) for lit in clause)
               for clause in clauses)


def unit_propagate(clauses, assignment):
    """Monotone forced-literal closure. None means a contradiction was found."""
    assignment = dict(assignment)
    while True:
        forced = {}
        for clause in clauses:
            if any(assignment.get(abs(lit)) == (lit > 0)
                   for lit in clause):
                continue
            free = [lit for lit in clause if abs(lit) not in assignment]
            if not free:
                return None
            if len(free) == 1:
                lit = free[0]
                key, value = abs(lit), lit > 0
                if key in forced and forced[key] != value:
                    return None
                forced[key] = value
        next_values = {k: v for k, v in forced.items() if k not in assignment}
        if not next_values:
            return assignment
        assignment.update(next_values)


def exhaustive_count(clauses, n_edges):
    total = 0
    for bits in range(1 << n_edges):
        colors = {i + 1: bool(bits & (1 << i)) for i in range(n_edges)}
        if satisfies(clauses, colors):
            total += 1
    return total


def finite_branch_refutation(clauses, n_edges):
    """Exhaust both choices; never select a color as an asserted fact.

    When both child subproblems fail, their common parent fails.
    This is Shannon splitting / DPLL, and can be translated to resolution.
    """
    counts = Counter()

    def solve(partial):
        counts['visited'] += 1
        closed = unit_propagate(clauses, partial)
        if closed is None:
            counts['conflicts'] += 1
            return None
        if len(closed) == n_edges:
            counts['satisfying_leaves'] += 1
            return closed
        pivot = next(i for i in range(1, n_edges + 1) if i not in closed)
        counts['split_nodes'] += 1
        for color in (False, True):
            next_partial = dict(closed)
            next_partial[pivot] = color
            witness = solve(next_partial)
            if witness is not None:
                return witness
        return None

    solution = solve({})
    return solution, dict(counts)


def check_local_eight_vertex_conflict():
    # 0,...,6 are an almost-blue K7; 7 is a common red neighbor of 0 and 1.
    edge_set, cnf = ramsey_clauses(8, 3, 7)
    eid = {edge: i + 1 for i, edge in enumerate(edge_set)}
    partial = {eid[e]: False for e in combinations(range(7), 2) if e != (0, 1)}
    partial[eid[(0, 7)]] = True
    partial[eid[(1, 7)]] = True
    # A blue K7 forces 01 red; the red two-star forces 01 blue.
    assert eid[(0, 1)] not in partial
    assert unit_propagate(cnf, partial) is None
    for color in (False, True):
        completed = dict(partial)
        completed[eid[(0, 1)]] = color
        # Show an explicit contradictory clause in the supplied partial assignment.
        assert any(all(abs(lit) in completed and
                       completed[abs(lit)] != (lit > 0) for lit in clause)
                   for clause in cnf)
    return len(cnf)


def main():
    check_primitive()
    for n in (5, 6):
        edges, cnf = ramsey_clauses(n, 3, 3)
        count = exhaustive_count(cnf, len(edges))
        solution, counts = finite_branch_refutation(cnf, len(edges))
        assert (count > 0) == (solution is not None)
        assert count == (12 if n == 5 else 0)
        if n == 6:
            assert unit_propagate(cnf, {}) == {}
            assert counts == {'visited':39,'split_nodes':19,'conflicts':20}
        print(f'R(3,3), n={n}: {len(edges)} edges, {len(cnf)} clauses, '
              f'{count} avoiding colorings, DPLL={counts}')
    clause_count = check_local_eight_vertex_conflict()
    assert clause_count == 56 + 8
    print('Eight-vertex crossed witnesses: opposite forced colors of edge 01.')
    print('J R J^-1=B, J B J^-1=R, J^2=-I: verified exactly.')
    print('This verifies conditional logical witnessing; it does NOT prove R(3,7)=23.')

if __name__ == '__main__':
    main()

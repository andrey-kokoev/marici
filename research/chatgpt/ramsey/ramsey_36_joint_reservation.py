"""Construct 17 addresses with a reserved four-address block; no catalogue input.
Run: uv run --with python-sat python research/chatgpt/ramsey/ramsey_36_joint_reservation.py
Positive SAT literals denote positive edges. Base 1..10; reserve 11..14.
"""
from itertools import combinations
from pysat.solvers import Solver


def main():
    vertices = range(1, 18)
    edges = list(combinations(vertices, 2))
    var = {e: i for i, e in enumerate(edges, 1)}
    def lits(vs):
        return [var[e] for e in combinations(sorted(vs), 2)]
    clauses = [[-v for v in lits(t)] for t in combinations(vertices, 3)]
    clauses += [lits(t) for t in combinations(vertices, 6)]
    future = range(11, 15)
    reservation = [-v for v in lits(future)] + [-var[i,j] for i in (9,10) for j in future]
    with Solver(name='cadical195', bootstrap_with=clauses) as solver:
        # Negative reservation -> positive base sign, before any base sign is chosen.
        assert not solver.solve(assumptions=reservation + [-var[9,10]])
        # Return influence: try one further future reading; a base triangle rules out its mate.
        trial = var[9,15]
        assert not solver.solve(assumptions=reservation + [trial,var[10,15]])
        assert solver.solve(assumptions=reservation + [trial])
        model = set(solver.get_model())
    positive = {e for e in edges if var[e] in model}
    assert (9,10) in positive and (10,15) not in positive
    assert all(-v not in model for v in reservation)
    assert all(not set(combinations(t,2)) <= positive for t in combinations(vertices,3))
    assert all(set(combinations(t,2)) & positive for t in combinations(vertices,6))
    print('positive neighbors at smaller addresses; all other signs negative:')
    for j in vertices:print(j,[i for i in range(1,j) if (i,j) in positive])

if __name__=='__main__':main()

"""Exact finite tests of a proposed linear cell-interface assembly contract.

The full-spinor ports and their transports are supplied choices, not derived
from pentachoron geometry. The old tetrahedral Pauli projectors are retained.
Run from the repository root; no third-party dependencies.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json
import random
from check_electron_tetrahedral_spinor import D, cast, ident, adj, sm, ma, trace
from check_electron_charge_spin_frontier import ga, gs, gm, gc, gt, gmm, G0, G1

BASE = Path(__file__).resolve().parents[1]
I = ident(2)
EDGES = list(combinations(range(5), 2))


def divide(a, b):
    den = gm(gc(b), b)
    assert den[1] == 0 and den[0] != 0
    num = gm(a, gc(b))
    return (cast(num[0]) / cast(den[0]), cast(num[1]) / cast(den[0]))


def rref(matrix, columns):
    a = [list(row) for row in matrix]
    pivots = []
    for c in range(columns):
        p = next((i for i in range(len(pivots), len(a)) if a[i][c] != G0), None)
        if p is None:
            continue
        r = len(pivots)
        a[r], a[p] = a[p], a[r]
        scale = a[r][c]
        a[r] = [divide(x, scale) for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c] != G0:
                scale = a[i][c]
                a[i] = [ga(x, gs(-1, gm(scale, y))) for x, y in zip(a[i], a[r])]
        pivots.append(c)
    return tuple(tuple(row) for row in a[:len(pivots)]), pivots


def nullspace(matrix, columns=10):
    reduced, pivots = rref(matrix, columns)
    free = [i for i in range(columns) if i not in pivots]
    basis = []
    for j in free:
        v = [G0] * columns
        v[j] = G1
        for row, p in zip(reduced, pivots):
            v[p] = gs(-1, row[j])
        basis.append(v)
    return tuple(tuple(v[i] for v in basis) for i in range(columns))


def inverse(matrix):
    n = len(matrix)
    a, pivots = rref([list(row) + list(unit) for row, unit in zip(matrix, ident(n))], 2*n)
    assert pivots == list(range(n))
    return tuple(row[n:] for row in a)


def projector(matrix, columns=10):
    k = nullspace(matrix, columns)
    if not k[0]:
        return tuple(tuple(G0 for _ in range(columns)) for _ in range(columns))
    return gmm(gmm(k, inverse(gmm(adj(k), k))), adj(k))


def matching(edges=EDGES, transports=None):
    """Constraints z_b = U_ab z_a, two complex rows per interface."""
    transports = transports or {}
    rows = []
    for a, b in edges:
        u = transports.get((a, b), I)
        for i in range(2):
            row = [G0]*10
            for j in range(2):
                row[2*a+j] = gs(-1, u[i][j])
            row[2*b+i] = G1
            rows.append(row)
    return rows


def main():
    tests = []
    normals = [tuple(D(0, F(s, 3)) for s in n)
               for n in [(1,1,-1), (1,-1,1), (-1,1,1), (-1,-1,-1)]]
    p = []
    for x, y, z in normals:
        h = (((z, D()), (x, -y)), ((x, y), (-z, D())))
        q = sm(F(1,2), ma(I, sm(-1, h)))
        assert gmm(q, q) == q and trace(q) == G1
        p.append(q)
    total = tuple(tuple(gt(q[i][j] for q in p) for j in range(2)) for i in range(2))
    assert total == sm(2, I)
    for a, b in combinations(p, 2):
        assert trace(gmm(a, b)) == (F(1,3), F(0))
        assert len(rref(list(a)+list(b), 2)[1]) == 2
    tests.append('Each inherited face port has rank one; any two distinct ports jointly recover rank two.')
    local = tuple(tuple(gs(F(1,2), gmm(p[i//2], p[j//2])[i%2][j%2])
                        for j in range(8)) for i in range(8))
    assert gmm(local, local) == local and trace(local) == (F(2), F(0))
    tests.append('Retained ABCD projector is exactly the original rank-two four-face return.')

    flat = matching()
    assert len(rref(flat, 10)[1]) == 8
    n = projector(flat)
    expected = tuple(tuple((F(1,5), F(0)) if i%2 == j%2 else G0
                           for j in range(10)) for i in range(10))
    assert n == expected and adj(n) == n and gmm(n,n) == n
    assert trace(n) == (F(2), F(0))
    assert all(x == G0 for row in gmm(flat, n) for x in row)
    tests.append('Supplied flat full-spinor gluing on K5 has dimension two and orthogonal return blocks I/5.')

    # Every labelled tree gives the same compatible subspace when all transports
    # are identity. Enumerate the 125 trees directly among four-edge subsets.
    trees = 0
    for edges in combinations(EDGES, 4):
        rows = matching(edges)
        if len(rref(rows, 10)[1]) == 8:
            trees += 1
            assert rref(rows, 10)[0] == rref(flat, 10)[0]
    assert trees == 125
    rng = random.Random(0)
    for _ in range(20):
        rows = list(flat)
        rng.shuffle(rows)
        assert rref(rows, 10)[0] == rref(flat, 10)[0]
    assert rref(matching([(b,a) for a,b in EDGES]), 10)[0] == rref(flat,10)[0]
    tests.append('All 125 spanning-tree assemblies, reversed interfaces and 20 row orders give the same flat kernel.')

    minus = sm(-1,I)
    reflection = ((G1,G0),(G0,gs(-1,G1)))
    assert len(rref(matching(transports={(3,4): minus}),10)[1]) == 10
    assert len(rref(matching(transports={(3,4): reflection}),10)[1]) == 9
    assert len(rref(matching(transports={edge: minus for edge in EDGES}),10)[1]) == 10
    tests.append('Unitary seam controls retain respectively zero, one, and zero components: pairwise invertibility is insufficient.')
    # The scalar -I defect still commutes with every common spin rotation.
    u = ((G0,gs(-1,G1)),(G1,G0))
    assert gmm(u,minus) == gmm(minus,u)
    rotation = tuple(tuple(u[i%2][j%2] if i//2==j//2 else G0 for j in range(10)) for i in range(10))
    assert gmm(rotation,n) == gmm(n,rotation)
    tests.append('Flat return is rotation compatible; central -I seam obstruction cannot be rejected by rotation covariance alone.')

    # Relabelling local frames must not alter assembly: U_ab = G_b G_a*.
    frames = [I, minus, u, sm(-1,u), I]
    transports = {(a,b):gmm(frames[b],adj(frames[a])) for a,b in EDGES}
    gauge = matching(transports=transports)
    assert len(rref(gauge,10)[1]) == 8
    for a,b,c in combinations(range(5),3):
        assert gmm(transports[b,c],transports[a,b]) == transports[a,c]
    ng = projector(gauge)
    block = tuple(tuple(frames[i//2][i%2][j%2] if i//2==j//2 else G0 for j in range(10)) for i in range(10))
    assert ng == gmm(gmm(block,n),adj(block))
    tests.append('Pure frame changes preserve the return and satisfy all ten triple-overlap cocycles.')

    # Deliberately naive convention, NOT a geometric spin-frame derivation:
    # order the four neighbours of each cell, assign the four old projectors,
    # then equate their ambient C2 face vectors without a line adapter.
    neighbors = [[b for b in range(5) if b != a] for a in range(5)]
    naive = []
    for a,b in EDGES:
        left, right = p[neighbors[a].index(b)], p[neighbors[b].index(a)]
        for i in range(2):
            row = [G0]*10
            for j in range(2):
                row[2*a+j] = left[i][j]
                row[2*b+j] = gs(-1,right[i][j])
            naive.append(row)
    assert len(rref(naive,10)[1]) == 10
    tests.append('Naive sorted-label matching of inherited rank-one face vectors kills every global state.')

    # Full physical carrier: five copies of the old eight-coordinate cell.
    # K_c = J/sqrt(5), hence (KK*)_cd = N_local/5; no sqrt arithmetic needed.
    physical = tuple(tuple(gs(F(1,5),local[i%8][j%8]) for j in range(40)) for i in range(40))
    assert trace(physical) == (F(2),F(0))
    # Block multiplication gives 5 * N_local^2 / 25 = N_local / 5.
    assert sm(F(1,5),gmm(local,local)) == sm(F(1,5),local)
    assert sm(5,tuple(tuple(physical[i][j] for j in range(8)) for i in range(8))) == local
    tests.append('Forty-coordinate conditional extension has rank two; ABCD compression is N_local/5, not N_local.')
    result = dict(verification_passed=True, tests=tests, test_count=len(tests),
                  logical_cell_dimensions=[2]*5, inherited_face_port_rank=1,
                  supplied_full_port_rank=2, flat_global_dimension=2,
                  single_central_sign_defect_dimension=0, single_reflection_defect_dimension=1,
                  naive_rank_one_matching_dimension=0, spanning_trees_checked=trees,
                  physical_raw_dimension=40, abcd_compression_factor='1/5',
                  interface_geometry_derived=False, charge_or_mass_derived=False)
    out = BASE/'results/cell_interface_assembly.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()

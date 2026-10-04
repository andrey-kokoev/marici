"""Exact finite augmentation/witness/dephasing theorem, not a source/physics bridge.

Standard library only. Scalars are pairs (a,b) representing a+i*sqrt(3)*b.
All operators are computed in the four-state delta basis before Fourier checks.
"""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import hashlib
import json


def z(a=0, b=0): return (F(a), F(b))
def za(x, y): return (x[0]+y[0], x[1]+y[1])
def zm(x, y): return (x[0]*y[0]-3*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def zs(x, a): return (x[0]*a, x[1]*a)
def conj(x): return (x[0], -x[1])
def total(xs):
    out = z()
    for x in xs: out = za(out, x)
    return out


def adj(a): return tuple(tuple(conj(x) for x in col) for col in zip(*a))
def mm(a, b):
    return tuple(tuple(total(zm(x, y) for x, y in zip(row, col))
                       for col in zip(*b)) for row in a)
def add(a, b): return tuple(tuple(za(x, y) for x, y in zip(r, s)) for r, s in zip(a, b))
def scale(a, c): return tuple(tuple(zs(x, c) for x in row) for row in a)
def sub(a, b): return add(a, scale(b, -1))
def eye(n): return tuple(tuple(z(i == j) for j in range(n)) for i in range(n))
def tr(a): return total(a[i][i] for i in range(len(a)))
def hs(a, b): return total(zm(conj(x), y) for r, s in zip(a, b) for x, y in zip(r, s))
def outer(v): return tuple(tuple(zm(x, conj(y)) for y in v) for x in v)
def mv(a, v): return tuple(total(zm(x, y) for x, y in zip(row, v)) for row in a)
def norm2(v):
    value = total(zm(x, conj(x)) for x in v)
    assert value[1] == 0
    return value[0]
def projector(v): return scale(outer(v), 1/norm2(v))
def permutation(p): return tuple(tuple(z(i == p[j]) for j in range(4)) for i in range(4))
def compose(p, q): return tuple(p[q[i]] for i in range(4))
def chi(k, x): return (-1)**((k & x).bit_count() % 2)


I4 = eye(4)
H = sub(I4, tuple(tuple(z(F(1, 4)) for _ in range(4)) for _ in range(4)))
U = tuple(tuple(z(2*(F(i == x)-F(1, 4))) for i in range(4)) for x in range(4))
translations = tuple(permutation(tuple(v ^ x for x in range(4))) for v in range(4))
omega = z(F(-1, 2), F(1, 2))
mode = (z(1), omega, zm(omega, omega))


def expectation(a):
    out = scale(a, 0)
    for t in translations: out = add(out, mm(mm(t, a), adj(t)))
    return scale(out, F(1, 4))


def witness(x, y, third, conjugated=False):
    b = tuple(zs(total((U[x][i], U[y][i], U[third][i])), F(1, 3)) for i in range(4))
    coefficients = tuple(map(conj, mode)) if conjugated else mode
    return tuple(total(zm(c, v[i]) for c, v in zip(coefficients, (b, U[x], U[y])))
                 for i in range(4))


def main():
    assert total(mode) == z() and zm(mode[1], mode[2]) == z(1)
    assert mm(H, H) == H and adj(H) == H and tr(H) == z(3)
    for x in range(4):
        assert mv(H, U[x]) == U[x]
        for y in range(4):
            assert total(zm(a, conj(b)) for a, b in zip(U[x], U[y])) == z(4*(x == y)-1)
    # Fourier map W -> C^3, derived from characters rather than supplied geometry.
    T = tuple(tuple(z(F(chi(k, x), 2)) for x in range(4)) for k in (1, 2, 3))
    assert mm(T, adj(T)) == eye(3) and mm(adj(T), T) == H
    vertices = tuple(mv(T, u) for u in U)
    assert all(vertices[x] == tuple(z(chi(k, x)) for k in (1, 2, 3)) for x in range(4))
    for v, t in enumerate(translations):
        assert mm(t, H) == mm(H, t)
        diagonal = mm(mm(T, t), adj(T))
        assert diagonal == tuple(tuple(z(chi(k, v) if i == j else 0)
                                      for j in range(3)) for i, k in enumerate((1, 2, 3)))
    r = (0, 2, 3, 1)
    ident = tuple(range(4))
    powers = (ident, r, compose(r, r))
    assert compose(r, powers[2]) == ident
    group = tuple(tuple(b ^ q[x] for x in range(4)) for b in range(4) for q in powers)
    assert len(set(group)) == 12
    assert all(compose(p, q) in group for p in group for q in group)
    assert all(sum(p[i] > p[j] for i in range(4) for j in range(i+1, 4)) % 2 == 0 for p in group)
    triples = tuple(permutations(range(4), 3))
    oriented = {tuple(p[x] for x in (0, 1, 2)) for p in group}
    reversed_boundary = {(y, x, third) for x, y, third in oriented}
    assert len(oriented) == len({(x, y) for x, y, _ in oriented}) == 12
    assert not oriented & reversed_boundary and oriented | reversed_boundary == set(triples)

    # A spanning set of End(W_C); complex linearity extends these exact tests.
    basis = []
    for i in range(3):
        for j in range(3):
            unit = tuple(tuple(z(a == i and b == j) for b in range(3)) for a in range(3))
            basis.append(mm(mm(adj(T), unit), T))
    images = [expectation(a) for a in basis]
    for a, e in zip(basis, images):
        assert expectation(e) == e and tr(e) == tr(a)
        for b in basis: assert hs(e, b) == hs(a, expectation(b))
        for t in translations: assert mm(t, e) == mm(e, t)
    assert expectation(H) == H
    assert sum(e != scale(H, 0) for e in images) == 3

    states = {}
    covariance_checks = 0
    for x, y, third in triples:
        psi = witness(x, y, third)
        assert total(psi) == z() and norm2(psi) == F(20, 3)
        P = projector(psi)
        states[(x, y, third)] = P
        assert adj(P) == P and mm(P, P) == P and tr(P) == z(1)
        assert mm(H, P) == P
        d = x ^ y
        rho_d = mm(translations[d], H)  # Embedded W operator, zero on constants.
        assert mm(rho_d, rho_d) == H and tr(rho_d) == z(-1)
        expected = sub(scale(H, F(4, 15)), scale(rho_d, F(1, 5)))
        E = expectation(P)
        assert E == expected
        p = tuple(zm(a, conj(a))[0]/norm2(psi) for a in mv(T, psi))
        assert sorted(p) == [F(1, 15), F(7, 15), F(7, 15)]
        assert all(p[i] == (F(1, 15) if chi(k, d) == 1 else F(7, 15))
                   for i, k in enumerate((1, 2, 3)))
        residual = sub(P, E)
        assert hs(E, E) == z(F(11, 25)) and hs(residual, residual) == z(F(14, 25))
        assert hs(E, residual) == z() and hs(P, E) == z(F(11, 25))
        assert expectation(projector(witness(x, y, third, True))) == E
        # Finite rank/normalization does not enforce the witness prescription.
        difference = tuple(za(b, zs(a, -1)) for a, b in zip(U[x], U[y]))
        rival = projector(difference)
        rival_E = expectation(rival)
        assert hs(rival_E, rival_E) == z(F(1, 2)) != hs(E, E)
        weights = tuple(zm(a, conj(a))[0]/norm2(difference) for a in mv(T, difference))
        assert sorted(weights) == [F(0), F(1, 2), F(1, 2)]
        for pmap in group:
            M = permutation(pmap)
            target = tuple(pmap[a] for a in (x, y, third))
            assert mv(M, psi) == witness(*target)
            assert mm(mm(M, P), adj(M)) == projector(witness(*target))
            assert expectation(mm(mm(M, P), adj(M))) == mm(mm(M, E), adj(M))
            transported_difference = tuple(za(b, zs(a, -1))
                                           for a, b in zip(U[pmap[x]], U[pmap[y]]))
            assert mm(mm(M, rival), adj(M)) == projector(transported_difference)
            covariance_checks += 1
    # Face choice is forgotten by the dephasing map, not by the pure state.
    assert states[(0, 1, 2)] != states[(0, 1, 3)]
    assert expectation(states[(0, 1, 2)]) == expectation(states[(0, 1, 3)])

    report = {
        'schema': 'marici.nima.augmentation-fourier-dephasing.v1',
        'status': 'passed',
        'classification': 'exact_finite_theorem_given_centroid_cyclic_witness',
        'source': 'four delta states of F2^2; counting metric; nontrivial C3 action',
        'augmentation_dimension': 3,
        'gram_diagonal_off_diagonal': [3, -1],
        'group_order': len(group),
        'ordered_distinct_triples_checked': len(triples),
        'edges_per_boundary_orientation': len(oriented),
        'equivariance_checks': covariance_checks,
        'reynolds_spanning_basis_checks': len(basis),
        'operator_space_dimensions': {'total': 9, 'retained': 3, 'transverse': 6},
        'state_norm_squared': '20/3',
        'dephased_identity': 'E_V(P_e)=(4/15)I_W-(1/5)rho(y-x)',
        'dephased_spectrum': ['1/15', '7/15', '7/15'],
        'retained_squared_hilbert_schmidt_norm': '11/25',
        'transverse_squared_hilbert_schmidt_norm': '14/25',
        'hostiles': {
            'equivariant_edge_difference_retained_squared_norm': '1/2',
            'minimal_faithful_carrier_alone_selects_state': False,
            'different_incident_faces_can_have_equal_dephasing_and_unequal_states': True},
        'uses_rank25_carrier_or_K_over_25_state': False,
        'residuals': ['explicit stable-source K0 and rotation comparison',
                      'source derivation of centroid-cyclic witness prescription',
                      'physical preparation/channel/effect identification'],
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    dest = Path(__file__).resolve().parents[1]/'results'/'augmentation-fourier-dephasing.json'
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print('PASS: augmentation geometry, 24 witnesses, 288 covariance checks, exact Reynolds identity.')
    print('PASS: squared norms 11/25 and 14/25; equivariant rival yields 1/2.')
    print('OPEN: stable-source comparison, witness prescription derivation, physical readout.')


if __name__ == '__main__':
    main()

"""Exact 2T -> A4 Pauli bridge and its state/operator boundary.

Dependency-free. Q(sqrt(3), i) arithmetic; imports the existing labelled
geometry, not a previous results file. Run from any working directory.
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json

from check_twelve_triangle_positive_geometry import (
    I, C, POINTS, ONE, ZERO, OMEGA, compose, rotation, mean, inv,
    mm, mv, transpose, projector, zmv, zadd, zmul, zconj, zscale, znorm,
)

ROOT = Path(__file__).resolve().parents[1]
SEEDS = ((1, 2, 0, 3), (3, 0, 2, 1))

# a + b*sqrt(3) + i*c + i*sqrt(3)*d. No floats or symbolic dependencies.
def k(a=0, b=0, c=0, d=0):
    return tuple(map(F, (a, b, c, d)))


K0, K1, KI = k(), k(1), k(c=1)


def ka(x, y):
    return tuple(a + b for a, b in zip(x, y))


def ks(x, c):
    return tuple(c * a for a in x)


def km(x, y):
    out = [F(0)] * 4
    for a, b in product(range(4), repeat=2):
        # bit 0 is sqrt(3); bit 1 is i.
        factor = (3 if a & b & 1 else 1) * (-1 if a & b & 2 else 1)
        out[a ^ b] += factor * x[a] * y[b]
    return tuple(out)


def kc(x):
    return (x[0], x[1], -x[2], -x[3])


def total(xs):
    out = K0
    for x in xs:
        out = ka(out, x)
    return out


def matmul(a, b):
    return tuple(tuple(total(km(x, y) for x, y in zip(row, col))
                       for col in zip(*b)) for row in a)


def adj(a):
    return tuple(tuple(kc(x) for x in row) for row in zip(*a))


def mscale(a, c):
    return tuple(tuple(km(x, c) for x in row) for row in a)


def madd(a, b):
    return tuple(tuple(ka(x, y) for x, y in zip(row, col))
                 for row, col in zip(a, b))


def tr(a):
    return total(a[i][i] for i in range(len(a)))


def determinant2(a):
    return ka(km(a[0][0], a[1][1]), ks(km(a[0][1], a[1][0]), -1))


E2 = ((K1, K0), (K0, K1))
Z2 = ((K0, K0), (K0, K0))
PAULI = (
    ((K0, K1), (K1, K0)),
    ((K0, ks(KI, -1)), (KI, K0)),
    ((K1, K0), (K0, ks(K1, -1))),
)


def phi(v):
    out = Z2
    for z, sigma in zip(v, PAULI):
        out = madd(out, mscale(sigma, z))
    return out


def unphi(a):
    assert tr(a) == K0
    return tuple(ks(tr(matmul(s, a)), F(1, 2)) for s in PAULI)


def old_z(z):
    return k(a=z[0], d=z[1])


def hs(a, b):
    return ks(tr(matmul(adj(a), b)), F(1, 2))


def qmul(p, q):
    w, x, y, z = p
    a, b, c, d = q
    return (w*a-x*b-y*c-z*d, w*b+x*a+y*d-z*c,
            w*c-x*d+y*a+z*b, w*d+x*c-y*b+z*a)


def qneg(q):
    return tuple(-a for a in q)


def qinv(q):
    return (q[0], -q[1], -q[2], -q[3])


Q1 = (F(1), F(0), F(0), F(0))


def qpower(q, n):
    out = Q1
    for _ in range(n):
        out = qmul(out, q)
    return out


def spin(q):
    # U(q)=w*I-i*(x*sigma_x+y*sigma_y+z*sigma_z).
    return madd(mscale(E2, k(q[0])), mscale(phi(tuple(k(a) for a in q[1:])), ks(KI, -1)))


def closure(generators, identity, multiply):
    found, front = {identity}, [identity]
    while front:
        current = front.pop()
        for gen in generators:
            nxt = multiply(gen, current)
            if nxt not in found:
                found.add(nxt)
                front.append(nxt)
    return sorted(found)


def sparse_mul(a, b):
    rows = defaultdict(list)
    for (i, j), z in b.items():
        rows[i].append((j, z))
    out = {}
    for (i, j), z in a.items():
        for t, w in rows[j]:
            out[i, t] = zadd(out.get((i, t), ZERO), zmul(z, w))
    return {ij: z for ij, z in out.items() if z != ZERO}


def sparse_adj(a):
    return {(j, i): zconj(z) for (i, j), z in a.items()}


def main():
    group = closure(SEEDS, tuple(range(4)), compose)
    rotations = [rotation(p) for p in group]
    assert len(group) == len(set(rotations)) == 12
    binary = {tuple(F(s if j == i else 0) for j in range(4))
              for i in range(4) for s in (-1, 1)}
    binary.update(tuple(F(s, 2) for s in signs) for signs in product((-1, 1), repeat=4))
    binary = sorted(binary)
    assert len(binary) == 24
    us = {q: spin(q) for q in binary}
    rs = {}
    for q in binary:
        assert sum(a*a for a in q) == 1
        u = us[q]
        assert matmul(adj(u), u) == E2 and determinant2(u) == K1
        columns = [unphi(matmul(matmul(u, s), adj(u))) for s in PAULI]
        assert all(z[1:] == (0, 0, 0) for col in columns for z in col)
        rs[q] = tuple(tuple(columns[j][i][0] for j in range(3)) for i in range(3))
        assert rs[q] in rotations
        assert matmul(matmul(u, E2), adj(u)) == E2
        assert ka(K1, k(sum(rs[q][i][i] for i in range(3)))) == km(tr(u), kc(tr(u)))
    # Exhaustive finite-group laws and labelled forward realization.
    for p, q in product(binary, repeat=2):
        pq = qmul(p, q)
        assert pq in us
        assert us[pq] == matmul(us[p], us[q])
        assert rs[pq] == mm(rs[p], rs[q])
    assert Counter(rs.values()) == Counter({r: 2 for r in rotations})
    assert {q for q in binary if rs[q] == I} == {Q1, qneg(Q1)}
    seed_lifts = [next(q for q in binary if rs[q] == rotation(p) and q[0] > 0) for p in SEEDS]
    assert closure(seed_lifts, Q1, qmul) == binary
    assert all(qpower(q, 3) == qneg(Q1) and qpower(q, 6) == Q1 for q in seed_lifts)
    v4 = {r for r in rotations if mm(r, r) == I}
    q8 = {q for q in binary if rs[q] in v4}
    assert len(v4) == 4 and len(q8) == 8
    axes = [tuple(F(j == i) for j in range(4)) for i in (1, 2, 3)]
    for a, b in product(axes, repeat=2):
        assert qmul(a, a) == qneg(Q1)
        if a != b:
            assert qmul(a, b) == qneg(qmul(b, a))
            assert qmul(qmul(qmul(a, b), qinv(a)), qinv(b)) == qneg(Q1)
    # Every lift of an order-two rotation has order four: no group section.
    assert all(qpower(q, 2) == qneg(Q1) for q in q8 if rs[q] != I)
    # A chosen sign section is projective, with an explicit nontrivial cocycle.
    section = {r: max(q for q in binary if rs[q] == r) for r in rotations}
    signs = {}
    for r, s in product(rotations, repeat=2):
        lift = qmul(section[r], section[s])
        target = section[mm(r, s)]
        assert lift in (target, qneg(target))
        signs[r, s] = 1 if lift == target else -1
    assert -1 in signs.values()
    for r, s, t in product(rotations, repeat=3):
        assert signs[r, s] * signs[mm(r, s), t] == signs[s, t] * signs[r, mm(s, t)]
    # Character norms independently check the irreducible doublet and vector.
    assert total(km(tr(u), kc(tr(u))) for u in us.values()) == k(24)
    assert sum(sum(r[i][i] for i in range(3))**2 for r in rs.values()) == 24
    assert us[qneg(Q1)] == mscale(E2, k(-1))
    assert rs[qneg(Q1)] == I
    # Wrong handedness is detected against labelled generators, not fitted away.
    wrong_hand = sum(matmul(matmul(adj(us[q]), s), us[q]) !=
                     phi(tuple(k(rs[q][i][j]) for i in range(3)))
                     for q in binary for j, s in enumerate(PAULI))
    assert wrong_hand > 0
    for i, j in product(range(3), repeat=2):
        assert hs(PAULI[i], PAULI[j]) == k(i == j)

    # Reconstruct precisely the original triangle mode and its projectors.
    centre = mean([POINTS[a] for a in 'ABC'])
    x0 = transpose((centre, POINTS['A'], POINTS['B']))
    v0 = zmv(x0, (ONE, OMEGA, zmul(OMEGA, OMEGA)))
    norm0 = sum(znorm(z) for z in v0)
    assert norm0 == F(20, 3)
    a0 = mm(mm(x0, C), inv(x0))
    orthogonal_defect = tuple(tuple(mm(transpose(a0), a0)[i][j] - I[i][j]
                                    for j in range(3)) for i in range(3))
    assert any(a for row in orthogonal_defect for a in row)
    vectors = [zmv(r, v0) for r in rotations]
    operators = [phi(tuple(map(old_z, v))) for v in vectors]
    reference_op = phi(tuple(map(old_z, v0)))
    assert hs(reference_op, reference_op) == k(norm0)
    # The old complex vector is not a Hermitian density matrix, nor a
    # rank-one traceless spinor bilinear: det(Phi(v0)) is nonzero.
    assert adj(reference_op) != reference_op
    assert determinant2(reference_op) == k(F(16, 3))
    assert matmul(reference_op, reference_op) == mscale(E2, k(F(-16, 3)))
    for q in binary:
        target = operators[rotations.index(rs[q])]
        assert matmul(matmul(us[q], reference_op), adj(us[q])) == target
    local, symmetry = {}, {}
    for x, r in enumerate(rotations):
        px = projector(vectors[x])
        for i, j in product(range(3), repeat=2):
            if px[i][j] != ZERO:
                local[3*x+i, 3*x+j] = px[i][j]
        # Test J P_x = P^HS_{Phi(v_x)} J on a complete basis, including i.
        for j in range(3):
            lhs = phi(tuple(old_z(px[i][j]) for i in range(3)))
            rhs = mscale(operators[x], ks(hs(operators[x], PAULI[j]), 1/norm0))
            assert lhs == rhs
            assert mscale(lhs, KI) == mscale(rhs, KI)
        for y, s in enumerate(rotations):
            block = mm(r, transpose(s))
            # Each transport block is exactly conjugation by a relative lift.
            relative = qmul(section[r], qinv(section[s]))
            assert rs[relative] == block
            for i, j in product(range(3), repeat=2):
                if block[i][j]:
                    symmetry[3*x+i, 3*y+j] = (block[i][j]/12, F(0))
    assembled = tuple(z for v in vectors for z in v)
    norm = sum(znorm(z) for z in assembled)
    assert norm == 80
    collective = {(i, j): zscale(zmul(a, zconj(b)), 1/norm)
                  for i, a in enumerate(assembled) for j, b in enumerate(assembled)}
    collective = {ij: z for ij, z in collective.items() if z != ZERO}
    for op in (local, symmetry, collective):
        assert sparse_adj(op) == op and sparse_mul(op, op) == op
    assert sparse_mul(local, symmetry) == sparse_mul(symmetry, local) == collective
    ranks = [sum(op.get((i, i), ZERO)[0] for i in range(36))
             for op in (local, symmetry, collective)]
    assert ranks == [12, 3, 1]
    assert [len(op) for op in (local, symmetry, collective)] == [108, 432, 1296]
    # D(g)v_x = g v_{g^-1 x}. Test invariance of the line (and hence N).
    for g in rotations:
        for x, r in enumerate(rotations):
            source = rotations.index(mm(transpose(g), r))
            assert zmv(g, vectors[source]) == vectors[x]
    # Explicitly transport the dense collective projector in the HS pairing.
    for x, y, j in product(range(12), range(12), range(3)):
        lhs = phi(tuple(old_z(collective.get((3*x+i, 3*y+j), ZERO)) for i in range(3)))
        rhs = mscale(operators[x], ks(hs(operators[y], PAULI[j]), 1/norm))
        assert lhs == rhs
    # Charge no-go counterexample: N commutes with D, Nu=u, spectrum {0,1}.
    applied = [ZERO] * 36
    for (i, j), z in collective.items():
        applied[i] = zadd(applied[i], zmul(z, assembled[j]))
    assert tuple(applied) == assembled

    # An actual spinor extension W=C[A4] tensor S has dimension 24, not 72.
    # T(q)_{x,y}=delta_{x,r(q)y} U(q). Verify its full group average is zero.
    average_blocks = {}
    for q in binary:
        for y, r in enumerate(rotations):
            x = rotations.index(mm(rs[q], r))
            average_blocks[x, y] = madd(average_blocks.get((x, y), Z2), us[q])
    assert all(block == Z2 for block in average_blocks.values())
    assert all(madd(us[q], us[qneg(q)]) == Z2 for q in binary)

    # A DIFFERENT, explicitly added tensor factor does preserve the mode:
    # V36 tensor S has projectors L tensor I2, R tensor I2, N tensor I2.
    # Its collective sector is a doublet, not an invariant vector.
    extended = [{(2*i+a, 2*j+a): z for (i, j), z in op.items() for a in range(2)}
                for op in (local, symmetry, collective)]
    el, er, en = extended
    for op in extended:
        assert sparse_adj(op) == op and sparse_mul(op, op) == op
    assert sparse_mul(el, er) == sparse_mul(er, el) == en
    extended_ranks = [sum(op.get((i, i), ZERO)[0] for i in range(72)) for op in extended]
    assert extended_ranks == [24, 6, 2]
    embedding = [tuple(old_z(z) if b == a else K0 for z in assembled for b in range(2))
                 for a in range(2)]
    for q in binary:
        for a in range(2):
            transformed = []
            for x, r in enumerate(rotations):
                source = rotations.index(mm(transpose(rs[q]), r))
                # D_vector(q) tensor U(q) on u tensor e_a.
                rotated = zmv(rs[q], vectors[source])
                transformed.extend(km(old_z(z), us[q][b][a]) for z in rotated for b in range(2))
            expected = tuple(total(km(embedding[b][i], us[q][b][a]) for b in range(2))
                             for i in range(72))
            assert tuple(transformed) == expected
    # At the central element both basis states change sign; their sector remains.
    assert all(any(z != K0 for z in basis) for basis in embedding)

    source_paths = [Path(__file__), Path(__file__).with_name('check_twelve_triangle_positive_geometry.py'),
                    Path(__file__).with_name('check_triangle_half_phase.py')]
    report = {
        'status': 'passed',
        'classification': 'exact_finite_group_operator_intertwiner_not_physical_spin_assignment',
        'coherence_obligation': 'forward realization and route compatibility on the operator sector',
        'arithmetic': 'Q(sqrt(3), i), four rational coefficients; no floats',
        'source_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in source_paths},
        'group': {'A4_order': len(group), 'binary_tetrahedral_order': len(binary),
                  'V4_order': len(v4), 'Q8_order': len(q8), 'kernel_order': 2,
                  'checked_products': 24**2, 'checked_cocycle_triples': 12**3,
                  'seed_permutations': SEEDS, 'positive_scalar_seed_lifts': seed_lifts,
                  'negative_section_cocycle_pairs': sum(s == -1 for s in signs.values()),
                  'extension_splits': False},
        'pauli_bridge': {'formula': 'Phi(v)=sum_i v_i sigma_i; U Phi(v) U*=Phi(R v)',
                         'basis': ['I', 'sigma_x', 'sigma_y', 'sigma_z'],
                         'decomposition': 'End(S)=1+3', 'spinor_dimension': 2,
                         'spinor_character_norm': 1, 'vector_character_norm': 1,
                         'central_action_spinor': '-I', 'central_action_operator': '+I'},
        'projectors': {'reference_vector_Q_i_sqrt3': v0, 'reference_squared_norm': norm0,
                       'assembled_squared_norm': norm, 'ranks_L_R_N': ranks,
                       'supports_in_inherited_Pauli_basis': [len(local), len(symmetry), len(collective)],
                       'relations': 'L^2=L; R^2=R; N^2=N; LR=RL=N',
                       'carrier': 'direct sum of 12 traceless complex 2x2 operator spaces',
                       'complex_dimension': 36, 'transport': 'Hilbert-Schmidt superoperators, not 2x2 density matrices'},
        'optional_tensor_extension': {
            'extra_input': 'An independent defining spinor factor S is added, not derived from V36.',
            'carrier': 'V36 tensor S', 'complex_dimension': 72,
            'projector_ranks': extended_ranks,
            'collective_sector': 'Im(N tensor I2) = span(u) tensor S',
            'embedding_intertwiner': 'E(s)=u tensor s; D_extended(q) E = E U(q)',
            'checked_doublet_basis_images': 48,
            'central_action_on_collective_sector': '-I2',
            'invariant_vectors': 0,
        },
        'hostiles': {'wrong_handed_basis_squares_nonzero': wrong_hand,
                     'order_two_downstairs_order_four_upstairs': True,
                     'local_triangle_cycle_orthogonality_defect': orthogonal_defect,
                     'reference_Pauli_operator_determinant': F(16, 3),
                     'reference_Pauli_operator_Hermitian': False,
                     'spinor_state_descent_to_A4_fails': True,
                     '24_coordinate_spinor_group_average_rank': 0,
                     'charge_no_go_refuted_by_invariant_projector_N': True},
        'residuals': [
            'No nonzero equivariant linear map from the old central-even space to a central-odd spinor carrier exists.',
            'A0=X0 C X0^-1 is nonorthogonal; its HS superoperator is not SU(2) conjugation.',
            'Physical state selection, continuous rotation action on the whole carrier, Hamiltonian and charge coupling are not constructed.',
            'Support counts are retained in the inherited Pauli basis, not claimed basis invariant or physical masses.',
        ],
    }
    dest = ROOT / 'results' / 'binary-tetrahedral-spinor-bridge.json'
    dest.parent.mkdir(exist_ok=True)
    dest.write_text(json.dumps(report, indent=2, default=str) + '\n', encoding='utf-8')
    print('PASS: 2T(24) -> A4(12); Q8 -> V4; 576 products; 1728 cocycle triples.')
    print('PASS: Pauli 1+3 bridge; projector ranks 12,3,1 and LR=RL=N preserved.')
    print('PASS: explicit V36 tensor S extension has a rank-2 collective doublet; 48 basis images.')
    print('BOUNDARY: operators central-even; spinors central-odd; spinor average rank 0.')
    print('HOSTILES: nonunitary triangle cycle; det(Phi(v0))=16/3; charge no-go refuted.')


if __name__ == '__main__':
    main()

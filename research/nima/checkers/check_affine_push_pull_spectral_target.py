"""Exact affine-nerve adapter, weighted push-pull, and joint spectral audit.

Dependency-free. Exit zero certifies the bounded audit, NOT the target fractions.
No existing results files are inputs. Does not run imported checker entrypoints.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json

from check_twelve_triangle_positive_geometry import (
    POINTS, ONE, ZERO, OMEGA, mean, transpose, rotation, zmv, zmul,
    zadd, zconj, zscale, znorm, projector, cross, sub,
)

ROOT = Path(__file__).resolve().parents[1]


def fm(a, b):
    """F2[w]/(w^2+w+1), represented by two binary coefficients."""
    out = 0
    while b:
        if b & 1:
            out ^= a
        a <<= 1
        if a & 4:
            a ^= 7
        b >>= 1
    return out


def fi(a):
    assert a
    return next(b for b in (1, 2, 3) if fm(a, b) == 1)


def affine(g, x):
    b, a = g
    return b ^ fm(a, x)


def phi(t):
    x, y, z = t
    a = x ^ y
    return (x, a), fm(z ^ y, fi(a))


def unphi(g, r):
    b, a = g
    return b, b ^ a, b ^ fm(a, 1 ^ r)


# Sparse exact matrices over Q(i sqrt(3)); missing entries are zero.
def add(*terms):
    out = {}
    for m in terms:
        for ij, x in m.items():
            out[ij] = zadd(out.get(ij, ZERO), x)
    return {ij: x for ij, x in out.items() if x != ZERO}


def scale(m, a):
    return {ij: zscale(x, a) for ij, x in m.items() if a}


def mul(a, b):
    rows = {}
    for (j, k), y in b.items():
        rows.setdefault(j, []).append((k, y))
    out = {}
    for (i, j), x in a.items():
        for k, y in rows.get(j, ()):
            out[i, k] = zadd(out.get((i, k), ZERO), zmul(x, y))
    return {ij: x for ij, x in out.items() if x != ZERO}


def adj(a):
    return {(j, i): zconj(x) for (i, j), x in a.items()}


def eye(n):
    return {(i, i): ONE for i in range(n)}


def trace(a, n):
    out = ZERO
    for i in range(n):
        out = zadd(out, a.get((i, i), ZERO))
    return out


def exact_projector(p, n, rank):
    assert adj(p) == p
    assert mul(p, p) == p
    assert trace(p, n) == (F(rank), F(0))


def rmat(m):
    return {(i, j): (F(x), F(0)) for i, row in enumerate(m)
            for j, x in enumerate(row) if x}


def dense_small(m):
    return {(i, j): x for i, row in enumerate(m)
            for j, x in enumerate(row) if x != ZERO}


def main():
    # Verify the declared coefficient field, rather than arithmetic modulo four.
    assert all(fm(a, b ^ c) == (fm(a, b) ^ fm(a, c))
               for a, b, c in product(range(4), repeat=3))
    assert all(fm(a, fm(b, c)) == fm(fm(a, b), c)
               for a, b, c in product(range(4), repeat=3))
    A = list(product(range(4), (1, 2, 3)))
    M = (1, 2, 3)
    T = [t for t in product(range(4), repeat=3)
         if t[0] != t[1] and t[1] != t[2]]
    ports = list(product(A, M))
    index = {p: i for i, p in enumerate(ports)}
    assert len(T) == 36 and len(set(map(phi, T))) == 36
    assert all(unphi(*phi(t)) == t for t in T)
    assert all(phi(unphi(g, r)) == (g, r) for g, r in ports)
    perms = [tuple(affine(g, x) for x in range(4)) for g in A]
    assert len(set(perms)) == 12
    assert all(sum(p[i] > p[j] for i in range(4) for j in range(i+1, 4)) % 2 == 0
               for p in perms)
    assert all(tuple(p[q[i]] for i in range(4)) in perms for p, q in product(perms, repeat=2))

    # Faces are computed on full simplices. d1 can be degenerate.
    degenerate_middle = 0
    for t in T:
        g, r = phi(t)
        first, last, composite = t[:2], t[1:], (t[0], t[2])
        assert first == (affine(g, 0), affine(g, 1))
        assert last == (affine(g, 1), affine(g, 1 ^ r))
        assert composite == (affine(g, 0), affine(g, 1 ^ r))
        assert (composite[0] == composite[1]) == (r == 1)
        degenerate_middle += r == 1
    assert degenerate_middle == 12
    distinct_vertex_count = sum(len(set(t)) == 3 for t in T)
    assert distinct_vertex_count == 24
    # All degree-three face identities, including degenerate faces.
    def face(t, i):
        return t[:i] + t[i+1:]
    for t in product(range(4), repeat=4):
        for i in range(4):
            for j in range(i+1, 4):
                assert face(face(t, j), i) == face(face(t, i), j-1)

    # Relations are defined in the source, not pulled back from desired matrices.
    orbit = {t: {tuple(affine(g, x) for x in t) for g in A} for t in T}
    assert all(len(o) == 12 for o in orbit.values())
    H, V = set(), set()
    for t, s in product(T, repeat=2):
        i, j = index[phi(t)], index[phi(s)]
        if t[:2] == s[:2]:
            H.add((i, j))
        if s in orbit[t]:
            V.add((i, j))
    assert H == {(i, j) for i, (g, r) in enumerate(ports)
                 for j, (h, s) in enumerate(ports) if g == h}
    assert V == {(i, j) for i, (g, r) in enumerate(ports)
                 for j, (h, s) in enumerate(ports) if r == s}
    assert len(H) == 108 and len(V) == 432
    for i, k in product(range(36), repeat=2):
        assert sum((i, j) in V and (j, k) in H for j in range(36)) == 1
        assert sum((i, j) in H and (j, k) in V for j in range(36)) == 1
    Hcount = {ij: (F(1, 3), F(0)) for ij in H}
    Vcount = {ij: (F(1, 12), F(0)) for ij in V}
    Ncount = mul(Hcount, Vcount)
    assert Ncount == mul(Vcount, Hcount)
    assert set(Ncount.values()) == {(F(1, 36), F(0))}
    exact_projector(Hcount, 36, 12)
    exact_projector(Vcount, 36, 3)
    exact_projector(Ncount, 36, 1)

    # Recover the actual source geometric line and spatial rotations.
    x0 = transpose((mean([POINTS[a] for a in 'ABC']), POINTS['A'], POINTS['B']))
    c = zmv(x0, (ONE, OMEGA, zmul(OMEGA, OMEGA)))
    assert c == ((F(-2, 3), F(0)), (F(1, 3), F(1)), (F(-1, 3), F(1)))
    P = dense_small(projector(c))
    mu = [P[i, i][0] for i in range(3)]
    assert mu == [F(1, 15), F(7, 15), F(7, 15)]
    countP = {(i, j): (F(1, 3), F(0)) for i, j in product(range(3), repeat=2)}
    assert P != countP
    # A monomial unitary can only permute diagonal weights, not equalize them.
    assert sorted(mu) != [F(1, 3)] * 3
    K = {(i, j): (mu[j], F(0)) for i, j in product(range(3), repeat=2)}
    assert mul(K, K) == K
    D = {(i, i): c[i] for i in range(3)}
    Di = {(i, i): zscale(zconj(c[i]), 1 / znorm(c[i])) for i in range(3)}
    assert mul(mul(D, K), Di) == P
    # Selected-line coefficients compose by sums, not by edgewise multiplication.
    assert zmul(P[0, 0], P[0, 0]) != P[0, 0]
    exact_projector(P, 3, 1)

    rotations = [rmat(rotation(p)) for p in perms]
    local, alignment, U = {}, {}, {}
    unsigned_alignment = {}
    for a, R in enumerate(rotations):
        Pa = mul(mul(R, P), adj(R))
        for (i, j), z in Pa.items():
            local[3*a+i, 3*a+j] = z
        for (i, j), z in adj(R).items():
            U[3*a+i, 3*a+j] = z
        for b, S in enumerate(rotations):
            for (i, j), z in mul(R, adj(S)).items():
                alignment[3*a+i, 3*b+j] = zscale(z, F(1, 12))
                unsigned_alignment[3*a+i, 3*b+j] = (F(1, 12), F(0))
    I = eye(36)
    assert mul(U, adj(U)) == I
    L = mul(mul(U, local), adj(U))
    G = mul(mul(U, alignment), adj(U))
    Lexpected = {(3*a+i, 3*a+j): z for a in range(12) for (i, j), z in P.items()}
    assert L == Lexpected and G == Vcount
    assert L != Hcount
    N = mul(L, G)
    assert N == mul(G, L)
    assert [len(local), len(alignment), len(N)] == [108, 432, 1296]
    assert sum([len(local), len(alignment), len(N)]) == 1836
    nativeN = mul(local, alignment)
    assert nativeN == mul(alignment, local)
    assert mul(mul(U, nativeN), adj(U)) == N
    sign_defect = add(mul(local, unsigned_alignment), scale(mul(unsigned_alignment, local), -1))
    assert sign_defect

    # Four mutually orthogonal atoms: ranks are traces of exact idempotents.
    atoms = [N, add(L, scale(N, -1)), add(G, scale(N, -1)),
             add(I, scale(L, -1), scale(G, -1), N)]
    ranks = [1, 11, 2, 22]
    assert add(*atoms) == I
    for i, E in enumerate(atoms):
        exact_projector(E, 36, ranks[i])
        for j, Fm in enumerate(atoms):
            if i != j:
                assert not mul(E, Fm)
    assert L == add(atoms[0], atoms[1]) and G == add(atoms[0], atoms[2])
    # All spectral idempotents in C[L,G] are sums of the four nonzero atoms.
    masks = list(product((0, 1), repeat=4))
    sizes = {m: sum(bit*r for bit, r in zip(m, ranks)) for m in masks}
    by_rank = {r: [m for m in masks if sizes[m] == r] for r in (11, 14, 25)}
    assert all(len(ms) == 1 for ms in by_rank.values())
    e11, e14, e25 = (by_rank[r][0] for r in (11, 14, 25))
    assert e11 == (0, 1, 0, 0)
    assert e14 == (1, 1, 1, 0)
    assert e25 == (1, 0, 1, 1)
    overlap = lambda m, n: sum(a*b*r for a, b, r in zip(m, n, ranks))
    assert overlap(e11, e25) == 0
    assert overlap(e14, e25) == 3
    assert overlap(e11, e14) == 11
    splits = [(a, b, k) for a in masks for b in masks for k in masks
              if sizes[a] == 11 and sizes[b] == 14 and sizes[k] == 25
              and all(x+y == z for x, y, z in zip(a, b, k))]
    assert not splits

    # Two declared rate conventions; neither is a physical Hamiltonian selection.
    Hnormalized = add(scale(I, 2), scale(L, -1), scale(G, -1))
    Hcounting = add(scale(I, 15), scale(L, -3), scale(G, -12))
    for E, en, ec in zip(atoms, (0, 1, 1, 2), (0, 12, 3, 15)):
        assert mul(Hnormalized, E) == scale(E, en)
        assert mul(Hcounting, E) == scale(E, ec)
    rho1 = scale(atoms[1], F(1, 11))
    rho0 = atoms[0]
    assert trace(rho1, 36) == trace(rho0, 36) == ONE
    assert trace(mul(rho1, atoms[1]), 36) == ONE
    assert trace(mul(rho0, atoms[1]), 36) == ZERO

    # Source-internal successor: triangle normal, independently of target ratios.
    centre = mean([POINTS[a] for a in 'ABC'])
    normal = cross(sub(POINTS['A'], centre), sub(POINTS['B'], centre))
    assert normal == (F(4, 3), F(4, 3), F(-4, 3))
    Rnormal = dense_small(projector(tuple((x, F(0)) for x in normal)))
    Rreverse = dense_small(projector(tuple((-x, F(0)) for x in normal)))
    assert Rnormal == Rreverse
    exact_projector(Rnormal, 3, 1)
    assert not mul(Rnormal, P) and not mul(P, Rnormal)
    Rtan = add(eye(3), scale(P, -1), scale(Rnormal, -1))
    exact_projector(Rtan, 3, 1)
    assert add(P, Rnormal, Rtan) == eye(3)
    normal_local = {(3*a+i, 3*a+j): z for a in range(12) for (i, j), z in Rnormal.items()}
    # Verify normal construction covaries in the actual spatial frames.
    normal_native = {}
    for a, rot in enumerate(rotations):
        block = mul(mul(rot, Rnormal), adj(rot))
        perm = perms[a]
        vertices = [POINTS['ABCD'[perm[i]]] for i in range(3)]
        transported_centre = mean(vertices)
        geometric_normal = cross(sub(vertices[0], transported_centre),
                                 sub(vertices[1], transported_centre))
        assert block == dense_small(projector(tuple((x, F(0)) for x in geometric_normal)))
        for (i, j), z in block.items():
            normal_native[3*a+i, 3*a+j] = z
    assert mul(mul(U, normal_native), adj(U)) == normal_local
    Knative = add(I, scale(L, -1), N)
    Fnormal = mul(add(I, scale(G, -1)), normal_local)
    Fother = add(Knative, scale(Fnormal, -1))
    exact_projector(Knative, 36, 25)
    exact_projector(Fnormal, 36, 11)
    exact_projector(Fother, 36, 14)
    assert not mul(Fnormal, Fother)
    assert add(Fnormal, Fother) == Knative
    assert mul(Knative, Fnormal) == Fnormal
    assert mul(atoms[3], Fnormal) == Fnormal and Fnormal != atoms[3]
    # This is a proper refinement of the old rank-22 atom, not its scalar image.
    assert not mul(Fnormal, atoms[1])
    rhoK = scale(Knative, F(1, 25))
    conditional_weights = [trace(mul(rhoK, E), 36)[0] for E in (Fnormal, Fother)]
    assert conditional_weights == [F(11, 25), F(14, 25)]
    # Admissible pure states inside K do not have a forced 11/25 normal weight.
    qR = mul(G, normal_local)
    exact_projector(qR, 36, 1)
    # (delta_a-delta_b) tensor normal, with the already normalized normal projector.
    contrast = {(0, 0): (F(1, 2), F(0)), (1, 1): (F(1, 2), F(0)),
                (0, 1): (F(-1, 2), F(0)), (1, 0): (F(-1, 2), F(0))}
    pure_normal = {(3*a+i, 3*b+j): zmul(z, w)
                   for (a, b), z in contrast.items() for (i, j), w in Rnormal.items()}
    exact_projector(pure_normal, 36, 1)
    for rho, probability in ((qR, 0), (pure_normal, 1)):
        assert mul(Knative, rho) == rho
        assert trace(mul(rho, Fnormal), 36) == (F(probability), F(0))

    # Changing the full-support selected line preserves the entire rank algebra.
    altP = dense_small(projector(((F(1), F(0)), (F(2), F(0)), (F(3), F(0)))))
    assert altP != P and len(altP) == 9
    axisP = dense_small(projector((ONE, ZERO, ZERO)))
    assert len(axisP) == 1  # support hypothesis is essential, not a fitted exception.
    paths = [Path(__file__), ROOT/'checkers/check_twelve_triangle_positive_geometry.py',
             ROOT/'checkers/check_triangle_half_phase.py']
    report = {
        'schema': 'marici.nima.affine-push-pull-spectral-target.v1',
        'audit_passed': True,
        'scientific_disposition': 'affine_support_adapter_proved; counting_native_coefficients_differ; bare_joint_algebra_split_refuted; geometric_normal_refinement_gives_conditional_11_14_split_and_trace_weights',
        'coherence_obligation': 'forward_realization_then_attachment_transport_then_route_compatibility; readout_not_promoted',
        'source': {'candidate': 'pair_groupoid_nerve_on_labelled_F4_with_diagonal_AGL_action',
                   'not_identified_with_unspecified_historical_X': True,
                   'ports': 36, 'affine_even_permutations': 12,
                   'distinct_vertex_triples_only': distinct_vertex_count,
                   'nondegenerate_triples_with_degenerate_middle_face': degenerate_middle,
                   'degree_three_full_face_identity_checks': 256 * 6},
        'source_relations': {'horizontal': 'kernel_pair_d2', 'vertical': 'diagonal_affine_orbits',
                             'support_sizes': [len(H), len(V), len(Ncount)],
                             'mixed_fiber_cardinality': 1,
                             'counting_ranks': [12, 3, 1],
                             'counted_diagonals_per_relation': 36,
                             'typed_support_sum': 1836},
        'coefficient_transport': {'native_diagonal': list(map(str, mu)),
                                  'counting_diagonal': ['1/3'] * 3,
                                  'native_equals_counting': False,
                                  'weighted_conditional_expectation_conjugates_to_native': True,
                                  'decoration_input': 'geometric_eigenline_c; complex_phases_and_nonuniform_measure',
                                  'signed_comoving_frame_intertwines_native': True,
                                  'extra_choice': 'ordered_M_to_reference_axes_identification'},
        'joint_algebra': {'atom_order': ['N', 'L-N', 'G-N', 'I-L-G+N'],
                         'atom_ranks': ranks,
                         'idempotent_count': 16,
                         'idempotent_rank_set': sorted(set(sizes.values())),
                         'unique_rank11': list(e11), 'unique_rank14': list(e14),
                         'unique_rank25': list(e25),
                         'rank11_rank25_intersection': 0,
                         'rank14_rank25_intersection': 3,
                         'rank11_rank14_intersection': 11,
                         'eleven_fourteen_splits_of_twentyfive': len(splits)},
        'spectral_tests': {'normalized_gap_spectrum': {'0': 1, '1': 13, '2': 22},
                           'counting_gap_spectrum': {'0': 1, '3': 2, '12': 11, '15': 22},
                           'general_gap': {'definition': 'alpha(I-L)+beta(I-G)',
                                           'eigenvalues_in_atom_order': ['0', 'beta', 'alpha', 'alpha+beta']},
                           'same_joint_algebra_admits_rank11_probabilities': ['0', '1'],
                           'target_fractions_derived': False},
        'geometric_normal_successor': {
            'source_operation': 'Euclidean_normal_of_existing_centroid_edge_triangle',
            'normal': list(map(str, normal)),
            'normal_projector_rank': 1,
            'normal_annihilates_selected_line': True,
            'orientation_reversal_preserves_projector': True,
            'transport_intertwines': True,
            'K': 'I-L+N; excludes selected-line disagreement',
            'normal_sector': '(I-Q) tensor Rnormal',
            'other_sector': 'Q tensor I3 + (I-Q) tensor (I-P-Rnormal)',
            'ranks': [25, 11, 14],
            'new_rank11_is_orthogonal_to_old_L_minus_N': True,
            'conditional_normalized_trace_weights': list(map(str, conditional_weights)),
            'state_assumption': 'rhoK=K/25; not selected by incidence or geometry',
            'pure_states_within_K_have_normal_weights': ['0', '1'],
            'wheel_25_field_comparison': 'absent',
            'target_fractions_unconditionally_derived': False},
        'hostiles': {'all_vertices_distinct_loses_12_ports': True,
                     'discard_spatial_signs_nonzero_commutator_entries': len(sign_defect),
                     'single_edge_product_not_projector_composition': True,
                     'alternate_full_support_line_changes_coefficients': True,
                     'axis_line_loses_full_support': True},
        'residuals': ['historical_source_X_and_its_comparison_not_supplied',
                      'affine_counting_does_not_select_native_geometric_decoration',
                      'wheel_25_entry_field_not_identified_with_rank25_joint_sector',
                      'normal_refinement_uses_preexisting_Euclidean_geometry_not_bare_affine_counting',
                      'selection_of_K_and_its_normalized_trace_state_not_source_forced',
                      'no_physical_mass_or_time_or_fraction_selection'],
        'source_sha256': {str(p.relative_to(ROOT.parents[1])).replace('\\', '/'): hashlib.sha256(p.read_bytes()).hexdigest()
                          for p in paths},
    }
    dest = ROOT/'results/affine-push-pull-spectral-target.json'
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print('PASS: 36-element affine adapter; source H=d2 kernel pair, V=affine orbits; 1296 unique mixed fibers.')
    print('PASS: native signed frame and weighted push-pull; joint ranks 1,11,2,22; all 16 spectral idempotents.')
    print('REFUTED: counting coefficients equal native coefficients (1/3 versus 1/15,7/15,7/15).')
    print('REFUTED in C[L,G]: rank-25 carrier splits into rank 11 and rank 14; rank-11 atom is orthogonal to rank-25 sector.')
    print('PASS: geometric normal refines the rank-22 atom; K=I-L+N splits into new normal rank 11 and rank 14.')
    print('CONDITIONAL: rho=K/25 yields 11/25,14/25; pure states in K also yield normal weights 0 or 1.')
    print('OPEN: source selection of K/state/readout and faithful wheel-25 comparison; no unconditional fraction derivation.')


if __name__ == '__main__':
    main()

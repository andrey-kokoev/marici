"""Minimal seam-respecting observation closures in the declared pair carrier.

Readers are D-coordinates plus a seam-addressed coefficient. Operation families
are stated separately. This is conditional linear observability, not selection
of physical preparations, symmetry quotients, or available controls.
"""
from dataclasses import dataclass, replace
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import check_record4_spectral_promotion as sp
import check_spectral_successor_many_many as rec
import check_spectral_invariant_path_algebra as alg


def power(matrix, exponent):
    out = rec.IDENTITY
    for _ in range(exponent):
        out = sp.zmm(matrix, out)
    return out


def rank(matrix):
    assert matrix and all(value[1] == 0 for row in matrix for value in row)
    rows = [[value[0] for value in row] for row in matrix]
    pivot_row = 0
    for column in range(len(rows[0])):
        pivot = next((i for i in range(pivot_row, len(rows)) if rows[i][column]), None)
        if pivot is None:
            continue
        rows[pivot], rows[pivot_row] = rows[pivot_row], rows[pivot]
        divisor = rows[pivot_row][column]
        rows[pivot_row] = [value / divisor for value in rows[pivot_row]]
        for i in range(len(rows)):
            if i != pivot_row:
                multiplier = rows[i][column]
                rows[i] = [v - multiplier * p for v, p in zip(rows[i], rows[pivot_row])]
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return pivot_row


@dataclass(frozen=True)
class SplitPacket:
    length: int
    visible: tuple
    residual: tuple
    rows: tuple
    parents: tuple = ()


def main():
    slots = alg.SLOTS
    words = alg.WORDS
    cycles = tuple(sp.cycle_from_packets(tuple(sp.TwoPacket(e, e[0], e[1]) for e in word))
                   for word in words)
    L = rec.kron(sp.zreal(cycles[0]), sp.zreal(sp.I))
    T = rec.kron(sp.zreal(sp.I), sp.zreal(cycles[1]))
    M = sp.zmm(L, T)
    W = tuple(tuple(rec.ONE if row == 3 * (col % 3) + col // 3 else rec.Z
                    for col in range(9)) for row in range(9))
    P = sp.zmscale(sp.zmadd(rec.IDENTITY, W), (F(1, 2), F(0)))
    Q = sp.zmadd(rec.IDENTITY, sp.zmscale(P, (F(-1), F(0))))
    D = rec.matrix_sum(rec.kron(sp.spectral_projector(cycles[0], mode)[1],
                               sp.spectral_projector(cycles[1], mode)[1]) for mode in rec.MODES)
    assert sp.zmm(W, W) == rec.IDENTITY
    assert sp.zmm(M, W) == sp.zmm(W, M)
    assert sp.dagger(P) == P and sp.zmm(P, P) == P
    assert sp.ztrace(P) == (F(6), F(0)) and sp.ztrace(Q) == (F(3), F(0))
    assert sp.zmm(P, D) == sp.zmm(D, P) == D

    manifest = tuple((words[0][i], words[1][j]) for i, j in slots)
    # Reciprocal endpoint extraction fixes the reader before any rank test.
    seam = tuple(rec.ONE if a[0] == b[1] and a[1] == b[0] else rec.Z for a, b in manifest)
    assert seam.count(rec.ONE) == 1 and seam[0] == rec.ONE
    h = (seam,)
    assert sp.zmm(h, P) == h
    # W is the actual seed vertex swap accompanied by context exchange.
    rename = dict(zip('ABCD', 'BADC'))
    for index, pair in enumerate(manifest):
        transformed = tuple(rename[e[0]] + rename[e[1]] for e in reversed(pair))
        i, j = slots[index]
        assert transformed == manifest[3 * j + i]

    # Base observations: all D-coordinate outputs plus one seam-coordinate.
    # These are numerical functionals, not quotienting history labels.
    O_base = tuple(D) + h
    assert rank(D) == 3 and rank(O_base) == 4
    joint_ops = tuple(sp.zmm(power(M, k), power(W, flip)) for k, flip in product(range(3), range(2)))
    O_joint = tuple(row for operation in joint_ops for row in sp.zmm(O_base, operation))
    assert rank(O_joint) == 6
    assert sp.zmm(O_joint, P) == O_joint
    assert sp.zmm(O_joint, Q) == tuple((rec.Z,) * 9 for _ in O_joint)
    for operation in joint_ops:
        assert sp.zmm(P, sp.zmm(operation, Q)) == rec.ZERO
        assert sp.zmm(Q, sp.zmm(operation, P)) == rec.ZERO

    # Six independent readings: orbit-average coordinates d_q, and the three
    # successive seam readings h M^k. Recover symmetric off-diagonal values by
    # subtracting the diagonal from each three-slot orbit sum.
    representatives = (0, 1, 2)
    orbit_readers = tuple(D[i] for i in representatives)
    seam_readers = tuple(sp.zmm(h, power(M, k))[0] for k in range(3))
    O_six = orbit_readers + seam_readers
    assert rank(O_six) == 6
    decoder = []
    for i, j in slots:
        row = [rec.Z] * 6
        if i == j:
            row[3 + i] = rec.ONE
        else:
            q = (i + j) % 3
            diagonal = (2 * q) % 3  # 2*diagonal == q (mod 3)
            row[q] = (F(3, 2), F(0))
            row[3 + diagonal] = (F(-1, 2), F(0))
        decoder.append(tuple(row))
    decoder = tuple(decoder)
    assert sp.zmm(decoder, O_six) == P
    assert sp.zmm(O_six, decoder) == sp.zreal(tuple(tuple(F(i == j) for j in range(6)) for i in range(6)))
    for omitted in range(6):
        assert rank(tuple(row for k, row in enumerate(O_six) if k != omitted)) == 5

    # Independent local advances move the seam reader across all nine slots.
    independent_ops = tuple(sp.zmm(power(L, a), power(T, b)) for a, b in product(range(3), repeat=2))
    O_nine = tuple(sp.zmm(h, operation)[0] for operation in independent_ops)
    assert O_nine == rec.IDENTITY  # in this fixed probe/slot order
    O_independent = tuple(row for operation in independent_ops for row in sp.zmm(O_base, operation))
    assert rank(O_independent) == 9
    assert sp.zmm(P, sp.zmm(L, Q)) != rec.ZERO
    assert sp.zmm(P, sp.zmm(T, Q)) != rec.ZERO

    basis = tuple(tuple(rec.ONE if i == j else rec.Z for j in range(9)) for i in range(9))
    mixed = tuple((F(i - 4, 7), F(i % 3 - 1, 5)) for i in range(9))
    for x in basis + (mixed,):
        assert rec.apply(decoder, rec.apply(O_six, x)) == rec.apply(P, x)
        assert rec.apply(O_joint, x) == rec.apply(O_joint, rec.apply(P, x))
        assert rec.apply(O_nine, x) == x
    # A retained antisymmetric direction invisible to all joint-family readers
    # becomes visible under a specified independent right advance.
    hidden = rec.subtract(basis[1], basis[3])
    assert rec.apply(P, hidden) == (rec.Z,) * 9
    assert rec.apply(O_joint, hidden) == (rec.Z,) * len(O_joint)
    assert rec.apply(sp.zmm(h, T), hidden) == (rec.ONE,)
    assert rec.apply(P, rec.apply(T, hidden)) != (rec.Z,) * 9

    # Invariant-state closure is a separate property from lossless projection
    # of products. W commutes with path shift and acts multiplicatively, so its
    # fixed sector is closed under the existing length-graded product.
    for length, i, j in product(range(3), range(9), range(9)):
        a, b = basis[i], basis[j]
        ab = alg.multiply(a, b, length)
        assert rec.apply(W, ab) == alg.multiply(rec.apply(W, a), rec.apply(W, b), length)
        pa, pb, qa, qb = rec.apply(P, a), rec.apply(P, b), rec.apply(Q, a), rec.apply(Q, b)
        pp = alg.multiply(pa, pb, length)
        assert rec.apply(P, pp) == pp
        assert rec.apply(P, ab) == alg.add(pp, rec.apply(P, alg.multiply(qa, qb, length)))
    # Hidden product is not harmless: choose a length-one partner so the
    # concatenated coefficient product is pointwise hidden^2.
    hidden_partner = alg.shift(hidden, -1)
    assert rec.apply(P, hidden_partner) == (rec.Z,) * 9
    visible_product = alg.multiply(hidden, hidden_partner, 1)
    assert visible_product != (rec.Z,) * 9 and rec.apply(P, visible_product) == visible_product
    assert rec.apply(O_joint, visible_product) != (rec.Z,) * len(O_joint)

    # Exact retained six-plus-three successor, not a new multiplication law.
    # Visible coordinates use the already checked O_six/decoder interface:
    # (three D orbit means, three diagonal/seam-orbit readings).
    off_diagonal = ((0, 1), (0, 2), (1, 2))

    def residual_coordinates(vector):
        return tuple(vector[3 * i + j] for i, j in off_diagonal)

    def residual_lift(values):
        if len(values) != 3:
            raise ValueError('Three antisymmetric coordinates required')
        out = [rec.Z] * 9
        for (i, j), value in zip(off_diagonal, values):
            out[3 * i + j] = value
            out[3 * j + i] = sp.zscale(value, -1)
        return tuple(out)

    def encode_split(original):
        alg.validate(original)
        return SplitPacket(original.length, rec.apply(O_six, original.coefficients),
                           residual_coordinates(rec.apply(Q, original.coefficients)), original.rows,
                           tuple(encode_split(parent) for parent in original.parents))

    def split_parts(split):
        if len(split.visible) != 6 or split.rows != alg.paths(split.length):
            raise ValueError('Malformed visible coordinates or retained paths')
        return rec.apply(decoder, split.visible), residual_lift(split.residual)

    def decode_split(split):
        symmetric, antisymmetric = split_parts(split)
        parents = tuple(decode_split(parent) for parent in split.parents)
        if len(parents) not in (0, 2):
            raise ValueError('Expected an input leaf or two retained parents')
        result = alg.Packet(split.length, alg.add(symmetric, antisymmetric), split.rows, parents)
        if parents:
            expected = alg.compose(*parents)
            if result != expected:
                raise ValueError('Output disagrees with retained parent composition')
        return result

    def compose_split(left, right):
        # Validate full history bindings; output coefficients below are computed
        # through four parity blocks, not by dropping/re-preparing the residual.
        decode_split(left)
        decode_split(right)
        s1, a1 = split_parts(left)
        s2, a2 = split_parts(right)
        ss = alg.multiply(s1, s2, left.length)
        aa = alg.multiply(a1, a2, left.length)
        sa = alg.multiply(s1, a2, left.length)
        ass = alg.multiply(a1, s2, left.length)
        symmetric_out = alg.add(ss, aa)
        antisymmetric_out = alg.add(sa, ass)
        assert rec.apply(P, symmetric_out) == symmetric_out
        assert rec.apply(Q, antisymmetric_out) == antisymmetric_out
        return SplitPacket(left.length + right.length, rec.apply(O_six, symmetric_out),
                           residual_coordinates(antisymmetric_out), alg.paths(left.length + right.length),
                           (left, right))

    for vector in basis + (mixed, hidden):
        original = alg.packet(1, vector)
        assert decode_split(encode_split(original)) == original
    # Basis bilinearity checks cover all complex input coefficients. The only
    # length dependence of coefficients is the already retained shift residue.
    for length, i, j in product(range(3), range(9), range(9)):
        left = alg.packet(length, basis[i])
        right = alg.packet((i + j) % 4, basis[j])
        split_output = compose_split(encode_split(left), encode_split(right))
        full_output = alg.compose(left, right)
        assert decode_split(split_output) == full_output
        assert split_output == encode_split(full_output)
        assert split_output.length == left.length + right.length

    y = tuple((F(i + 1, 11), F(i % 2, 3)) for i in range(9))
    z = tuple((F(2 * i - 3, 13), F(i % 4 - 2, 9)) for i in range(9))
    for m, n, k in product(range(4), repeat=3):
        a, b, c = (encode_split(alg.packet(length, value))
                   for length, value in ((m, mixed), (n, y), (k, z)))
        first = compose_split(compose_split(a, b), c)
        second = compose_split(a, compose_split(b, c))
        assert first.visible == second.visible and first.residual == second.residual
        assert first.length == second.length == m + n + k and first.rows == second.rows
        assert first.parents != second.parents
        assert decode_split(first) == alg.compose(alg.compose(decode_split(a), decode_split(b)), decode_split(c))
        assert decode_split(second) == alg.compose(decode_split(a), alg.compose(decode_split(b), decode_split(c)))

    # Locate the complete AA correction span at each length residue. Every
    # antisymmetric coefficient array vanishes on its diagonal, and the joint
    # shift preserves the diagonal. Thus no AA term enters seam-orbit readings.
    residual_basis = tuple(residual_lift(tuple(rec.ONE if i == j else rec.Z for j in range(3)))
                           for i in range(3))
    correction_ranks = []
    for length in range(3):
        corrections = [alg.multiply(a, b, length) for a, b in product(residual_basis, repeat=2)]
        assert rank(tuple(corrections)) == 3
        correction_profiles = tuple(rec.apply(O_six, value) for value in corrections)
        assert rank(correction_profiles) == 3
        assert all(profile[3:] == (rec.Z,) * 3 for profile in correction_profiles)
        assert all(value[3 * i + i] == rec.Z for value in corrections for i in range(3))
        correction_ranks.append(3)
        # Each off-diagonal symmetric coordinate is individually reachable.
        for index, a in enumerate(residual_basis):
            b = alg.shift(a, -length)
            value = alg.multiply(a, b, length)
            ii, jj = off_diagonal[index]
            expected = alg.add(basis[3 * ii + jj], basis[3 * jj + ii])
            assert value == expected
            q = (ii + jj) % 3
            expected_profile = tuple((F(2, 3), F(0)) if i == q else rec.Z for i in range(6))
            assert rec.apply(O_six, value) == expected_profile

    # A nontrivial full complex fixture also verifies that the diagonal visible
    # readings are already correct without AA, whereas orbit means need it.
    sample_left = encode_split(alg.packet(1, mixed))
    sample_right = encode_split(alg.packet(2, y))
    sample_out = compose_split(sample_left, sample_right)
    s1, a1 = split_parts(sample_left)
    s2, a2 = split_parts(sample_right)
    ss_reading = rec.apply(O_six, alg.multiply(s1, s2, 1))
    aa_reading = rec.apply(O_six, alg.multiply(a1, a2, 1))
    assert sample_out.visible == alg.add(ss_reading, aa_reading)
    assert sample_out.visible[3:] == ss_reading[3:]
    assert aa_reading != (rec.Z,) * 6

    # Grade/history recovery includes units and loops, not just coefficient data.
    unit = encode_split(alg.packet(0, (rec.ONE,) * 9))
    with_unit = compose_split(unit, sample_left)
    assert with_unit.visible == sample_left.visible and with_unit.residual == sample_left.residual
    assert with_unit.length == sample_left.length and with_unit.parents == (unit, sample_left)
    loop = encode_split(alg.packet(3, (rec.ONE,) * 9))
    with_loop = compose_split(loop, sample_left)
    assert with_loop.visible == sample_left.visible and with_loop.residual == sample_left.residual
    assert with_loop.length == sample_left.length + 3 and with_loop.rows != sample_left.rows
    rec.reject(lambda: decode_split(replace(sample_out, residual=sample_out.residual[:-1])))
    rec.reject(lambda: decode_split(replace(sample_out, rows=sample_out.rows[:-1])))
    rec.reject(lambda: decode_split(replace(sample_out, length=sample_out.length + 1)))
    rec.reject(lambda: decode_split(replace(sample_out, parents=tuple(reversed(sample_out.parents)))))
    rec.reject(lambda: decode_split(replace(sample_out, residual=(rec.Z,) * 3)))

    report = {
        'status': 'passed',
        'scope': 'fixed seam/D coefficient readers under specified operation families; not physical admission',
        'ranks': {'D_only': 3, 'D_plus_seam_no_evolution': 4,
                  'joint_advance_and_seed_exchange_closure': 6, 'independent_advance_closure': 9},
        'six_sector': {'projection': 'P=(I+W)/2', 'kernel_dimension': 3,
                       'contains_D': True, 'seam_reader_preserved': True,
                       'six_reading_decoder_verified': True,
                       'all_six_reading_deletions_reduce_rank_to_five': True},
        'nine_sector': {'seam_orbit_observation_matrix': 'I_9',
                        'independent_right_advance_reveals_antisymmetric_hostile': True},
        'graded_product': {'six_sector_is_invariant_subalgebra': True,
                           'projection_is_algebra_homomorphism': False,
                           'hidden_hidden_product_visible': True},
        'retained_six_plus_three_successor': {
            'visible_coordinates': ['D orbit mean 0', 'D orbit mean 1', 'D orbit mean 2',
                                    'diagonal 00', 'diagonal 11', 'diagonal 22'],
            'residual_coordinates': ['antisymmetric 01', 'antisymmetric 02', 'antisymmetric 12'],
            'update': ['s_out=s1*s2+a1*a2', 'a_out=s1*a2+a1*s2'],
            'basis_pair_length_checks': 243,
            'complex_graded_associativity_fixtures': 64,
            'AA_correction_rank_by_length_residue': correction_ranks,
            'AA_support': 'symmetric off-diagonal entries; only the three D orbit means in visible coordinates',
            'AA_diagonal_seam_correction': 'identically zero under the declared joint-shift product',
            'exact_full_packet_reconstruction': True,
            'parent_trees_and_true_lengths_retained': True,
            'negative_controls': ['missing residual', 'missing path row', 'wrong length',
                                  'reversed parents', 'zeroed residual inconsistent with parents'],
            'scope': 'lossless coordinate implementation of the existing conditional product, not a new coupling'},
        'interpretation': 'Minimal rank 6 for joint-control interface, rank 9 when independent controls admitted; keep histories separately.',
        'not_claimed': ['unconditional six-state sufficiency for arbitrary binary contexts',
                        'physical quotient by seed symmetry', 'lossless recovery of history from coefficients'],
    }
    dest = Path(__file__).resolve().parents[1] / 'results' / 'seam-respecting-observation-closure.json'
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print('PASS: observation ranks 3 -> 4 -> 6 -> 9 as seam and operation contexts are admitted.')
    print('PASS: joint controls require exactly the W-symmetric six-sector; explicit minimal decoder verified.')
    print('PASS: independent local advances expose the remaining three directions and reconstruct all nine.')
    print('PASS: six-sector is a graded subalgebra, but projection still loses hidden-product effects.')
    print('PASS: exact six-plus-three successor matches full composition, with graded associativity and history recovery.')
    print('PASS: residual-residual correction has rank-three off-diagonal support; diagonal seam readings are unchanged.')
    print('Report: research/nima/results/seam-respecting-observation-closure.json')


if __name__ == '__main__':
    main()

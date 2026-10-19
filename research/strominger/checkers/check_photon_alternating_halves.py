"""Exact tests of the operator's alternating filled/complex photon conjecture.

Reuses the actual packet registry and rational matrix operations. No source
checker main() is invoked and no shared result store is overwritten.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'research/nima/checkers'))
import check_natural_tower_return as source
import check_photon_two_packet_candidate as photon


def rank(matrix):
    a = [list(row) for row in matrix]
    r = 0
    for c in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        value = a[r][c]
        a[r] = [x / value for x in a[r]]
        for i in range(len(a)):
            if i != r:
                value = a[i][c]
                a[i] = [x - value * y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def main():
    packets = source.PACKETS
    assert tuple(p[0] for p in packets) == ('AB', 'BC', 'CA', 'BA', 'AD', 'DB')
    K = tuple(tuple(F(a[2] == b[1]) for a in packets) for b in packets)
    w2 = photon.scalar_power(photon.OMEGA, 2)
    plus = (photon.ONE, (-F(1), F(0)), (-w2[0], -w2[1]),
            (-F(1), F(0)), photon.ONE, w2)
    candidate = photon.TwoPacketVector(packets, plus, photon.OMEGA)
    photon.validate_candidate(candidate, packets, K)
    U = tuple(tuple(z) for z in plus)
    T = ((-F(1, 2), F(1, 2)), (-F(3, 2), -F(1, 2)))
    I = ((F(1), F(0)), (F(0), F(1)))
    zero = ((F(0), F(0)),) * 2
    mm = source.mm
    T2 = mm(T, T)
    checks = {
        'actual_continuation_preserves_candidate_plane': mm(K, U) == mm(U, T),
        'three_steps_identity': mm(T2, T) == I,
        'two_steps_not_identity': T2 != I,
        'no_nonzero_two_step_fixed_vector': rank(source.sub(T2, I)) == 2,
        'each_triangle_recovers_real_candidate_plane': rank(U[:3]) == rank(U[3:]) == 2,
        'triangle_coefficients_are_opposites': U[3:] == source.scale(U[:3], -1),
    }
    # A filled/complex grading J exchanged by T would obey JT=-TJ.
    # Compute all four linear equations on an arbitrary 2x2 J.
    basis = [tuple(tuple(F(i == a and j == b) for j in range(2)) for i in range(2))
             for a in range(2) for b in range(2)]
    images = [source.add(mm(J, T), mm(T, J)) for J in basis]
    equations = [[image[i][j] for image in images] for i in range(2) for j in range(2)]
    checks['no_nonzero_linear_swapped_grading'] = rank(equations) == 4
    # Under a common complex amplitude c=a+i sqrt(3)b, imaginary parts
    # of c*g on a triangle are a*imag(g)+b*real(g). Rank two means that
    # no nonzero amplitude makes that whole triangle purely real.
    imag_constraints = [[z[1], z[0]] for z in plus[:3]]
    real_constraints = [[z[0], -3*z[1]] for z in plus[:3]]
    checks['no_nonzero_all_real_eigenmode_triangle'] = rank(imag_constraints) == 2
    checks['no_nonzero_all_imaginary_eigenmode_triangle'] = rank(real_constraints) == 2
    # One complex coefficient does encode the DECLARED real candidate plane:
    # z=x+i sqrt(3)y, decode to U(x,y). This is not a new primitive edge.
    # Recover coordinates from AB=x and CA=(x+y)/2.
    recover = ((F(1), F(0), F(0)), (-F(1), F(0), F(2)))
    checks['real_plane_one_complex_coordinate_lossless'] = mm(recover, U[:3]) == I
    # But a generic vector a*g+ + b*g- in the complexified plane cannot
    # be encoded by any single complex-linear scalar map C^2 -> C.
    minus = tuple((z[0], -z[1]) for z in plus)
    difference = tuple((p[0]-m[0], p[1]-m[1]) for p, m in zip(plus, minus))
    checks['single_AB_readout_loses_complexified_state'] = difference[0] == photon.Z and any(z != photon.Z for z in difference)
    # Deliberate positive control: an added swap CAN have period two. It
    # passes the desired pattern but is not the source continuation.
    S = ((F(0), F(1)), (F(1), F(0)))
    checks['invented_swap_detectably_different'] = mm(S, S) == I and S != T
    powers = [I, T, T2, mm(T2, T)]
    trace = [{'step': n, 'plane_action': [[str(v) for v in row] for row in P],
              'six_slot_real_plane_frame': [[str(v) for v in row] for row in mm(U, P)]}
             for n, P in enumerate(powers)]
    paths = [Path(__file__), Path(source.__file__), Path(photon.__file__),
             ROOT / 'research/voevodsky/checkers/evolve_relative_geometry_modes.py']
    report = {'status': 'passed' if all(checks.values()) else 'failed', 'checks': checks,
        'operator_conjecture': 'Photon has alternating ordinary/complex halves; one filled triangle and one unfilled partner exchange roles each assembly cycle; possibly one triangle plus one complex arrow.',
        'tested_step': 'actual endpoint continuation K restricted to the existing photon candidate plane; not physical time',
        'trace': trace, 'grading_equation_rank': rank(equations),
        'disposition': {
            'alternating_two_sector_source_cycle': 'refuted on this candidate: T has order three; no nonzero linear swapped grading',
            'whole_triangle_real_imaginary_split': 'refuted for the existing eigenmode and any nonzero common complex amplitude',
            'one_complex_arrow': 'one complex coordinate can encode the declared REAL plane with U and labels retained; not a derived structural arrow or face filler',
            'full_complexified_pair': 'one complex-linear scalar loses information',
            'filled_unfilled': 'not identified by real/imaginary coefficients; no such exchange constructor supplied by tested operations',
            'different_cycle': 'encode/decode representation steps are not the order-three continuation; a different source-defined operation could reopen the conjecture'},
        'source_hashes': {str(p.relative_to(ROOT)).replace('\\', '/'): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
    dest = ROOT / 'research/strominger/results/photon_alternating_halves.json'
    dest.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'status': report['status'], 'checks': checks, 'disposition': report['disposition']}, indent=2))
    if not all(checks.values()):
        raise SystemExit(1)


if __name__ == '__main__':
    main()

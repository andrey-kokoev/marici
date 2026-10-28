"""Source-defined four-point invariant and exact factorization/rank hostiles."""
import json
import sys
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT/'research/benincasa/checkers'), str(ROOT/'research/nima')]
from check_history6_twistor_cross_ratio import cross_ratio, symbolic_incidence
from check_history6_projection_descent import s, EPS, twistors, ratio, localize, incidence
from momentum_twistor_constructors import four_bracket, line_plane_point
from nnmhv_coherence_paths import compile_nnmhv_histories, supports_component_23
from dual_spinor_kinematics import x_interval, adjugate2

PATHS = [
    'research/benincasa/checkers/check_history6_twistor_cross_ratio.py',
    'research/benincasa/checkers/check_history6_projection_descent.py',
    'research/benincasa/checkers/check_history6_endpoint_boundary.py',
    'research/benincasa/checkers/check_untransported_simple_root_candidate.py',
    'research/nima/momentum_twistor_constructors.py',
    'research/nima/dual_spinor_kinematics.py',
    'research/nima/dual_r_invariant.py',
    'research/nima/nnmhv_coherence_paths.py',
    'research/nima/source-projective-bridge-protocol.md',
    'research/nima/checkers/check_source_projective_bridge.py',
]


def require(ok, why):
    if not ok:
        raise ValueError(why)


def hashes():
    return {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in PATHS}


def det_rows(a, b):
    return s.factor(s.Matrix.vstack(a, b).det())


def four_point(points):
    A, B, W, Q = points
    require(all(p != s.zeros(1, 2) for p in points), 'zero projective representative')
    denominator = det_rows(A, W)*det_rows(B, Q)
    require(denominator != 0, 'collapsed cross-ratio denominator')
    return s.factor(det_rows(A, B)*det_rows(W, Q)/denominator)


def transport(x, vertices):
    M = s.eye(2)
    for k, (a, b) in enumerate(zip(vertices, vertices[1:])):
        X = x_interval(x, a, b)
        M = M*(X if k % 2 == 0 else adjugate2(X))
    return M.applyfunc(s.factor)


def main():
    pins = hashes()
    symbolic = symbolic_incidence()  # Existing symbolic proof, no owner output writes.
    records = compile_nnmhv_histories(8)
    h6 = records[6]
    require(supports_component_23(h6), 'history6 outside selected source')
    pair = (h6.inner_pair[1]-4, h6.outer_pair[1]-4)
    require(pair == (2, 2), 'history6 interval boundary')
    fixtures, rank_rows = [], []
    inverse_cases, collapsed_cases = 0, 0
    for shift in range(3):
        Z, lam, x = twistors(shift)
        source, factors = ratio(lam, x)
        locality = localize(lam, x)
        br = lambda *labels: four_bracket(*(Z[j] for j in labels))
        W = line_plane_point(Z[5], Z[6], Z[8], Z[1], Z[2])
        Q = line_plane_point(Z[5], Z[6], Z[1], Z[2], Z[3])
        # The spinor projection is an invertible coordinate map on this line.
        require(s.Matrix.hstack(lam[5], lam[6]).det() != 0, 'line projection singular')
        points = [V[:2, 0].T*EPS for V in (Z[5], Z[6], W, Q)]
        intrinsic = cross_ratio(Z)
        require(s.factor(four_point(points)-intrinsic) == 0 and intrinsic == source, 'source/line invariant mismatch')
        require(all(det_rows(a, b) != 0 for i, a in enumerate(points) for b in points[i+1:]), 'four distinct points')
        require(s.factor(1-br(6,8,1,2)*br(5,1,2,3)/(br(5,8,1,2)*br(6,1,2,3))-source) == 0, 'bracket identity')
        for M in (s.Matrix([[2, 1], [1, 1]]), s.diag(2, 3), s.Matrix([[0, 1], [-1, 0]])):
            require(four_point([p*M for p in points]) == source, 'line frame invariance')
        require(four_point([(j+2)*p for j, p in enumerate(points)]) == source, 'representative invariance')
        G = s.eye(4); G[0, 2] = 2; G[1, 3] = 2
        zz = {j: G*Z[j] for j in Z}
        ll, xx = incidence(zz)
        localize(ll, xx)
        require(cross_ratio(zz) == ratio(ll, xx)[0] == source, 'common projective frame mismatch')
        # Every selected prefix, not just history6, in these frozen fixtures.
        for index, history in enumerate(records):
            if not supports_component_23(history):
                continue
            vertices = (8,)+history.inner_prefix
            M = transport(x, vertices)
            rank = M.rank()
            transformed = [p*M for p in points]
            if rank == 2:
                require(four_point(transformed) == source, 'rank-two transport invariant')
                inverse_cases += 1
                status = 'invariant'
            else:
                require(rank == 1, 'unexpected zero transport')
                require(all(det_rows(a, b) == 0 for i, a in enumerate(transformed) for b in transformed[i+1:]), 'rank-one image not collapsed')
                try:
                    four_point(transformed)
                except ValueError:
                    pass
                else:
                    raise AssertionError('singular transport assigned a cross-ratio')
                collapsed_cases += 1
                status = 'undefined_after_collapse'
            rank_rows.append({'shift': shift, 'history_index': index, 'interval': [history.inner_pair[1]-4, history.outer_pair[1]-4],
                              'prefix': list(vertices), 'rank': rank, 'status': status})
        fixtures.append({'shift': shift, 'interval': list(pair), 'source_c6': str(source),
                         'line_cross_ratio': str(four_point(points)), 'source_factors': factors,
                         'source_localization': locality})
    require(len({r['source_c6'] for r in fixtures}) == 3, 'record factorization hostile failed')
    require(inverse_cases > 0 and collapsed_cases > 0, 'both rank strata required')
    require(hashes() == pins, 'source drift')
    out = {'schema': 'marici.nima.source-projective-bridge.v1', 'passed': True,
           'verdict': 'source_line_invariant_constructed_bare_record_factorization_and_universal_group_action_rejected',
           'symbolic_source_identity': symbolic['symbolic_source_minus_intrinsic'],
           'history_index': 6, 'interval': list(pair), 'metric_visible': False,
           'four_points': ['Z5', 'Z6', '(56) intersect (812)', '(56) intersect (123)'],
           'fixtures': fixtures, 'selected_prefix_transports': rank_rows,
           'rank_two_cases': inverse_cases, 'rank_one_cases': collapsed_cases,
           'native_endpoint_PSL_action_derived': False,
           'scope': 'Invariant of enriched kinematic line data; not a function of the bare interval record, not a curvature/continuum derivation. Prefix test is row-covector linear action, not an asserted full native action on the line packet.',
           'source_sha256': pins}
    (ROOT/'research/nima/results/source-projective-bridge.json').write_text(json.dumps(out, indent=2)+'\n', encoding='utf-8')
    summary = {k: v for k, v in out.items() if k not in ('source_sha256', 'selected_prefix_transports', 'fixtures')}
    summary['coefficients'] = [r['source_c6'] for r in fixtures]
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()

"""Exact chain/prism and Hodge-type controls for a cycle-supplied dictionary.
Triangulation, cycle-class, elliptic uniformization and duality facts are imported.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations
from hashlib import sha256
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = ROOT / 'research/conjecture_net/contracts/hodge-cycle-packet-dictionary.v1.json'
NOTE = ROOT / 'research/voevodsky/hodge-cycle-packet-dictionary-v1.md'
OUT = ROOT / 'research/voevodsky/results/hodge-cycle-packet-dictionary-v1.json'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def clean(chain):
    return {simplex: coefficient for simplex, coefficient in chain.items() if coefficient}


def put(chain, simplex, coefficient):
    if len(set(simplex)) != len(simplex):
        return
    inversions = sum(simplex[i] > simplex[j] for i in range(len(simplex)) for j in range(i + 1, len(simplex)))
    key = tuple(sorted(simplex))
    chain[key] += coefficient * (-1) ** inversions


def boundary(chain):
    result = Counter()
    for simplex, coefficient in chain.items():
        if len(simplex) > 1:
            for i in range(len(simplex)):
                put(result, simplex[:i] + simplex[i + 1:], coefficient * (-1) ** i)
    return clean(result)


def add(a, b, sign=1):
    result = Counter(a)
    for simplex, value in b.items():
        result[simplex] += sign * value
    return clean(result)


def cross(a, b, second_vertices):
    result = Counter()
    for x, cx in a.items():
        for y, cy in b.items():
            p, q = len(x) - 1, len(y) - 1
            for positions in combinations(range(p + q), p):
                a_steps = set(positions)
                # Each B-before-A interchange contributes a Koszul sign.
                inversions = sum(position - i for i, position in enumerate(positions))
                i = j = 0
                vertices = [x[0] * second_vertices + y[0]]
                for step in range(p + q):
                    if step in a_steps:
                        i += 1
                    else:
                        j += 1
                    vertices.append(x[i] * second_vertices + y[j])
                put(result, tuple(vertices), cx * cy * (-1) ** inversions)
    return clean(result)


def lift(chain, side):
    return {tuple(2 * v + side for v in simplex): coefficient for simplex, coefficient in chain.items()}


def prism(chain):
    result = Counter()
    for simplex, coefficient in chain.items():
        for i in range(len(simplex)):
            vertices = tuple(2 * v for v in simplex[:i + 1]) + tuple(2 * v + 1 for v in simplex[i:])
            put(result, vertices, coefficient * (-1) ** i)
    return clean(result)


def f_vector(chain):
    dimension = len(next(iter(chain))) - 1
    return [len({face for simplex in chain for face in combinations(simplex, k + 1)}) for k in range(dimension + 1)]


def validate_dictionary(c):
    require(c['schema'] == 'marici.hodge-cycle-packet-dictionary.v1', 'dictionary schema')
    require(c['node'] == 'packet-coherence-dictionary' and
            c['resolution_kind'] == 'cycle_supplied_fundamental_chain_dictionary_and_necessity_lemma', 'dictionary binding')
    require(set(c['objects']) == {'Z', 'P_alg', 'P_top', 'C', 'H'}, 'typed object inventory')
    require({m['id'] for m in c['maps']} == {'support', 'chain', 'forget', 'homology'}, 'map inventory')
    require(c['positive_example']['complex_codimension_Z'] == 2 and c['positive_example']['top_dimensional_simplices'] == 96, 'positive scope')
    require(c['negative_example']['Hodge_type_p_p'] is c['negative_example']['counterexample_to_Hodge'] is False, 'non-Hodge control promoted')
    require(c['rejected_candidate']['id'] == 'bare-chain-closure-obstruction' and c['rejected_candidate']['verdict'] == 'rejected', 'closure-only rejection lost')
    require(len(c['boundary']) == 6 and all(v is False for v in c['boundary'].values()), 'dictionary scope promoted')


def report():
    c = json.loads(CONTRACT.read_text(encoding='utf-8'))
    validate_dictionary(c)
    sphere = boundary({(0, 1, 2, 3): 1})
    circle = boundary({(0, 1, 2): 1})
    require(not boundary(sphere) and not boundary(circle), 'source cycles')
    surface = cross(sphere, sphere, 4)
    torus = cross(circle, circle, 3)
    require(len(surface) == 96 and len(torus) == 18, 'shuffle census')
    require(not boundary(surface) and not boundary(torus), 'codimension-one cancellation')
    # Leibniz on nonclosed source simplices, not merely closed-cycle samples.
    for p in range(3):
        for q in range(3):
            a, b = {tuple(range(p + 1)): 1}, {tuple(range(q + 1)): 1}
            actual = boundary(cross(a, b, q + 1))
            expected = add(cross(boundary(a), b, q + 1), cross(a, boundary(b), q + 1), (-1) ** p)
            require(actual == expected, 'cross-product boundary law')
    for chain in (sphere, circle, surface, torus, {(0, 1, 2): 1}, {(0, 1): 1}):
        require(not boundary(boundary(chain)), 'boundary squared')
        require(add(boundary(prism(chain)), prism(boundary(chain))) == add(lift(chain, 1), lift(chain, 0), -1), 'prism comparison')
    broken = dict(surface)
    broken.pop(next(iter(broken)))
    require(bool(boundary(broken)), 'missing-face hostile')
    unsigned = {simplex: 1 for simplex in surface}
    require(bool(boundary(unsigned)), 'orientation erasure hostile')
    sf, tf = f_vector(surface), f_vector(torus)
    require(sf == [16, 84, 216, 240, 96] and sum((-1) ** i * n for i, n in enumerate(sf)) == 4, 'surface cell structure')
    require(tf == [9, 27, 18] and sum((-1) ** i * n for i, n in enumerate(tf)) == 0, 'torus cell structure')

    # E_i^2 real coordinates (x1,y1,x2,y2). J*dx=-dy, J*dy=dx.
    # For a real degree-two class, type (1,1) is precisely J* invariance.
    alpha = {(1, 3): Q(-1)}
    pullback = {0: (1, -1), 1: (0, 1), 2: (3, -1), 3: (2, 1)}
    Jalpha = Counter()
    for (a, b), value in alpha.items():
        i, si = pullback[a]
        j, sj = pullback[b]
        Jalpha[tuple(sorted((i, j)))] += value * si * sj * (1 if i < j else -1)
    require(alpha != dict(Jalpha), 'non-Hodge negative control')
    # Compute in basis (dz1,dz2,dzbar1,dzbar2), complex scalars (real,imag).
    dy1 = {0: (Q(0), Q(-1, 2)), 2: (Q(0), Q(1, 2))}
    dy2 = {1: (Q(0), Q(-1, 2)), 3: (Q(0), Q(1, 2))}
    expansion = {}
    for i, a in dy1.items():
        for j, b in dy2.items():
            sign = -1 if i < j else 1  # Overall minus in -dy1 wedge dy2.
            expansion[tuple(sorted((i, j)))] = (sign * (a[0] * b[0] - a[1] * b[1]),
                                                sign * (a[0] * b[1] + a[1] * b[0]))
    holomorphic_coefficient = expansion[(0, 1)][0]
    require(expansion[(0, 1)] == expansion[(2, 3)] == (Q(1, 4), Q(0)), 'Hodge component hostile')
    # Orientation: (-dy1 dy2) wedge (dx1 dx2) integrates to +1.
    permutation = (1, 3, 0, 2)
    inversion_count = sum(permutation[i] > permutation[j] for i in range(4) for j in range(i + 1, 4))
    require(-(-1) ** inversion_count == 1, 'Poincare dual sign')
    # All six middle classes of (P1)^4 are algebraic coordinate surfaces.
    bases = tuple(combinations(range(4), 2))
    pairing = [[int(not set(a) & set(b)) for b in bases] for a in bases]
    require(all(sum(row) == 1 for row in pairing), 'coordinate-cycle complementary pairing')
    require(all(sum(pairing[i][k] * pairing[k][j] for k in range(6)) == int(i == j) for i in range(6) for j in range(6)), 'middle pairing nondegeneracy')

    checks = {
        'actual_cycle_supplied_dictionary_keeps_source_generation_distinct': True,
        'codimension_two_algebraic_surface_has_96_closed_oriented_four_simplices': True,
        'shuffle_cross_product_obeys_boundary_leibniz_in_nine_bidegrees': True,
        'simplicial_prism_comparison_holds_on_open_and_closed_chains': True,
        'missing_face_and_erased_orientation_have_nonzero_boundary': True,
        'surface_and_torus_cell_censuses_have_correct_euler_characteristics': True,
        'closed_real_torus_has_rational_non_p_p_class_not_hodge_counterexample': True,
        'dual_orientation_and_nonzero_holomorphic_component_are_retained': True,
        'six_algebraic_middle_coordinate_surfaces_have_nondegenerate_pairing': True,
    }
    return {
        'schema': 'marici.hodge-cycle-packet-dictionary-result.v1', 'passed': all(checks.values()), 'checks': checks,
        'resolution_kind': c['resolution_kind'],
        'verification_level': 'Written necessity and closure-only no-go proofs using declared imported geometry; exact finite shuffle, prism and Hodge-type controls. Not proof-assistant formalization.',
        'positive_surface_f_vector': sf, 'negative_torus_f_vector': tf,
        'prism_four_chain_top_simplex_count': len(prism(surface)),
        'negative_class': '-dy1 wedge dy2', 'negative_class_holomorphic_coefficient': str(holomorphic_coefficient),
        'bare_chain_closure_candidate_verdict': 'rejected',
        'full_algebraic_packet_source_generated': False, 'general_higher_coherence_constructed': False,
        'Hodge_proved': False, 'Hodge_refuted': False, 'specific_hodge_obstruction_constructed': False,
        'source_sha256': {p.relative_to(ROOT).as_posix(): sha256(p.read_bytes()).hexdigest()
                          for p in (CONTRACT, NOTE, Path(__file__).resolve())},
    }


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k != 'source_sha256'}, indent=2))

#!/usr/bin/env python3
"""Exact finite q2 flag test and ordinary local-collar mapping calculation.

Standard library only. The source reference supplies labels, signs, and the
local collar; the code independently enumerates the hexagon. It does not
construct a physical support-PC or reciprocal/BM correspondence.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from collections import Counter
from itertools import combinations
from pathlib import Path
from typing import Mapping

VARIABLES = ('X03', 'x0', 'x1', 'x2', 'x3', 'x4', 'x5', 'X14', 'X25', 'U03')
M = len(VARIABLES)
Monomial = tuple[int, ...]
Poly = dict[Monomial, int]
ZERO: Poly = {}
ONE: Poly = {(0,) * M: 1}
COUNT = 0


def check(condition: bool, description: str) -> None:
    global COUNT
    COUNT += 1
    if not condition:
        raise AssertionError(description)


def const(a: int) -> Poly:
    return {(0,) * M: a} if a else {}


def var(name: str, power: int = 1) -> Poly:
    p = [0] * M
    p[VARIABLES.index(name)] = power
    return {tuple(p): 1}


def add(*args: Mapping[Monomial, int]) -> Poly:
    out: Counter = Counter()
    for arg in args:
        for p, a in arg.items():
            out[p] += a
    return {p: a for p, a in out.items() if a}


def scale(a: int, f: Poly) -> Poly:
    return {p: a * b for p, b in f.items() if a * b}


def mul(f: Poly, g: Poly) -> Poly:
    out: Counter = Counter()
    for p, a in f.items():
        for q, b in g.items():
            out[tuple(i + j for i, j in zip(p, q))] += a * b
    return {p: a for p, a in out.items() if a}


def mod_variable(f: Poly, name: str) -> Poly:
    i = VARIABLES.index(name)
    if any(p[i] < 0 for p in f):
        raise ValueError('Cannot specialize an inverted variable to zero.')
    return {p: a for p, a in f.items() if p[i] == 0}


def quotient_monomial(f: Poly, denominator: Poly) -> Poly:
    if len(denominator) != 1:
        raise ValueError('A single positive monomial is required.')
    (q, b), = denominator.items()
    if b != 1:
        raise ValueError('A labelled monic generator is required.')
    if any(any(i < j for i, j in zip(p, q)) for p in f):
        raise ValueError('Not divisible in the polynomial ring.')
    return {tuple(i - j for i, j in zip(p, q)): a for p, a in f.items()}


def fmt(f: Poly) -> str:
    if not f:
        return '0'
    terms = []
    for p, a in sorted(f.items(), reverse=True):
        mon = '*'.join(name if k == 1 else f'{name}^{k}'
                       for name, k in zip(VARIABLES, p) if k)
        terms.append(f'{a}*{mon}' if mon else str(a))
    return ' + '.join(terms).replace('+ -', '- ')


def matmul(A: list[list[Poly]], B: list[list[Poly]]) -> list[list[Poly]]:
    if not A or not B or len(A[0]) != len(B):
        raise ValueError('Nonempty compatible matrices required.')
    return [[add(*(mul(a, b) for a, b in zip(row, col)))
             for col in zip(*B)] for row in A]


def diagonal(i: int, j: int) -> tuple[int, int]:
    return tuple(sorted((i % 6, j % 6)))


DIAGONALS = tuple((i, j) for i in range(6) for j in range(i + 1, 6)
                 if j != i + 1 and (i, j) != (0, 5))
SHORT = {i: diagonal(i, i + 2) for i in range(6)}
LABEL = {SHORT[i]: f'x{i}' for i in range(6)}
LABEL.update({(0, 3): 'X03', (1, 4): 'X14', (2, 5): 'X25'})
Face = frozenset[tuple[int, int]]


def crosses(d: tuple[int, int], e: tuple[int, int]) -> bool:
    a, b = d
    c, f = e
    return a < c < b < f or c < a < f < b


def face_name(face: Face) -> list[str]:
    return [LABEL[d] for d in sorted(face)]


def product_label(face: Face) -> Poly:
    f = dict(ONE)
    for d in face:
        f = mul(f, var(LABEL[d]))
    return f


def incidence(F: Face, G: Face) -> tuple[int, Poly]:
    if not F < G or len(G) != len(F) + 1:
        raise ValueError('A saturated face-label inclusion is required.')
    d, = G - F
    sign = (-1) ** sum(a < d for a in F)
    coefficient = quotient_monomial(product_label(G), product_label(F))
    return sign, coefficient


def geometric_audit() -> dict:
    faces = tuple(frozenset(c) for k in range(4)
                  for c in combinations(DIAGONALS, k)
                  if all(not crosses(d, e) for d, e in combinations(c, 2)))
    Fset = set(faces)
    tris = tuple(f for f in faces if len(f) == 3)
    check(tuple(sum(len(f) == k for f in faces) for k in range(4)) == (1, 9, 21, 14),
          'Hexagon face census')
    check(sum(2 ** len(f) for f in faces) == 215, 'Loaded generator census')
    for f in faces:
        for k in range(len(f) + 1):
            for s in combinations(f, k):
                check(frozenset(s) in Fset, 'Face-set downward closure')

    # Polynomial occurrence differential: codimension-one insertion.
    differentials = {}
    for f in faces:
        differentials[f] = {}
        for d in DIAGONALS:
            g = f | {d}
            if d not in f and g in Fset:
                sign, a = incidence(f, g)
                differentials[f][g] = scale(sign, a)
    for f in faces:
        twice: dict[Face, Poly] = {}
        for g, a in differentials[f].items():
            for h, b in differentials[g].items():
                twice[h] = add(twice.get(h, {}), mul(a, b))
        check(not any(twice.values()), 'Actual weighted incidence d squared')

    road = frozenset({(0, 3)})
    vp = frozenset({SHORT[1], SHORT[3], SHORT[5]})
    q0 = frozenset({SHORT[5]})
    q2 = frozenset({SHORT[1]})
    e3 = q0 | q2
    ec = frozenset({SHORT[1], SHORT[3]})
    Z3 = road | {SHORT[3]}
    road_vertices = tuple(v for v in tris if road <= v)
    check(len(road_vertices) == 4, 'Four road vertices')
    flips = tuple(v for v in road_vertices if (v - road | q0) == vp)
    check(len(flips) == 1, 'Unique fixed central flip')
    v10, = flips
    check(v10 == road | {SHORT[1], SHORT[3]}, 'Central flip labels')
    flags = tuple((ed, v) for ed in faces if len(ed) == 2 and road <= ed
                  for v in road_vertices if ed <= v)
    check(len(flags) == 8, 'All saturated road flags')
    selected = tuple((ed, v) for ed, v in flags if ed == Z3 and v == v10)
    check(len(selected) == 1, 'Unique inherited marked road flag')
    check(not any(q0 <= v for v in road_vertices), 'q0 facet misses F03')
    q2_vertices = tuple(v for v in road_vertices if q2 <= v)
    check(len(q2_vertices) == 2, 'q2 facet meets F03 along an edge')
    endpoint_q2_flags = tuple(ed for ed in faces if len(ed) == 2 and q2 <= ed <= vp)
    check(len(endpoint_q2_flags) == 2, 'Two q2 flags before terminal marking')
    marked_q2_flags = tuple(ed for ed in endpoint_q2_flags if SHORT[5] in ed)
    check(marked_q2_flags == (e3,), 'x5 endpoint mark forces e3')

    trunk = (road, Z3, v10, ec, vp, e3)
    routes = {}
    for name, endpoint in [('q0', q0), ('q2', q2)]:
        route = trunk + (endpoint,)
        for f, g in zip(route, route[1:]):
            check((f < g or g < f) and abs(len(f) - len(g)) == 1,
                  'Every route arrow is an actual saturated incidence')
        routes[name] = [face_name(f) for f in route]

    sign1, mult1 = incidence(road, Z3)
    sign2, mult2 = incidence(Z3, v10)
    top_product = scale(sign1 * sign2, mul(mult1, mult2))
    b = quotient_monomial(top_product, var('x3'))
    check(top_product == mul(var('x1'), var('x3')), 'Derived selected road product')
    check(b == var('x1'), 'First-normal evaluation retains x1')
    flag_inventory = []
    for ed, v in flags:
        s, m = incidence(road, ed)
        t, p = incidence(ed, v)
        value = scale(s * t, mul(m, p))
        check(all(exp[VARIABLES.index('x5')] == 0 for exp in value),
              'No road flag has an x5 occurrence factor')
        flag_inventory.append({'edge': face_name(ed), 'vertex': face_name(v),
                               'signed_coefficient': fmt(value)})

    symmetry_swaps = []
    fixed_road_swaps = []
    for reflection in (0, 1):
        for offset in range(6):
            def action(f: Face) -> Face:
                return frozenset(diagonal(offset + (-1) ** reflection * a,
                                          offset + (-1) ** reflection * b) for a, b in f)
            for f in faces:
                check(action(f) in Fset, 'Dihedral action preserves all faces')
            if action(road) == road and action(q0) == q2:
                fixed_road_swaps.append((offset, reflection))
            if action(vp) == vp and action(frozenset({SHORT[3]})) == frozenset({SHORT[3]}) and action(q0) == q2:
                symmetry_swaps.append({'offset': offset, 'reflection': reflection,
                                       'road_image': face_name(action(road))})
    check(fixed_road_swaps == [], 'No F03 stabilizer exchanges these endpoint facets')
    check(symmetry_swaps == [{'offset': 2, 'reflection': 1, 'road_image': ['X25']}],
          'Mark-preserving endpoint reflection changes the road to F25')

    return {'face_counts': [1, 9, 21, 14], 'loaded_generators': 215,
            'routes': routes, 'road_flags': flag_inventory,
            'road_prefix_product': fmt(top_product), 'b0_flag': fmt(b), 'b2_flag': fmt(b),
            'q2_endpoint_flags': [face_name(f) for f in endpoint_q2_flags],
            'mark_preserving_endpoint_swap': symmetry_swaps,
            'same_road_endpoint_swap': fixed_road_swaps}


def endpoint_equations() -> dict:
    x1, x5 = var('x1'), var('x5')
    d1 = [[x5, x1]]
    d2 = [[scale(-1, x1)], [x5]]
    check(matmul(d1, d2) == [[ZERO]], 'Full Koszul hull d squared')
    a0, a2 = const(-1), ONE
    b0 = b2 = x1
    defect0 = add(b0, mul(x1, a0))
    defect2 = add(b2, scale(-1, mul(x5, a2)))
    check(defect0 == ZERO, 'q0 coefficient equation')
    check(defect2 == add(x1, scale(-1, x5)), 'q2 primitive flag defect')
    check(mod_variable(defect2, 'x5') == x1, 'Obstruction is nonzero modulo x5')
    check(mod_variable(mod_variable(defect2, 'x5'), 'x1') == ZERO,
          'Premature central specialization erases this obstruction')

    # All-degree classification is proved in the note by polynomial
    # divisibility. These exact instances check the resulting identities.
    samples = [ZERO, ONE, const(-2), x1, x5, var('X03'),
               add(ONE, x1, scale(-2, x5), mul(x1, x5))]
    for h in samples:
        g = mul(x5, h)
        a0 = scale(-1, g)
        a2 = mul(x1, h)
        check(add(mul(g, b0), mul(x1, a0)) == ZERO, 'General first equation')
        check(add(mul(g, b2), scale(-1, mul(x5, a2))) == ZERO, 'General second equation')
    # No orientation change fixes polynomial divisibility.
    for source_sign in (-1, 1):
        for endpoint_sign in (-1, 1):
            defect = add(scale(source_sign, x1), scale(-endpoint_sign, x5))
            check(mod_variable(defect, 'x5') == scale(source_sign, x1),
                  'Orientation cannot erase x5-divisibility failure')
    return {'koszul_d2': ['-x1', 'x5'], 'koszul_d1': ['x5', 'x1'],
            'primitive_endpoint_coefficients': [-1, 1],
            'defects': [fmt(defect0), fmt(defect2)],
            'obstruction_module': 'R/(x5)', 'obstruction_class': 'x1 mod x5 != 0',
            'all_diagonal_solutions_in_fixed_flag_target':
                '(g,a0,a2)=(x5*h,-x5*h,x1*h)',
            'generic_unit_solution_exists': False}


Combination = dict[str, Poly]


def cadd(*xs: Combination) -> Combination:
    out: Combination = {}
    for xs1 in xs:
        for b, a in xs1.items():
            out[b] = add(out.get(b, ZERO), a)
    return {b: a for b, a in out.items() if a}


def extend_map(value: Combination, rule: dict[str, Combination]) -> Combination:
    out: Combination = {}
    for source, coefficient in value.items():
        for target, multiplier in rule.get(source, {}).items():
            out[target] = add(out.get(target, ZERO), mul(coefficient, multiplier))
    return {b: a for b, a in out.items() if a}


def collar_audit() -> dict:
    x1, x5, X, U = var('x1'), var('x5'), var('X03'), var('U03')
    inverse_U = var('U03', -1)
    dP = {'e3': {'q0': scale(-1, x1), 'q2': x5},
          'q0': {'a': x5}, 'q2': {'a': x1}}
    dC = {'k': {'p': mul(X, inverse_U)}, 'n': {'p': ONE}}
    f = {'e3': {'p': ONE}}
    h = {'e3': {'n': ONE}}
    for basis in ('e3', 'q0', 'q2', 'a'):
        v = {basis: ONE}
        check(extend_map(extend_map(v, dP), dP) == {}, 'Full source d squared')
        check(extend_map(extend_map(v, f), dC) == extend_map(extend_map(v, dP), f),
              'Unit-coefficient map into ordinary collar is closed')
        boundary_h = cadd(extend_map(extend_map(v, h), dC),
                         extend_map(extend_map(v, dP), h))
        check(boundary_h == extend_map(v, f), 'Explicit nullhomotopy f=dH+Hd')

    cycle = {'k': U, 'n': scale(-1, X)}
    check(extend_map(cycle, dC) == {}, 'Unlocalized top cycle U*k-X*n')
    check(extend_map({'n': ONE}, dC) == {'p': ONE}, 'p is an ordinary boundary')
    check(extend_map({'k': ONE}, dC) == {'p': mul(X, inverse_U)},
          'X/U times p is an ordinary boundary')
    for generator in ('k', 'n'):
        for a in dC[generator].values():
            check(all(p[-1] >= -1 for p in a), 'Only permitted target pole')
    # A residue projection certifies the 1/U class against all homotopies:
    # set x1=x5=X=0, retain negative powers of U. Images of n are regular;
    # images of k and of source differentials vanish under this projection.
    def witness(a: Poly) -> Poly:
        for variable in ('x1', 'x5', 'X03'):
            a = mod_variable(a, variable)
        return {p: c for p, c in a.items() if p[-1] < 0}
    check(witness(inverse_U) == inverse_U, 'Nonzero pole witness')
    samples = [ONE, x1, x5, X, U, mul(U, U), add(ONE, X, x1)]
    for a in samples:
        check(witness(a) == ZERO, 'Regular normal homotopies vanish under witness')
        check(witness(mul(mul(X, inverse_U), a)) == ZERO,
              'Generic-top homotopies vanish under witness')
    for k in range(-4, 4):
        for a in (ONE, X, x1, x5):
            pole = mul(var('U03', k), a)
            check(witness(mul(x1, pole)) == ZERO, 'q0 homotopy witness')
            check(witness(mul(x5, pole)) == ZERO, 'q2 homotopy witness')
    return {'degrees': {'e3': 2, 'q0': 1, 'q2': 1, 'a': 0,
                        'k': 3, 'n': 3, 'p': 2},
            'collar_terms': 'R*k + R*n -> R[U03^-1]*p',
            'collar_differential': '[X03/U03,1]',
            'unit_map': 'e3->p, q0,q2,a->0',
            'unit_map_nullhomotopy': 'H(e3)=n; H(q0)=H(q2)=H(a)=0',
            'ordinary_mapping_classes':
                'R[U03^-1]/(R+(X03/U03)*R+(x1,x5)*R[U03^-1])',
            'nonzero_control': '[U03^-1*p]',
            'control_annihilators': ['x1', 'x5', 'X03', 'U03'],
            'physical_relative_identification': 'NOT CONSTRUCTED'}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path,
                        default=Path('branch_a_q2_completion_certificate.json'))
    args = parser.parse_args()
    geometry = geometric_audit()
    equations = endpoint_equations()
    collar = collar_audit()
    data = {'schema': 'marici.branch-a.q2-fixed-flag-test.v1',
            'source_commit': 'd1947b67a60d3e88ba77f4ca60ea02c2a306ee61',
            'source_blobs': {
              'check_d03_q0_endpoint_exit_flags.rs': '528fca153efcf4720f24016ee285cabaabe75d4e',
              'check_d03_q0_endpoint_relative_tor_lift.rs': 'f5b13df4421187c70e97b8625a2f1a76d2e12502',
              '20260815-174 Two-Edge Bivariant Trace and the Unlocalized Two-Flip Alignment Gate.md':
                'ae5d4fc93fa135e7dc0ee6088928f9b8f8cad405'},
            'geometric_audit': geometry, 'endpoint_equations': equations,
            'ordinary_collar_audit': collar, 'exact_assertions_passed': COUNT,
            'verdict': 'The direct fixed-F03 q2 continuation has no normalized diagonal polynomial lift.',
            'scope': ['Finite literal marked flags and necessary coefficient equations.',
                      'Ordinary local-collar mapping problem with displayed degree placement.',
                      'No claim that this is the full source-relative physical obstruction.',
                      'No source or target generator was deleted; no source coefficient inverted.',
                      'No repository changes.'],
            'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'assertions': COUNT, 'verdict': data['verdict'],
                      'certificate': str(args.output)}, indent=2))


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Exact controls for the proposed Marici framed target.

This checks the supplied four-generator contraction and a finite mapping-fibre
model. It does not construct a physical Gysin map or compute a physical class.
Python standard library only.
"""
from __future__ import annotations
import argparse
import json
from collections import Counter
from pathlib import Path

# Sparse integral combinations of x**power times a basis generator.
Vector = dict[tuple[str, int], int]
CHECKS: Counter[str] = Counter()

def check(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)
    CHECKS[label] += 1

def add(a: Vector, b: Vector, scale: int = 1) -> Vector:
    result = dict(a)
    for key, value in b.items():
        result[key] = result.get(key, 0) + scale * value
        if result[key] == 0:
            del result[key]
    return result

def extend(table: dict[str, Vector], value: Vector) -> Vector:
    result: Vector = {}
    for (generator, power), coefficient in value.items():
        for (target, shift), multiplier in table[generator].items():
            key = (target, power + shift)
            result[key] = result.get(key, 0) + coefficient * multiplier
    return {key: coefficient for key, coefficient in result.items() if coefficient}

D: dict[str, Vector] = {
    'H': {('q', 0): 1, ('xi', 1): -1},
    'q': {('b', 1): 1},
    'xi': {('b', 0): 1},
    'b': {},
}
S: dict[str, Vector] = {
    'H': {}, 'q': {('H', 0): 1}, 'xi': {}, 'b': {('xi', 0): 1},
}
DEGREE = {'H': 2, 'q': 1, 'xi': 1, 'b': 0}


def contraction_control() -> dict:
    for generator in D:
        check(all(DEGREE[t] == DEGREE[generator] - 1 for t, _ in D[generator]),
              'd_degree')
        check(all(DEGREE[t] == DEGREE[generator] + 1 for t, _ in S[generator]),
              's_degree')
        for power in range(9):
            value = {(generator, power): 1}
            check(extend(D, extend(D, value)) == {}, 'd_squared')
            check(add(extend(D, extend(S, value)), extend(S, extend(D, value))) == value,
                  'ds_plus_sd_identity')
            check(extend(S, extend(S, value)) == {}, 's_squared')
            check(all(k >= power for _, k in extend(S, value)), 'uniform_x_filtration')
    for generator in ('xi', 'b'):
        check(all(t in ('xi', 'b') for t, _ in D[generator]), 'road_subcomplex')
        check(all(t in ('xi', 'b') for t, _ in S[generator]), 'road_contraction_preserved')
    # The finer endpoint support is a distinct, geometrically motivated test.
    check(D['b'] == {}, 'endpoint_subcomplex')
    check(any(t != 'b' for t, _ in S['b']), 's_fails_endpoint_support')
    # The quotient by <xi,b> has differential H -> q and contraction q -> H.
    def quotient(v: Vector) -> Vector:
        return {key: a for key, a in v.items() if key[0] in ('H', 'q')}
    check(quotient(D['H']) == {('q', 0): 1}, 'Q_unit_differential')
    check(quotient(S['q']) == {('H', 0): 1}, 'Q_contraction')
    return {
        'dH': 'q-x*xi', 'dq': 'x*b', 'dxi': 'b',
        's_q': 'H', 's_b': 'xi',
        'uniform_x_adic_filtration_excludes_s': False,
        'two_stage_road_filtration_excludes_s': False,
        'endpoint_subcomplex_Rb_is_preserved_by_s': False,
        'Q_after_road_quotient': '[R H --1--> R q]',
        'q_is_boundary_in_Q': True,
        'proof_scope': 'Identities are R-linear; monomial tests supplement the basis proof.',
    }


def relative_fibre_control() -> dict:
    # M^{-1}=Z e, M^0=Z f, d(e)=f.
    # N^{-1}=Z u, d=0, r(e)=m*u, r(f)=0.
    # F=Cone(r)[-1]: Z -> Z^2, s -> (s,m*s).
    # A class (a,h) has invariant h-m*a; it is zero iff h=m*a.
    for m in range(-4, 5):
        for a in range(-5, 6):
            for h in range(-5, 6):
                invariant = h - m*a
                # A nullhomotopy in the ordinary M always exists: s=a.
                s = a
                framed_boundary = (s, m*s)
                check(((a, h) == framed_boundary) == (invariant == 0),
                      'secondary_obstruction_criterion')
                check((0, invariant) == (a-s, h-m*s), 'subtract_ambient_primitive')
                for shift in (-2, 0, 3):
                    check((h+m*shift)-m*(a+shift) == invariant,
                          'relative_class_boundary_independence')
        # (a,h) -> (a,h-m*a) is unimodular for every integer m.
        check(1*1 - 0*(-m) == 1, 'unimodular_fibre_reduction')
    return {
        'M': 'Z[-1] --1--> Z[0]',
        'N': 'Z in cohomological degree -1',
        'r_minus_1': 'multiplication by m',
        'F': 'Z[-1] --(1,m)--> Z^2[0]',
        'H0_F': 'Z, with coordinate h-m*a',
        'ordinary_H0_M': '0',
        'all_other_fibre_cohomology': '0',
        'interpretation': 'Relative framing can retain a comparison class; this is a control, not a Marici result.',
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path,
                        default=Path('framed_target_category_certificate.json'))
    args = parser.parse_args()
    result = {
        'schema': 'marici.branch-a.framed-target-controls.v1',
        'source_commit': 'd1947b67a60d3e88ba77f4ca60ea02c2a306ee61',
        'mixed_contraction_control': contraction_control(),
        'mapping_fibre_control': relative_fibre_control(),
        'scope': [
            'Target-category specification and exact algebraic controls only.',
            'No full spatial support-PC functor or boundary-frame diagram is claimed constructed.',
            'No physical q_J survival, endpoint parity, or RH result is claimed.',
            'The endpoint-support failure concerns the displayed contraction, not a physical nonvanishing theorem.',
            'No repository files were modified.',
        ],
    }
    result['checks'] = dict(sorted(CHECKS.items()))
    result['total_checks'] = sum(CHECKS.values())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'total_checks': result['total_checks'], 'output': str(args.output)}, indent=2))

if __name__ == '__main__':
    main()

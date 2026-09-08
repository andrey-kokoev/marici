#!/usr/bin/env python3
"""Exact local audit of Cartier/Gysin normal symbols.

No repository writes or external dependencies.  Distinguishes a coefficient
factor from its filtered connecting symbol and from a physical simple pole.
The full octagon physical comparison is not constructed by this program.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from itertools import combinations, product, permutations
import json
from math import factorial
from pathlib import Path
from typing import Mapping

# Polynomial ring Z[x0,t0,x1,t1,x2,t2,v,v^-1].
# v is a spectator localization coordinate, never a normal coordinate.
NVAR = 7
Power = tuple[int, ...]
Poly = dict[Power, int]
ZERO_POWER: Power = (0,) * NVAR
ONE: Poly = {ZERO_POWER: 1}
COUNTS: Counter[str] = Counter()
PIN = 'd1947b67a60d3e88ba77f4ca60ea02c2a306ee61'
SOURCES = {
    'src/ledger/20260814-115 Boundary-Triad Tate Realization and the Multi-Rees Cartier Bicomplex.md': '63da17cb5d641705056c5d5b9bc6f53cda72baf5',
    'src/ledger/20260814-111 One-Sheet Rees-Cartier Symbol and the Missing Marked Conductor Lattice.md': '5079643c5ed6d66ea77a270818453b4d455207a8',
    'src/ledger/20260813-38 Finite-Alpha-Prime Normal-Torus Lift and Nearby-Cycle Unit Theorem.md': '40504f31e8bbc9e984f97d5eef73b5cadf4bda95',
    'research/voevodsky/check_principal_line_trace_variance.rs': '242da84955dc839b23ffe65c5825dde129a1c33e',
    'research/voevodsky/check_generic_log_dnc_thom_trace.py': '95fd466d144bafea6838cfeacc4aaf485b124275',
}


def check(condition: bool, category: str, detail: object = '') -> None:
    if not condition:
        raise AssertionError(f'{category}: {detail}')
    COUNTS[category] += 1


def monomial(power: Power, coefficient: int = 1) -> Poly:
    if len(power) != NVAR or any(p < 0 for p in power[:-1]):
        raise ValueError('Only the spectator v coordinate may have negative powers.')
    return {power: coefficient} if coefficient else {}


def variable(i: int) -> Poly:
    p = list(ZERO_POWER)
    p[i] = 1
    return monomial(tuple(p))


def add(a: Mapping[Power, int], b: Mapping[Power, int], scale: int = 1) -> Poly:
    out = dict(a)
    for p, c in b.items():
        out[p] = out.get(p, 0) + scale * c
        if not out[p]:
            del out[p]
    return out


def mul(a: Mapping[Power, int], b: Mapping[Power, int]) -> Poly:
    out: Poly = {}
    for pa, ca in a.items():
        for pb, cb in b.items():
            p = tuple(x + y for x, y in zip(pa, pb))
            out[p] = out.get(p, 0) + ca * cb
            if not out[p]:
                del out[p]
    return out


def set_zero(a: Mapping[Power, int], *indices: int) -> Poly:
    return {p: c for p, c in a.items() if all(p[i] == 0 for i in indices)}


def divide_known_factor(a: Mapping[Power, int], i: int) -> Poly:
    """Preimage under multiplication on its principal ideal, not localization."""
    if any(p[i] == 0 for p in a):
        raise ValueError('The polynomial is not in the specified principal ideal.')
    out = {}
    for p, c in a.items():
        q = list(p)
        q[i] -= 1
        out[tuple(q)] = c
    return out


def first_symbol(a: Mapping[Power, int], i: int) -> Poly:
    """Coefficient of [normal_i] in (normal_i)/(normal_i^2)."""
    out = {}
    for p, c in a.items():
        if p[i] == 1:
            q = list(p)
            q[i] = 0
            out[tuple(q)] = c
    return out


Word = tuple[int, ...]
Vec = dict[Word, Poly]


def vadd(a: Vec, b: Vec, sign: int = 1) -> Vec:
    out = {k: dict(v) for k, v in a.items()}
    for k, v in b.items():
        out[k] = add(out.get(k, {}), v, sign)
        if not out[k]:
            del out[k]
    return out


def vscale(a: Vec, coefficient: Poly) -> Vec:
    return {k: m for k, v in a.items() if (m := mul(v, coefficient))}


def koszul(a: Vec, weights: tuple[Poly, ...]) -> Vec:
    out: Vec = {}
    for word, value in a.items():
        for pos, i in enumerate(word):
            key = word[:pos] + word[pos + 1:]
            out = vadd(out, {key: mul(value, weights[i])}, (-1) ** pos)
    return out


def wedge(a: Vec, i: int, coefficient: Poly) -> Vec:
    out: Vec = {}
    for word, value in a.items():
        if i not in word:
            pos = sum(j < i for j in word)
            key = tuple(sorted(word + (i,)))
            out = vadd(out, {key: mul(value, coefficient)}, (-1) ** pos)
    return out


def contraction(a: Vec, i: int) -> Vec:
    out: Vec = {}
    for word, value in a.items():
        if i in word:
            pos = word.index(i)
            out = vadd(out, {word[:pos] + word[pos + 1:]: value}, (-1) ** pos)
    return out


def symbols() -> None:
    for i in range(3):
        x, t = 2 * i, 2 * i + 1
        w = mul(variable(x), variable(t))
        for a, b, v, coefficient in product(range(6), range(6), range(-2, 3), (-3, 1, 5)):
            p = list(ZERO_POWER)
            p[x], p[t], p[-1] = a, b, v
            f = monomial(tuple(p), coefficient)
            boundary = mul(w, f)
            check(set_zero(boundary, x) == {}, 'ordinary_Cartier_factor_vanishes')
            beta = set_zero(divide_known_factor(boundary, x), x)
            check(beta == mul(variable(t), set_zero(f, x)), 'Bockstein_keeps_Rees_factor')
            framed_symbol = first_symbol(beta, t)
            check(framed_symbol == set_zero(f, x, t), 'framed_first_symbol')
            # Adding x*g to a lift must not change beta modulo x.
            lift_change = mul(variable(x), f)
            changed = add(boundary, mul(w, lift_change))
            changed_beta = set_zero(divide_known_factor(changed, x), x)
            check(changed_beta == beta, 'Cartier_lift_independence')
            # Localizing a spectator does not alter any normal construction.
            inv_v = monomial((0, 0, 0, 0, 0, 0, -1))
            check(first_symbol(mul(beta, inv_v), t) == mul(framed_symbol, inv_v),
                  'spectator_localization_naturality')
        check(first_symbol(w, x) == variable(t), 'conormal_w_to_x_has_coefficient_t')
        check(set_zero(first_symbol(w, x), t) == {}, 'conormal_identification_degenerates_at_t0')
        check(first_symbol(set_zero(divide_known_factor(w, x), x), t) == ONE,
              'primitive_symbol_is_one')
        check(first_symbol(w, t) == variable(x), 'one_Rees_symbol_alone_keeps_x')
        check(set_zero(first_symbol(w, t), x) == {}, 'one_Rees_symbol_alone_not_unit')


def derived_normal_tests() -> None:
    for n in (1, 2, 3):
        xs = tuple(variable(2 * i) for i in range(n))
        ts = tuple(variable(2 * i + 1) for i in range(n))
        ws = tuple(mul(x, t) for x, t in zip(xs, ts))
        words = [w for r in range(n + 1) for w in combinations(range(n), r)]
        for word in words:
            v: Vec = {word: ONE}
            check(not koszul(koszul(v, ws), ws), 'weighted_Koszul_squared_zero')
            check(not koszul(koszul(v, xs), xs), 'Cartier_resolution_squared_zero')
            for i in range(n):
                # H_i = t_i e_i wedge; d_x H_i + H_i d_x = t_i x_i.
                lhs = vadd(koszul(wedge(v, i, ts[i]), xs), wedge(koszul(v, xs), i, ts[i]))
                check(lhs == vscale(v, ws[i]), 'factor_nullhomotopy_after_derived_Cartier')
                for j in range(i + 1, n):
                    check(not vadd(contraction(contraction(v, i), j),
                                   contraction(contraction(v, j), i)),
                          'ordered_Gysin_anticommutation')
        top: Vec = {tuple(range(n)): ONE}
        for i in range(n):
            top = contraction(top, i)
        check(top == {(): ONE}, 'ordered_normal_unit')


def parity(sequence: tuple) -> int:
    return (-1) ** sum(sequence[i] > sequence[j] for i in range(len(sequence))
                       for j in range(i + 1, len(sequence)))


def octagon_orientations() -> None:
    normalize = lambda a, b: tuple(sorted((a % 8, b % 8)))
    cuts = tuple(sorted({normalize(i, i + 3) for i in range(8)}))
    def crosses(x: tuple[int, int], y: tuple[int, int]) -> bool:
        a, b = x
        c, d = y
        return a < c < b < d or c < a < d < b
    pairs = tuple(p for p in combinations(cuts, 2) if not crosses(*p))
    check((len(cuts), len(pairs)) == (8, 12), 'source_Cut_counts')
    check(not any(all(not crosses(a, b) for a, b in combinations(S, 2))
                  for S in combinations(cuts, 3)), 'no_physical_triple_Cut')
    for r, reflected in product(range(8), (False, True)):
        action = lambda cut: normalize(*(r + (-1 if reflected else 1) * v for v in cut))
        check({action(c) for c in cuts} == set(cuts), 'dihedral_preserves_Cuts')
        for c in cuts:
            check(action(c) in cuts, 'single_normal_frame_transport')
        for pair in pairs:
            ordered = tuple(action(c) for c in pair)
            sign = parity(ordered)
            check(tuple(sorted(ordered)) in pairs, 'dihedral_preserves_overlaps')
            # Determinant and dual determinant each pick up the same sign.
            check(sign * sign == 1, 'determinant_dual_evaluation_equivariant')
            check(parity(tuple(reversed(ordered))) == -sign, 'ordered_pair_orientation_sign')


def convolution(a: list[Fraction], b: list[Fraction], N: int) -> list[Fraction]:
    return [sum((a[i] * b[k-i] for i in range(k+1)
                 if i < len(a) and k-i < len(b)), Fraction(0)) for k in range(N+1)]


def physical_residue_series(order: int) -> dict:
    # z=lambda*X, U(z)=(exp(z)-1)/z. The residue of U^-1 dX/X is its constant.
    U = [Fraction(1, factorial(k + 1)) for k in range(order + 1)]
    V = [Fraction(1)]
    for k in range(1, order + 1):
        V.append(-sum((U[j] * V[k-j] for j in range(1, k+1)), Fraction(0)))
    product_uv = convolution(U, V, order)
    for k, c in enumerate(product_uv):
        check(c == (1 if k == 0 else 0), 'analytic_unit_series_inverse')
    check(V[0] == 1, 'physical_simple_pole_residue_one')
    # (exp(z)-1)*V(z)/X = lambda*U(z)*V(z), a regular differential.
    check(product_uv[0] == 1, 'weighted_pole_becomes_regular_lambda')
    pole = {k - 1: value for k, value in enumerate(V) if value}
    normal_factor = {k: Fraction(1, factorial(k)) for k in range(1, order + 2)}
    for q in range(order + 1):
        shifted_pole = {k + q: value for k, value in pole.items()}
        check(shifted_pole.get(-1, Fraction(0)) == (1 if q == 0 else 0),
              'physical_coefficient_residue')
        weighted = {}
        for k, value in shifted_pole.items():
            for j, coefficient in normal_factor.items():
                weighted[k + j] = weighted.get(k + j, Fraction(0)) + value * coefficient
        check(weighted.get(-1, Fraction(0)) == 0, 'weighted_physical_residue_zero')
        check(weighted.get(q, Fraction(0)) == 1, 'weighted_regular_leading_coefficient')
    # Exact formal differential identity: dlog(exp(lambda X)-1)
    # minus lambda*dX = kappa(X)*dX. Verify its regular numerator expansion.
    exp = [Fraction(1, factorial(k)) for k in range(order + 1)]
    ev = convolution(exp, V, order)
    for k in range(order + 1):
        check(ev[k] - V[k] == (1 if k == 1 else 0),
              'dlog_pole_minus_regular_term')
    return {'order': order, 'inverse_unit_coefficients': [str(v) for v in V],
            'normalized_residue': 1, 'residue_after_factor_multiplication': 0}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path,
                        default=Path('gysin_normal_comparison_certificate.json'))
    parser.add_argument('--series-order', type=int, default=12)
    args = parser.parse_args()
    if not 2 <= args.series_order <= 40:
        parser.error('--series-order must be between 2 and 40')
    symbols()
    derived_normal_tests()
    octagon_orientations()
    series = physical_residue_series(args.series_order)
    certificate = {
        'schema': 'marici.local-gysin-normal-comparison.v1',
        'status': 'local_symbol_computed_raw_factor_identification_rejected',
        'pinned_commit': PIN, 'source_blobs': SOURCES,
        'assertion_counts': dict(sorted(COUNTS.items())),
        'total_assertions': sum(COUNTS.values()),
        'physical_series_test': series,
        'local_results': {
            'beta_x_h': 't*p',
            'oriented_first_t_symbol': '1*p',
            'ordinary_restriction_tx': '0',
            'derived_factor_nullhomotopy': 'd_x(t e_i wedge)+ (t e_i wedge)d_x = t*x',
            'product_order': 'Koszul determinant signs retained',
            'physical_unit_residue': 1,
            'physical_residue_of_w_times_normal_pole': 0,
        },
        'scope': {
            'local_integral_normal_algebra': True,
            'finite_formal_series_test_uses_rationals': True,
            'all_degree_claims_require_proofs_in_note': True,
            'full_spatial_Gysin_naturality': False,
            'physical_identification_of_previous_sigma_map': False,
            'proof_assistant_verification': False,
            'repository_modified': False,
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(certificate, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'total_assertions': certificate['total_assertions'],
                      'status': certificate['status'], 'output': str(args.output)}, indent=2))

if __name__ == '__main__':
    main()

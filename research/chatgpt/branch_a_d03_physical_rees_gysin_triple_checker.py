#!/usr/bin/env python3
"""Source-defined D03 Rees/Cartier specialization of a complete chain triple.

Standard library only. Reconstructs all 430 corrected coefficient states and
four original homogeneous contractions; recovers the four exported chains;
checks the physical graph u03=lambda*X03 on every column, including support
connectors; verifies the full Koszul-Hom Gysin and first-symbol calculations.
No occurrence, Rees, or monodromy parameter is inverted. The sole unit lambda
is the source's fixed-beta formal Koba--Nielsen factor. This checker computes
no physical conductor--Morse Delta and asserts no nonlinear realization.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
import json
from math import gcd
from pathlib import Path
from typing import Any

DIAGONALS = ('02', '03', '04', '13', '14', '15', '24', '25', '35')
PLUS = frozenset(('13', '15', '35'))
MINUS = frozenset(('02', '04', '24'))
SHORT = tuple(sorted(PLUS | MINUS))
LONG = ('03', '14', '25')
VARIABLES = (tuple('X' + a for a in DIAGONALS)
             + tuple('t' + a for a in SHORT)
             + tuple('u' + a for a in LONG))
NORMAL_VARIABLES = VARIABLES[9:]
POSITION = {a: i for i, a in enumerate(VARIABLES)}
NV = len(VARIABLES)
Power = tuple[int, ...]
State = tuple[tuple[str, ...], tuple[str, ...], int]
Vector = dict[int, int]
Matrix = dict[int, Vector]
PolyChain = dict[tuple[int, Power], int]
COUNTS: Counter[str] = Counter()


def check(ok: bool, category: str, detail: Any = '') -> None:
    if not ok:
        raise AssertionError(f'{category}: {detail}')
    COUNTS[category] += 1


def add_power(a: Power, b: Power) -> Power:
    return tuple(x + y for x, y in zip(a, b))


def sub_power(a: Power, b: Power) -> Power:
    return tuple(x - y for x, y in zip(a, b))


def unit(name: str) -> Power:
    return tuple(int(j == POSITION[name]) for j in range(NV))


def survives(power: Power) -> bool:
    return not (any(power[POSITION['X' + a]] for a in PLUS)
                and any(power[POSITION['X' + a]] for a in MINUS))


def normal_power(a: str) -> Power:
    if a in SHORT:
        return add_power(unit('X' + a), unit('t' + a))
    return unit('u' + a)


def crossings(a: str, b: str) -> bool:
    x, y = map(int, a)
    u, v = map(int, b)
    return x < u < y < v or u < x < v < y


def vec_add(left: Vector, right: Vector, scale: int = 1) -> Vector:
    out = dict(left)
    for i, c in right.items():
        out[i] = out.get(i, 0) + scale * c
        if out[i] == 0:
            del out[i]
    return out


def apply(matrix: Matrix, vector: Vector) -> Vector:
    out: Vector = {}
    for j, c in vector.items():
        out = vec_add(out, matrix.get(j, {}), c)
    return out


def matrix_rank(matrix: list[list[int]], ncols: int) -> int:
    if not matrix or not ncols:
        return 0
    a = [[Fraction(c) for c in row] for row in matrix]
    pivot_row = 0
    for col in range(ncols):
        hit = next((r for r in range(pivot_row, len(a)) if a[r][col]), None)
        if hit is None:
            continue
        a[pivot_row], a[hit] = a[hit], a[pivot_row]
        v = a[pivot_row][col]
        a[pivot_row] = [x / v for x in a[pivot_row]]
        for r in range(len(a)):
            if r != pivot_row and a[r][col]:
                v = a[r][col]
                a[r] = [x - v * y for x, y in zip(a[r], a[pivot_row])]
        pivot_row += 1
        if pivot_row == len(a):
            break
    return pivot_row


def maximal_minor_gcd(a: list[list[int]], ncols: int, rank: int) -> int:
    """Attachment ranks are at most two in this particular model."""
    if rank == 0:
        return 1
    if rank == 1:
        answer = 0
        for row in a:
            for c in row:
                answer = gcd(answer, abs(c))
        return answer
    if rank != 2:
        raise ValueError('Unexpected attachment rank; implement general minors.')
    answer = 0
    for r, s in combinations(range(len(a)), 2):
        for j, k in combinations(range(ncols), 2):
            answer = gcd(answer, abs(a[r][j] * a[s][k] - a[r][k] * a[s][j]))
    return answer


class Model:
    def __init__(self) -> None:
        self.faces = [tuple(c) for k in range(4) for c in combinations(DIAGONALS, k)
                      if all(not crossings(a, b) for a, b in combinations(c, 2))]
        check(Counter(map(len, self.faces)) == {0: 1, 1: 9, 2: 21, 3: 14}, 'K6_faces')
        self.face_set = set(self.faces)
        self.states: list[State] = [
            (face, marks, bit) for face in self.faces
            for k in range(len(face) + 1) for marks in combinations(face, k)
            for bit in (0, 1)]
        self.index = {g: j for j, g in enumerate(self.states)}
        self.degree = {j: 3 - len(f) + len(h) + e
                       for j, (f, h, e) in enumerate(self.states)}
        self.weights = [self.weight(g) for g in self.states]
        self.boundary: dict[int, list[tuple[int, Power, int]]] = {}
        for j, (face, marks, bit) in enumerate(self.states):
            terms = []
            for a in DIAGONALS:
                new_face = tuple(sorted(face + (a,)))
                if a not in face and new_face in self.face_set:
                    terms.append((self.index[new_face, marks, bit], unit('X' + a),
                                  (-1) ** sum(b < a for b in face)))
            for pos, a in enumerate(marks):
                terms.append((self.index[face, marks[:pos] + marks[pos + 1:], bit],
                              normal_power(a), (-1) ** (3 - len(face) + pos)))
            if bit:
                terms.append((self.index[face, marks, 0], unit('X35'),
                              (-1) ** (3 - len(face) + len(marks))))
            self.boundary[j] = terms
            for i, power, _ in terms:
                check(self.degree[i] == self.degree[j] - 1, 'full_differential_degree')
                check(add_power(self.weights[i], power) == self.weights[j],
                      'full_differential_multidegree')
        check(len(self.states) == 430, 'corrected_state_count')
        for j in self.boundary:
            basis = {(j, (0,) * NV): 1}
            check(self.poly_d(self.poly_d(basis)) == {}, 'full_polynomial_d_squared')
        for j, (face, _, _) in enumerate(self.states):
            if set(face) & set(SHORT):
                check(all(set(self.states[i][0]) & set(SHORT)
                          for i, _, _ in self.boundary[j]), 'short_support_closed')
            if frozenset(face) in (PLUS, MINUS):
                check(all(frozenset(self.states[i][0]) == frozenset(face)
                          for i, _, _ in self.boundary[j]), 'endpoint_support_closed')

    def weight(self, g: State) -> Power:
        face, marks, bit = g
        out = (0,) * NV
        for a in face:
            out = sub_power(out, unit('X' + a))
        for a in marks:
            out = add_power(out, normal_power(a))
        if bit:
            out = add_power(out, unit('X35'))
        return out

    def poly_d(self, chain: PolyChain) -> PolyChain:
        out: PolyChain = {}
        for (j, coeff), c in chain.items():
            for i, power, sg in self.boundary[j]:
                total = add_power(coeff, power)
                if not survives(total):
                    continue
                key = i, total
                out[key] = out.get(key, 0) + c * sg
                if out[key] == 0:
                    del out[key]
        return out

    def slice(self, normal_weight: tuple[int, ...]) -> tuple[Matrix, dict[int, Power]]:
        if len(normal_weight) != 9 or min(normal_weight) < 0:
            raise ValueError('Expected nine nonnegative normal/Rees weights.')
        weight = (0,) * 9 + normal_weight
        coeff = {j: sub_power(weight, w) for j, w in enumerate(self.weights)}
        coeff = {j: p for j, p in coeff.items() if min(p) >= 0 and survives(p)}
        matrix: Matrix = {}
        for j, p in coeff.items():
            col: Vector = {}
            for i, q, sg in self.boundary[j]:
                total = add_power(p, q)
                if not survives(total):
                    continue
                check(i in coeff and total == coeff[i], 'homogeneous_column_legality', (j, i))
                col[i] = col.get(i, 0) + sg
                if col[i] == 0:
                    del col[i]
            matrix[j] = col
        return matrix, coeff

    def support(self, matrix: Matrix) -> dict[str, Matrix]:
        short_ids = {i for i in matrix if set(self.states[i][0]) & set(SHORT)}
        endpoint_ids = {i for i in matrix if frozenset(self.states[i][0]) in (PLUS, MINUS)}
        short = {j: dict(matrix[j]) for j in sorted(short_ids)}
        endpoint = {j: dict(matrix[j]) for j in sorted(endpoint_ids)}
        quotient = {j: {i: c for i, c in col.items() if i not in short_ids}
                    for j, col in matrix.items() if j not in short_ids}
        check(all(set(v) <= short_ids for v in short.values()), 'slice_short_support')
        check(all(set(v) <= endpoint_ids for v in endpoint.values()), 'slice_endpoint_support')
        for j, col in matrix.items():
            expected = apply(quotient, {j: 1}) if j in quotient else {}
            check({i: c for i, c in col.items() if i in quotient} == expected,
                  'quotient_projection_chain')
        return {'full': matrix, 'short': short, 'Q': quotient, 'endpoint': endpoint}

    def retract(self, original: Matrix) -> dict[str, Any]:
        d = {i: dict(col) for i, col in original.items()}
        proj = {i: {i: 1} for i in original}
        inc = {i: {i: 1} for i in original}
        hom = {i: {} for i in original}
        active = set(original)
        log: list[tuple[int, int, int]] = []
        while True:
            pivot = None
            for hi in sorted(active, key=lambda i: (-self.degree[i], i)):
                for lo, c in sorted(d[hi].items()):
                    if abs(c) == 1:
                        pivot = lo, hi, c
                        break
                if pivot is not None:
                    break
            if pivot is None:
                break
            lo, hi, sg = pivot
            rest = {i: c for i, c in d[hi].items() if i != lo}
            ihi = inc[hi]
            for j, pj in list(proj.items()):
                c = pj.get(lo, 0)
                if c:
                    hom[j] = vec_add(hom[j], ihi, sg * c)
                proj[j] = vec_add({i: c for i, c in pj.items() if i not in (lo, hi)},
                                  rest, -sg * c)
            for j in sorted(active - {lo, hi}):
                c = d[j].get(lo, 0)
                if c:
                    inc[j] = vec_add(inc[j], ihi, -sg * c)
                d[j] = vec_add({i: c for i, c in d[j].items() if i not in (lo, hi)},
                               rest, -sg * c)
            for j in (lo, hi):
                del d[j]
                del inc[j]
            active -= {lo, hi}
            log.append(pivot)
        check(all(not col for col in d.values()), 'zero_residual_differential')
        for j in original:
            check(apply(original, original[j]) == {}, 'slice_d_squared')
            check(apply(proj, original[j]) == {}, 'projection_chain')
            check(vec_add(apply(original, hom[j]), apply(hom, original[j]))
                  == vec_add({j: 1}, apply(inc, proj[j]), -1), 'deformation_homotopy')
            check(all(self.degree[i] == self.degree[j] + 1 for i in hom[j]), 'homotopy_degree')
        for j, v in inc.items():
            check(apply(original, v) == {}, 'inclusion_cycle')
            check(apply(proj, v) == {j: 1}, 'projection_inclusion')
        return {'d': d, 'p': proj, 'i': inc, 'h': hom, 'pivots': log,
                'homology': dict(sorted(Counter(self.degree[i] for i in d).items()))}

    def pattern(self, mask: int) -> dict[str, Any]:
        weight = tuple(int(mask >> k & 1) for k in range(9))
        matrix, coeff = self.slice(weight)
        complexes = self.support(matrix)
        reductions = {name: self.retract(mat) for name, mat in complexes.items()}
        qids = sorted(j for j in reductions['Q']['d'] if self.degree[j] == 2)
        bids = sorted(j for j in reductions['short']['d'] if self.degree[j] == 1)
        attachment = {}
        for j in qids:
            bdry = apply(matrix, reductions['Q']['i'][j])
            check(set(bdry) <= set(complexes['short']), 'connecting_map_short_support')
            check(apply(complexes['short'], bdry) == {}, 'connecting_map_cycle')
            attachment[j] = apply(reductions['short']['p'], bdry)
        a = [[attachment[j].get(i, 0) for j in qids] for i in bids]
        rank = matrix_rank(a, len(qids))
        minor_gcd = maximal_minor_gcd(a, len(qids), rank)
        check(minor_gcd == 1, 'attachment_saturated')
        # Positive exponents do not change the basis or integer differential.
        # One simultaneous high-exponent replay checks the implemented rule;
        # the all-exponent argument is proved separately in the Markdown file.
        high = tuple((2 + k) if mask >> k & 1 else 0 for k in range(9))
        matrix_high, _ = self.slice(high)
        check(matrix_high == matrix, 'positive_weight_support_stability')
        row = {
            'mask': mask,
            'positive_normal_coordinates': [NORMAL_VARIABLES[k] for k in range(9) if mask >> k & 1],
            'chain_ranks': {name: dict(sorted(Counter(self.degree[j] for j in mat).items()))
                            for name, mat in complexes.items()},
            'homology': {name: red['homology'] for name, red in reductions.items()},
            'attachment_row_basis_ids': bids, 'attachment_column_basis_ids': qids,
            'attachment_matrix': a, 'attachment_rank': rank,
            'attachment_kernel_rank': len(qids) - rank,
            'attachment_maximal_minor_gcd': minor_gcd,
            'unit_cancellation_pivots': {name: red['pivots'] for name, red in reductions.items()},
            'residual_basis_ids': {name: sorted(red['d']) for name, red in reductions.items()},
        }
        return {'row': row, 'matrix': matrix, 'coeff': coeff, 'complexes': complexes,
                'reductions': reductions}


def polynomial(chain: Vector, coeff: dict[int, Power]) -> PolyChain:
    return {(j, coeff[j]): c for j, c in chain.items()}


def poly_add(left: PolyChain, right: PolyChain, scale: int = 1) -> PolyChain:
    out = dict(left)
    for k, c in right.items():
        out[k] = out.get(k, 0) + scale * c
        if out[k] == 0:
            del out[k]
    return out


def multiply(chain: PolyChain, power: Power) -> PolyChain:
    return {(j, add_power(p, power)): c for (j, p), c in chain.items()
            if survives(add_power(p, power))}


def serialize_poly(chain: PolyChain, model: Model) -> list[dict[str, Any]]:
    result = []
    for (j, power), c in sorted(chain.items()):
        face, marks, bit = model.states[j]
        result.append({'state_id': j, 'face': face, 'marks': marks,
                       'occurrence_partner': bit, 'coefficient': c,
                       'monomial': {n: p for n, p in zip(VARIABLES, power) if p}})
    return result


def minimal_masks(masks: list[int]) -> list[int]:
    return [m for m in masks if not any(n != m and n & m == n for n in masks)]



EXPECTED_WITNESS_SHA256 = {'omega': 'f6a55b410199a0451c8dde229587e336dda080f7be65146548d1e82a979fbf49', 'u03_primitive': '6506620da253928119d6cbd0686a8087dac8ba0116b3f7c9c9fa307a7845c8b1', 'product_primitive': '8359c795a5c8d31c7be83d6621daddee855c12cb3aeb8839d69737f97a968cee', 'secondary_cycle': '7aa3f861f40e5b34989db39d27f2ebd482e1b7714caefffe0a6c7688c5cff3df'}

def canonical_hash(obj: Any) -> str:
    return sha256(json.dumps(obj, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def build_original_triple(model: Model) -> tuple[dict[str, PolyChain], dict[str, Any]]:
    mask = sum(1 << NORMAL_VARIABLES.index(n) for n in ('t02', 't04', 't13'))
    umask = 1 << NORMAL_VARIABLES.index('u03')
    mmask = sum(1 << NORMAL_VARIABLES.index(n) for n in ('t15', 't24', 'u14', 'u25'))
    pats = {k: model.pattern(k) for k in (mask, mask | umask, mask | mmask, mask | umask | mmask)}
    p = pats[mask]
    red, d = p['reductions']['full'], p['matrix']
    h2 = [j for j in red['i'] if model.degree[j] == 2]
    check(len(h2) == 1, 'original_filling_H2_rank')
    base = dict(red['i'][h2[0]])
    for ep in sorted(p['complexes']['endpoint']):
        c = base.get(ep, 0)
        if c:
            pivot = next(j for j in d if abs(d[j].get(ep, 0)) == 1)
            base = vec_add(base, d[pivot], -c * d[pivot][ep])
    omega = vec_add(d[model.index[(), (), 0]], base, -1)
    wu = apply(pats[mask | umask]['reductions']['full']['h'], omega)
    wm = apply(pats[mask | mmask]['reductions']['full']['h'], omega)
    theta = vec_add(wm, wu, -1)
    result = {'omega': polynomial(omega, p['coeff']),
              'u03_primitive': polynomial(wu, pats[mask | umask]['coeff']),
              'product_primitive': polynomial(wm, pats[mask | mmask]['coeff']),
              'secondary_cycle': polynomial(theta, pats[mask | umask | mmask]['coeff'])}
    hashes = {}
    for name, chain in result.items():
        hashes[name] = canonical_hash(serialize_poly(chain, model))
        check(hashes[name] == EXPECTED_WITNESS_SHA256[name], 'original_exported_chain_hash', name)
    check(model.poly_d(result['omega']) == {}, 'original_omega_cycle')
    check(model.poly_d(result['u03_primitive']) == multiply(result['omega'], unit('u03')),
          'original_u_homotopy')
    mu = sum_powers('t15', 't24', 'u14', 'u25')
    check(model.poly_d(result['product_primitive']) == multiply(result['omega'], mu),
          'original_mu_homotopy')
    check(result['secondary_cycle'] == poly_add(multiply(result['product_primitive'], unit('u03')),
                                               multiply(result['u03_primitive'], mu), -1),
          'original_whole_comparison')
    check(model.poly_d(result['secondary_cycle']) == {}, 'original_secondary_cycle')
    return result, {'chain_hashes': hashes, 'pattern_results': [pats[k]['row'] for k in sorted(pats)]}


def sum_powers(*names: str) -> Power:
    answer = (0,) * NV
    for n in names:
        answer = add_power(answer, unit(n))
    return answer


class D03GraphModel(Model):
    """Physical u03=lambda*X03, expressed in the normalized X03-circle basis."""
    def __init__(self) -> None:
        super().__init__()
        self.boundary = {j: [(i, unit('X03') if p == unit('u03') else p, sg)
                             for i, p, sg in col] for j, col in self.boundary.items()}
        self.weights = []
        for face, marks, bit in self.states:
            w = (0,) * NV
            for a in face:
                w = sub_power(w, unit('X' + a))
            for a in marks:
                w = add_power(w, unit('X03') if a == '03' else normal_power(a))
            if bit:
                w = add_power(w, unit('X35'))
            self.weights.append(w)
        for j, col in self.boundary.items():
            for i, p, _ in col:
                check(add_power(self.weights[i], p) == self.weights[j], 'graph_d_fine_degree')
            check(self.poly_d(self.poly_d({(j, (0,) * NV): 1})) == {}, 'graph_d_squared')

    def homogeneous_slice(self, w: Power, on_divisor: bool = False) -> tuple[Matrix, dict[int, Power]]:
        coeff = {j: sub_power(w, v) for j, v in enumerate(self.weights)}
        coeff = {j: p for j, p in coeff.items() if min(p) >= 0 and survives(p)
                 and (not on_divisor or p[POSITION['X03']] == 0)}
        d: Matrix = {}
        for j, p in coeff.items():
            col: Vector = {}
            for i, q, sg in self.boundary[j]:
                total = add_power(p, q)
                if not survives(total) or (on_divisor and total[POSITION['X03']]):
                    continue
                check(i in coeff and total == coeff[i], 'graph_homogeneous_legality')
                col[i] = col.get(i, 0) + sg
                if not col[i]:
                    del col[i]
            d[j] = col
        return d, coeff


def transported(chain: PolyChain, model: Model) -> tuple[int, PolyChain]:
    """Substitute u03=lambda*X03, then send marked e03 to lambda*e03^X.

    All chains used here have uniform lambda degree. Lambda is a formal unit;
    its degree is returned, not set to one in the actual physical formula.
    """
    answer: PolyChain = {}
    powers = set()
    for (j, p), c in chain.items():
        q = list(p)
        k = q[POSITION['u03']] + int('03' in model.states[j][1])
        powers.add(k)
        q[POSITION['X03']] += q[POSITION['u03']]
        q[POSITION['u03']] = 0
        key = j, tuple(q)
        answer[key] = answer.get(key, 0) + c
        if not answer[key]:
            del answer[key]
    check(len(powers) <= 1, 'uniform_transport_unit_weight')
    return next(iter(powers), 0), answer


def restrict_divisor(chain: PolyChain) -> PolyChain:
    return {(j, p): c for (j, p), c in chain.items() if p[POSITION['X03']] == 0}


def factor_known_X03(chain: PolyChain) -> PolyChain:
    """Coefficient factorization on a proven divisible chain, not localization."""
    check(all(p[POSITION['X03']] > 0 for j, p in chain), 'known_Cartier_divisibility')
    result = {(j, sub_power(p, unit('X03'))): c for (j, p), c in chain.items()}
    check(all(min(p) >= 0 for j, p in result), 'Cartier_factorization_nonnegative')
    check(multiply(result, unit('X03')) == chain, 'Cartier_factorization_exact')
    return result


def selected(chain: PolyChain, model: Model, kind: str) -> PolyChain:
    def keep(j: int) -> bool:
        face = frozenset(model.states[j][0])
        if kind == 'endpoint':
            return face in (PLUS, MINUS)
        if kind == 'Q':
            return not (face & frozenset(SHORT))
        if kind == 'short':
            return bool(face & frozenset(SHORT))
        if kind == 'endpoint_quotient':
            return face not in (PLUS, MINUS)
        raise ValueError(kind)
    return {key: c for key, c in chain.items() if keep(key[0])}


def hom_d(model: Model, pair: tuple[PolyChain, PolyChain]) -> tuple[PolyChain, PolyChain]:
    """Homological Hom(K(X03),C): H_n=C_n plus C_(n+1)."""
    a, b = pair
    return model.poly_d(a), poly_add(multiply(a, unit('X03')), model.poly_d(b), -1)


def scaled(pair: tuple[PolyChain, PolyChain], p: Power) -> tuple[PolyChain, PolyChain]:
    return multiply(pair[0], p), multiply(pair[1], p)


def add_pairs(a: tuple[PolyChain, PolyChain], b: tuple[PolyChain, PolyChain], c: int = 1):
    return poly_add(a[0], b[0], c), poly_add(a[1], b[1], c)


def pair_json(pair, model):
    return {'first_component': serialize_poly(pair[0], model),
            'Koszul_component': serialize_poly(pair[1], model)}


def main(output: Path) -> dict[str, Any]:
    old = Model()
    source, source_evidence = build_original_triple(old)
    target = D03GraphModel()
    zero = (0,) * NV
    x = unit('X03')
    mu = sum_powers('t15', 't24', 'u14', 'u25')
    w = sum_powers('t02', 't04', 't13')
    A = add_power(w, sum_powers('t15', 't24'))

    # Check the source-to-physical comparison and each support leg on every state.
    for j in range(len(old.states)):
        c = {(j, zero): 1}
        kd, td = transported(old.poly_d(c), old)
        kc, tc = transported(c, old)
        check(td == target.poly_d(tc) and (not td or kd == kc), 'all_430_graph_chain_columns')
        for kind in ('endpoint', 'Q', 'short', 'endpoint_quotient'):
            _, before = transported(selected(c, old, kind), old)
            after = selected(tc, target, kind)
            check(before == after, 'diagonal_comparison_preserves_support', kind)
        # Actual endpoint connecting block, not an unsupported endpoint projection.
        ec = selected(c, old, 'endpoint_quotient')
        old_conn = selected(old.poly_d(ec), old, 'endpoint')
        _, lhs = transported(old_conn, old)
        _, tec = transported(ec, old)
        rhs = selected(target.poly_d(tec), target, 'endpoint')
        check(lhs == rhs, 'endpoint_connecting_block_naturality')

    unit_weights = {}
    images = {}
    for name, c in source.items():
        unit_weights[name], images[name] = transported(c, old)
    check(unit_weights == {'omega': 0, 'u03_primitive': 1,
                           'product_primitive': 0, 'secondary_cycle': 1},
          'transported_whole_triple_unit_weights')
    O, U, M, T = [images[k] for k in ('omega', 'u03_primitive', 'product_primitive', 'secondary_cycle')]
    S = factor_known_X03(U)
    Z = poly_add(M, multiply(S, mu), -1)
    check(target.poly_d(S) == O, 'physical_omega_explicit_primitive')
    check(target.poly_d(Z) == {}, 'physical_remaining_secondary_cycle')
    check(T == multiply(Z, x), 'whole_theta_factorization')
    check(len(S) == 15 and len(Z) == 45, 'whole_chain_counts')
    check(not selected(S, target, 'endpoint'), 'physical_primitive_endpoint_zero')
    check(not selected(O, target, 'endpoint'), 'physical_omega_endpoint_zero')

    epZ = selected(Z, target, 'endpoint')
    eZ = selected(Z, target, 'endpoint_quotient')
    ep_bdry = target.poly_d(epZ)
    kappaZ = selected(target.poly_d(eZ), target, 'endpoint')
    check(poly_add(ep_bdry, kappaZ) == {}, 'secondary_endpoint_comparison_equation')
    check(len(epZ) == 2 and len(ep_bdry) == 6, 'retained_endpoint_terms_and_defects')
    check(target.poly_d(eZ) == {k: -c for k, c in ep_bdry.items()},
          'deleting_endpoint_terms_breaks_chain_equation')
    qZ = selected(Z, target, 'Q')
    lowerZ = poly_add(Z, qZ, -1)
    check(selected(target.poly_d(qZ), target, 'Q') == {}, 'whole_Q_cycle')
    check(target.poly_d(lowerZ) == {k: -c for k, c in target.poly_d(qZ).items()},
          'whole_Q_lower_attachment')
    q_expect = {
        (target.index[(), (), 0], add_power(A, sum_powers('u14', 'u25'))): 1,
        (target.index[('03',), ('03',), 0], add_power(A, sum_powers('u14', 'u25'))): -1,
        (target.index[('14',), ('14',), 0], add_power(A, sum_powers('X14', 'u25'))): -1,
        (target.index[('25',), ('25',), 0], add_power(A, sum_powers('X25', 'u14'))): -1,
    }
    check(qZ == q_expect, 'complete_secondary_Q_formula')

    # Standard supported Koszul Hom, including its counit and shifted purity map.
    for j in range(len(target.states)):
        c = {(j, zero): 1}
        for pair in ((c, {}), ({}, c)):
            dpair = hom_d(target, pair)
            check(hom_d(target, dpair) == ({}, {}), 'supported_Hom_all_860_d_squared')
            check(dpair[0] == target.poly_d(pair[0]), 'supported_counit_chain')
            # Purity sends (a,b) to b mod X in C_D[-1], whose differential is -d.
            check(restrict_divisor(dpair[1]) == {
                k: -v for k, v in restrict_divisor(target.poly_d(restrict_divisor(pair[1]))).items()},
                'supported_purity_all_columns')
    supported_pair = (O, U)
    check(hom_d(target, supported_pair) == ({}, {}), 'supported_omega_pair_cycle')
    check(hom_d(target, (S, {})) == supported_pair, 'supported_omega_pair_exact')
    compatibility_pair = ({}, T)
    check(hom_d(target, compatibility_pair) == ({}, {}), 'supported_compatibility_pair_cycle')
    check(add_pairs(hom_d(target, (M, {})), scaled(supported_pair, mu), -1) == compatibility_pair,
          'supported_whole_triple_relation')
    check(hom_d(target, (Z, {})) == compatibility_pair, 'supported_compatibility_pair_exact')
    check(restrict_divisor(U) == {} and restrict_divisor(T) == {}, 'ordinary_purity_values_zero')

    # The first normal symbol is a different, explicitly framed map on X*C.
    # Its action on every generator of X*C commutes with the chain differential.
    for j in range(len(target.states)):
        c = {(j, zero): 1}
        xc = multiply(c, x)
        left = restrict_divisor(factor_known_X03(target.poly_d(xc)))
        right = restrict_divisor(target.poly_d(restrict_divisor(factor_known_X03(xc))))
        check(left == right, 'first_normal_symbol_chain_map_all_columns')
    Od, Sd, Zd = map(restrict_divisor, (O, S, Z))
    check(restrict_divisor(target.poly_d(Sd)) == Od, 'first_symbol_of_Wu_has_Omega_boundary')
    check(restrict_divisor(target.poly_d(Zd)) == {}, 'first_symbol_of_Theta_closed')
    check(restrict_divisor(factor_known_X03(T)) == Zd, 'first_symbol_Theta_exact_readout')
    check(restrict_divisor(factor_known_X03(U)) == Sd, 'first_symbol_Wu_exact_readout')

    # Complete relevant homogeneous support components, with and without Cartier restriction.
    summaries = []
    saved = {}
    for label, weight in [('Omega_weight', w), ('secondary_symbol_weight', add_power(w, mu))]:
        for on_divisor in (False, True):
            d, coeff = target.homogeneous_slice(weight, on_divisor)
            support = target.support(d)
            reds = {n: target.retract(m) for n, m in support.items()}
            summaries.append({'weight_label': label, 'on_X03_divisor': on_divisor,
                              'weight': list(weight),
                              'chain_ranks': {n: dict(sorted(Counter(target.degree[j] for j in mat).items()))
                                              for n, mat in support.items()},
                              'homology': {n: red['homology'] for n, red in reds.items()},
                              'unit_cancellation_pivots': {n: red['pivots'] for n, red in reds.items()}})
            saved[label, on_divisor] = (d, coeff, support, reds)
    d, coeff, support, reds = saved['Omega_weight', True]
    ov = {j: c for (j, p), c in Od.items()}
    check(all(p == coeff[j] for j, p in Od), 'Cartier_omega_in_computed_component')
    check(set(ov) <= set(support['short']), 'Cartier_omega_short_supported')
    check(apply(reds['short']['p'], ov) == {}, 'Cartier_omega_zero_in_short_homology')
    L = polynomial(apply(reds['short']['h'], ov), coeff)
    check(restrict_divisor(target.poly_d(L)) == Od, 'Cartier_short_primitive_identity')
    check(len(L) == 6, 'Cartier_short_primitive_six_terms')
    check(not selected(L, target, 'endpoint') and not selected(L, target, 'Q'),
          'Cartier_short_primitive_preserves_endpoints_and_Q')
    secondary_difference = poly_add(Sd, L, -1)
    check(restrict_divisor(target.poly_d(secondary_difference)) == {},
          'difference_of_Cartier_primitives_closed')
    sv = {j: c for (j, p), c in secondary_difference.items()}
    sdcoord = apply(reds['full']['p'], sv)
    check(len(sdcoord) == 1 and abs(next(iter(sdcoord.values()))) == 1,
          'difference_of_Cartier_primitives_is_primitive')

    zd, zcoeff, zsupport, zreds = saved['secondary_symbol_weight', True]
    zvec = {j: c for (j, p), c in Zd.items()}
    check(all(p == zcoeff[j] for j, p in Zd), 'Gysin_symbol_homogeneous_component')
    zclass = apply(zreds['full']['p'], zvec)
    check(zclass and gcd(*zclass.values()) == 1, 'Gysin_symbol_primitive_class')
    top = target.index[(), (), 0]
    check(zvec.get(top) == 1, 'Gysin_symbol_top_coefficient_detector')
    check(not any(target.degree[j] == 4 for j in zd), 'Gysin_symbol_no_degree_four_primitive')
    for j, col in zd.items():
        if target.degree[j] == 4:
            check(col.get(top, 0) == 0, 'Gysin_symbol_detector_kills_boundaries')
    check(selected(Zd, target, 'endpoint') == epZ, 'Gysin_symbol_keeps_two_endpoint_terms')
    check(selected(Zd, target, 'Q') == qZ, 'Gysin_symbol_keeps_all_four_Q_terms')

    # A change of W_mu by the new physical cycle Z would erase the compatibility.
    # This is permitted by the boundary equation but not by the fixed exported triple.
    adjusted_mu = poly_add(M, Z, -1)
    check(adjusted_mu == multiply(S, mu), 'post_graph_primitive_ambiguity_exhibited')
    check(poly_add(multiply(adjusted_mu, x), multiply(U, mu), -1) == {},
          'post_graph_adjustment_erases_theta_not_original_data')

    def s(c): return serialize_poly(c, target)
    payload = {
        'schema': 'marici.branchA.d03_physical_rees_gysin_triple.v1',
        'source_commit': 'd1947b67a60d3e88ba77f4ca60ea02c2a306ee61',
        'source_rules': ['research/voevodsky/check_d03_formal_support_purity.rs',
                         'src/ledger/20260814-106 Marked Log Gallery Secondary Class and the Global Yoneda Gap.md',
                         'research/voevodsky/check_absolute_unlocalized_support_pc.rs'],
        'physical_base_change': {
            'ring_scope': 'characteristic-zero formal completion in X03; beta invertible; all other Rees and long-normal variables retained',
            'formula': 'u03=lambda03*X03, lambda03=beta*sum_(n>=0)(beta*X03)^n/(n+1)!',
            'normal_frame_map': '[F,H,e] -> lambda03^(03 in H)*[F,H,e]_X',
            'conormal_map_on_divisor': '[u03] -> beta*[X03]; dual -> beta^(-1)*[X03]^dual',
            'new_chain_generators': 0, 'occurrence_or_Rees_inverses': False,
            'lambda_inverse_is_source_supplied_unit': True},
        'source_witness_replay': source_evidence,
        'transported_unit_degrees': unit_weights,
        'states': [{'id': j, 'face': f, 'marks': h, 'occurrence_partner': e,
                    'homological_degree': target.degree[j]} for j, (f, h, e) in enumerate(target.states)],
        'physical_normalized_differential': {j: [[i, list(p), sg] for i, p, sg in col]
                                             for j, col in target.boundary.items()},
        'chains': {'Omega_physical': s(O), 'Wu_after_lambda_frame_removal': s(U),
                   'Wmu_physical': s(M), 'Theta_after_lambda_frame_removal': s(T),
                   'S_complete_primitive_of_Omega': s(S),
                   'Z_complete_remaining_cycle': s(Z),
                   'Z_Q_projection': s(qZ), 'Z_short_correction': s(lowerZ),
                   'Z_endpoint_terms': s(epZ), 'Z_endpoint_connectors': s(kappaZ),
                   'Omega_on_Cartier_divisor': s(Od),
                   'S_on_Cartier_divisor': s(Sd),
                   'Z_on_Cartier_divisor': s(Zd),
                   'Cartier_short_primitive_L': s(L),
                   'difference_S_minus_L_on_divisor': s(secondary_difference)},
        'normal_form': ['dS=Omega_physical',
                        'Wu_physical=lambda03*X03*S',
                        'Wmu_physical=mu*S+Z',
                        'Theta_physical=lambda03*X03*Z', 'dZ=0'],
        'supported_Hom': {'states': 860, 'differential': 'D(a,b)=(da,X03*a-db)',
                          'purity': '(a,b) -> b mod X03, into C_D[-1] with normal dual line',
                          'Omega_pair': pair_json(supported_pair, target),
                          'Omega_pair_primitive': pair_json((S, {}), target),
                          'Theta_pair': pair_json(compatibility_pair, target),
                          'Theta_pair_primitive': pair_json((Z, {}), target),
                          'ordinary_supported_classes': 'both zero'},
        'first_symbol': {'Theta': '[u03] tensor Z_D', 'Wu': '[u03] tensor S_D',
                         'typed_evaluation': '(u03)/(u03)^2 dual tensor gr1(C) -> C_D',
                         'not_a_readout_of_ordinary_Hom_cohomology': True,
                         'Z_supported_homology_coordinates': sorted(zclass.items()),
                         'normal_line_retained': True,
                         'two_endpoint_terms_retained': True,
                         'top_coefficient_detector_value': 1},
        'homogeneous_support_summaries': summaries,
        'scope': {'local_D03_source_graph_applied': True,
                  'global_physical_Delta_J_identified': False,
                  'full_six_functor_comparison_constructed': False,
                  'ordinary_supported_Gysin_equals_first_symbol': False,
                  'new_Z_is_independent_of_all_post_graph_primitive_choices': False,
                  'original_exported_primitive_Wmu_retained': True,
                  'full_all_normal_Koba_Nielsen_graph_claimed': False,
                  'scalar_Q_unit_inferred': False},
        'verification': {'checks_by_family': dict(sorted(COUNTS.items())),
                         'total_checks': sum(COUNTS.values())}}
    payload['content_sha256'] = canonical_hash(payload)
    output.write_text(json.dumps(payload, sort_keys=True, indent=2) + '\n')
    print(json.dumps({'certificate': str(output), 'checks': sum(COUNTS.values()),
                      'states': 430, 'ordinary_supported_primary_and_compatibility': 'zero',
                      'first_symbol_Z': 'primitive_nonzero_with_two_endpoint_terms',
                      'content_sha256': payload['content_sha256']}, indent=2))
    return payload


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).with_name('branch_a_d03_physical_rees_gysin_triple_certificate.json'))
    args = parser.parse_args()
    main(args.output)

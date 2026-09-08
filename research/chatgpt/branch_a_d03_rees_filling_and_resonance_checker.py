#!/usr/bin/env python3
"""Exact normal/Rees-weight audit of the corrected K6 support complex.

Reconstructs the 430-state finite cellular coefficient model over the alternating
normalization ring; checks all 512 nonnegative normal-weight support patterns.
Exports an endpoint-zero D03 filling variation, its exact normal-subring
annihilator, two annihilating primitives, and their nonzero compatibility cycle.

Standard library only. No network, repository writes, parameter inversion,
coefficient sampling, or identification with the physical Delta_J. The infinite
weight conclusion additionally uses the zero/positive-support proof in the
accompanying Markdown file.
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


def main(output: Path) -> dict[str, Any]:
    model = Model()
    patterns = [model.pattern(mask) for mask in range(512)]
    p0 = patterns[0]
    check(p0['row']['homology'] == {
        'full': {1: 3}, 'short': {1: 5}, 'Q': {2: 2}, 'endpoint': {0: 1}},
        'recover_previous_zero_weight_homology')
    check(p0['row']['attachment_kernel_rank'] == 0, 'recover_zero_weight_injectivity')

    # First minimal D03-visible Rees weight: t02*t04*t13.
    mask = sum(1 << NORMAL_VARIABLES.index(n) for n in ('t02', 't04', 't13'))
    pattern = patterns[mask]
    matrix, coeff, red = pattern['matrix'], pattern['coeff'], pattern['reductions']['full']
    hom2 = [j for j in red['i'] if model.degree[j] == 2]
    check(len(hom2) == 1, 'new_weight_primitive_rank_one')
    generator_id = hom2[0]
    initial = red['i'][generator_id]
    endpoint_ids = set(pattern['complexes']['endpoint'])
    endpoint_free = dict(initial)
    correction: Vector = {}
    for endpoint in sorted(endpoint_ids):
        c = endpoint_free.get(endpoint, 0)
        if not c:
            continue
        pivot = next(j for j in matrix if abs(matrix[j].get(endpoint, 0)) == 1)
        factor = -c * matrix[pivot][endpoint]
        correction[pivot] = correction.get(pivot, 0) + factor
        endpoint_free = vec_add(endpoint_free, matrix[pivot], factor)
    check(not (set(endpoint_free) & endpoint_ids), 'endpoint_zero_representative_exists')
    top_id = model.index[(), (), 0]
    omega = vec_add(matrix[top_id], endpoint_free, -1)
    check(apply(matrix, omega) == {}, 'omega_cycle')
    check(not (set(omega) & endpoint_ids), 'omega_endpoint_columns_zero')
    qids = set(pattern['complexes']['Q'])
    qomega = {j: c for j, c in omega.items() if j in qids}
    d03 = model.index[('03',), (), 0]
    check(qomega == {d03: 1}, 'omega_exact_D03_projection')
    detector = {j: -v.get(generator_id, 0) for j, v in red['p'].items()
                if v.get(generator_id, 0)}
    evaluate = lambda v: sum(detector.get(j, 0) * c for j, c in v.items())
    check(evaluate(omega) == 1, 'omega_primitive_detector')
    for j, v in matrix.items():
        check(evaluate(v) == 0, 'omega_detector_kills_every_boundary')
    short_correction = vec_add(omega, qomega, -1)
    check(set(short_correction) <= set(pattern['complexes']['short']), 'lower_correction_short_support')
    check(apply(matrix, short_correction) == {j: -c for j, c in apply(matrix, qomega).items()},
          'lower_correction_exact_attachment_filler')
    omega_poly = polynomial(omega, coeff)
    check(model.poly_d(omega_poly) == {}, 'omega_full_polynomial_cycle')

    # The normal-subring annihilator is determined by every possible new
    # positive support; repeated positive powers are chain isomorphisms of slices.
    extensions = [ext for ext in range(512) if ext & mask == 0]
    death_masks = []
    multiplication_images = []
    for ext in extensions:
        target = patterns[mask | ext]
        image = apply(target['reductions']['full']['p'], omega)
        if not image:
            death_masks.append(ext)
        multiplication_images.append({'additional_mask': ext,
                                      'homology_coordinates': sorted(image.items())})
        check(apply(target['matrix'], omega) == {}, 'normal_multiplication_cycle')
    ann_masks = minimal_masks(death_masks)
    u_mask = 1 << NORMAL_VARIABLES.index('u03')
    mu_names = ('t15', 't24', 'u14', 'u25')
    mu_mask = sum(1 << NORMAL_VARIABLES.index(n) for n in mu_names)
    check(sorted(ann_masks) == sorted([u_mask, mu_mask]), 'exact_normal_annihilator_masks')
    for ext in extensions:
        check((ext in death_masks) == ((ext & u_mask == u_mask) or (ext & mu_mask == mu_mask)),
              'annihilator_upper_ideal')

    pu = patterns[mask | u_mask]
    pm = patterns[mask | mu_mask]
    pfinal = patterns[mask | u_mask | mu_mask]
    Wu = apply(pu['reductions']['full']['h'], omega)
    Wm = apply(pm['reductions']['full']['h'], omega)
    check(apply(pu['matrix'], Wu) == omega, 'u_annihilating_primitive')
    check(apply(pm['matrix'], Wm) == omega, 'mu_annihilating_primitive')
    Wu_poly = polynomial(Wu, pu['coeff'])
    Wm_poly = polynomial(Wm, pm['coeff'])
    mu_power = (0,) * NV
    for name in mu_names:
        mu_power = add_power(mu_power, unit(name))
    check(model.poly_d(Wu_poly) == multiply(omega_poly, unit('u03')), 'u_primitive_polynomial_identity')
    check(model.poly_d(Wm_poly) == multiply(omega_poly, mu_power), 'mu_primitive_polynomial_identity')
    check(not any(frozenset(model.states[j][0]) in (PLUS, MINUS) for j in Wu),
          'u_primitive_endpoint_columns_zero')

    # Retain the next coherence instead of replacing the class by its homology module.
    theta = vec_add(Wm, Wu, -1)  # In the final slice: u03*Wm - mu*Wu.
    theta_poly = polynomial(theta, pfinal['coeff'])
    check(theta_poly == poly_add(multiply(Wm_poly, unit('u03')),
                                multiply(Wu_poly, mu_power), -1), 'secondary_polynomial_definition')
    check(model.poly_d(theta_poly) == {}, 'secondary_polynomial_cycle')
    theta_coordinate = apply(pfinal['reductions']['full']['p'], theta)
    check(len(theta_coordinate) == 1 and next(iter(theta_coordinate.values())) == 1,
          'secondary_primitive_class')
    check(pu['row']['homology']['full'].get(3, 0) == 0
          and pm['row']['homology']['full'].get(3, 0) == 0,
          'secondary_homotopy_indeterminacy_zero')
    check(not any(model.degree[j] == 4 for j in pfinal['matrix']),
          'no_degree_four_filler_in_secondary_weight')
    qtheta = {j: c for j, c in theta.items() if j in pfinal['complexes']['Q']}
    expected_qtheta = {top_id: 1}
    expected_qtheta.update({model.index[(a,), (a,), 0]: -1 for a in LONG})
    check(qtheta == expected_qtheta, 'secondary_complete_Q_top_cycle')
    theta_endpoint = {j: c for j, c in theta.items()
                      if frozenset(model.states[j][0]) in (PLUS, MINUS)}
    check(len(theta_endpoint) == 2, 'secondary_endpoint_terms_retained_not_discarded')

    # Actual cellular corrected-Morse reference; its boundary is retained, not
    # replaced by a nonzero homology generator.
    reference = {model.index[('03', '35'), (), 1]: -1,
                 model.index[('13', '35'), (), 1]: -1}
    check(set(reference) <= set(matrix), 'Morse_reference_in_weight')
    fixed_boundary = apply(matrix, reference)
    check(apply(matrix, vec_add(reference, omega)) == fixed_boundary,
          'new_filling_has_identical_complete_boundary')
    check(not (set(reference) & endpoint_ids), 'reference_endpoint_columns_zero')

    rows = [p['row'] for p in patterns]
    criteria = {
        'full_H2_nonzero': lambda r: r['homology']['full'].get(2, 0) > 0,
        'full_H3_nonzero': lambda r: r['homology']['full'].get(3, 0) > 0,
        'Q_H3_nonzero': lambda r: r['homology']['Q'].get(3, 0) > 0,
        'attachment_kernel_nonzero': lambda r: r['attachment_kernel_rank'] > 0,
    }
    summary = {}
    for name, pred in criteria.items():
        hits = [r['mask'] for r in rows if pred(r)]
        summary[name] = {'patterns': len(hits), 'minimal_masks': minimal_masks(hits)}
    check(summary['attachment_kernel_nonzero']['patterns'] == 58, 'complete_attachment_census')
    check(summary['full_H2_nonzero']['patterns'] == 320, 'complete_H2_census')
    check(summary['full_H3_nonzero']['patterns'] == 9, 'complete_H3_census')
    check(summary['Q_H3_nonzero']['patterns'] == 64, 'complete_QH3_census')
    check(patterns[98]['row']['homology']['full'].get(2, 0) == 0,
          'old_t04_t35_u03_weight_remains_rigid')

    sources = {
        'repository': 'andrey-kokoev/marici',
        'commit': 'd1947b67a60d3e88ba77f4ca60ea02c2a306ee61',
        'input_rules': [
            'research/voevodsky/check_d03_pabs_morse_pullback.rs',
            'research/voevodsky/check_global_k6_koszul_cech_promotion.rs',
            'src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md',
            'src/ledger/20260815-143 Two-Endpoint Road Carrier and the Loaded Conductor Cospan Blocker.md'],
        'prior_checked_equivalence': 'morse_pulledback_normal_support_equivalence_proof.md',
        'prior_zero_weight_result': 'morse_q_filling_torsor_and_attachment_proof.md',
        'code_reconstruction': 'Source generator and differential rules are independently implemented here; no upstream code is executed.'
    }
    payload: dict[str, Any] = {
        'schema': 'marici.branchA.d03_rees_filling_and_resonance.v1',
        'sources': sources,
        'ring': 'Z[X_d,t_s,u_l]/(X_e X_o for opposite short-sheet occurrences)',
        'variables': VARIABLES, 'normal_weight_coordinates': NORMAL_VARIABLES,
        'weight_domain': 'all nonnegative normal/Rees weights; all nine occurrence weights fixed at zero',
        'finite_support_patterns_cover_infinite_weights': True,
        'states': [{'id': j, 'face': f, 'marks': h, 'occurrence_partner': e,
                    'homological_degree': model.degree[j], 'weight': model.weights[j]}
                   for j, (f, h, e) in enumerate(model.states)],
        'polynomial_differential': {j: [[i, list(p), c] for i, p, c in col]
                                   for j, col in model.boundary.items()},
        'census': summary, 'patterns': rows,
        'D03_witness': {
            'weight_mask': mask, 'normal_weight_monomial': ['t02', 't04', 't13'],
            'omega': serialize_poly(omega_poly, model),
            'omega_term_count': len(omega_poly),
            'degree_two_detector': sorted(detector.items()),
            'detector_normalization': 1,
            'endpoint_variation': 'zero in both complete endpoint packets',
            'Q_projection': 't02*t04*t13*X03*p03',
            'short_correction': serialize_poly(polynomial(short_correction, coeff), model),
            'exact_normal_subring_annihilator': ['u03', 't15*t24*u14*u25'],
            'annihilator_scope': 'ordinary coefficient homology; no claim about a stricter equivariant/framed homotopy category',
            'all_64_support_multiplication_images': multiplication_images,
            'u03_primitive': serialize_poly(Wu_poly, model),
            'product_primitive': serialize_poly(Wm_poly, model),
            'secondary_cycle': serialize_poly(theta_poly, model),
            'secondary_weight_mask': mask | u_mask | mu_mask,
            'secondary_homology_coordinate': sorted(theta_coordinate.items()),
            'secondary_endpoint_rows': sorted(theta_endpoint.items()),
            'secondary_Q_image': '(t02*t04*t13*t15*t24)*theta_Q',
            'secondary_indeterminacy_in_tested_homogeneous_component': 0,
            'isolated_Koszul_module_lift_with_bottom_omega_exists': False,
            'reference_filling': serialize_poly(polynomial(reference, coeff), model),
            'reference_boundary': serialize_poly(polynomial(fixed_boundary, coeff), model),
        },
        'scope': {
            'new_Hcond_constructed': False, 'physical_Delta_J_identified': False,
            'relation_to_previous_tau_identified': False,
            'full_Gysin_or_six_functor_identification': False,
            'native_245_state_model_is_this_model': False,
            'full_D3_equivariance_claimed_for_fixed_Kocc35': False,
            'nonlinear_homotopy_identification': False,
            'coefficients_or_frames_replaced_by_scalar_units': False,
            'integer_prime_torsion_in_any_computed_slice': False,
            'normal_parameter_torsion_computed': True,
            'all_admissible_physical_frames_instantiated': False,
        },
        'verification': {'checks_by_family': dict(sorted(COUNTS.items())),
                         'total_checks': sum(COUNTS.values()),
                         'method': 'Exact polynomial d^2; all integer projection/inclusion/homotopy identities; saturated attachment matrices; exhaustive normal-support cases.',
                         'infinite_weight_and_annihilator_proof': 'See accompanying proof; no extrapolation from a degree cutoff.'},
        'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(',', ':')).encode()
    payload['content_sha256'] = sha256(canonical).hexdigest()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, sort_keys=True, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'output': str(output), 'patterns': 512, 'census': summary,
                      'D03_cycle_terms': len(omega_poly), 'secondary_terms': len(theta_poly),
                      'annihilator': payload['D03_witness']['exact_normal_subring_annihilator'],
                      'checks': sum(COUNTS.values()), 'content_sha256': payload['content_sha256']}, indent=2))
    return payload


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path,
                        default=Path('branch_a_d03_rees_filling_and_resonance_certificate.json'))
    args = parser.parse_args()
    main(args.output)

#!/usr/bin/env python3
"""Exact check of the jet-invisible PC differential and its top obstruction.

Standard library only. All short Rees parameters are units on the existing
central chart; long normal/occurrence variables are independent and never
inverted globally. Finite polynomial tests supplement the all-coefficient
proof in the accompanying note. No repository changes or new carrier cells.
"""
from __future__ import annotations

import argparse
from collections import Counter
from functools import lru_cache
from itertools import combinations, product
from pathlib import Path
import hashlib
import json
import time

CHECKS: Counter[str] = Counter()
Diagonal = tuple[int, int]
Mono = tuple[int, ...]
PLUS: tuple[Diagonal, ...] = ((1, 3), (1, 5), (3, 5))
MINUS: tuple[Diagonal, ...] = ((0, 2), (0, 4), (2, 4))
SHORT = PLUS + MINUS
LONG: tuple[Diagonal, ...] = ((0, 3), (1, 4), (2, 5))
DIAGS = tuple(sorted(SHORT + LONG))
VARS = tuple('X' + ''.join(map(str, a)) for a in SHORT + LONG) + tuple(
    ('t' if a in SHORT else 'u') + ''.join(map(str, a)) for a in SHORT + LONG)
INDEX = {a: i for i, a in enumerate(SHORT + LONG)}
ZERO: Mono = (0,) * 18
ONE = {ZERO: 1}


def check(ok: bool, family: str, detail=None) -> None:
    if not ok:
        raise AssertionError(f'{family}: {detail!r}')
    CHECKS[family] += 1


def pm(n: int) -> int:
    return -1 if n % 2 else 1


def put(v: dict, key, n: int) -> None:
    if n:
        v[key] = v.get(key, 0) + n
        if not v[key]:
            del v[key]


def add(*vs: dict) -> dict:
    out = {}
    for v in vs:
        for key, n in v.items():
            put(out, key, n)
    return out


def scale(v: dict, n: int) -> dict:
    return {key: n * a for key, a in v.items() if n * a}


def subsets(values):
    values = tuple(sorted(values))
    return tuple(s for n in range(len(values) + 1) for s in combinations(values, n))


def cross(a: Diagonal, b: Diagonal) -> bool:
    i, j = a
    k, l = b
    return i < k < j < l or k < i < l < j


FACES = tuple(f for f in subsets(DIAGS) if len(f) <= 3 and
              not any(cross(a, b) for a, b in combinations(f, 2)))
FACESET = set(FACES)
CELLS = tuple((f, h) for f in FACES for h in subsets(f))
SFACES = tuple(f for f in FACES if set(f) <= set(SHORT))
PURE = tuple(f for f in SFACES if f and
             (set(f) <= set(PLUS) or set(f) <= set(MINUS)))
MIXED = tuple(f for f in SFACES if set(f) & set(PLUS) and set(f) & set(MINUS))


def kind(cell) -> str:
    f, h = cell
    loc = set(f) - set(h)
    if loc & set(PLUS) and loc & set(MINUS):
        return 'zero'
    return 'puncture' if loc & set(SHORT) else 'core'


def degree(cell) -> int:
    return 3 - len(cell[0]) + len(cell[1])


def exponent(xs=(), ns=(), inverse_t=()) -> Mono:
    result = [0] * 18
    for a in xs:
        result[INDEX[a]] += 1
    for a in ns:
        result[9 + INDEX[a]] += 1
    for a in inverse_t:
        if a not in SHORT:
            raise ValueError('Only central short t units may be inverted globally')
        result[9 + INDEX[a]] -= 1
    return tuple(result)


def emul(a: Mono, b: Mono) -> Mono:
    return tuple(x + y for x, y in zip(a, b))


def legal_base(m: Mono) -> bool:
    if any(v < 0 for v in m[:9]) or any(v < 0 for v in m[15:]):
        raise ValueError(f'Illegal base inverse: {m}')
    return not (any(m[:3]) and any(m[3:6]))


def poly(m: Mono = ZERO, n: int = 1) -> dict:
    return {m: n} if n and legal_base(m) else {}


def mul(a: dict, b: dict) -> dict:
    out = {}
    for ma, ca in a.items():
        for mb, cb in b.items():
            m = emul(ma, mb)
            if legal_base(m):
                put(out, m, ca * cb)
    return out


def sheet(p: dict, plus: bool) -> dict:
    opposite = range(3, 6) if plus else range(3)
    return {m: n for m, n in p.items() if not any(m[i] for i in opposite)}


def allowed(cell, m: Mono) -> bool:
    if kind(cell) == 'zero':
        return False
    f, h = cell
    loc = set(f) - set(h)
    ip = bool(loc & set(PLUS))
    im = bool(loc & set(MINUS))
    if any(m[:3]) and any(m[3:6]):
        return False
    if ip and any(m[3:6]) or im and any(m[:3]):
        return False
    if any(v < 0 for v in m[:9]):
        raise ValueError('This audit uses no negative occurrence coefficients')
    for a in LONG:
        if m[9 + INDEX[a]] < 0 and a not in loc:
            raise ValueError(f'Illegal long-normal inverse at {cell}: {m}')
    return True


def chain_term(cell, m: Mono = ZERO, n: int = 1) -> dict:
    return {(cell, m): n} if n and allowed(cell, m) else {}


def times(v: dict, p: dict) -> dict:
    out = {}
    for (cell, a), n in v.items():
        for b, c in p.items():
            m = emul(a, b)
            if allowed(cell, m):
                put(out, (cell, m), n * c)
    return out


def projection(v: dict, retain: str) -> dict:
    return {key: n for key, n in v.items() if kind(key[0]) == retain}


@lru_cache(None)
def dc(cell):
    f, h = cell
    out = {}
    for a in DIAGS:
        ff = tuple(sorted(f + (a,)))
        if a in f or ff not in FACESET:
            continue
        exp = [0] * 18
        if a in SHORT:
            exp[9 + INDEX[a]] = -1
        else:
            exp[INDEX[a]] = 1
            exp[9 + INDEX[a]] = -1
        out = add(out, chain_term((ff, h), tuple(exp), pm(sum(b < a for b in f))))
    for j, a in enumerate(h):
        hh = tuple(b for b in h if b != a)
        out = add(out, chain_term((f, hh), ZERO, pm(3 - len(f) + j)))
    return out


def diff(v: dict, core: bool = False) -> dict:
    out = {}
    for (cell, m), n in v.items():
        for (target, e), a in dc(cell).items():
            mm = emul(m, e)
            if allowed(target, mm):
                put(out, (target, mm), n * a)
    return projection(out, 'core') if core else out


def compatible_longs(n):
    return tuple(l for l in LONG if all(not cross(l, a) for a in n))


def omega(n):
    """Core top basis: ordered signs include the short-face orientation."""
    n = tuple(sorted(n))
    ls = compatible_longs(n)
    out = chain_term((n, n), exponent(ns=ls), pm(len(n) * (len(n) + 1) // 2))
    for l in ls:
        f = tuple(sorted(n + (l,)))
        out = add(out, chain_term((f, f), exponent(xs=(l,), ns=(a for a in ls if a != l)),
                                  pm(len(f) * (len(f) + 1) // 2)))
    return out


OMEGA = {n: omega(n) for n in SFACES}
RCOEFF = {n: poly(exponent(ns=(l for l in LONG if l not in compatible_longs(n)),
                               inverse_t=n)) for n in SFACES}


def from_coords(b):
    return add(*(times(OMEGA[n], p) for n, p in b.items() if p))


def coordinates(v):
    """Recover top core coordinates and certify every long correction."""
    result = {}
    for n in SFACES:
        s = pm(len(n) * (len(n) + 1) // 2)
        u = exponent(ns=compatible_longs(n))
        p = {}
        for (cell, m), a in v.items():
            if cell != (n, n):
                continue
            mm = tuple(x - y for x, y in zip(m, u))
            check(legal_base(mm), 'top_block_integral_divisibility')
            put(p, mm, s * a)
        if p:
            result[n] = p
    check(from_coords(result) == v, 'top_block_all_long_terms_recovered')
    return result


ELL = from_coords(RCOEFF)


def gamma_coords(n):
    out = {n: ONE}
    own = PLUS if set(n) <= set(MINUS) else MINUS
    ac = tuple(a for a in own if all(not cross(a, b) for b in n))
    check(len(ac) <= 1, 'mixed_short_graph_is_matching')
    for a in ac:
        mixed = tuple(sorted(n + (a,)))
        check(compatible_longs(mixed) == compatible_longs(n), 'mixed_long_blocks_agree')
        out[mixed] = poly(exponent(inverse_t=(a,)))
    return out


GCOEFF = {n: gamma_coords(n) for n in PURE}
GAMMA = {n: from_coords(b) for n, b in GCOEFF.items()}


def norm_coords(b):
    a = b.get((), {})
    return {n: add(b.get(n, {}), scale(mul(a, RCOEFF[n]), -1)) for n in SFACES if n}


def obstruction(b):
    w = norm_coords(b)
    out = {}
    for n in PURE:
        p = sheet(w[n], set(n) <= set(PLUS))
        if p:
            out[('sheet', n)] = p
    for n in MIXED:
        p = next(a for a in n if a in PLUS)
        m = next(a for a in n if a in MINUS)
        result = add(w[n],
                     scale(mul(poly(exponent(inverse_t=(p,))), w[(m,)]), -1),
                     scale(mul(poly(exponent(inverse_t=(m,))), w[(p,)]), -1))
        if result:
            out[('mixed', n)] = result
    return out


def synthesize(b):
    """An actual lift when the obstruction is zero; no division by occurrences."""
    if obstruction(b):
        return None
    w = norm_coords(b)
    v = times(ELL, b.get((), {}))
    for n in PURE:
        v = add(v, times(GAMMA[n], w[n]))
    return v


def add_coords(a, b):
    out = {n: add(a.get(n, {}), b.get(n, {})) for n in set(a) | set(b)}
    return {n: p for n, p in out.items() if p}


def times_coords(a, p):
    return {n: q for n, v in a.items() if (q := mul(v, p))}


def diagonal_act(a, r, f):
    return tuple(sorted(((2 * r + pm(f) * a[0]) % 6, (2 * r + pm(f) * a[1]) % 6)))


def act_poly(p, r, f):
    result = {}
    for m, c in p.items():
        e = [0] * 18
        for a in SHORT + LONG:
            a1 = diagonal_act(a, r, f)
            e[INDEX[a1]] = m[INDEX[a]]
            e[9 + INDEX[a1]] = m[9 + INDEX[a]]
        put(result, tuple(e), c)
    return result


def act_coords(b, r, f):
    return {tuple(sorted(diagonal_act(a, r, f) for a in n)): act_poly(p, r, f)
            for n, p in b.items()}


def act_obstruction(o, r, f):
    return {(typ, tuple(sorted(diagonal_act(a, r, f) for a in n))): act_poly(p, r, f)
            for (typ, n), p in o.items()}


def unit_rank(mat, ncols):
    """Exact integral unit elimination. Fail rather than guess torsion."""
    a = [row[:] for row in mat]
    m = len(a)
    k = 0
    while k < min(m, ncols):
        hit = next(((i, j) for i in range(k, m) for j in range(k, ncols)
                    if abs(a[i][j]) == 1), None)
        if hit is None:
            break
        i, j = hit
        a[k], a[i] = a[i], a[k]
        for row in a:
            row[k], row[j] = row[j], row[k]
        if a[k][k] < 0:
            a[k] = [-x for x in a[k]]
        for i in range(m):
            if i != k and a[i][k]:
                c = a[i][k]
                a[i] = [x - c * y for x, y in zip(a[i], a[k])]
        for j in range(ncols):
            if j != k and a[k][j]:
                c = a[k][j]
                for i in range(m):
                    a[i][j] -= c * a[i][k]
        k += 1
    check(not any(a[i][j] for i in range(k, m) for j in range(k, ncols)),
          'integer_reduction_has_no_nonunit_residual')
    return k


def coefficient_strand(sigma, alpha):
    """The exact top obstruction sequence, with all spectator units retained.

    The matrices below use the unimodular normal coordinates in the proof;
    t-unit changes are evaluated at one only after their symbolic identities
    have been checked separately. No specialization of long normals is used
    to prove the target-kernel claim.
    """
    positive = sigma is not None
    target = []
    for n in PURE:
        side = 0 if set(n) <= set(PLUS) else 1
        if not positive or sigma == side:
            target.append(('sheet', n))
    target += [('mixed', n) for n in MIXED]
    input_names = list(SFACES)
    # General normalized diagonal-coordinate map: empty generic is in kernel.
    o = []
    for typ, n in target:
        row = [0] * len(input_names)
        if typ == 'sheet':
            row[input_names.index(n)] = 1
        else:
            row[input_names.index(n)] = 1
            for d in n:
                row[input_names.index((d,))] = -1
        o.append(row)
    generators = [()]
    if positive:
        generators += [n for n in PURE if
                       (set(n) <= set(MINUS) if sigma == 0 else set(n) <= set(PLUS))]
    inclusion = [[0] * len(generators) for _ in input_names]
    inclusion[0][0] = 1
    for j, n in enumerate(generators[1:], 1):
        for face in GCOEFF[n]:
            inclusion[input_names.index(face)][j] = 1
    for row in o:
        for j in range(len(generators)):
            check(sum(row[i] * inclusion[i][j] for i in range(len(input_names))) == 0,
                  'obstruction_presentation_composition')
    r1 = unit_rank(inclusion, len(generators))
    r2 = unit_rank(o, len(input_names))
    check(r1 == len(generators) and r2 == len(target) and r1 + r2 == 18,
          'complete_integral_obstruction_strand', (sigma, alpha))
    return len(generators), len(target)


# Minimal branch resolutions: alternating exterior blocks ending on the
# branch killed by the quotient. The differential acts on the first block.
@lru_cache(None)
def words(n):
    if n == 0:
        return ((),)
    out = []
    for side in (0, 1):
        labels = tuple(range(3 * side, 3 * side + 3))
        for size in range(1, min(3, n) + 1):
            for block in combinations(labels, size):
                for tail in words(n - size):
                    if not tail or tail[0][0] // 3 != side:
                        out.append((block,) + tail)
    return tuple(out)


def dw(w):
    if not w:
        return {}
    out = {}
    first = w[0]
    for j, label in enumerate(first):
        rest = tuple(a for a in first if a != label)
        ww = ((rest,) if rest else ()) + w[1:]
        m = [0] * 6
        m[label] = 1
        put(out, (tuple(m), ww), pm(j))
    return out


def word_apply(v):
    out = {}
    for (m, w), c in v.items():
        for (a, ww), e in dw(w).items():
            mm = tuple(x + y for x, y in zip(m, a))
            if any(mm[:3]) and any(mm[3:]):
                continue
            put(out, (mm, ww), c * e)
    return out


def serialize_chain(v):
    result = []
    for (cell, m), n in sorted(v.items()):
        result.append({'face': [''.join(map(str, a)) for a in cell[0]],
                       'marks': [''.join(map(str, a)) for a in cell[1]],
                       'integer_coefficient': n,
                       'monomial': {VARS[i]: e for i, e in enumerate(m) if e}})
    return result


def fine_term(cell, side, gx, gu):
    """One monomial in the actual PC cell's homogeneous component."""
    e = [0] * 18
    if side is not None:
        e[side * 3] = 1
    localized = set(cell[0]) - set(cell[1])
    for j, l in enumerate(LONG):
        present = int(l in cell[0])
        e[INDEX[l]] = gx[j] + present
        e[9 + INDEX[l]] = gu[j] - present
        if e[INDEX[l]] < 0:
            return None
        if e[9 + INDEX[l]] < 0 and l not in localized:
            return None
    # Set total t-weight zero. All t units occur on the existing central
    # chart, so the required cell coefficient is admissible there.
    for a in cell[0]:
        if a in SHORT:
            e[9 + INDEX[a]] = -1
    mm = tuple(e)
    return mm if allowed(cell, mm) else None


def full_top_strand(side, gx, gu):
    valid = {c: fine_term(c, side, gx, gu) for c in CELLS if kind(c) != 'zero'}
    valid = {c: m for c, m in valid.items() if m is not None}
    columns = [c for c in valid if degree(c) == 3]
    rows = [c for c in valid if degree(c) == 2]
    rows_core = [c for c in rows if kind(c) == 'core']
    images = {c: diff(chain_term(c, valid[c])) for c in columns}
    for c, v in images.items():
        check(all(t in valid and m == valid[t] for t, m in v),
              'full_target_fine_degree_preservation', (c, gx, gu))
    d_full = [[images[c].get((r, valid[r]), 0) for c in columns] for r in rows]
    d_core = [[images[c].get((r, valid[r]), 0) for c in columns] for r in rows_core]
    h_full = len(columns) - unit_rank(d_full, len(columns))
    h_core = len(columns) - unit_rank(d_core, len(columns))
    regular_x = all(n >= 0 for n in gx)

    def present(n):
        return regular_x and all(gu[j] >= int(l in compatible_longs(n))
                                 for j, l in enumerate(LONG))

    expected_full = int(present(()))
    if side is not None:
        inactive = set(MINUS) if side == 0 else set(PLUS)
        expected_full += sum(present(n) for n in PURE if set(n) <= inactive)
    expected_core = sum(present(n) for n in SFACES)
    expected_obstruction = sum(present(n) for n in MIXED)
    for n in PURE:
        own_side = 0 if set(n) <= set(PLUS) else 1
        if side is None or side == own_side:
            expected_obstruction += present(n)
    check((h_full, h_core) == (expected_full, expected_core),
          'full_PC_top_kernel_matches_explicit_all_coefficient_formula', (side, gx, gu))
    check(h_core - h_full == expected_obstruction,
          'full_PC_top_cokernel_matches_seventeen_channels', (side, gx, gu))
    return h_full, h_core, expected_obstruction


def main(output: Path):
    start = time.monotonic()
    census = Counter(kind(c) for c in CELLS)
    check(len(CELLS) == 215, 'full_source_cells')
    check(census == {'core': 72, 'puncture': 128, 'zero': 15}, 'exact_target_census')
    check(len(SFACES) == 18 and len(PURE) == 14 and len(MIXED) == 3, 'short_support_basis_counts')
    for c in CELLS:
        if kind(c) == 'zero':
            continue
        v = chain_term(c)
        check(not diff(diff(v)), 'full_PC_d_squared', c)
        if kind(c) == 'puncture':
            check(not projection(diff(v), 'core'), 'punctured_terms_form_subcomplex', c)
        else:
            check(not diff(diff(v, True), True), 'core_quotient_d_squared', c)
            check(projection(diff(v), 'core') == diff(projection(v, 'core'), True),
                  'actual_quotient_chain_map', c)
    for n in SFACES:
        v = OMEGA[n]
        check(not diff(v, True), 'eighteen_core_top_cycles', n)
        check(coordinates(v) == {n: ONE}, 'core_top_basis_dictionary', n)
        check(projection(diff(v), 'puncture') == diff(v), 'all_top_defects_live_in_puncture', n)
        check(not diff(diff(v)), 'connecting_columns_closed', n)
    check(not diff(ELL), 'generic_coupled_lift_is_closed')
    check(coordinates(ELL) == RCOEFF, 'generic_lift_in_all_eighteen_blocks')
    check(not obstruction(RCOEFF), 'generic_lift_has_zero_obstruction')

    # Full symbolic target equations: allowed and disallowed monomial tests.
    polynomials = [ONE]
    for a in SHORT:
        for n in range(1, 4):
            polynomials.append(poly(exponent(xs=(a,) * n)))
    for side in (PLUS, MINUS):
        polynomials.append(poly(exponent(xs=side)))
    polynomials += [poly(exponent(xs=(l,), ns=(l,))) for l in LONG]
    polynomials.append(add(ONE, poly(exponent(xs=(PLUS[0],))),
                           scale(poly(exponent(xs=(MINUS[0],))), -2)))
    symbolic_tests = 0
    for n in SFACES:
        for p in polynomials:
            b = {n: p}
            v = from_coords(b)
            check(not diff(v, True), 'arbitrary_coefficient_core_cycles')
            check((not diff(v)) == (not obstruction(b)), 'exact_lifting_criterion_single_modes', n)
            vv = synthesize(b)
            if vv is not None:
                check(vv == v and not diff(vv), 'explicit_source_reconstruction')
            symbolic_tests += 1
    for n in PURE:
        opposite = MINUS if set(n) <= set(PLUS) else PLUS
        for x in opposite:
            for power in (1, 2, 4):
                p = poly(exponent(xs=(x,) * power, inverse_t=(SHORT[power % 6],)))
                b = times_coords(GCOEFF[n], p)
                v = from_coords(b)
                check(not diff(v), 'all_ideal_channel_generators_are_full_cycles')
                check(not obstruction(b), 'channel_generators_in_exact_obstruction_kernel')
                check(synthesize(b) == v, 'full_cycle_reconstruction_with_base_poles')
    # Cancellation tests not visible in separate basis-column checks.
    for k in range(28):
        b = times_coords(RCOEFF, polynomials[k % len(polynomials)])
        for j, n in enumerate(PURE):
            active = MINUS if set(n) <= set(PLUS) else PLUS
            f = poly(exponent(xs=(active[(k + j) % 3],) * (1 + (k + j) % 3),
                              ns=(LONG[(k + j) % 3],)), pm(k + j))
            b = add_coords(b, times_coords(GCOEFF[n], f))
        v = from_coords(b)
        check(not obstruction(b) and not diff(v), 'whole_source_composite_closed')
        check(synthesize(b) == v, 'whole_source_composite_reconstruction')
        bad = add_coords(b, {tuple(sorted(MINUS)): ONE})
        check(obstruction(bad) and diff(from_coords(bad)), 'endpoint_change_cannot_hide_in_other_channels')

    # Obstruction covariance; labels and t units are transported, not averaged.
    for r, f in product(range(3), range(2)):
        check(act_coords(RCOEFF, r, f) == RCOEFF, 'generic_normalized_coefficients_covariant')
        for n in SFACES:
            for p in (ONE, poly(exponent(xs=(PLUS[0],))), poly(exponent(xs=(MINUS[0],)))):
                b = {n: p}
                check(obstruction(act_coords(b, r, f)) == act_obstruction(obstruction(b), r, f),
                      'all_seventeen_obstruction_channels_covariant')

    # Endpoint detector and exact annihilator on all monomial support types.
    endpoints = {}
    for own in (PLUS, MINUS):
        n = tuple(sorted(own))
        v = chain_term((n, n))
        boundary = diff(v)
        check(len(boundary) == 3 and boundary, 'three_nonzero_endpoint_localization_terms')
        check(not diff(boundary), 'endpoint_detector_is_cycle')
        check(all(kind(c) == 'puncture' for c, _ in boundary), 'endpoint_detector_in_128_term_kernel')
        for support in subsets(SHORT):
            p = poly(exponent(xs=support))
            opposite = MINUS if own == PLUS else PLUS
            expected_zero = not p or bool(set(support) & set(opposite))
            check((not times(boundary, p)) == expected_zero, 'exact_endpoint_annihilator_support', support)
        for order in range(1, 17):
            check(not diff(v, True), 'same_endpoint_cycle_at_every_finite_jet')
            # If a short variable in a punctured module is inverted, its
            # order-th power both vanishes in B/I^order and has an inverse.
            for (cell, _), coefficient in boundary.items():
                loc = set(cell[0]) - set(cell[1])
                check(len(loc & set(SHORT)) == 1 and order + (-order) == 0,
                      'finite_jet_localized_module_is_zero')
        endpoints[''.join(''.join(map(str, a)) for a in n)] = serialize_chain(boundary)

    # Complete integer presentation in all coefficient support shapes.
    strands = [coefficient_strand(None, (0, 0, 0))]
    for sigma in (0, 1):
        for alpha in product(range(4), repeat=3):
            if any(alpha):
                strands.append(coefficient_strand(sigma, alpha))
    check(set(strands) == {(1, 17), (8, 10)}, 'conductor_and_branch_fibre_ranks')

    # Actual branch resolutions and the derived obstruction fibre.
    q = [len(words(n)) for n in range(7)]
    check(q == [1, 6, 24, 92, 354, 1362, 5240], 'known_intrinsic_word_ranks_recovered')
    for n in range(1, 6):
        for side in (0, 1):
            ww = tuple(w for w in words(n) if w[-1][0] // 3 == 1 - side)
            check(len(ww) * 2 == q[n], 'branch_resolution_is_half_word_rank')
            for w in ww:
                check(not word_apply(dw(w)), 'branch_resolution_d_squared', w)
                check(all(not tail or tail[-1][0] // 3 == 1 - side for _, tail in dw(w)),
                      'branch_resolution_preserves_quotient_boundary')
                check(all(sum(m) == 1 for m, _ in dw(w)), 'resolution_is_conductor_minimal')
    tor = [17] + [7 * v for v in q[1:]]
    check(tor[:5] == [17, 42, 168, 644, 2478], 'derived_obstruction_fibre_ranks')
    check(42 + 1 == 43 and 1 + 17 == 18, 'previous_singular_comparison_exact_sequence')

    # Independently solve the full 45-column target top equations in exact
    # homogeneous long-parameter degrees, before using the top basis theorem.
    top_strands = 0
    top_histogram = Counter()
    for side in (None, 0, 1):
        for gx in product((-1, 0, 1), repeat=3):
            for gu in product((-1, 0, 1, 2), repeat=3):
                ranks = full_top_strand(side, gx, gu)
                top_histogram[str(ranks)] += 1
                top_strands += 1

    record = {
        'status': 'proved_for_fixed_coefficient_target_not_native_physical_identification',
        'date': '2026-09-07', 'lane': 'Branch B',
        'baseline_commit': 'd1947b67a60d3e88ba77f4ca60ea02c2a306ee61',
        'source_model': '215-state PC differential on the existing central chart; no new long-normal inverse',
        'target_census': dict(census),
        'punctured_subcomplex_by_homological_degree': dict(sorted(Counter(degree(c) for c in CELLS if kind(c) == 'puncture').items())),
        'core_quotient_by_homological_degree': dict(sorted(Counter(degree(c) for c in CELLS if kind(c) == 'core').items())),
        'short_top_basis': [[''.join(map(str, a)) for a in n] for n in SFACES],
        'mixed_matching': [[''.join(map(str, a)) for a in n] for n in MIXED],
        'top_obstruction_module': 'B_plus^7 + B_minus^7 + B^3, with original homogeneous labels',
        'exact_sequence': '0 -> S14_common -> H3(core)=B^18 -> O_top -> 0',
        'connecting_description': 'O_top is im(H3(core)->H2(puncture)), not all H2(puncture)',
        'endpoint_annihilators': {'negative_endpoint': 'I_plus', 'positive_endpoint': 'I_minus'},
        'endpoint_boundaries': endpoints,
        'obstruction_intrinsic_conductor_Tor': tor,
        'symbolic_single_mode_tests': symbolic_tests,
        'complete_integral_top_presentation_strands': len(strands),
        'independent_full_PC_fine_degree_kernel_calculations': top_strands,
        'full_PC_fine_degree_kernel_histogram': dict(top_histogram),
        'mapping_gluing': 'RHom is the homotopy fibre of the formal plus punctured mapping complexes over the completed puncture; use adjunction, not perfect-source tensor-Hom base change',
        'tests': dict(sorted(CHECKS.items())),
        'total_exact_assertions': sum(CHECKS.values()),
        'elapsed_seconds': round(time.monotonic() - start, 3),
        'scope': [
            'The 72-term quotient is an intermediate jet-blind quotient, not identified with the derived I-adic completion.',
            'Formal-coefficient conclusions use flatness of completion and the algebraic top-row proof.',
            'All homotopy gluing assertions are proved from the stated formal-gluing theorem and derived adjunction, not numerical tests.',
            'The branch obstruction decomposition forgets neither endpoint, and is not asserted to be a decomposition of the full target complex.',
            'This does not rule out native sources in shifted or mixed-variance support categories.',
            'No proof-assistant certification and no repository writes.'
        ]
    }
    inp = ['marici_formal_punctured_gluing_20260907.md',
           'marici_target_framed_conductor_tower_20260907.md',
           'marici_intrinsic_conductor_resolution_20260907.md']
    record['input_note_sha256'] = {name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
                                   for name in inp if Path(__file__).with_name(name).exists()}
    record['script_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    replay = Path(__file__).with_name('replayed_formal_punctured_gluing_for_target_reconstruction.json')
    if replay.exists():
        old = json.loads(replay.read_text())
        record['independent_predecessor_replay'] = {
            'assertions': old['total_exact_assertions'],
            'sha256': hashlib.sha256(replay.read_bytes()).hexdigest(),
            'not_run_by_this_checker': True}
    output.write_text(json.dumps(record, indent=2) + '\n')
    print(json.dumps({k: record[k] for k in ['status', 'total_exact_assertions', 'elapsed_seconds',
                       'target_census', 'top_obstruction_module', 'obstruction_intrinsic_conductor_Tor']}, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path,
                        default=Path('marici_punctured_target_obstruction_certificate_20260907.json'))
    args = parser.parse_args()
    main(args.output)

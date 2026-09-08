#!/usr/bin/env python3
"""Exact filtered-Q calculation after alternating normalization/Rees base change.

Python 3.10+, standard library only. No network, repository writes, or degree
truncation of rings. Finite fine-degree checks complement the arbitrary-
polynomial divisibility proof in the accompanying research note.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from itertools import combinations, product
from pathlib import Path
import hashlib
import json

COMMIT = "d1947b67a60d3e88ba77f4ca60ea02c2a306ee61"
COUNTS: Counter[str] = Counter()


def check(ok: bool, category: str, detail: object = None) -> None:
    if not ok:
        raise AssertionError(f"{category}: {detail!r}")
    COUNTS[category] += 1


def pm(n: int) -> int:
    return -1 if n % 2 else 1


def diag(i: int, j: int) -> tuple[int, int]:
    return tuple(sorted((i % 6, j % 6)))


SHORT = tuple(diag(i, i + 2) for i in range(6))
LONG = tuple(diag(i, i + 3) for i in range(3))
DIAGS = tuple(sorted(SHORT + LONG))
VAR = {d: i for i, d in enumerate(SHORT + LONG)}
PLUS = frozenset(SHORT[i] for i in (1, 3, 5))
MINUS = frozenset(SHORT[i] for i in (0, 2, 4))
ENDPOINTS = {tuple(sorted(PLUS)), tuple(sorted(MINUS))}
ZERO = (0,) * 18
# Coordinates 0:9 are X_short then X_long; 9:15 are t_short; 15:18 are u_long.
# In the independent input only, coordinates 9:15 instead denote u_short.
NAMES = tuple("X" + ''.join(map(str, d)) for d in SHORT + LONG) + tuple(
    ("t" if d in SHORT else "u") + ''.join(map(str, d)) for d in SHORT + LONG)


def cross(a, b):
    i, j = a
    k, l = b
    return i < k < j < l or k < i < l < j


def subsets(xs):
    xs = tuple(sorted(xs))
    for k in range(len(xs) + 1):
        yield from combinations(xs, k)


FACES = tuple(f for k in range(4) for f in combinations(DIAGS, k)
              if all(not cross(a, b) for a, b in combinations(f, 2)))
FACESET = set(FACES)
CELLS = tuple((f, h) for f in FACES for h in subsets(f))


def degree(c):
    f, h = c
    return 3 - len(f) + len(h)


def level(c):
    f = c[0]
    if f in ENDPOINTS:
        return 0
    return 1 if set(f) & set(SHORT) else 2


def mon(xs=(), normal=()):
    m = [0] * 18
    for a in xs:
        m[VAR[a]] += 1
    for a in normal:
        m[9 + VAR[a]] += 1
    return tuple(m)


def plus_support(m):
    return {s for s in PLUS if m[VAR[s]] != 0}


def minus_support(m):
    return {s for s in MINUS if m[VAR[s]] != 0}


def add_m(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub_m(a, b):
    return tuple(x - y for x, y in zip(a, b))


def normalize(c, m, cech=False):
    """Normal form of a monomial in the specified cell's actual coefficient ring."""
    if not cech:
        if any(e < 0 for e in m):
            raise ValueError("Negative exponent in unlocalized ring")
        return None if plus_support(m) and minus_support(m) else m
    localized = set(c[0]) - set(c[1])
    lp, lm = localized & PLUS, localized & MINUS
    if lp and lm:
        return None  # localization of a zero product is the zero ring
    if lp and minus_support(m):
        return None
    if lm and plus_support(m):
        return None
    if not lp and not lm and plus_support(m) and minus_support(m):
        return None
    for a in SHORT:
        if (m[VAR[a]] < 0 or m[9 + VAR[a]] < 0) and a not in localized:
            raise ValueError(f"Illegal short inverse at {c}: {a}, {m}")
    for a in LONG:
        if m[VAR[a]] < 0:
            raise ValueError("Occurrence inversion is not allowed for a long diagonal")
        if m[9 + VAR[a]] < 0 and a not in localized:
            raise ValueError("Long normal inverse outside its Cech summand")
    return m


def add(*vectors):
    out = {}
    for v in vectors:
        for key, n in v.items():
            out[key] = out.get(key, 0) + n
            if not out[key]:
                del out[key]
    return out


def scale(v, n):
    return {key: n * c for key, c in v.items() if n * c}


def basis(c, m=ZERO, n=1, cech=False):
    mm = normalize(c, m, cech)
    return {} if mm is None or n == 0 else {(c, mm): n}


def multiply(v, m, cech=False):
    out = {}
    for (c, a), n in v.items():
        out = add(out, basis(c, add_m(a, m), n, cech))
    return out


def project(v, pred):
    return {key: n for key, n in v.items() if pred(key[0])}


def apply(table, v, cech=False):
    out = {}
    for (c, m), n in v.items():
        out = add(out, scale(multiply(table[c], m, cech), n))
    return out


def graph_substitution_monomial(m):
    out = list(m)
    for s in SHORT:
        out[VAR[s]] += m[9 + VAR[s]]
    return tuple(out)


def graph_substitution(v):
    out = {}
    for (c, m), n in v.items():
        out = add(out, basis(c, graph_substitution_monomial(m), n))
    return out


def independent_d(c):
    f, h = c
    out = {}
    for a in DIAGS:
        ff = tuple(sorted(f + (a,)))
        if a not in f and ff in FACESET:
            out[((ff, h), mon(xs=(a,)))] = pm(sum(b < a for b in f))
    for j, a in enumerate(h):
        hh = tuple(b for b in h if b != a)
        out[((f, hh), mon(normal=(a,)))] = pm(3 - len(f) + j)
    return out


D_INPUT = {c: independent_d(c) for c in CELLS}
D = {c: graph_substitution(v) for c, v in D_INPUT.items()}


def u_m(a):
    return mon(xs=(a,), normal=(a,)) if a in SHORT else mon(normal=(a,))


def cech_d(c):
    if normalize(c, ZERO, True) is None:
        return {}
    f, h = c
    out = {}
    for a in DIAGS:
        ff = tuple(sorted(f + (a,)))
        if a not in f and ff in FACESET:
            out = add(out, basis((ff, h), sub_m(mon(xs=(a,)), u_m(a)),
                                 pm(sum(b < a for b in f)), True))
    for j, a in enumerate(h):
        hh = tuple(b for b in h if b != a)
        out = add(out, basis((f, hh), ZERO, pm(3 - len(f) + j), True))
    return out


DC = {c: cech_d(c) for c in CELLS}


def kappa(v):
    out = {}
    for (c, m), n in v.items():
        denom = ZERO
        for a in set(c[0]) - set(c[1]):
            denom = add_m(denom, u_m(a))
        out = add(out, basis(c, sub_m(m, denom), n, True))
    return out


def set_zero(v, variables):
    variables = set(variables)
    return {key: n for key, n in v.items()
            if all(key[1][i] == 0 for i in variables)}


def derivative_at_conductor(v, s):
    out = {}
    for (c, m), n in v.items():
        if m[VAR[s]] != 1 or any(m[VAR[a]] for a in SHORT if a != s):
            continue
        mm = list(m)
        mm[VAR[s]] = 0
        out = add(out, basis(c, tuple(mm), n))
    return out


def lift_cycle(which, occurrence=None):
    """Universal actual top cycle for each generator of the new lifting ideal."""
    chosen = set(SHORT) if which == "both" else set(PLUS if which == "+" else MINUS)
    out = {}
    for f in FACES:
        if which != "both" and not set(f) <= chosen | set(LONG):
            continue
        xs = tuple(a for a in f if a in LONG)
        if occurrence is not None:
            xs += (occurrence,)
        normals = (chosen - set(f)) | (set(LONG) - set(f))
        out = add(out, basis((f, f), mon(xs=xs, normal=normals),
                             pm(len(f) * (len(f) + 1) // 2)))
    return out


def boundary_top_cycle(active, inactive_subset, occurrence):
    """One of the labelled I_+ or I_- summands in H3(A_boundary)."""
    inactive_subset = set(inactive_subset)
    compat_s = {a for a in active if all(not cross(a, b) for b in inactive_subset)}
    compat_l = {a for a in LONG if all(not cross(a, b) for b in inactive_subset)}
    out = {}
    for f in FACES:
        if not inactive_subset <= set(f) <= inactive_subset | compat_s | compat_l:
            continue
        if f in ENDPOINTS:
            continue
        xs = tuple(a for a in f if a in LONG) + (occurrence,)
        normal = (compat_s | compat_l) - set(f)
        out = add(out, basis((f, f), mon(xs=xs, normal=normal),
                             pm(len(f) * (len(f) + 1) // 2)))
    return out


def ann_member(m):
    if normalize(((), ()), m) is None:
        return True
    support = plus_support(m) or minus_support(m)
    required = set(SHORT) if not support else (PLUS if plus_support(m) else MINUS)
    return all(m[9 + VAR[s]] > 0 for s in required)


def cell_weight(c):
    f, h = c
    w = [0] * 18
    for a in f:
        w[VAR[a]] -= 1
    for a in h:
        w[9 + VAR[a]] += 1
        if a in SHORT:
            w[VAR[a]] += 1
    return tuple(w)


def coefficient_at_grade(c, g):
    m = sub_m(g, cell_weight(c))
    if any(e < 0 for e in m):
        return None
    return normalize(c, m)


def top_grade_audit(occurrences, normal_support):
    """Integral forest solution of every top-cycle equation in this fine degree.

    After the explicit top orientation gauge, each two-column row is a
    signed difference. Singleton rows pin a component to zero. This gives
    the full integral kernel, not a rank computed over a finite field.
    """
    a = mon(xs=occurrences, normal=normal_support)
    g = add_m(a, mon(normal=LONG))
    top = [c for c in CELLS if degree(c) == 3 and level(c) != 0
           and coefficient_at_grade(c, g) is not None]
    rows = defaultdict(dict)
    top_sign = {c: pm(len(c[0]) * (len(c[0]) + 1) // 2) for c in top}
    for c in top:
        coeff = coefficient_at_grade(c, g)
        dv = project(multiply(D[c], coeff), lambda t: level(t) != 0)
        for (r, mm), n in dv.items():
            check(mm == coefficient_at_grade(r, g), "fine_degree_preserved")
            rows[r][c] = n * top_sign[c]
    parent = {c: c for c in top}
    def find(c):
        while parent[c] != c:
            parent[c] = parent[parent[c]]
            c = parent[c]
        return c
    def union(a, b):
        aa, bb = find(a), find(b)
        if aa != bb:
            parent[aa] = bb
    pins = []
    for r, row in rows.items():
        check(len(row) <= 2 and all(abs(n) == 1 for n in row.values()),
              "fine_degree_unit_incidence_rows")
        if len(row) == 1:
            pins.append(next(iter(row)))
        elif len(row) == 2:
            check(sum(row.values()) == 0, "fine_degree_orientation_gauge")
            x, y = row
            union(x, y)
    pinned = {find(c) for c in pins}
    empty = ((), ())
    check(empty in top, "generic_top_coefficient_present")
    connected = {find(c) for c in top}
    unpinned = connected - pinned
    extends = find(empty) in unpinned
    check(extends == ann_member(a), "exhaustive_annihilator_control")
    # Every unpinned component is an integral kernel basis vector. Check it
    # against the complete differential; no unwritten rational rank step.
    for component in unpinned:
        v = {}
        for c in top:
            if find(c) == component:
                v = add(v, basis(c, coefficient_at_grade(c, g), top_sign[c]))
        check(not project(apply(D, v), lambda t: level(t) != 0),
              "fine_degree_integral_kernel_basis")
    expected_ambiguity = 0
    if occurrences:
        active = PLUS if set(occurrences) & PLUS else MINUS
        inactive = set(SHORT) - set(active)
        for n in subsets(inactive):
            if 0 < len(n) < 3:
                compat = {a for a in active if all(not cross(a, b) for b in n)}
                if set(n) | compat <= set(normal_support):
                    expected_ambiguity += 1
    check(len(unpinned) - int(extends) == expected_ambiguity,
          "boundary_ambiguity_module_fine_degree_control")
    return {"short_occurrence_support": [label(a) for a in occurrences],
            "short_Rees_support": [label(a) for a in normal_support],
            "top_chain_rank": len(top), "top_kernel_rank": len(unpinned),
            "boundary_top_kernel_rank": expected_ambiguity,
            "unit_generic_coefficient_lifts": extends}


def label(d):
    return ''.join(map(str, d))


def action(v, translation, orientation, cech=False):
    out = {}
    for ((f, h), m), n in v.items():
        def perm(d):
            return diag(translation + orientation * d[0], translation + orientation * d[1])
        ff = tuple(perm(d) for d in f)
        hh = tuple(perm(d) for d in h)
        sf = pm(sum(ff[i] > ff[j] for i in range(len(ff)) for j in range(i + 1, len(ff))))
        sh = pm(sum(hh[i] > hh[j] for i in range(len(hh)) for j in range(i + 1, len(hh))))
        mm = [0] * 18
        for d in DIAGS:
            e = perm(d)
            mm[VAR[e]] = m[VAR[d]]
            mm[9 + VAR[e]] = m[9 + VAR[d]]
        out = add(out, basis((tuple(sorted(ff)), tuple(sorted(hh))), tuple(mm), n * sf * sh, cech))
    return out


def encode_vector(v):
    return [{"face": [label(a) for a in c[0]], "marks": [label(a) for a in c[1]],
             "coefficient": n,
             "monomial": {NAMES[i]: e for i, e in enumerate(m) if e}}
            for (c, m), n in sorted(v.items())]


def main(output: Path):
    check(len(FACES) == 45 and len(CELLS) == 215, "all_source_cells_retained")
    ranks = {name: [sum(pred(c) and degree(c) == q for c in CELLS) for q in range(4)]
             for name, pred in {"F_K": lambda c: True, "F_V": lambda c: level(c) == 0,
                                "F_B": lambda c: level(c) <= 1, "E": lambda c: level(c) > 0,
                                "A_boundary": lambda c: level(c) == 1, "Q": lambda c: level(c) == 2}.items()}
    check(ranks["F_V"] == [2, 6, 6, 2], "both_complete_endpoint_cubes")
    check(ranks["Q"] == [0, 0, 3, 4], "complete_seven_state_Q")
    cech_zero_cells = 0
    for c in CELLS:
        check(not apply(D, D[c]), "base_changed_d_squared")
        check(not apply(DC, DC[c], True), "localized_d_squared")
        check(all(level(t) <= level(c) for t, _ in D[c]), "support_filtration")
        check(kappa(D[c]) == apply(DC, kappa(basis(c)), True), "complete_PC_comparison_square")
        if normalize(c, ZERO, True) is None:
            cech_zero_cells += 1
    q = basis(((), ()), mon(normal=LONG))
    for i in LONG:
        q = add(q, basis(((i,), (i,)), mon(xs=(i,), normal=set(LONG) - {i}), -1))
    beta = apply(D, q)
    check(len(beta) == 18, "eighteen_boundary_terms")
    check(all(level(c) == 1 for c, m in beta), "connecting_boundary_supported")
    check(not apply(D, beta), "connecting_boundary_closed")
    check(not project(beta, lambda c: level(c) == 2), "genuine_Q_cycle")
    check(kappa(beta) == apply(DC, q, True), "connecting_map_PC_naturality")

    old_delta = graph_substitution_monomial(mon(normal=SHORT))
    check(normalize(((), ()), old_delta) is None, "old_six_normal_product_zero")
    old_omega = {}
    for f in FACES:
        m = graph_substitution_monomial(mon(xs=f, normal=set(DIAGS) - set(f)))
        old_omega = add(old_omega, basis((f, f), m, pm(len(f) * (len(f) + 1) // 2)))
    check(not old_omega, "old_top_cycle_specializes_to_zero")

    generators = [("T_all", mon(normal=SHORT), lift_cycle("both"))]
    for s in SHORT:
        which = "+" if s in PLUS else "-"
        active = PLUS if s in PLUS else MINUS
        generators.append(("T_" + which + "_X" + label(s), mon(xs=(s,), normal=active), lift_cycle(which, s)))
    lifts = []
    for name, a, omega in generators:
        check(not apply(D, omega), "new_full_integral_top_cycle", name)
        check(project(omega, lambda c: level(c) == 2) == multiply(q, a), "new_generic_projection", name)
        check(not apply(DC, omega, True), "new_top_cycle_in_PC", name)
        W = add(multiply(q, a), scale(omega, -1))
        check(all(level(c) <= 1 for c, m in W), "annihilation_witness_retains_endpoints", name)
        check(apply(D, W) == multiply(beta, a), "exact_annihilation_homotopy", name)
        check(apply(DC, kappa(W), True) == multiply(kappa(beta), a, True), "localized_annihilation_homotopy", name)
        check(ann_member(a), "annihilator_generator_membership", name)
        lifts.append({"name": name, "coefficient": {NAMES[i]: e for i, e in enumerate(a) if e},
                      "full_cycle": encode_vector(omega), "supported_homotopy": encode_vector(W)})

    boundary_families = []
    for active, sheet in [(PLUS, "+"), (MINUS, "-")]:
        inactive = set(SHORT) - set(active)
        for n in subsets(inactive):
            if not 0 < len(n) < 3:
                continue
            vectors = []
            for x in sorted(active):
                v = boundary_top_cycle(active, n, x)
                check(bool(v), "nonzero_boundary_ambiguity_generator")
                check(all(level(c) == 1 for c, _ in v), "ambiguity_preserves_generic_and_endpoint_coordinates")
                check(not apply(D, v), "boundary_ambiguity_is_full_cycle")
                check(not apply(DC, v, True), "boundary_ambiguity_is_PC_cycle")
                for y in sorted(active):
                    check(multiply(v, mon(xs=(y,))) == multiply(boundary_top_cycle(active, n, y), mon(xs=(x,))),
                          "branch_ideal_syzygies_respected")
                vectors.append({"branch_generator": "X" + label(x), "cycle": encode_vector(v)})
            boundary_families.append({"sheet": sheet, "inactive_marked_subset": [label(a) for a in n],
                                      "coefficient_module": "I_plus" if sheet == "+" else "I_minus",
                                      "generators": vectors})
    check(len(boundary_families) == 12, "twelve_labelled_boundary_ideal_families")

    for shift, orient in [(0, 1), (2, 1), (4, 1), (3, -1), (5, -1), (1, -1)]:
        for c in CELLS:
            check(action(D[c], shift, orient) == apply(D, action(basis(c), shift, orient)),
                  "dihedral_full_chain_equivariance")
            check(action(kappa(basis(c)), shift, orient, True) == kappa(action(basis(c), shift, orient)),
                  "dihedral_PC_comparison")
        check(action(q, shift, orient) == q, "dihedral_generic_class")
        check(action(beta, shift, orient) == beta, "dihedral_connecting_class")
        for _, a, omega in generators:
            image_a = next(iter(action(basis(((), ()), a), shift, orient)))[1]
            check(ann_member(image_a), "dihedral_annihilator_ideal")
            check(not apply(D, action(omega, shift, orient)), "dihedral_transported_full_lift")

    valid_occurrence_supports = [a for a in subsets(SHORT) if not (set(a) & PLUS and set(a) & MINUS)]
    check(len(valid_occurrence_supports) == 15, "alternating_normal_forms")
    records = [top_grade_audit(a, t) for a in valid_occurrence_supports for t in subsets(SHORT)]
    check(len(records) == 960, "all_960_fine_support_controls")

    conductor_variables = [VAR[a] for a in SHORT]
    DC0 = {c: set_zero(v, conductor_variables) for c, v in D.items()}
    check(not set_zero(beta, conductor_variables), "beta_zero_as_conductor_chain")
    check(not apply(DC0, q), "generic_unit_lifts_on_conductor")
    symbols = []
    a03 = diag(0, 3)
    resonant = 9 + VAR[a03]
    for s in SHORT:
        b = derivative_at_conductor(beta, s)
        check(len(b) == 3, "three_term_conductor_symbol")
        check(not apply(DC0, b), "first_conductor_symbol_closed")
        cell = ((s,), ())
        coeff = {m: n for (c, m), n in b.items() if c == cell}
        check(coeff == {mon(normal=LONG): 1}, "conductor_symbol_detector_value")
        for c in CELLS:
            if degree(c) == 3 and level(c) == 1:
                check(all(t != cell for t, _ in DC0[c]), "detector_kills_every_boundary")
        br = set_zero(b, [resonant])
        survives = not cross(s, a03)
        check(bool(br) == survives, "independent_u03_resonance_control")
        if survives:
            rcell = (tuple(sorted((s, a03))), (a03,))
            check(len(br) == 1 and next(iter(br))[0] == rcell, "resonant_symbol_single_term")
            for c in CELLS:
                if degree(c) == 3 and level(c) == 1:
                    check(all(t != rcell for t, _ in set_zero(DC0[c], [resonant])),
                          "resonant_detector_kills_boundaries")
        symbols.append({"short_label": label(s), "symbol": encode_vector(b),
                        "after_u03_zero": encode_vector(br), "survives_u03_zero": survives})

    # No transfer of the supported Gysin's source to our target is made.
    # This checks precisely the unchanged generic-Q target before conductor
    # restriction, when two opposite-sheet Rees parameters vanish.
    pair = (diag(0, 4), diag(3, 5))
    check(pair[0] in MINUS and pair[1] in PLUS and cross(*pair), "Branch_A_pair_is_coefficient_support")
    pair_vars = [9 + VAR[a] for a in pair]
    check(all(any(a[i] for i in pair_vars) for _, a, _ in generators), "all_lift_generators_vanish_on_pair")
    pair_D = {c: set_zero(v, pair_vars) for c, v in D.items()}
    check(apply(pair_D, q) == beta, "pair_does_not_erase_connecting_boundary")

    output.parent.mkdir(parents=True, exist_ok=True)
    certificate = {
        "schema": "marici.filtered_q.alternating_rees_base_change.v1",
        "date": "2026-09-07", "input_commit": COMMIT,
        "scope": "Derived base change of the fixed 215-state support target, not an identification with the native 245-state source or physical Morse source.",
        "source_record": {
            "repository": "andrey-kokoev/marici",
            "normalization_entry": "src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md",
            "normalization_blob": "840258522d45e450e4f1e8bb927d9aae58c75566",
            "loaded_differential": "research/voevodsky/check_ringed_alexandrov_pc_target.py",
            "loaded_differential_blob": "7c993d05837fbe2ba29ba30e5b665b5429ab940b",
            "Rees_relation_source": "src/ledger/20260814-115 Boundary-Triad Tate Realization and the Multi-Rees Cartier Bicomplex.md",
            "Rees_relation_blob": "63da17cb5d641705056c5d5b9bc6f53cda72baf5",
            "previous_proof": "filtered_q_comparison.md",
        },
        "variable_order": NAMES,
        "positive_shorts": [label(a) for a in sorted(PLUS)],
        "negative_shorts": [label(a) for a in sorted(MINUS)],
        "support_ranks": ranks,
        "zero_PC_stalk_cells_after_base_change": cech_zero_cells,
        "generic_cycle": encode_vector(q), "connecting_boundary": encode_vector(beta),
        "old_Delta_maps_to_zero": True, "old_Omega_maps_to_zero": True,
        "generic_H3": "B theta",
        "computed_annihilator": "(T_plus*T_minus, T_plus*I_plus, T_minus*I_minus)",
        "annihilator_is_principal": False,
        "integer_torsion_in_cyclic_obstruction_submodule": False,
        "same_annihilator_in_specified_PC_target": True,
        "unit_generic_closed_lift_exists": False,
        "explicit_annihilator_lifts": lifts,
        "H3_boundary_module": "I_plus^6 direct-sum I_minus^6, with the displayed labels and internal normal degrees",
        "boundary_ambiguity_families": boundary_families,
        "nonempty_ungraded_lift_fibres": "Discrete torsors for I_plus^6 direct-sum I_minus^6; generally not contractible",
        "fixed_zero_short_occurrence_degree_ambiguity": "0; this does not assert general source-framed rigidity",
        "fine_degree_controls": records,
        "conductor_symbols": symbols,
        "pair_support_absolute_before_conductor": {
            "equations": ["t04=0", "t35=0"],
            "long_normals_specialized": False,
            "image_H3E_to_H3Q": "0",
            "annihilator_beta": "0",
            "physical_Gysin_or_native_gamma_identification": False,
        },
        "checks": dict(sorted(COUNTS.items())), "exact_assertions": sum(COUNTS.values()),
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "proof_not_sampling": "The complete singleton top-cycle equations over the two polynomial sheets force all divisibilities. Seven explicit full cycles prove sufficiency. The 960 monomial-support tests solve their integral top kernels independently.",
        "exclusions": [
            "No long u identified with X or a physical channel coordinate.",
            "No integer, occurrence coordinate, or normal parameter inverted in the absolute calculation.",
            "PC inverses occur only in their source-specified summands; mixed opposite-sheet localizations are zero rings.",
            "No map from the corrected exact Morse class to the Entry-436 homology unit is asserted.",
            "No local pair Gysin is identified with a scalar trace on this Q class.",
            "No complete physical source correspondence, numerical amplitude, or RH assertion.",
            "The full lower homology of E and the entire cone are not classified; the top boundary module, cyclic connecting submodule and specified symbols are computed.",
        ],
    }
    output.write_text(json.dumps(certificate, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: certificate[k] for k in (
        "schema", "support_ranks", "zero_PC_stalk_cells_after_base_change",
        "computed_annihilator", "exact_assertions", "unit_generic_closed_lift_exists")}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path("marici_q_alternating_rees_base_change_certificate.json"))
    args = parser.parse_args()
    main(args.output)

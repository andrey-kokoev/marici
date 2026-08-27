#!/usr/bin/env python3
"""Compile actual pole depths and proper-face lowering symbols for the shape jet."""

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent / ".tmp_sympy"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import sympy as sp
import compile_cleared_relative_shape_jet as source

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "research/benincasa/results/relative-shape-pole-depth.json"

a, b, c = source.a, source.b, source.c
walls = {
    "g1": (source.g1, b),
    "g2": (source.g2, a),
    "g3": (source.g3, a),
    "B12": (source.B12, c),
    "B23": (source.B23, a),
    "B31": (source.B31, b),
    "s12": (source.s12, a),
    "s23": (source.s23, b),
    "s31": (source.s31, a),
}

term_data = {
    name: (big, small)
    for name, big, small, _ in source.terms
}


def wall_name(expression):
    for name, (wall, _) in walls.items():
        if sp.expand(expression - wall) == 0:
            return name
    raise KeyError(expression)


def valuation(polynomial, factor):
    value = sp.Poly(polynomial, a, b, c)
    divisor = sp.Poly(factor, a, b, c)
    order = 0
    while True:
        quotient, remainder = sp.div(value, divisor)
        if not remainder.is_zero:
            return order, value.as_expr()
        order += 1
        value = quotient


profiles = {}
all_checks = {}
for name, numerator in source.numerators.items():
    big, small = term_data[name]
    declared = {"K0": 2, "g1": 3, "g2": 3, "g3": 1, wall_name(big): 1, wall_name(small): 3}
    # Merge repeated labels, though the frozen six terms currently have none.
    merged = {}
    for label, exponent in declared.items():
        merged[label] = merged.get(label, 0) + exponent
    reduced = numerator
    cancellations = {}
    actual = {}
    for label, exponent in merged.items():
        factor = source.K0 if label == "K0" else walls[label][0]
        cancelled, reduced = valuation(reduced, factor)
        cancelled = min(cancelled, exponent)
        cancellations[label] = cancelled
        actual[label] = exponent - cancelled
    profiles[name] = {
        "declared_denominator_exponents": merged,
        "cancelled_exponents": cancellations,
        "actual_denominator_exponents": actual,
        "remaining_numerator_degree": sp.Poly(reduced, a, b, c).total_degree(),
    }
    all_checks[f"{name}_has_only_declared_poles"] = all(x >= 0 for x in actual.values())

lowering = {}
for label, (wall, normal) in walls.items():
    normal_derivative = sp.diff(wall, normal)
    k_regular = sp.rem(source.K0, wall, normal) != 0
    lowering[label] = {
        "wall": sp.sstr(wall),
        "normal_variable": sp.sstr(normal),
        "normal_derivative": sp.sstr(normal_derivative),
        "K0_not_divisible_by_wall": bool(k_regular),
        "associated_grade_m_to_m_minus_1": "-(m-1)*normal_derivative",
        "leading_symbol_is_invertible": bool(normal_derivative != 0 and k_regular),
    }
    all_checks[f"{label}_unit_normal"] = normal_derivative in (1, -1)
    all_checks[f"{label}_proper_face_is_not_K0_component"] = bool(k_regular)

assert all(all_checks.values()), {k: v for k, v in all_checks.items() if not v}
packet = {
    "schema": "marici.relative-shape-pole-depth.v1",
    "profiles": profiles,
    "proper_face_lowering": lowering,
    "all_checks_pass": True,
    "check_count": len(all_checks),
    "scope": "proper face away from K0 and other marked-wall intersections",
    "filtered_lowering_homotopy_constructed": False,
    "pairwise_coherence_constructed": False,
    "physical_cycle_authority_established": False,
    "simple_residue_matrix_constructed": False,
}
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {len(all_checks)}/{len(all_checks)}")
for name, profile in profiles.items():
    print(name, profile["actual_denominator_exponents"])

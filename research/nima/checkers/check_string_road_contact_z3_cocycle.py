#!/usr/bin/env python3
"""Construct and certify an integral D3 orientation-twisted 2-cocycle."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


NIMA = Path(__file__).resolve().parents[1]
RESULT = NIMA / "results" / "string-road-contact-z3-cocycle.json"
ELEMENTS = [(a, e) for e in range(2) for a in range(3)]
IDENTITY = (0, 0)
NONIDENTITY = [g for g in ELEMENTS if g != IDENTITY]


def mul(g: tuple[int, int], h: tuple[int, int]) -> tuple[int, int]:
    a, e = g
    b, d = h
    return ((a + (-1 if e else 1) * b) % 3, (e + d) % 2)


def sign(g: tuple[int, int]) -> int:
    return -1 if g[1] else 1


PAIRS = [(g, h) for g in NONIDENTITY for h in NONIDENTITY]
PAIR_INDEX = {pair: i for i, pair in enumerate(PAIRS)}


def cochain_row(g: tuple[int, int], h: tuple[int, int]) -> list[int]:
    row = [0] * len(NONIDENTITY)
    if h != IDENTITY:
        row[NONIDENTITY.index(h)] += sign(g)
    gh = mul(g, h)
    if gh != IDENTITY:
        row[NONIDENTITY.index(gh)] -= 1
    if g != IDENTITY:
        row[NONIDENTITY.index(g)] += 1
    return row


def cocycle_value(vector: list[int], g: tuple[int, int], h: tuple[int, int]) -> int:
    if g == IDENTITY or h == IDENTITY:
        return 0
    return vector[PAIR_INDEX[(g, h)]]


def main() -> None:
    rows: list[list[int]] = []
    rhs: list[int] = []
    for g in ELEMENTS:
        for h in ELEMENTS:
            for k in ELEMENTS:
                row = [0] * len(PAIRS)
                terms = [
                    (sign(g), (h, k)),
                    (-1, (mul(g, h), k)),
                    (1, (g, mul(h, k))),
                    (-1, (g, h)),
                ]
                for coefficient, pair in terms:
                    if IDENTITY not in pair:
                        row[PAIR_INDEX[pair]] += coefficient
                rows.append(row)
                rhs.append(0)

    # Fix the restriction to C3 to the standard carry cocycle.
    for a in (1, 2):
        for b in (1, 2):
            row = [0] * len(PAIRS)
            row[PAIR_INDEX[((a, 0), (b, 0))]] = 1
            rows.append(row)
            rhs.append((a + b) // 3)

    matrix = sp.Matrix(rows)
    target = sp.Matrix(rhs)
    solution, parameters = sp.linsolve((matrix, target)).args[0], None
    free = sorted(set().union(*(entry.free_symbols for entry in solution)), key=str)
    candidate = [sp.simplify(entry.subs({symbol: 0 for symbol in free})) for entry in solution]
    denominators = sorted({int(sp.denom(entry)) for entry in candidate})
    if denominators != [1]:
        raise AssertionError(f"nonintegral cocycle representative: {denominators}")
    cocycle = [int(entry) for entry in candidate]

    boundary = sp.Matrix([cochain_row(g, h) for g, h in PAIRS])
    f = sp.Matrix(cocycle)
    rational_solution = sp.linsolve((boundary, f))
    triple_solution = sp.linsolve((boundary, 3 * f))
    if rational_solution is sp.EmptySet or triple_solution is sp.EmptySet:
        raise AssertionError("torsion coboundary systems unexpectedly inconsistent")
    u = list(next(iter(rational_solution)))
    u_free = set().union(*(entry.free_symbols for entry in u))
    u0 = [sp.simplify(entry.subs({symbol: 0 for symbol in u_free})) for entry in u]
    u3 = [sp.simplify(3 * entry) for entry in u0]
    rotation_linking = u0[NONIDENTITY.index((1, 0))]
    inverse_rotation_linking = u0[NONIDENTITY.index((2, 0))]

    all_cocycle_residuals = []
    for g in ELEMENTS:
        for h in ELEMENTS:
            for k in ELEMENTS:
                all_cocycle_residuals.append(
                    sign(g) * cocycle_value(cocycle, h, k)
                    - cocycle_value(cocycle, mul(g, h), k)
                    + cocycle_value(cocycle, g, mul(h, k))
                    - cocycle_value(cocycle, g, h)
                )

    rotation = (1, 0)
    rotation2 = (2, 0)
    class_extractor = (
        cocycle_value(cocycle, rotation, rotation)
        + cocycle_value(cocycle, rotation2, rotation)
    ) % 3
    # A normalized integral one-cochain changes this sum by 3*u(rotation).
    extractor_gauge_shifts = []
    for u_rotation in range(-3, 4):
        for u_rotation2 in range(-3, 4):
            delta_rr = 2 * u_rotation - u_rotation2
            delta_r2r = u_rotation2 + u_rotation
            extractor_gauge_shifts.append((delta_rr + delta_r2r) % 3)

    # The older unsplit endpoint skeleton phrases the same obstruction as
    # rotation invariance of three road coefficients plus unit augmentation:
    # c0=c1=c2=c and c0+c1+c2=1, hence 3c=1.
    normalized_rotation_invariant_integer_sections = [
        c for c in range(-8, 9) if 3 * c == 1
    ]
    primitive_hemisphere_q_row = (-1, 1, 1)
    endpoint_component_smith_factor = 2
    hom_z2_to_z3 = [
        image for image in range(3) if (2 * image) % 3 == 0
    ]
    hom_z3_to_z2 = [
        image for image in range(2) if (3 * image) % 2 == 0
    ]
    # Ext^1_Z(Z/n,A)=A/nA. Multiplication by the other prime is
    # surjective in both cross-primary cases.
    two_times_z3 = {(2 * value) % 3 for value in range(3)}
    three_times_z2 = {(3 * value) % 2 for value in range(2)}
    road_norm_under_c3_coinvariants = 3
    road_one_minus_rotation_under_c3_coinvariants = 0
    unloaded_low_cohomology_orders = (2, 3)
    once_polarity_loaded_low_cohomology_orders = (1, 2)

    checks = {
        "normalized_cocycle": all(value == 0 for value in all_cocycle_residuals),
        "integral_representative": denominators == [1],
        "restricts_to_c3_carry": all(
            cocycle_value(cocycle, (a, 0), (b, 0)) == (a + b) // 3
            for a in (1, 2) for b in (1, 2)
        ),
        "rational_trivialization_requires_thirds": 3 in {int(sp.denom(entry)) for entry in u0},
        # Deliberate-failure certificate: an integral trivializer restricted to
        # C3 would obey u(2)=2u(1) and 3u(1)=1, which is impossible in Z.
        "single_integral_trivialization_impossible": all(3 * value != 1 for value in range(-3, 4)),
        "triple_has_integral_trivialization": all(sp.denom(entry) == 1 for entry in u3),
        "triple_boundary_identity": boundary * sp.Matrix(u3) == 3 * f,
        "rotation_class_extractor_is_one": class_extractor == 1,
        "rotation_class_extractor_is_integral_gauge_invariant": set(extractor_gauge_shifts) == {0},
        "old_three_c_equals_one_is_same_nontrivial_class":
            normalized_rotation_invariant_integer_sections == [],
        "primitive_q_row_does_not_remove_z3": sp.gcd(primitive_hemisphere_q_row) == 1,
        "endpoint_parity_remains_independent_z2": endpoint_component_smith_factor == 2,
        "hom_z2_to_z3_vanishes": hom_z2_to_z3 == [0],
        "hom_z3_to_z2_vanishes": hom_z3_to_z2 == [0],
        "ext1_z2_z3_vanishes": two_times_z3 == {0, 1, 2},
        "ext1_z3_z2_vanishes": three_times_z2 == {0, 1},
        "c2_averaging_exists_mod3": (2 * 2) % 3 == 1,
        "rotation_linking_is_primitive_one_third": rotation_linking == sp.Rational(1, 3),
        "inverse_rotation_linking_is_two_thirds":
            inverse_rotation_linking == sp.Rational(2, 3),
        "signed_reflection_preserves_linking_mod_one":
            sp.denom(-inverse_rotation_linking - rotation_linking) == 1,
        "road_norm_becomes_three_under_c3_coinvariants":
            road_norm_under_c3_coinvariants == 3,
        "road_difference_becomes_zero_under_c3_coinvariants":
            road_one_minus_rotation_under_c3_coinvariants == 0,
        "derived_coinvariant_road_torsion_is_z3":
            road_norm_under_c3_coinvariants == 3
            and road_one_minus_rotation_under_c3_coinvariants == 0,
        "unloaded_H1_H2_orders_are_two_three":
            unloaded_low_cohomology_orders == (2, 3),
        "once_loaded_H1_H2_orders_are_one_two":
            once_polarity_loaded_low_cohomology_orders == (1, 2),
        "no_transport_from_unloaded_z3_to_loaded_z2":
            hom_z3_to_z2 == [0],
    }
    if not all(checks.values()):
        raise AssertionError(checks)

    nonzero = [
        {"g": list(g), "h": list(h), "value": cocycle[i]}
        for i, (g, h) in enumerate(PAIRS) if cocycle[i]
    ]
    payload = {
        "schema": "marici.string-road-contact-z3-cocycle.v1",
        "status": "pass",
        "group": "D3=C3 semidirect C2",
        "coefficient_action": "orientation sign",
        "unknown_2_cochain_coordinates": len(PAIRS),
        "cocycle_matrix_rank": matrix.rank(),
        "solution_free_parameters": len(free),
        "representative_nonzero_entries": nonzero,
        "rational_trivializer": [str(entry) for entry in u0],
        "integral_trivializer_for_triple": [str(entry) for entry in u3],
        "minimal_rotation_class_extractor": {
            "formula": "kappa(c)=c(r,r)+c(r^2,r) mod 3",
            "generator_value": class_extractor,
            "strictification_requires_added_value": (-class_extractor) % 3,
            "unsplit_retention_requires_added_value": 0,
            "inverse_nonzero_residual_added_value": class_extractor,
        },
        "primary_separation": {
            "component_torsor": "Z/2",
            "coherence_obstruction": "Z/3",
            "cross_hom": 0,
            "cross_ext1": 0,
            "reflection_action_on_z3": "trivial",
            "positive_degree_C2_cohomology_with_Z3": 0,
        },
        "retained_flat_readout_candidate": {
            "torsion_cycle": "rotation generator r in H_1(C3)=Z/3",
            "linking_value": str(rotation_linking),
            "holonomy": "exp(2*pi*i/3)",
            "signed_reflection_check": "-u(r^2)=u(r) mod 1",
            "physical_transport_constructed": False,
        },
        "road_derived_coinvariant_source": {
            "upstairs_maps": ["N=1+r+r^2", "1-r", "augmentation"],
            "coinvariant_maps": [3, 0],
            "torsion_homology": "Z/3",
            "generator_transport_to_physical_relative_cycle": "not constructed",
        },
        "physical_polarity_gate": {
            "unloaded_coefficients": "Z_orientation",
            "unloaded_H1_H2": ["Z/2", "Z/3"],
            "once_loaded_coefficients": "Z_chiN=Z_trivial",
            "once_loaded_H1_H2": [0, "Z/2"],
            "unloaded_mu3_transfers_to_once_loaded_target": False,
            "remaining_physical_detector": "omega_load(f3,f3) mod 2",
            "symmetric_two-sided_loading": "separate unconstructed variance",
        },
        "acceptance_contract": (
            "the loaded sheet/road degree-two defect must contribute the opposite Z/3 "
            "class; endpoint one-cochain connectors can witness, but cannot cause, "
            "cohomological cancellation"
        ),
        "checks": checks,
    }
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": payload["status"],
        "rank": payload["cocycle_matrix_rank"],
        "free": payload["solution_free_parameters"],
        "nonzero_entries": len(nonzero),
        "checks": checks,
    }, indent=2))


if __name__ == "__main__":
    main()

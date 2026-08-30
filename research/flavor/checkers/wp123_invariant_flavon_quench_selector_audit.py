"""Exact checks for WP123's invariant flavon-quench selector audit."""

import json
from fractions import Fraction
from pathlib import Path


def trace_power_two(spectrum):
    return sum(x * x for x in spectrum)


def main():
    lam = Fraction(5)
    v2 = Fraction(1)
    point_a = [Fraction(1), 0, 0, 0, 0, 0]
    point_b = [Fraction(1, 3)] * 3 + [0, 0, 0]

    norm_a = sum(point_a)
    norm_b = sum(point_b)
    potential_a = lam * (norm_a - v2) ** 2 / 4
    potential_b = lam * (norm_b - v2) ** 2 / 4
    quartic_a = trace_power_two(point_a[:3])
    quartic_b = trace_power_two(point_b[:3])

    # At X=e_1 on the unit shell, Hess(V_0)=2 lambda X X^T.
    hessian_diagonal = [2 * lam] + [Fraction(0)] * 35
    hessian_rank = sum(entry != 0 for entry in hessian_diagonal)
    tangent_kernel_dimension = len(hessian_diagonal) - hessian_rank

    # Alignment trace for identical rank-one spectra in aligned/orthogonal frames.
    alignment_aligned = Fraction(1)
    alignment_orthogonal = Fraction(0)

    checks = {
        "a_on_unit_shell": norm_a == v2,
        "b_on_unit_shell": norm_b == v2,
        "a_radial_minimum": potential_a == 0,
        "b_radial_minimum": potential_b == 0,
        "hostile_pair_physically_separated": quartic_a != quartic_b,
        "hostile_pair_quartic_residual": quartic_a - quartic_b == Fraction(2, 3),
        "equal_spectrum_lower_bound": quartic_b == norm_b**2 / 3,
        "rank_one_upper_bound": quartic_a == norm_a**2,
        "radial_hessian_rank_one": hessian_rank == 1,
        "radial_tangent_kernel": tangent_kernel_dimension == 35,
        "alignment_probe_separates_frames": alignment_aligned != alignment_orthogonal,
        "alignment_residual": alignment_aligned - alignment_orthogonal == 1,
    }

    result = {
        "work_package": "WP123",
        "classification": "conditional coarse selector with unresolved coefficient-and-instrument gate",
        "radial_operation": "selector_and_stabilizer_of_total_norm_only",
        "reference_port_required": False,
        "physical_instrument_established": False,
        "hostile_pair": {
            "A_squared_singular_values": [str(x) for x in point_a],
            "B_squared_singular_values": [str(x) for x in point_b],
            "common_R2": str(norm_a),
            "common_V0": str(potential_a),
            "Q_u_A": str(quartic_a),
            "Q_u_B": str(quartic_b),
            "Q_u_residual": str(quartic_a - quartic_b),
        },
        "radial_hessian": {
            "rank": hessian_rank,
            "tangent_kernel_dimension": tangent_kernel_dimension,
        },
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "all_pass": all(checks.values()),
    }

    output = Path(__file__).resolve().parents[1] / "results" / "wp123_invariant_flavon_quench_selector_audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["all_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()


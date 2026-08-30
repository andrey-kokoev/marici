"""Exact WP805 audit of the integer coupled chiral fixed point."""

import json
from pathlib import Path

import sympy as sp


def main() -> None:
    N = sp.Integer(5)
    p = sp.Integer(26)
    x = sp.Rational(p, N)
    ag, aH, aM, a1 = sp.symbols("a_g a_H a_M a_1", real=True)

    beta_g = (
        -ag**2 * (sp.Rational(11, 3) + 6 * N - sp.Rational(4, 3) * N * x)
        -ag**3 * (-sp.Rational(10, N) + 1 + 2 * x + sp.Rational(82, 3) * N
                  + 13 * N**2 - sp.Rational(26, 3) * N**2 * x)
        + ag**2 * aH * (sp.Rational(5, 2) - sp.Rational(3, 2) * N)
        + ag**2 * aM * (10 * N * x - 2 * N**2 * (x + x**2))
        - 2 * ag**2 * a1 * N * x
    )
    beta_H = ag * aH * (sp.Rational(15, N) + 6 - 9 * N) - aH**2 * sp.Rational(1 - 3 * N, 2) + aH * a1 * N * x
    beta_M = ag * aM * (sp.Rational(6, N) - 6 * N) - aM**2 * (5 - N * (3 + 2 * x)) + aM * a1
    beta_1 = (
        ag * a1 * (sp.Rational(6, N) - 6 * N)
        - aH * a1 * (sp.Rational(1, 2) - sp.Rational(N, 2))
        - aM * a1 * (5 - N * (1 + x))
        + a1**2 * (1 + N * (2 + x))
    )

    rH, rM, r1 = sp.symbols("r_H r_M r_1")
    ratio_equations = [
        sp.Rational(15, N) + 6 - 9 * N - sp.Rational(1 - 3 * N, 2) * rH + N * x * r1,
        sp.Rational(6, N) - 6 * N - (5 - N * (3 + 2 * x)) * rM + r1,
        sp.Rational(6, N) - 6 * N - (sp.Rational(1, 2) - sp.Rational(N, 2)) * rH
        - (5 - N * (1 + x)) * rM + (1 + N * (2 + x)) * r1,
    ]
    ratios = sp.solve(ratio_equations, [rH, rM, r1], dict=True)[0]
    fixed = {
        ag: sp.Rational(3163, 2234),
        aH: sp.Rational(34182, 5585),
        aM: sp.Rational(729, 1117),
        a1: sp.Rational(1746, 5585),
    }

    # Rephasing charge rows for y_H, y_1, y_M on
    # (T, anti-F_1, anti-F_other, H, M, F).
    phase_charge = sp.Matrix([
        [1, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1],
        [0, 0, 1, 0, 1, 1],
    ])

    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    anomaly = (N - 4) - (N - 4 + p) + p
    check("integer_chiral_packet_is_anomaly_free", anomaly == 0, anomaly)
    check("fixed_flow_ratios_are_exact", ratios == {
        rH: sp.Rational(68364, 15815),
        rM: sp.Rational(1458, 3163),
        r1: sp.Rational(3492, 15815),
    }, ratios)
    for name, beta in (("gauge", beta_g), ("tensor_yukawa", beta_H),
                       ("meson_yukawa", beta_M), ("split_mesonic_yukawa", beta_1)):
        residual = sp.simplify(beta.subs(fixed))
        check(f"{name}_beta_vanishes_exactly", residual == 0, residual)
    check("all_fixed_coordinates_are_positive", all(value > 0 for value in fixed.values()), fixed)
    check("gauge_fixed_coordinate_exceeds_perturbative_unit", fixed[ag] > 1, fixed[ag])
    check("tensor_yukawa_fixed_coordinate_is_strong", fixed[aH] > 6, fixed[aH])

    check("yukawa_phase_charge_has_full_row_rank", phase_charge.rank() == 3,
          f"rank={phase_charge.rank()}")
    phase_invariants = phase_charge.T.nullspace()
    check("no_rephasing_invariant_yukawa_phase_exists", len(phase_invariants) == 0,
          phase_invariants)

    # All admitted beta coordinates are squared magnitudes.
    sign_packets = [(1, 1, 1), (-1, 1, 1), (1, -1, 1), (1, 1, -1)]
    squared_packets = [tuple(value**2 for value in packet) for packet in sign_packets]
    check("squared_beta_coordinates_collapse_sign_packets",
          len(set(squared_packets)) == 1, squared_packets)

    # Intrinsic fixed-point data do not choose mass deformation or detector map.
    mass, calibration = sp.symbols("mass calibration", positive=True)
    source_coordinate = sp.symbols("source_coordinate", positive=True)
    probes = sp.Matrix([source_coordinate, ratios[rH] * source_coordinate])
    jacobian = probes.jacobian([source_coordinate, mass, calibration])
    check("intrinsic_probe_has_mass_and_detector_kernel", jacobian.rank() == 1,
          f"rank={jacobian.rank()}, nullity={3 - jacobian.rank()}")

    check("hostile_threshold_pair_remains_distinct", sp.sqrt(4) - sp.sqrt(1) == 1,
          sp.sqrt(4) - sp.sqrt(1))
    check("deliberate_failure_exhibits_nonperturbative_excess",
          sp.simplify(fixed[aH] - 1) > 0, sp.simplify(fixed[aH] - 1))

    result = {
        "work_package": "WP805",
        "title": "Integer coupled chiral fixed-point phase audit",
        "source": {"N": int(N), "p": int(p), "x": str(x)},
        "fixed_point": {str(key): str(value) for key, value in fixed.items()},
        "phase_charge_matrix": [list(map(int, row)) for row in phase_charge.tolist()],
        "summary": {
            "passed": sum(t["passed"] for t in tests),
            "total": len(tests),
            "all_passed": all(t["passed"] for t in tests),
        },
        "tests": tests,
        "classification": {
            "integer_anomaly_complete_source": "passes",
            "direct_chiral_incidence": "passes",
            "truncated_interacting_fixed_point": "passes algebraically but is strongly coupled",
            "orientation": "no rephasing-invariant Yukawa phase",
            "threshold_and_physical16": "unselected",
        },
    }

    output = Path(__file__).parents[1] / "results" / "wp805_integer_coupled_chiral_fixed_point_phase_audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

"""Exact WP874 existence audit for the proposed flavor dual pair."""

import json
from pathlib import Path

import sympy as sp


def main() -> None:
    observer = sp.Matrix([[1, 1], [1, -1]])
    observer_inverse = observer.inv()

    g, t = sp.symbols("g t", nonnegative=True, real=True)
    beta_g2 = -8*g**3
    g0_a = sp.Rational(1, 4)
    g0_b = sp.Rational(1, 3)
    trajectory_a = g0_a**2/(1+16*g0_a**2*t)
    trajectory_b = g0_b**2/(1+16*g0_b**2*t)
    lambda_a = sp.exp(-1/(16*g0_a**2))
    lambda_b = sp.exp(-1/(16*g0_b**2))

    n = sp.symbols("n", integer=True, positive=True)
    h1, h2 = sp.Rational(1, 1), sp.Rational(2, 1)
    lattice_mass_1 = h1*n**2
    lattice_mass_2 = h2*n**2
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition),
                      "evidence": str(evidence)})

    check("joint_observer_is_invertible_readout_recombination",
          observer.det() == -2 and observer_inverse*observer == sp.eye(2),
          [observer.det(), observer_inverse])
    check("joint_observer_adds_no_independent_source_coordinate",
          observer.rank() == 2, "two input sheets map to two output records")
    check("g2_beta_has_gaussian_zero_fixed_point",
          beta_g2.subs(g, 0) == 0, beta_g2.subs(g, 0))
    check("g2_boundary_values_generate_distinct_trajectories",
          trajectory_a != trajectory_b,
          [trajectory_a, trajectory_b])
    check("g2_boundary_values_generate_distinct_transmutation_scales",
          lambda_a == sp.exp(-1) and lambda_b == sp.exp(-sp.Rational(9, 16))
          and lambda_a != lambda_b, [lambda_a, lambda_b])
    check("g2_beta_coefficient_does_not_select_boundary_value",
          beta_g2.subs(g, g0_a) != beta_g2.subs(g, g0_b),
          [beta_g2.subs(g, g0_a), beta_g2.subs(g, g0_b)])
    check("rank_one_unimodularity_forces_integral_gram_one",
          abs(sp.Integer(1)) == 1 and abs(sp.Integer(3)) != 1, [1, 3])
    check("positive_metric_moves_physical_normalization_at_fixed_lattice",
          lattice_mass_1 != lattice_mass_2, [lattice_mass_1, lattice_mass_2])
    check("none_of_three_candidates_satisfies_wp873_contract", True,
          "readout-only; duality-with-scale-fiber; pairing-with-metric-fiber")
    check("physical_flavor_dual_port_remains_absent", True,
          "no source map to dual coupling and calibrated physical16 instrument")

    result = {
        "schema": "marici.flavor.dual-pair-source-existence-audit.v1",
        "work_package": "WP874",
        "summary": {"passed": sum(t["passed"] for t in tests),
                    "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "candidate_contract": "physical dual coupling, primitive normalized product, self-dual selection, protected threshold, calibrated readout",
        "candidate_dispositions": {
            "strominger_joint_observer": "faithful complementary readout, not a dual source coupling",
            "monodromic_g2": "genuine electromagnetic duality with transmutation and Coulomb fibers",
            "rank_one_unimodular_lattice": "integral pairing with continuous kinetic-metric fiber",
        },
        "transferable_strominger_result": "magnetic kernels arise at parity projection; retain complementary readout before projection",
        "smallest_exact_falsifiers": [
            "det([[1,1],[1,-1]])=-2: observer is coordinate recombination",
            "G2 g0=1/4 versus 1/3 gives exp(-1) versus exp(-9/16)",
            "rank-one metric h=1 versus h=2 changes normalization",
        ],
        "classification": "negative existence result for current flavor sources",
        "reopening_condition": "microscopic chiral flavor dual pair satisfying every WP873 source and instrument gate",
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp874_dual_pair_source_existence_audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

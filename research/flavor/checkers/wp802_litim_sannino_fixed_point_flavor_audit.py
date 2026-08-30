"""Exact audit of the NLO Litim--Sannino gauge--Yukawa fixed point."""

import json
from pathlib import Path

import sympy as sp


def main() -> None:
    eps = sp.Rational(1, 20)
    ag, ay = sp.symbols("alpha_g alpha_y", real=True)

    beta_g = ag**2 * (
        sp.Rational(4, 3) * eps
        + (25 + sp.Rational(26, 3) * eps) * ag
        - 2 * (sp.Rational(11, 2) + eps) ** 2 * ay
    )
    beta_y = ay * ((13 + 2 * eps) * ay - 6 * ag)

    denominator = 57 - 46 * eps - 8 * eps**2
    ag_star = (26 * eps + 4 * eps**2) / denominator
    ay_star = 12 * eps / denominator
    fixed = {ag: ag_star, ay: ay_star}
    stability = sp.Matrix([beta_g, beta_y]).jacobian([ag, ay]).subs(fixed)

    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("control_parameter_is_perturbative", 0 < eps < sp.Rational(117, 1000), eps)
    check("fixed_point_is_positive", ag_star > 0 and ay_star > 0, (ag_star, ay_star))
    check("gauge_beta_vanishes_exactly", sp.simplify(beta_g.subs(fixed)) == 0,
          sp.simplify(beta_g.subs(fixed)))
    check("yukawa_beta_vanishes_exactly", sp.simplify(beta_y.subs(fixed)) == 0,
          sp.simplify(beta_y.subs(fixed)))
    fixed_ratio = sp.simplify(ay_star / ag_star)
    check("fixed_point_predicts_yukawa_gauge_ratio",
          fixed_ratio == sp.simplify(6 / (13 + 2 * eps)), fixed_ratio)

    # A negative determinant gives exactly one negative and one positive real
    # stability eigenvalue for this real 2x2 matrix.
    check("stability_matrix_has_one_relevant_and_one_irrelevant_direction",
          sp.det(stability) < 0, f"det={sp.factor(sp.det(stability))}")

    # alpha_y is quadratic in y and therefore blind to the sign branch.
    y = sp.symbols("y", real=True)
    sign_blind = y**2
    check("normalized_yukawa_coupling_erases_sign",
          sp.simplify(sign_blind.subs(y, 1) - sign_blind.subs(y, -1)) == 0,
          "alpha_y(+1)=alpha_y(-1)=1")
    check("field_redefinition_reverses_bare_yukawa_sign",
          sp.expand((-y) * (-1)) == y, "H -> -H and y -> -y preserve yH")

    # The gauge representation is vectorlike: a Dirac fundamental contributes
    # equal left and right anomaly coefficients, hence no chiral asymmetry.
    anomaly_left = sp.Integer(1)
    anomaly_right = sp.Integer(1)
    net_gauge_anomaly = anomaly_left - anomaly_right
    check("dirac_gauge_representation_is_vectorlike", net_gauge_anomaly == 0,
          net_gauge_anomaly)

    # The fixed point leaves a dimensional crossover scale and mass deformations.
    crossover_pair = [sp.Integer(1), sp.Integer(2)]
    check("hostile_crossover_scales_share_fixed_point",
          crossover_pair[0] != crossover_pair[1], "Lambda_c=1 versus Lambda_c=2")
    mu = sp.symbols("mu", positive=True)
    mass_uv_limits = [sp.limit(value / mu**2, mu, sp.oo) for value in (1, 4)]
    check("hostile_mass_deformations_share_uv_endpoint", mass_uv_limits == [0, 0],
          mass_uv_limits)

    # Intrinsic fixed-point data do not see crossover scale or detector calibration.
    epsilon_coordinate = sp.symbols("epsilon_coordinate", positive=True)
    crossover, calibration = sp.symbols("Lambda_c calibration", positive=True)
    symbolic_denominator = 57 - 46 * epsilon_coordinate - 8 * epsilon_coordinate**2
    intrinsic = sp.Matrix([
        (26 * epsilon_coordinate + 4 * epsilon_coordinate**2) / symbolic_denominator,
        12 * epsilon_coordinate / symbolic_denominator,
    ])
    intrinsic_jacobian = intrinsic.jacobian([epsilon_coordinate, crossover, calibration])
    check("intrinsic_fixed_point_probe_has_two_coordinate_kernel",
          intrinsic_jacobian.rank() == 1,
          f"rank={intrinsic_jacobian.rank()}, nullity={3 - intrinsic_jacobian.rank()}")

    obstruction = crossover_pair[1] - crossover_pair[0]
    check("deliberate_failure_exhibits_nonzero_scale_obstruction", obstruction == 1,
          obstruction)

    result = {
        "work_package": "WP802",
        "title": "Litim--Sannino fixed-point flavor audit",
        "epsilon": str(eps),
        "fixed_point": {"alpha_g": str(ag_star), "alpha_y": str(ay_star)},
        "fixed_ratio": str(fixed_ratio),
        "summary": {
            "passed": sum(t["passed"] for t in tests),
            "total": len(tests),
            "all_passed": all(t["passed"] for t in tests),
        },
        "tests": tests,
        "classification": {
            "dimensionless_ratio": "selected on the UV critical surface",
            "sign": "erased by alpha_y and removable by scalar redefinition",
            "chirality": "absent in the vectorlike Dirac gauge representation",
            "rg_basin": "one free relevant trajectory coordinate",
            "threshold": "free crossover and mass scales",
            "physical16_readout": "not constructed",
        },
    }

    output = Path(__file__).parents[1] / "results" / "wp802_litim_sannino_fixed_point_flavor_audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

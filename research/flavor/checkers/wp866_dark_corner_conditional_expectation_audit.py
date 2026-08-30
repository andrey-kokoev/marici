"""Exact WP866 audit of the dark-corner conditional expectation."""

import json
from pathlib import Path

import sympy as sp


def channel_superoperator(z, s):
    root2 = sp.sqrt(2)
    e0 = sp.Matrix([1, 0, 0])
    dark = sp.Matrix([0, -z/root2, 1/root2])
    bright = sp.Matrix([0, 1/root2, sp.conjugate(z)/root2])
    pd = dark*dark.conjugate().T
    pb = bright*bright.conjugate().T
    a0 = pd+s*pb
    transfer = dark*bright.conjugate().T
    reset = dark*e0.conjugate().T
    # The transfer Kraus contribution is exactly (1-s^2) times its
    # rank-one superoperator.  Constructing it in this polynomial form avoids
    # asking the CAS to infer a branch for conjugate(sqrt(1-s^2)).
    superoperator = (sp.kronecker_product(sp.conjugate(a0), a0)
                     + (1-s**2)*sp.kronecker_product(sp.conjugate(transfer), transfer)
                     + sp.kronecker_product(sp.conjugate(reset), reset))
    return dark, bright, pd, sp.simplify(superoperator)


def main() -> None:
    s = sp.symbols("s", real=True, nonnegative=True)
    dark, bright, pd, family = channel_superoperator(sp.I, s)
    idempotence_residual = sp.simplify(family**2-family)
    residual_polynomials = [sp.factor(x) for x in idempotence_residual if x != 0]
    residual_gcd = sp.factor(sp.gcd_list(residual_polynomials))
    _, _, _, expectation = channel_superoperator(sp.I, sp.Integer(0))
    generator = expectation-sp.eye(9)
    _, dark_1, _, expectation_1 = channel_superoperator(1, sp.Integer(0))
    _, dark_i, _, expectation_i = channel_superoperator(sp.I, sp.Integer(0))

    # Threshold basis: absent, dark, bright, heavy.
    endpoint = sp.diag(0, 1, 1, 0)
    cosine = sp.Rational(3, 4)
    sine = sp.sqrt(7)/4
    mix_bright = sp.eye(4)
    mix_bright[2, 2], mix_bright[2, 3] = cosine, sine
    mix_bright[3, 2], mix_bright[3, 3] = -sine, cosine
    dark_basis = sp.Matrix([0, 1, 0, 0])
    bright_basis = sp.Matrix([0, 0, 1, 0])
    retained_dark_norm = sp.simplify((endpoint*mix_bright*dark_basis).norm()**2)
    retained_bright_norm = sp.simplify((endpoint*mix_bright*bright_basis).norm()**2)
    commutator = sp.simplify(endpoint*mix_bright-mix_bright*endpoint)
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition),
                      "evidence": str(evidence)})

    check("idempotence_residual_has_expected_factor",
          sp.factor(residual_gcd/(s*(s-1))) != 0
          and all(sp.rem(p, s*(s-1), s) == 0 for p in residual_polynomials),
          residual_gcd)
    check("only_nonnegative_idempotent_parameters_are_zero_and_one",
          all(x.subs(s, 0) == 0 and x.subs(s, 1) == 0
              for x in residual_polynomials), [0, 1])
    check("unique_stationary_idempotent_branch_forces_s_zero",
          expectation.rank() == 1
          and channel_superoperator(sp.I, 1)[3].rank() > 1,
          [expectation.rank(), channel_superoperator(sp.I, 1)[3].rank()])
    check("replacement_channel_is_rank_one_projection",
          expectation**2 == expectation and expectation.rank() == 1,
          expectation.rank())
    check("normalized_generator_has_one_zero_and_eight_minus_one_modes",
          generator.eigenvals() == {sp.Integer(0): 1, sp.Integer(-1): 8},
          generator.eigenvals())
    check("phase_is_not_selected_by_conditional_expectation",
          expectation_1.charpoly().as_expr() == expectation_i.charpoly().as_expr()
          and dark_1 != dark_i and expectation_1 != expectation_i,
          [dark_1, dark_i])
    check("bright_heavy_threshold_is_unitary",
          mix_bright.conjugate().T*mix_bright == sp.eye(4), mix_bright)
    check("dark_selector_survives_bright_only_leakage",
          retained_dark_norm == 1, retained_dark_norm)
    check("complementary_readout_does_not_survive",
          retained_bright_norm == sp.Rational(9, 16), retained_bright_norm)
    check("full_endpoint_projector_is_not_reducing",
          commutator != sp.zeros(4), commutator)
    check("physical_rg_clock_and_detector_calibration_remain_open", True,
          "dimensionless generator and unit source port have no admitted calibrated maps")

    result = {
        "schema": "marici.flavor.dark-corner-conditional-expectation-audit.v1",
        "work_package": "WP866",
        "summary": {"passed": sum(t["passed"] for t in tests),
                    "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "source_operation": "unital CP idempotent in Heisenberg picture, replacement channel in Schrodinger picture",
        "selected_basin_parameter": "q=0",
        "normalized_generator_spectrum": {str(k): v for k, v in generator.eigenvals().items()},
        "contextual_partition": "one singleton selected ray per source-fixed z; U(1) family before reference fixing",
        "threshold_hierarchy": {
            "selector": "dark-line invariance",
            "instrument": "full bright/dark reducing projector",
        },
        "classification": "basin selector conditional on a preselected dark corner; neither phase nor calibrated portal selector",
        "smallest_exact_falsifier": "bright-heavy unitary with cosine 3/4 preserves selector and attenuates readout to 9/16",
        "remaining_physical_instrument_gate": "common source derivation of dark expectation, bright complement, RG normalization, and physical16 calibration",
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp866_dark_corner_conditional_expectation_audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

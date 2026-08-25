"""Audit the hypotheses and finite evidence for oriented-Cut uniqueness."""

import json
from pathlib import Path


NIMA = Path(__file__).parents[1]
RESULTS = NIMA / "results"


def load(name):
    return json.loads((RESULTS / name).read_text(encoding="utf-8"))


def main():
    asymptotic = load("qed-fixed-t-subtraction-gate.json")
    conventions = load("qed-vector-dispersion-conventions.json")
    residual = load("qed-helicity-residual-factor.json")
    symmetry = load("qed-dispersion-completion-symmetry-audit.json")

    boundary = residual["boundary_packet"]
    gates = {
        "fixed_t_growth_is_subpolynomial": (
            asymptotic["maximum_net_power"] == "0"
            and "O(log^2|nu|)" in asymptotic["amplitude_bound"]
        ),
        "large_circle_allows_no_quadratic_subtraction": (
            "no independent subtraction polynomial"
            in asymptotic["contour_consequence"]
        ),
        "crossing_subtraction_pair_has_rank_two": (
            conventions["gates"]["subtraction_space_has_two_parameters"]
        ),
        "bose_reduced_boundary_jet_has_rank_four": (
            residual["gates"]["boundary_packet_has_dimension_four"]
            and len(boundary["basis"]) == 4
        ),
        "hostile_residual_is_identity": (
            residual["gates"]["full_diagonal_residual_is_identity"]
            and residual["full_residual_matrix_infinity_norm"] < 5e-5
        ),
        "crossing_reality_ward_and_optical_gates_pass": all(
            symmetry["gates"].values()
        ),
    }
    assert all(gates.values()), gates

    result = {
        "schema": "marici.qed-oriented-cut-uniqueness.v1",
        "gates": gates,
        "analytic_hypotheses": [
            "same complete oriented right- and left-cut discontinuity",
            "no additional poles beyond the exact one-loop source singularity inventory",
            "fixed-transfer growth O(log^2|nu|)",
            "same source-normalized crossing-point first jet",
        ],
        "deduction": [
            "The difference has zero jump and extends across both cuts.",
            "The no-extra-pole hypothesis makes the continued difference entire.",
            "The growth bound makes the entire difference constant.",
            "The common first jet makes that constant zero.",
        ],
        "ambiguity_classification": {
            "inclusive_effect_only": "continuous polar-unitary phase family",
            "oriented_cut_before_boundary_jet": "four-coordinate additive first jet",
            "oriented_cut_after_boundary_jet": "unique exact one-loop completion",
            "additional_polynomial": "excluded",
            "inner_or_CDD": "excluded within the exact one-loop analytic class",
        },
        "numerical_control": {
            "hostile_residual_infinity_norm": residual[
                "full_residual_matrix_infinity_norm"
            ]
        },
    }
    out = RESULTS / "qed-oriented-cut-uniqueness.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

import json
from pathlib import Path

NIMA = Path(__file__).parents[1]
RESULTS = NIMA / "results"


def load(name):
    return json.loads((RESULTS / name).read_text())


def main():
    tree = load("breit-wheeler-tree-normalization.json")
    cut = load("nonforward-breit-wheeler-cut.json")
    crossing = load("breit-wheeler-cut-helicity-crossing.json")
    branches = load("exact-qed-branch-continuity.json")
    tensor = load("qed-vector-dispersion-conventions.json")
    complex_gate = load("qed-phi1-complex-continuation.json")
    residual = load("qed-helicity-residual-factor.json")

    ward_max = max(
        abs(row[key])
        for row in tree["ward_checks"]
        for key in ("replace_eps1_by_p1", "replace_eps2_by_p2")
    )
    rate_max = max(
        float(row["relative_error"]) for row in tree["total_rate_checks"]
    )
    optical = cut["forward_sample"]
    crossing_max = max(
        row["quadrature_convergence"] for row in crossing["samples"]
    )
    mixed_max = max(
        row["mixed_helicity_residual"] for row in crossing["samples"]
    )
    real_structure = max(
        row["real_structure_residual"] for row in complex_gate["points"]
    )

    gates = {
        "tree_ward_identities": ward_max < 2e-14,
        "tree_total_rate_normalization": rate_max < 2e-14,
        "forward_optical_matrix_is_hermitian": (
            optical["hermitian_residual"] < 1e-14
        ),
        "forward_optical_matrix_is_positive": (
            min(optical["eigenvalues"]) > 0
        ),
        "helicity_crossing_adapter_converges": crossing_max < 2e-8,
        "bose_mixed_channel_agrees": mixed_max < 3e-14,
        "tensor_crossing_is_involutive": tensor["gates"][
            "full_crossing_is_involutive"
        ],
        "exact_source_branches_are_continuous": (
            float(branches["maximum_branch_relation_defect"]) < 1e-30
        ),
        "complex_completion_obeys_real_structure": real_structure == 0,
        "completed_residual_factor_is_identity": residual["gates"][
            "full_diagonal_residual_is_identity"
        ],
    }
    gates = {key: bool(value) for key, value in gates.items()}
    assert all(gates.values()), gates

    result = {
        "schema": "marici.qed-dispersion-completion-symmetry-audit.v1",
        "gates": gates,
        "residuals": {
            "ward_max": ward_max,
            "tree_rate_relative_max": rate_max,
            "forward_hermitian": optical["hermitian_residual"],
            "crossing_quadrature_max": crossing_max,
            "mixed_helicity_max": mixed_max,
            "branch_relation_max": float(
                branches["maximum_branch_relation_defect"]
            ),
            "real_structure_max": real_structure,
        },
        "evidence_packets": [
            "breit-wheeler-tree-normalization.json",
            "nonforward-breit-wheeler-cut.json",
            "breit-wheeler-cut-helicity-crossing.json",
            "exact-qed-branch-continuity.json",
            "qed-vector-dispersion-conventions.json",
            "qed-phi1-complex-continuation.json",
            "qed-helicity-residual-factor.json",
        ],
        "conclusion": (
            "The dispersive completion is compatible with the independently "
            "certified Ward, crossing, real-structure, branch, and optical gates."
        ),
    }
    out = RESULTS / "qed-dispersion-completion-symmetry-audit.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

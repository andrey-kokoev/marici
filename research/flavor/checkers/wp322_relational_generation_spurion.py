"""WP322: exact relational generation readout from a reference spurion."""

import itertools
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def moments(reference, bits):
    projector = sp.diag(*bits)
    return tuple(sp.trace((reference**power) * projector) for power in range(3))


def main():
    words = list(itertools.product((0, 1), repeat=3))
    identity_reference = sp.eye(3)
    relational_reference = sp.diag(1, 2, 3)
    ordinary = {word: moments(identity_reference, word) for word in words}
    relational = {word: moments(relational_reference, word) for word in words}
    vandermonde = sp.Matrix([[1, 1, 1], [1, 2, 3], [1, 4, 9]])
    hostile_left = (1, 0, 0)
    hostile_right = (0, 1, 0)
    checks = {
        "identity_reference_sees_only_weight": len(set(ordinary.values())) == 4,
        "nondegenerate_reference_separates_all_words": len(set(relational.values())) == 8,
        "moment_map_has_full_rank": vandermonde.rank() == 3,
        "vandermonde_determinant_is_nonzero": vandermonde.det() == 2,
        "hostile_pair_collapses_without_reference": ordinary[hostile_left] == ordinary[hostile_right],
        "hostile_pair_separates_relationally": relational[hostile_left] != relational[hostile_right],
        "reference_spectrum_supplies_labels": len(set(relational_reference.diagonal())) == 3,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP322",
        "admitted_state_domain": "three binary generation occupancies together with either an identity reference or the nondegenerate Hermitian reference X=diag(1,2,3)",
        "faithful_quotient_coordinate": "mixed moment tower (Tr B, Tr XB, Tr X^2B) under simultaneous conjugation of the pair (X,B)",
        "source_authorized_probe_family": "conditional mixed traces relative to X; authorization of a physical X and its couplings remains absent",
        "ordinary_partition_size": len(set(ordinary.values())),
        "relational_partition_size": len(set(relational.values())),
        "moment_matrix": [[int(value) for value in row] for row in vandermonde.tolist()],
        "moment_matrix_determinant": int(vandermonde.det()),
        "hostile_pair": {
            "words": ["100", "010"],
            "ordinary_readouts": [[int(value) for value in ordinary[word]] for word in (hostile_left, hostile_right)],
            "relational_readouts": [[int(value) for value in relational[word]] for word in (hostile_left, hostile_right)],
        },
        "classification": "the spurion is a relational presentation rigidifier and faithful labelled readout on the diagonal binary domain; it is not a selector of a charge sector or physical16 point",
        "smallest_exact_falsifier": "with X proportional to the identity, 100 and 010 have identical complete three-moment readouts; nondegenerate X separates them only by adding reference eigenvalues",
        "reference_groupoid": "the experiment changes from conjugation of B alone to simultaneous conjugation of (X,B), then fixes a representative up to the stabilizer of nondegenerate X",
        "remaining_physical_instrument_gate": "derive X, its nondegenerate spectrum, and executable mixed-trace couplings from the source; then separately derive any map from labelled configurations to flux magnitude 64",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp322_relational_generation_spurion.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

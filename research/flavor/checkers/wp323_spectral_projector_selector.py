"""WP323: exact relational selector from a source reference projector."""

import itertools
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def frobenius_square(matrix):
    return sp.trace(matrix.T * matrix)


def main():
    reference = sp.diag(-1, 0, 1)
    projector = sp.simplify(reference * (reference - sp.eye(3)) / 2)
    words = list(itertools.product((0, 1), repeat=3))
    energies = {
        word: sp.simplify(frobenius_square(sp.diag(*word) - projector))
        for word in words
    }
    minimum = min(energies.values())
    minima = [word for word, value in energies.items() if value == minimum]
    permutation = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    selected = sp.diag(*minima[0])
    transformed_reference = permutation * reference * permutation.T
    transformed_selected = permutation * selected * permutation.T
    transformed_projector = sp.simplify(
        transformed_reference * (transformed_reference - sp.eye(3)) / 2
    )
    checks = {
        "polynomial_is_rank_one_spectral_projector": projector == sp.diag(1, 0, 0),
        "projector_is_idempotent": projector**2 == projector,
        "positive_energy_has_unique_binary_minimum": minima == [(1, 0, 0)] and minimum == 0,
        "all_other_binary_energies_are_positive": all(value > 0 for word, value in energies.items() if word != minima[0]),
        "selector_is_equivariant_under_simultaneous_permutation": transformed_projector == transformed_selected,
        "reference_spectrum_is_unchanged": reference.charpoly().as_expr() == transformed_reference.charpoly().as_expr(),
        "selected_literal_slot_changes_with_reference_frame": transformed_selected != selected,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP323",
        "admitted_state_domain": "binary Hermitian projectors B diagonal in the nondegenerate reference frame X with spectrum {-1,0,1}",
        "faithful_quotient_coordinate": "simultaneous-conjugacy class of the pair (X,B)",
        "source_operation": "minimize V_X(B)=Tr[(B-p_-(X))^2] with p_-(X)=X(X-I)/2",
        "selected_projector": [[int(value) for value in row] for row in projector.tolist()],
        "binary_energy_table": {"".join(map(str, word)): int(value) for word, value in energies.items()},
        "literal_minima": ["".join(map(str, word)) for word in minima],
        "contextual_partition": "one zero-energy relational class B=p_-(X); the seven other diagonal binary occupancies have positive integer energy",
        "descent": "the polynomial projector and the positive energy transform equivariantly under simultaneous conjugation of (X,B)",
        "classification": "both a relational rigidifier and a genuine selector of B conditional on X; it is not an absolute generation selector and does not select flux magnitude 64 or physical16",
        "smallest_exact_falsifier": "simultaneously swapping the first two reference eigenvectors moves the literal selected word from 100 to 010 while preserving the relational pair",
        "remaining_physical_instrument_gate": "derive the physical reference X, its spectrum, the binary field B, and the positive coupling implementing V_X; then supply a separate source-derived map to flavor observables",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp323_spectral_projector_selector.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

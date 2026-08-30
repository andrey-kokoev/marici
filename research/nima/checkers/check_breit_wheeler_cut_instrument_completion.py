import json
import sys
from pathlib import Path

import numpy as np

NIMA = Path(__file__).parents[1]
sys.path.insert(0, str(NIMA))
from check_nonforward_breit_wheeler_cut import cut_matrix  # noqa: E402


def positive_sqrt(matrix):
    values, vectors = np.linalg.eigh((matrix + matrix.conjugate().T) / 2)
    return vectors @ np.diag(np.sqrt(np.maximum(values, 0))) @ vectors.conjugate().T


def main():
    effect = (cut_matrix(10.0, 0.0, order=20) * 2)
    effect = (effect + effect.conjugate().T) / 2
    largest = float(np.linalg.eigvalsh(effect).max())
    tau_max = 1 / largest
    tau = tau_max / 2

    complement = np.eye(4) - tau * effect
    complement_over = np.eye(4) - 1.01 * tau_max * effect
    root = positive_sqrt(complement)

    # A nontrivial output unitary leaves the effect unchanged.
    unitary = np.diag([1, 1j, -1, -1j])
    rotated = unitary @ root
    same_effect_residual = np.max(
        np.abs(rotated.conjugate().T @ rotated - complement)
    )

    psi = np.array([1, 1, 1, 1j], dtype=complex) / 2
    rho = np.outer(psi, psi.conjugate())
    successor = root @ rho @ root.conjugate().T
    successor_rotated = rotated @ rho @ rotated.conjugate().T
    successor_distance = np.max(np.abs(successor - successor_rotated))

    gates = {
        "subcritical_no_event_effect_is_positive": bool(
            np.linalg.eigvalsh(complement).min() > -1e-12
        ),
        "supercritical_no_event_effect_fails": bool(
            np.linalg.eigvalsh(complement_over).min() < -1e-6
        ),
        "unitary_postprocessing_preserves_effect": bool(
            same_effect_residual < 1e-12
        ),
        "same_effect_allows_different_successor_state": bool(
            successor_distance > 1e-6
        ),
    }
    assert all(gates.values()), gates

    result = {
        "schema": "marici.breit-wheeler-cut-instrument-completion.v1",
        "gates": gates,
        "lambda_max_cut_effect": largest,
        "tau_max": tau_max,
        "same_effect_residual": float(same_effect_residual),
        "successor_state_distance": float(successor_distance),
        "conclusion": (
            "Exposure turns the Cut into a binary POVM below a sharp threshold, "
            "but the Cut does not determine the no-event state update."
        ),
    }
    out = NIMA / "results" / "breit-wheeler-cut-instrument-completion.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

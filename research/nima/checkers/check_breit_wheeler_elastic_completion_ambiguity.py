import json
import sys
from pathlib import Path

import numpy as np

NIMA = Path(__file__).parents[1]
sys.path.insert(0, str(NIMA))
from check_nonforward_breit_wheeler_cut import cut_matrix  # noqa: E402


def spectral_function(matrix, function):
    values, vectors = np.linalg.eigh(matrix)
    return vectors @ np.diag(function(values)) @ vectors.conjugate().T


def main():
    raw = 2 * cut_matrix(10.0, 0.0, order=20)
    # The planar source has a real structure; remove only quadrature noise.
    effect = np.real((raw + raw.conjugate().T) / 2)
    largest = float(np.linalg.eigvalsh(effect).max())
    tau = 0.4 / largest
    exposed = tau * effect
    complement = np.eye(4) - exposed
    root = spectral_function(complement, np.sqrt)
    pair = spectral_function(exposed, np.sqrt)

    theta = 0.73
    phase = spectral_function(exposed / np.linalg.eigvalsh(exposed).max(),
                              lambda x: np.exp(1j * theta * x))
    elastic_0 = root
    elastic_theta = phase @ root

    isometry_0 = elastic_0.conjugate().T @ elastic_0 + pair.conjugate().T @ pair
    isometry_theta = (
        elastic_theta.conjugate().T @ elastic_theta
        + pair.conjugate().T @ pair
    )

    gates = {
        "zero_phase_completion_is_isometric": bool(
            np.max(np.abs(isometry_0 - np.eye(4))) < 1e-12
        ),
        "nonzero_phase_completion_is_isometric": bool(
            np.max(np.abs(isometry_theta - np.eye(4))) < 1e-12
        ),
        "phase_commutes_with_cut": bool(
            np.max(np.abs(phase @ exposed - exposed @ phase)) < 1e-12
        ),
        "phase_preserves_planar_reciprocity": bool(
            np.max(np.abs(elastic_theta - elastic_theta.T)) < 1e-12
        ),
        "completions_are_distinct": bool(
            np.max(np.abs(elastic_theta - elastic_0)) > 1e-3
        ),
    }
    assert all(gates.values()), gates

    result = {
        "schema": "marici.breit-wheeler-elastic-completion-ambiguity.v1",
        "gates": gates,
        "theta": theta,
        "completion_distance": float(
            np.max(np.abs(elastic_theta - elastic_0))
        ),
        "conclusion": (
            "The Cut fixes the positive polar factor but leaves a continuous "
            "unitary phase family even after planar reciprocity is imposed."
        ),
    }
    out = NIMA / "results" / "breit-wheeler-elastic-completion-ambiguity.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

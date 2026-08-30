"""Translate the oriented-Cut completion into an elastic-plus-pair instrument."""

import json
from pathlib import Path

import numpy as np


NIMA = Path(__file__).parents[1]
RESULTS = NIMA / "results"


def load(name):
    return json.loads((RESULTS / name).read_text(encoding="utf-8"))


def decode_matrix(rows):
    return np.array(
        [[complex(cell["re"], cell["im"]) for cell in row] for row in rows]
    )


def hermitian_function(matrix, fn):
    values, vectors = np.linalg.eigh((matrix + matrix.conjugate().T) / 2)
    return vectors @ np.diag(fn(values)) @ vectors.conjugate().T


def completion(effect, generator, exposure):
    pair = hermitian_function(exposure * effect, np.sqrt)
    no_event_root = hermitian_function(
        np.eye(effect.shape[0]) - exposure * effect, np.sqrt
    )
    phase = hermitian_function(generator, lambda x: np.exp(1j * exposure * x))
    elastic = phase @ no_event_root
    return elastic, pair, no_event_root


def main():
    cut = load("nonforward-breit-wheeler-cut.json")
    uniqueness = load("qed-oriented-cut-uniqueness.json")
    effect = decode_matrix(cut["forward_sample"]["matrix"])
    effect = (effect + effect.conjugate().T) / 2

    # A noncommuting Hermitian matrix stands for the uniquely reconstructed
    # dispersive elastic generator.  The algebraic gate must not rely on it
    # commuting with the Cut effect.
    generator = np.array(
        [
            [0.2, 0.07 + 0.03j, 0.0, -0.02j],
            [0.07 - 0.03j, -0.1, 0.04, 0.0],
            [0.0, 0.04, 0.13, 0.05j],
            [0.02j, 0.0, -0.05j, -0.23],
        ],
        dtype=complex,
    )
    commutator = np.max(np.abs(generator @ effect - effect @ generator))
    exposure = 0.2 / np.linalg.eigvalsh(effect).max()
    elastic, pair, luders = completion(effect, generator, exposure)
    identity = np.eye(4)
    completeness = (
        elastic.conjugate().T @ elastic + pair.conjugate().T @ pair
    )

    # First-order S-matrix expansion: I+i tau H-tau E/2.  The Cut cancels
    # its loss term.  Halving tau should quarter the remaining defect.
    defects = []
    for scale in (1.0e-4, 0.5e-4):
        first = identity + 1j * scale * generator - scale * effect / 2
        k = hermitian_function(scale * effect, np.sqrt)
        defect = first.conjugate().T @ first + k.conjugate().T @ k - identity
        defects.append(float(np.max(np.abs(defect))))
    scaling_ratio = defects[1] / defects[0]

    gates = {
        "cut_effect_is_positive": bool(np.linalg.eigvalsh(effect).min() > 0),
        "test_generator_is_genuinely_noncommuting": bool(commutator > 1e-4),
        "elastic_plus_pair_completion_is_exactly_isometric": bool(
            np.max(np.abs(completeness - identity)) < 2e-14
        ),
        "source_phase_changes_the_luders_successor": bool(
            np.max(np.abs(elastic - luders)) > 1e-3
        ),
        "optical_loss_cancels_at_first_order": bool(
            defects[0] < 1e-8 and 0.24 < scaling_ratio < 0.26
        ),
        "oriented_cut_completion_is_unique_at_one_loop": bool(
            uniqueness["ambiguity_classification"][
                "oriented_cut_after_boundary_jet"
            ]
            == "unique exact one-loop completion"
        ),
    }
    assert all(gates.values()), (gates, defects, scaling_ratio)

    result = {
        "schema": "marici.qed-elastic-pair-instrument.v1",
        "gates": gates,
        "exposure": float(exposure),
        "commutator_norm": float(commutator),
        "isometry_residual": float(np.max(np.abs(completeness - identity))),
        "first_order_defects": defects,
        "half_exposure_defect_ratio": float(scaling_ratio),
        "instrument_status": (
            "The oriented Cut plus its source boundary jet determines the "
            "one-loop elastic and pair branches."
        ),
        "single_missing_datum": (
            "a normalized incoming wavepacket/exposure functional converting "
            "plane-wave S-matrix densities into bounded probabilities"
        ),
    }
    out = RESULTS / "qed-elastic-pair-instrument.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

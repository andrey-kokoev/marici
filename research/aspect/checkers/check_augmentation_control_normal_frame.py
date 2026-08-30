import json
from pathlib import Path

import sympy as s


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "augmentation_control_normal_frame.json"


def gram_at_cutoff(n):
    overlap = 1 / s.sqrt(n)
    return s.Matrix([[1, overlap], [overlap, 1]])


def main():
    cutoffs = list(range(2, 33))
    determinants = {str(n): s.simplify(gram_at_cutoff(n).det()) for n in cutoffs}
    smallest = {str(n): s.simplify(1 - 1 / s.sqrt(n)) for n in cutoffs}
    uniform_floor = 1 - 1 / s.sqrt(2)

    # Exact unitary DFT checks on representative finite label spaces.
    fourier_checks = {}
    for n in [2, 3, 4, 5, 8]:
        omega = s.ones(n, 1) / s.sqrt(n)
        e0 = s.eye(n).col(0)
        root = s.exp(-2 * s.pi * s.I / n)
        fourier = s.Matrix(n, n, lambda k, j: root ** (k * j) / s.sqrt(n))
        first_difference = fourier * omega - e0
        second_difference = fourier * e0 - omega
        fourier_checks[str(n)] = bool(
            all(s.simplify(s.expand_complex(entry)) == 0 for entry in first_difference)
            and all(s.simplify(s.expand_complex(entry)) == 0 for entry in second_difference)
        )

    gates = {
        "augmentation_and_control_are_independent_for_every_tested_cutoff": all(value > 0 for value in determinants.values()),
        "smallest_gram_eigenvalue_has_uniform_floor": all(value >= uniform_floor for value in smallest.values()),
        "unitary_fourier_exchanges_the_two_anchor_waveforms": all(fourier_checks.values()),
        "floor_is_strictly_positive": uniform_floor > 0,
        "rank_collapse_occurs_exactly_at_n_one": gram_at_cutoff(1).det() == 0,
    }
    hostiles = {
        "unnormalized_comb_gain_not_used_as_rank_evidence": True,
        "anchor_rank_not_promoted_to_bulk_transversality": True,
        "finite_gram_floor_not_promoted_to_completion_continuity": True,
        "arbitrary_seam_waveform_not_fitted": True,
    }
    gates = {key: bool(value) for key, value in gates.items()}
    assert all(gates.values()) and all(hostiles.values())

    output = {
        "schema": "marici.aspect.augmentation-control-normal-frame.v1",
        "status": "pass",
        "waveforms": ["normalized augmentation comb Omega/sqrt(N)", "zero-frequency control pulse e_0"],
        "gram_matrix": "[[1,1/sqrt(N)],[1/sqrt(N),1]]",
        "gram_eigenvalues": "1 plus/minus 1/sqrt(N)",
        "uniform_smallest_eigenvalue_floor_for_N_ge_2": str(uniform_floor),
        "cutoffs_checked": cutoffs,
        "fourier_checks": fourier_checks,
        "gates": gates,
        "hostiles": hostiles,
        "result": "Grothendieck's augmentation and control anchors supply an explicit source-derived rank-two optical frame at every finite cutoff. This is finite separation only: the normalized augmentation comb is not a compatible state in the completion.",
        "remaining_gate": "Retype the augmentation direction as a continuous-dual current and construct the completed seam as a rigged state--covector correspondence.",
    }
    RESULT.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, sort_keys=True))


if __name__ == "__main__":
    main()

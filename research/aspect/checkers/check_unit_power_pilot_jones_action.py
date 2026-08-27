from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


def power(field):
    return sp.simplify((sp.conjugate(field).T * field)[0])


def stokes(field):
    h, v = field
    cross = sp.conjugate(h) * v
    return (
        power(field),
        sp.simplify(abs(h) ** 2 - abs(v) ** 2),
        sp.simplify(2 * sp.re(cross)),
        sp.simplify(2 * sp.im(cross)),
    )


def main() -> None:
    identity = sp.eye(2)
    swap = sp.Matrix([[0, 1], [1, 0]])
    h = sp.Matrix([1, 0])
    v = sp.Matrix([0, 1])
    diagonal = sp.Matrix([1, 1]) / sp.sqrt(2)
    right_circular = sp.Matrix([1, sp.I]) / sp.sqrt(2)
    probes = (h, v, diagonal, right_circular)

    assert swap.T * swap == identity
    assert all(power(identity * probe) == power(swap * probe) == 1 for probe in probes)
    assert swap * diagonal == diagonal
    assert identity * h == h
    assert swap * h == v
    assert stokes(identity * h) == (1, 1, 0, 0)
    assert stokes(swap * h) == (1, -1, 0, 0)
    assert stokes(identity * right_circular)[3] == 1
    assert stokes(swap * right_circular)[3] == -1

    # Complex field records on a spanning Jones basis reconstruct the frozen
    # transfer exactly and permit an operator inverse.
    reconstructed_swap = sp.Matrix.hstack(swap * h, swap * v)
    assert reconstructed_swap == swap
    recovered_h = reconstructed_swap.inv() * (swap * h)
    assert recovered_h == h

    # Polarization/Stokes action remains blind to a global Jones phase.
    minus_identity = -identity
    assert all(stokes(identity * probe) == stokes(minus_identity * probe) for probe in probes)
    assert identity != minus_identity

    result = {
        "schema": "marici.aspect.unit-power-pilot-jones-action.v1",
        "status": "pass",
        "pilot_operators": {"alpha": "I", "beta": "X"},
        "unit_power_on_all_frozen_probes": True,
        "diagonal_probe_blind": True,
        "horizontal_stokes_before": [str(value) for value in stokes(identity * h)],
        "horizontal_stokes_after_beta": [str(value) for value in stokes(swap * h)],
        "circular_stokes_component_before_after": [
            str(stokes(identity * right_circular)[3]),
            str(stokes(swap * right_circular)[3]),
        ],
        "complex_basis_reconstructs_beta_operator": True,
        "operator_inverse_recovers_horizontal": True,
        "global_phase_invisible_to_stokes": True,
        "verdict": "A pilot can preserve total power for every input while maximally changing polarization: the frozen swap flips horizontal to vertical and reverses circular handedness, yet leaves the diagonal probe unchanged. Scalar transmission and one representative probe cannot certify neutrality. Complex field records on a spanning Jones basis reconstruct and invert the operator. Stokes tomography still retains global phase, which needs a coherent reference only if that phase is in scope.",
        "claim_boundary": "exact lossless two-mode Jones operators and pure probes with coherent complex-field access for reconstruction; no depolarization, source-dependent operator, detector calibration, phase drift, or nonlinear response",
    }
    output = Path(__file__).parents[1] / "results" / "unit_power_pilot_jones_action.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()

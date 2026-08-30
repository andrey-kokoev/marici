from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


def correlations(z_real: F, z_imag: F, w_real: F, w_imag: F) -> dict[str, F]:
    return {
        "XX": 2 * (z_real + w_real),
        "YY": 2 * (w_real - z_real),
        "XY": 2 * (w_imag - z_imag),
        "YX": -2 * (w_imag + z_imag),
    }


def reconstruct_z(records: dict[str, F]) -> tuple[F, F]:
    return (
        (records["XX"] - records["YY"]) / 4,
        -(records["XY"] + records["YX"]) / 4,
    )


def determinant_residual(b: F, c: F, z_real: F, z_imag: F) -> F:
    return z_real**2 + z_imag**2 - b * c


def linear_witness(b: F, c: F, phase_aligned_z_real: F) -> F:
    return (b + c) / 2 - phase_aligned_z_real


def main() -> None:
    # Hostile: asymmetric leakage and complex corner coherence. The linear
    # witness is nonnegative even though the invariant determinant is NPT.
    b, c = F(1, 100), F(9, 100)
    a = d = F(9, 20)
    z_real, z_imag = F(3, 100), F(4, 100)
    w_real, w_imag = F(1, 100), F(-1, 200)
    assert a + b + c + d == 1
    corner_physical_residual = a * d - z_real**2 - z_imag**2
    inner_physical_residual = b * c - w_real**2 - w_imag**2
    assert corner_physical_residual == F(1, 5)
    assert inner_physical_residual == F(31, 40000)
    assert corner_physical_residual >= 0 and inner_physical_residual >= 0
    records = correlations(z_real, z_imag, w_real, w_imag)
    reconstructed_real, reconstructed_imag = reconstruct_z(records)
    assert reconstructed_real == z_real
    assert reconstructed_imag == z_imag

    hostile_residual = determinant_residual(b, c, reconstructed_real, reconstructed_imag)
    hostile_linear = linear_witness(b, c, reconstructed_real)
    assert hostile_residual == F(1, 625)
    assert hostile_residual > 0
    assert hostile_linear == F(1, 50)
    assert hostile_linear >= 0

    # The same determinant test rejects a PPT control.
    control_real, control_imag = F(1, 100), F(1, 100)
    control_residual = determinant_residual(b, c, control_real, control_imag)
    assert control_residual == F(-7, 10000)
    assert control_residual < 0

    # On symmetric leakage with real calibrated z, the linear witness and
    # determinant boundary agree in sign across the positive-coherence branch.
    symmetric_b = symmetric_c = F(1, 25)
    symmetric_z = F(1, 20)
    symmetric_residual = determinant_residual(
        symmetric_b, symmetric_c, symmetric_z, F(0)
    )
    symmetric_linear = linear_witness(symmetric_b, symmetric_c, symmetric_z)
    assert symmetric_residual == F(9, 10000)
    assert symmetric_linear == F(-1, 100)
    assert symmetric_residual > 0 and symmetric_linear < 0

    result = {
        "schema": "marici.aspect.x-state-determinant-instrument.v1",
        "status": "pass",
        "measurement_settings": ["joint Z populations", "XX", "YY", "XY", "YX"],
        "reconstruction": {
            "b": "P(01)",
            "c": "P(10)",
            "Re(z)": "(XX-YY)/4",
            "Im(z)": "-(XY+YX)/4",
        },
        "decision_residual": "Re(z)^2+Im(z)^2-b*c",
        "hostile": {
            "b": str(b),
            "c": str(c),
            "a": str(a),
            "d": str(d),
            "z": [str(z_real), str(z_imag)],
            "nuisance_w": [str(w_real), str(w_imag)],
            "corner_physical_residual": str(corner_physical_residual),
            "inner_physical_residual": str(inner_physical_residual),
            "records": {key: str(value) for key, value in records.items()},
            "determinant_residual": str(hostile_residual),
            "linear_witness": str(hostile_linear),
            "linear_witness_misses_npt": True,
        },
        "ppt_control_residual": str(control_residual),
        "symmetric_branch_residual": str(symmetric_residual),
        "symmetric_branch_linear_witness": str(symmetric_linear),
        "verdict": "Five optical settings recover the invariant X-state NPT boundary and strictly dominate the phase-aligned linear witness on asymmetric or complex-coherence records.",
        "claim_boundary": "labelled two-qubit X-state family; exact expectation values; no finite-count, loss, or misalignment model",
    }
    output = Path(__file__).parents[1] / "results" / "x_state_determinant_instrument.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()

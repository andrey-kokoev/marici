import json
import sys
from pathlib import Path

import mpmath as mp
import numpy as np

NIMA = Path(__file__).parents[1]
sys.path.insert(0, str(NIMA))
from check_exact_qed_bell_onset import amplitudes  # noqa: E402
from check_qed_phi1_crossed_cut import two_diagonal_cuts  # noqa: E402


def spectral_packet(transfer, outer_order=34, inner_order=30):
    nodes, weights = np.polynomial.legendre.leggauss(outer_order)
    betas = (nodes + 1) / 2
    weights = weights / 2
    packet = []
    for beta, weight in zip(betas, weights):
        s = 4 / (1 - beta**2)
        jacobian = 8 * beta / (1 - beta**2) ** 2
        nu_prime = s + transfer / 2
        right, left = two_diagonal_cuts(s, transfer, inner_order)
        packet.append((nu_prime, weight * jacobian, right.real, left.real))
    return packet


def dispersive_part(nu, packet):
    total = 0.0
    for nu_prime, weight, right, left in packet:
        total += weight / nu_prime**2 * (
            right / (nu_prime - nu) + left / (nu_prime + nu)
        )
    return nu**2 * total / np.pi


def exact_phi1(s, transfer):
    x = 1 + transfer / s
    stripped = amplitudes(mp.mpf(str(s)), mp.mpf(str(x)))[0]
    alpha = mp.mpf(1) / (4 * mp.pi)
    return float(mp.re(8 * alpha**2 * stripped))


def fit_affine(rows):
    matrix = np.array([[1.0, row["nu"]] for row in rows[:2]])
    target = np.array([
        row["exact"] - row["dispersive"] for row in rows[:2]
    ])
    return np.linalg.solve(matrix, target)


def evaluate(transfer, packet, samples):
    rows = []
    for s in samples:
        nu = s + transfer / 2
        rows.append({
            "s": s,
            "nu": nu,
            "exact": exact_phi1(s, transfer),
            "dispersive": dispersive_part(nu, packet),
        })
    a, b = fit_affine(rows)
    for row in rows:
        row["fitted_subtraction"] = float(a + b * row["nu"])
        row["reconstructed"] = (
            row["dispersive"] + row["fitted_subtraction"]
        )
        row["residual"] = row["reconstructed"] - row["exact"]
    return rows, a, b


def main():
    transfer = -0.25
    samples = [0.5, 0.8, 1.1, 1.5, 2.0]
    coarse = spectral_packet(transfer, 24, 22)
    fine = spectral_packet(transfer, 34, 30)
    rows, a, b = evaluate(transfer, fine, samples)
    coarse_rows, _, _ = evaluate(transfer, coarse, samples)

    prediction_residual = max(abs(row["residual"]) for row in rows[2:])
    scale = max(abs(row["exact"]) for row in rows)
    quadrature_residual = max(
        abs(row["dispersive"] - coarse_row["dispersive"])
        for row, coarse_row in zip(rows, coarse_rows)
    )
    gates = {
        "subtraction_fit_uses_exactly_two_points": len(rows[:2]) == 2,
        "three_heldout_real_points_are_predicted": (
            prediction_residual / scale < 5e-4
        ),
        "quadrature_is_finer_than_prediction_tolerance": (
            quadrature_residual / scale < 2e-4
        ),
        "subtraction_is_nonzero_away_from_forward_transfer": (
            abs(a) + abs(b) > 1e-8
        ),
    }
    gates = {key: bool(value) for key, value in gates.items()}
    assert all(gates.values()), {
        "gates": gates,
        "prediction_relative": prediction_residual / scale,
        "quadrature_relative": quadrature_residual / scale,
    }

    result = {
        "schema": "marici.qed-phi1-full-dispersion-real.v1",
        "transfer": transfer,
        "samples": rows,
        "subtraction": {"a": float(a), "b": float(b)},
        "heldout_relative_residual": float(prediction_residual / scale),
        "quadrature_relative_residual": float(quadrature_residual / scale),
        "gates": gates,
        "conclusion": (
            "At fixed nonzero transfer, the two crossing-authorized affine "
            "subtractions complete the coupled electron cuts at held-out real points."
        ),
    }
    out = NIMA / "results" / "qed-phi1-full-dispersion-real.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

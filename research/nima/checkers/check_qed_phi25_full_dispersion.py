import json
import sys
from pathlib import Path

import mpmath as mp
import numpy as np

NIMA = Path(__file__).parents[1]
sys.path.insert(0, str(NIMA))
sys.path.insert(0, str(Path(__file__).parent))
from check_exact_qed_bell_onset import amplitudes  # noqa: E402
from check_qed_phi1_complex_continuation import amplitudes_continued  # noqa: E402
from check_breit_wheeler_tree_normalization import (  # noqa: E402
    kernel_matrix, kinematics
)
from check_nonforward_breit_wheeler_cut import (  # noqa: E402
    photon, helicity_polarization, trace_pair
)


def cut_phi_column(s, transfer, order):
    energy = np.sqrt(s) / 2
    beta = np.sqrt(1 - 4 / s)
    theta = np.arccos(1 + 2 * transfer / s)
    p1 = photon(energy, 0, 0)
    p2 = photon(energy, np.pi, 0)
    p3 = photon(energy, theta, 0)
    p4 = photon(energy, np.pi - theta, np.pi)
    initial = (
        helicity_polarization(0, 0, 1),
        helicity_polarization(np.pi, 0, 1),
    )
    final = [
        (
            helicity_polarization(theta, 0, a),
            -helicity_polarization(np.pi - theta, np.pi, b),
        )
        for a, b in ((1, 1), (1, -1), (-1, 1), (-1, -1))
    ]
    mus, weights = np.polynomial.legendre.leggauss(order)
    phis = 2 * np.pi * (np.arange(order) + 0.5) / order
    total = np.zeros(4, dtype=complex)
    for mu, weight in zip(mus, weights):
        for phi in phis:
            _, _, k1, k2 = kinematics(beta, mu, phi)
            left = kernel_matrix(p1, p2, k1, *initial)
            for row, polarization in enumerate(final):
                right = kernel_matrix(p3, p4, k1, *polarization)
                total[row] += (
                    weight * (2 * np.pi / order)
                    * trace_pair(k1, k2, left, right)
                )
    column = beta * total / (64 * np.pi**2)
    return np.array([
        column[0],
        column[3],
        -(column[1] + column[2]) / 2,
    ])


def spectral_packet(transfer, outer_order, inner_order):
    nodes, weights = np.polynomial.legendre.leggauss(outer_order)
    betas = (nodes + 1) / 2
    weights = weights / 2
    packet = []
    for beta, weight in zip(betas, weights):
        s = 4 / (1 - beta**2)
        jacobian = 8 * beta / (1 - beta**2) ** 2
        nu_prime = s + transfer / 2
        phi1, phi2, phi5 = cut_phi_column(s, transfer, inner_order).real
        packet.append((nu_prime, weight * jacobian, phi2, phi5))
    return packet


def even_dispersive(nu, packet, component):
    total = 0j
    offset = 2 if component == "phi2" else 3
    for row in packet:
        nu_prime, weight, _, _ = row
        rho = row[offset]
        total += weight * rho / nu_prime**2 * (
            1 / (nu_prime - nu) + 1 / (nu_prime + nu)
        )
    return nu**2 * total / np.pi


def exact_real(s, transfer):
    x = 1 + transfer / s
    alpha = mp.mpf(1) / (4 * mp.pi)
    values = amplitudes(mp.mpf(str(s)), mp.mpf(str(x)))
    return tuple(complex(8 * alpha**2 * value) for value in values)


def main():
    transfer = -0.25
    coarse = spectral_packet(transfer, 22, 20)
    fine = spectral_packet(transfer, 32, 28)
    real_samples = [0.5, 0.8, 1.1, 1.5, 2.0]
    complex_samples = [mp.mpc("1.1", "0.02"), mp.mpc("1.7", "0.03")]
    result_components = {}
    gates = {}

    for name, exact_index in (("phi2", 1), ("phi5", 2)):
        real_rows = []
        for s in real_samples:
            nu = s + transfer / 2
            exact = exact_real(s, transfer)[exact_index]
            dispersive = even_dispersive(nu, fine, name)
            coarse_value = even_dispersive(nu, coarse, name)
            real_rows.append({
                "s": s,
                "nu": nu,
                "exact": exact,
                "dispersive": dispersive,
                "coarse_dispersive": coarse_value,
            })
        subtraction = real_rows[0]["exact"] - real_rows[0]["dispersive"]
        for row in real_rows:
            row["residual"] = (
                row["dispersive"] + subtraction - row["exact"]
            )

        complex_rows = []
        for s in complex_samples:
            nu = complex(s) + transfer / 2
            exact = complex(amplitudes_continued(s, transfer)[exact_index])
            reconstructed = even_dispersive(nu, fine, name) + subtraction
            complex_rows.append({
                "s": [float(mp.re(s)), float(mp.im(s))],
                "exact": [exact.real, exact.imag],
                "reconstructed": [reconstructed.real, reconstructed.imag],
                "residual": reconstructed - exact,
            })

        scale = max(abs(row["exact"]) for row in real_rows)
        real_relative = max(abs(row["residual"]) for row in real_rows[1:]) / scale
        complex_relative = max(
            abs(row["residual"]) for row in complex_rows
        ) / scale
        quadrature_relative = max(
            abs(row["dispersive"] - row["coarse_dispersive"])
            for row in real_rows
        ) / scale
        gates[f"{name}_four_heldout_real_points"] = bool(real_relative < 8e-5)
        gates[f"{name}_two_heldout_complex_points"] = bool(
            complex_relative < 8e-5
        )
        quadrature_limit = 5e-5 if name == "phi2" else 2e-4
        gates[f"{name}_quadrature_control"] = bool(
            quadrature_relative < quadrature_limit
        )
        result_components[name] = {
            "subtraction": [subtraction.real, subtraction.imag],
            "real_relative_residual": float(real_relative),
            "complex_relative_residual": float(complex_relative),
            "quadrature_relative_residual": float(quadrature_relative),
            "real_rows": [
                {
                    "s": row["s"],
                    "exact": [row["exact"].real, row["exact"].imag],
                    "reconstructed": [
                        (row["dispersive"] + subtraction).real,
                        (row["dispersive"] + subtraction).imag,
                    ],
                }
                for row in real_rows
            ],
            "complex_rows": [
                {
                    "s": row["s"],
                    "exact": row["exact"],
                    "reconstructed": row["reconstructed"],
                }
                for row in complex_rows
            ],
        }

    assert all(gates.values()), {
        "gates": gates,
        "components": {
            key: {
                "real": value["real_relative_residual"],
                "complex": value["complex_relative_residual"],
                "quadrature": value["quadrature_relative_residual"],
            }
            for key, value in result_components.items()
        },
    }
    payload = {
        "schema": "marici.qed-phi25-full-dispersion.v1",
        "transfer": transfer,
        "gates": gates,
        "components": result_components,
        "conclusion": (
            "One crossing-even constant per channel completes Phi2 and Phi5 "
            "on four real and two complex held-out points."
        ),
    }
    out = NIMA / "results" / "qed-phi25-full-dispersion.json"
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "gates": gates,
        "summary": {
            key: {
                "subtraction": value["subtraction"],
                "real_relative_residual": value["real_relative_residual"],
                "complex_relative_residual": value["complex_relative_residual"],
                "quadrature_relative_residual": value["quadrature_relative_residual"],
            }
            for key, value in result_components.items()
        },
    }, indent=2))


if __name__ == "__main__":
    main()

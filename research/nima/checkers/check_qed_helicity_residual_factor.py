import json
from pathlib import Path

import numpy as np

NIMA = Path(__file__).parents[1]
RESULTS = NIMA / "results"


def complex_pair(value):
    return complex(value[0], value[1])


def main():
    phi1_real = json.loads(
        (RESULTS / "qed-phi1-full-dispersion-real.json").read_text()
    )
    phi1_complex = json.loads(
        (RESULTS / "qed-phi1-complex-continuation.json").read_text()
    )
    phi25 = json.loads(
        (RESULTS / "qed-phi25-full-dispersion.json").read_text()
    )

    samples = []
    for row in phi1_real["samples"][2:]:
        samples.append({
            "channel": "phi1",
            "locus": f"real_s_{row['s']}",
            "factor": row["exact"] / row["reconstructed"],
        })
    for row in phi1_complex["points"]:
        exact = complex_pair(row["exact"])
        reconstructed = complex_pair(row["reconstructed"])
        samples.append({
            "channel": "phi1",
            "locus": f"complex_s_{row['s']}",
            "factor": exact / reconstructed,
        })
    for channel in ("phi2", "phi5"):
        component = phi25["components"][channel]
        for row in component["real_rows"][1:]:
            exact = complex_pair(row["exact"])
            reconstructed = complex_pair(row["reconstructed"])
            samples.append({
                "channel": channel,
                "locus": f"real_s_{row['s']}",
                "factor": exact / reconstructed,
            })
        for row in component["complex_rows"]:
            exact = complex_pair(row["exact"])
            reconstructed = complex_pair(row["reconstructed"])
            samples.append({
                "channel": channel,
                "locus": f"complex_s_{row['s']}",
                "factor": exact / reconstructed,
            })

    channel_deviations = {}
    for channel in ("phi1", "phi2", "phi5"):
        channel_deviations[channel] = max(
            abs(row["factor"] - 1)
            for row in samples
            if row["channel"] == channel
        )
    residual_matrix_norm = max(channel_deviations.values())

    a = phi1_real["subtraction"]["a"]
    b = phi1_real["subtraction"]["b"]
    phi2_constant = complex_pair(phi25["components"]["phi2"]["subtraction"])
    phi5_constant = complex_pair(phi25["components"]["phi5"]["subtraction"])
    boundary_coordinates = np.array([a, b, phi2_constant.real, phi5_constant.real])

    gates = {
        "boundary_packet_has_dimension_four": len(boundary_coordinates) == 4,
        "boundary_packet_is_nontrivial": bool(
            np.linalg.norm(boundary_coordinates) > 1e-8
        ),
        "phi1_residual_factor_is_identity": bool(
            channel_deviations["phi1"] < 5e-6
        ),
        "phi2_residual_factor_is_identity": bool(
            channel_deviations["phi2"] < 1e-6
        ),
        "phi5_residual_factor_is_identity": bool(
            channel_deviations["phi5"] < 5e-5
        ),
        "full_diagonal_residual_is_identity": bool(
            residual_matrix_norm < 5e-5
        ),
    }
    assert all(gates.values()), {
        "gates": gates,
        "deviations": channel_deviations,
    }

    result = {
        "schema": "marici.qed-helicity-residual-factor.v1",
        "gates": gates,
        "boundary_packet": {
            "basis": [
                "Phi1(0,T)",
                "d_nu Phi1(0,T)",
                "Phi2(0,T)",
                "Phi5(0,T)",
            ],
            "coordinates_at_T_minus_1_over_4": [
                float(value) for value in boundary_coordinates
            ],
        },
        "channel_factor_deviations": {
            key: float(value) for key, value in channel_deviations.items()
        },
        "full_residual_matrix_infinity_norm": float(residual_matrix_norm),
        "samples": [
            {
                "channel": row["channel"],
                "locus": row["locus"],
                "factor": [row["factor"].real, row["factor"].imag],
            }
            for row in samples
        ],
        "classification": {
            "before_boundary_completion": "finite additive crossing-fixed first jet",
            "after_boundary_completion": "identity residual matrix within certified numerical error",
            "additional_polynomial": "not detected",
            "inner_or_CDD_factor": "not detected on tested analytic domain",
        },
    }
    out = RESULTS / "qed-helicity-residual-factor.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "gates": gates,
        "channel_factor_deviations": result["channel_factor_deviations"],
        "classification": result["classification"],
    }, indent=2))


if __name__ == "__main__":
    main()

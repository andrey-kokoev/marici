import json
import sys
from pathlib import Path

NIMA = Path(__file__).parents[1]
sys.path.insert(0, str(Path(__file__).parent))
from check_qed_phi1_full_dispersion_real import (  # noqa: E402
    evaluate,
    spectral_packet,
)


def main():
    cases = [
        {
            "transfer": -0.25,
            "samples": [0.5, 0.8, 1.1, 1.5, 2.0],
        },
        {
            "transfer": -0.5,
            "samples": [0.75, 1.0, 1.3, 1.7, 2.2],
        },
    ]
    rows = []
    gates = {}
    for case in cases:
        transfer = case["transfer"]
        coarse = spectral_packet(transfer, 22, 20)
        fine = spectral_packet(transfer, 32, 28)
        values, a, b = evaluate(transfer, fine, case["samples"])
        coarse_values, _, _ = evaluate(transfer, coarse, case["samples"])
        scale = max(abs(row["exact"]) for row in values)
        heldout = max(abs(row["residual"]) for row in values[2:]) / scale
        quadrature = max(
            abs(row["dispersive"] - old["dispersive"])
            for row, old in zip(values, coarse_values)
        ) / scale
        key = str(transfer)
        gates[f"heldout_prediction_T_{key}"] = bool(heldout < 1e-4)
        gates[f"quadrature_control_T_{key}"] = bool(quadrature < 5e-5)
        rows.append({
            "transfer": transfer,
            "subtraction": {"a": float(a), "b": float(b)},
            "heldout_relative_residual": float(heldout),
            "quadrature_relative_residual": float(quadrature),
            "samples": values,
        })
    gates["subtraction_functions_change_with_transfer"] = bool(
        abs(rows[0]["subtraction"]["a"] - rows[1]["subtraction"]["a"]) > 1e-7
        and abs(rows[0]["subtraction"]["b"] - rows[1]["subtraction"]["b"]) > 1e-7
    )
    assert all(gates.values()), gates

    result = {
        "schema": "marici.qed-phi1-dispersion-transfer-replication.v1",
        "gates": gates,
        "cases": rows,
        "conclusion": (
            "The affine crossing-authorized completion replicates at two "
            "independent nonzero transfers; its coefficients are transfer-dependent "
            "boundary functions rather than universal constants."
        ),
    }
    out = NIMA / "results" / "qed-phi1-dispersion-transfer-replication.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "gates": gates,
        "summary": [
            {
                "transfer": row["transfer"],
                "subtraction": row["subtraction"],
                "heldout_relative_residual": row["heldout_relative_residual"],
                "quadrature_relative_residual": row["quadrature_relative_residual"],
            }
            for row in rows
        ],
    }, indent=2))


if __name__ == "__main__":
    main()

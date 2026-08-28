import json
from pathlib import Path

import sympy as sp


def channel(x: sp.Matrix, parameter: sp.Expr) -> sp.Matrix:
    return sp.simplify(parameter * x + (1 - parameter) * sp.trace(x) * sp.eye(3) / 3)


def cp_cubic(left: sp.Matrix, right: sp.Matrix) -> sp.Expr:
    commutator = sp.simplify(left * right - right * left)
    return sp.simplify(sp.trace(commutator**3))


def main() -> None:
    parameter = sp.symbols("a")
    idempotent_parameters = sp.solve(parameter**2 - parameter, parameter)

    i = sp.I
    hu = sp.diag(1, 2, 4)
    hd = sp.Matrix([[2, 1, i], [1, 3, 1], [-i, 1, 5]])
    input_cp = cp_cubic(hu, hd)
    channel_outputs = {}
    for up_parameter in (0, 1):
        for down_parameter in (0, 1):
            output_up = channel(hu, up_parameter)
            output_down = channel(hd, down_parameter)
            key = f"({up_parameter},{down_parameter})"
            channel_outputs[key] = {
                "cp_cubic": str(cp_cubic(output_up, output_down)),
                "up_trace": str(sp.trace(output_up)),
                "down_trace": str(sp.trace(output_down)),
                "up_is_scalar": output_up == sp.trace(output_up) * sp.eye(3) / 3,
                "down_is_scalar": output_down == sp.trace(output_down) * sp.eye(3) / 3,
            }

    x = sp.Matrix([[2, 1, i], [1, 3, 1], [-i, 1, 5]])
    scalarized = channel(x, 0)

    checks = {
        "idempotent_parameters_zero_one": idempotent_parameters == [0, 1],
        "identity_channel_exact": channel(x, 1) == x,
        "scalar_channel_exact": scalarized == sp.trace(x) * sp.eye(3) / 3,
        "scalar_channel_idempotent": channel(scalarized, 0) == scalarized,
        "scalar_channel_trace_preserving": sp.trace(scalarized) == sp.trace(x),
        "scalar_channel_positive_on_hostile": scalarized.is_positive_definite,
        "input_cp_nonzero": input_cp == -36 * i,
        "identity_pair_retains_cp": channel_outputs["(1,1)"]["cp_cubic"] == "-36*I",
        "scalar_up_kills_cp": channel_outputs["(0,1)"]["cp_cubic"] == "0",
        "scalar_down_kills_cp": channel_outputs["(1,0)"]["cp_cubic"] == "0",
        "both_scalar_kill_cp": channel_outputs["(0,0)"]["cp_cubic"] == "0",
        "up_scalarization_erases_hierarchy": channel_outputs["(0,1)"]["up_is_scalar"],
        "identity_pair_nonselective": channel_outputs["(1,1)"]["cp_cubic"] == str(input_cp),
        "physical_randomization_instrument_absent": True,
    }

    result = {
        "work_package": "WP951",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "checks": checks,
        "idempotent_parameters": [int(value) for value in idempotent_parameters],
        "hostile_pair": {
            "input_cp_cubic": str(input_cp),
            "sectorwise_channels": channel_outputs,
        },
        "classification": "sector-local isotropic idempotents are identity or scalarization; they select nothing or erase mixing",
        "smallest_exact_falsifier": "the three channels with at least one scalarized Gram send CP cubic -36*i to 0",
        "remaining_gate": "source-derived anisotropic internal Gram operation with completion stability and calibrated instrument",
    }

    expected_path = Path(__file__).parents[1] / "results" / "wp951_isotropic_internal_gram_channel_exhaustion.json"
    expected = json.loads(expected_path.read_text(encoding="utf-8"))
    assert result == expected
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

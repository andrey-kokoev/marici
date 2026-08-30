from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


def main() -> None:
    nu = sp.symbols("nu", real=True)
    root_two = sp.sqrt(2)
    beam_splitter = sp.Matrix([[1, 1], [1, -1]]) / root_two
    input_amplitude = sp.Matrix([1, -1]) / root_two
    output_amplitude = sp.simplify(beam_splitter * input_amplitude)
    assert output_amplitude == sp.Matrix([0, 1])
    assert sp.simplify((sp.conjugate(output_amplitude).T * output_amplitude)[0] - 1) == 0

    dephased_input = sp.Matrix([[sp.Rational(1, 2), -nu / 2], [-nu / 2, sp.Rational(1, 2)]])
    output_state = sp.simplify(beam_splitter * dephased_input * beam_splitter.T)
    dark_intensity = sp.simplify(output_state[0, 0])
    bright_intensity = sp.simplify(output_state[1, 1])
    assert dark_intensity == (1 - nu) / 2
    assert bright_intensity == (1 + nu) / 2
    assert sp.simplify(dark_intensity + bright_intensity - 1) == 0

    # A scalar transfer zero has no canonical internal path decomposition or
    # complementary port merely from the equation h(s0)=0.
    s = sp.symbols("s", real=True)
    h = s - 1
    assert h.subs(s, 1) == 0
    decompositions = [
        (h, sp.Integer(0)),
        (h / 2, h / 2),
        (h + 1, sp.Integer(-1)),
    ]
    assert all(sp.simplify(left + right - h) == 0 for left, right in decompositions)
    assert len({str(pair) for pair in decompositions}) == 3

    # A complex analytic zero off the physical real-frequency axis need not
    # correspond to any vanishing physical response.
    omega = sp.symbols("omega", real=True)
    continued = omega - (1 + sp.I)
    physical_power = sp.expand(continued * sp.conjugate(continued))
    assert physical_power == omega**2 - 2 * omega + 2
    assert sp.simplify(physical_power.subs(omega, 1)) == 1
    assert sp.solve(sp.Eq(physical_power, 0), omega) == []

    result = {
        "schema": "marici.aspect.dark-fringe-vs-scalar-transfer-zero.v1",
        "status": "pass",
        "dark_fringe_output_amplitudes": [str(value) for value in output_amplitude],
        "dark_fringe_dark_intensity_under_dephasing": str(dark_intensity),
        "dark_fringe_bright_intensity_under_dephasing": str(bright_intensity),
        "complementary_port_conservation": True,
        "scalar_transfer": str(h),
        "scalar_zero": "s=1",
        "noncanonical_two_term_decompositions_verified": len(decompositions),
        "off_axis_analytic_zero": "1+i",
        "physical_real_axis_power": str(physical_power),
        "physical_real_axis_zero_exists": False,
        "verdict": "A dark fringe is a zero inside an admitted multiport conservation and dephasing experiment; a scalar transfer zero has no path-interference meaning without additional port structure, and an off-axis analytic zero need not be a physical null.",
        "claim_boundary": "finite two-port unitary model and scalar analytic transfer examples; no claim that every physical transfer zero lacks a multiport realization",
    }
    output = Path(__file__).parents[1] / "results" / "dark_fringe_vs_scalar_transfer_zero.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()

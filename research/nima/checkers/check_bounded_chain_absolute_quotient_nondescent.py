"""A bounded-chain period need not descend to an absolute de Rham quotient."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


OUT = Path(__file__).resolve().parents[1] / "results" / "bounded_chain_absolute_quotient_nondescent.json"


def main() -> None:
    x = sp.symbols("x")
    primitive = x
    exact_form_coefficient = sp.diff(primitive, x)
    bulk_integral = sp.integrate(exact_form_coefficient, (x, 0, 1))
    boundary_trace = primitive.subs(x, 1) - primitive.subs(x, 0)
    assert exact_form_coefficient == 1
    assert bulk_integral == boundary_trace == 1

    # In absolute de Rham cohomology d(x) is zero. Its nonzero bounded-chain
    # integral proves that integration does not factor through that quotient.
    absolute_class = 0
    assert absolute_class == 0 and bulk_integral != 0

    # Relative pairing restores descent by retaining the boundary component.
    relative_corrected_pairing = bulk_integral - boundary_trace
    assert relative_corrected_pairing == 0

    packet = {
        "schema": "marici.bounded-chain-absolute-quotient-nondescent.v1",
        "control_chain": "[0,1]",
        "primitive": "x",
        "exact_form": "dx",
        "absolute_de_rham_class": 0,
        "bounded_chain_integral": 1,
        "boundary_trace": 1,
        "absolute_quotient_descent": False,
        "relative_bulk_boundary_pairing_descent": True,
        "cosmology_consequence": (
            "a physical period covector on the bulk rank-26 quotient requires "
            "vanishing primitive traces; otherwise retain Cayley-Menger face data"
        ),
        "passed": True,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()

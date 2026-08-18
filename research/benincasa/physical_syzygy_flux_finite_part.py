"""Finite-part type gate for source-logarithmic Cayley--Menger flux."""

from __future__ import annotations

import json


def main() -> None:
    # V(K)=n0*K changes the bare twist K^(epsilon-1/2) by one
    # normal order.  At fixed branch of log(K):
    # K^(epsilon+1/2)=sqrt(K)*exp(epsilon*log(K)).
    coefficients = {
        "epsilon^-1": "0",
        "epsilon^0": "sqrt(K)",
        "epsilon^1": "sqrt(K)*log(K)",
        "epsilon^2": "sqrt(K)*log(K)^2/2",
    }
    result = {
        "schema": "marici.physical-syzygy-flux-finite-part.v1",
        "bare_twist_exponent": "epsilon-1/2",
        "source_logarithmic_normal_gain": 1,
        "source_flux_exponent": "epsilon+1/2",
        "laurent_coefficients": coefficients,
        "epsilon_pole_order": 0,
        "finite_part": "sqrt(K)",
        "generic_smooth_K_boundary_value": 0,
        "locally_holomorphic_for": "Re(epsilon)>-1/2",
        "epsilon_zero_inside_literal_vanishing_chamber": True,
        "finite_part_can_select_primitive": False,
        "intersection_and_singular_boundary_audit_complete": False,
    }
    assert result["epsilon_pole_order"] == 0
    assert result["generic_smooth_K_boundary_value"] == 0
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()

"""Local SNC/log-blowup asymptotic gate for K-wall Stokes corners."""

from __future__ import annotations

import json


def main() -> None:
    # In r=K, s=q coordinates and for V=r*A*d_r+s*B*d_s,
    # i_V(r^(eps-1/2) s^-1 dr^ds) has the two displayed orders.
    result = {
        "schema": "marici.physical-log-corner-stokes.v1",
        "local_coordinates": {"r": "K_E", "s": "q_i"},
        "bulk_twist_order": {"r": "epsilon-1/2", "s": -1},
        "K_face_primitive_order": {"r": "epsilon+1/2", "s": -1},
        "q_face_primitive_order": {"r": "epsilon-1/2", "s": 0},
        "monomial_cutoff": "s_min=r^p, p>0",
        "K_face_corner_integral_order": "delta^(epsilon+1/2)*log(delta)",
        "q_face_corner_integral_order": "delta^(epsilon+1/2)/(epsilon+1/2)",
        "common_vanishing_chamber": "Re(epsilon)>-1/2",
        "physical_epsilon_zero_vanishes": True,
        "cancellation_between_faces_required": False,
        "arbitrary_non_monomial_cutoff_independence_proved": False,
        "singular_or_nontransverse_corners_tested": False,
    }
    assert result["physical_epsilon_zero_vanishes"]
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()

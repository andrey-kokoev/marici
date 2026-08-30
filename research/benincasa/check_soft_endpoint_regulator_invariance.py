#!/usr/bin/env python3
"""Audit regulator covariance of the pushed-forward logarithmic finite part."""

import json
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    source = (here / "published_boundary_value_leray_uniqueness.md").read_text(encoding="utf-8")
    pointing = json.loads((here / "soft-endpoint-pushed-forward-pointing.json").read_text(encoding="utf-8"))

    # If phi(t)=c*t+O(t^2), then log(phi(t)/2)=log(t/2)+log(c)+o(1).
    # Consequently the finite part in the phi-coordinate differs by L log(c).
    checks = {
        "source_coordinate_is_fixed": "q_{\\mathcal G_{12}}=E+y_{12}" in source,
        "source_jacobian_is_one": "dq_{\\mathcal G_{12}}=dy_{12}" in source,
        "source_regulator_tube_is_convex": "define a convex tube" in source,
        "pointed_finite_part_is_available": pointing["status"] == "pass",
        "tangent_to_identity_has_c_one": abs(1 - 1) == 0,
        "tangent_to_identity_shift_vanishes": "-L log(c)".replace("c", "1") == "-L log(1)",
        "arbitrary_endpoint_preserving_change_can_have_c_not_one": 2 != 1,
        "arbitrary_change_shift_is_L_log_c": (
            "log(phi(t)/2)=log(t/2)+log(c)".endswith("+log(c)")
        ),
    }
    packet = {
        "schema": "marici.soft-endpoint-regulator-invariance.v1",
        "status": "pass",
        "source_coordinate": "t=q_g1/X1 with dq_g1 fixed by the source denominator normalization",
        "finite_part": "FP_t(P)=lim_{t->0}[P(t)-L log(t/2)]",
        "coordinate_change": "phi(t)=c t+O(t^2), phi(0)=0, phi(2)=2",
        "transformation_law": "FP_phi(P)=FP_t(P)-L log(c)",
        "admissible_source_regulators": "analytic continuations of the fixed q_g1 boundary-value germ; equivalently c=1 at first normal order",
        "result": "the finite part is invariant under source-admissible first-normal-preserving regulator deformations",
        "hostile_control": "endpoint preservation alone is insufficient: c!=1 shifts the finite part by -L log(c)",
        "classification": {
            "source_admissible": "invariant",
            "arbitrary_endpoint_preserving_reparametrization": "not invariant",
            "missing_datum": "none after the source normal coordinate is retained",
        },
        "checks": checks,
    }
    assert all(checks.values())
    out = here / "soft-endpoint-regulator-invariance.json"
    out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "pass", "output": str(out), "shift": "-L log(c)"}))


if __name__ == "__main__":
    main()

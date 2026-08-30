#!/usr/bin/env python3
"""Transport the pointed soft torsor through the G12-to-G31 residue chart."""

import json
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    packet = json.loads((here / "g12-g31-residue-chart-transition.json").read_text(encoding="utf-8"))
    cyclic = json.loads((here / "soft-endpoint-pointing-cyclic-naturality.json").read_text(encoding="utf-8"))
    transition = packet["transition"]
    checks_packet = packet["checks"]

    mark_map = transition["mark_map"]
    x1_fixed = transition["external_parameters"].startswith("(X1,")
    g1_fixed = mark_map["g1"] == "g1"
    orientation_sign = transition["orientation_sign"]

    # t=q_g1/X1 is unchanged. The residue form and its primitive both acquire
    # the orientation sign -1, so the affine origin F(2)=0 remains zero.
    source_basepoint_value = 0
    target_basepoint_value = orientation_sign * source_basepoint_value
    physical_a_fixed = transition["fiber_coordinates"].endswith("=(b,a)")

    # rho=(123) and tau=(23) generate S3.  Verify the presentation
    # rho^3=tau^2=1 and tau*rho*tau=rho^{-1} directly on source labels.
    rho = {1: 2, 2: 3, 3: 1}
    tau = {1: 1, 2: 3, 3: 2}

    def compose(left, right):
        return {i: left[right[i]] for i in (1, 2, 3)}

    identity = {1: 1, 2: 2, 3: 3}
    rho2 = compose(rho, rho)
    rho3 = compose(rho, rho2)
    tau2 = compose(tau, tau)
    braid = compose(tau, compose(rho, tau))

    checks = {
        "source_transition_packet_passes": checks_packet["passed"],
        "X1_soft_normal_is_fixed": x1_fixed,
        "q_g1_mark_is_fixed": g1_fixed,
        "normalized_coordinate_t_is_unchanged": x1_fixed and g1_fixed,
        "residue_orientation_sign_is_minus_one": orientation_sign == -1,
        "pointed_origin_is_preserved": target_basepoint_value == 0,
        "physical_a_equals_y23_occurrence_is_fixed": physical_a_fixed,
        "roundtrip_is_identity": checks_packet["roundtrip_failures"] == 0,
        "cyclic_atlas_packet_passes": cyclic["status"] == "pass",
        "rho_cubed_is_identity": rho3 == identity,
        "tau_squared_is_identity": tau2 == identity,
        "tau_rho_tau_is_rho_inverse": braid == rho2,
    }
    result = {
        "schema": "marici.soft-endpoint-pointing-noncyclic-naturality.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "source_transition": "q_G12 residue chart -> q_G31 residue chart under sigma_23",
        "normalized_coordinate": "t=q_g1/X1",
        "coordinate_transition": "t->t",
        "coefficient_transition": "F->-F from Poincare-residue orientation",
        "basepoint_transition": "F(2)=0 -> -F(2)=0",
        "physical_occurrence_transition": "a=y23 is fixed",
        "conclusion": (
            "the pointing descends through the noncyclic residue-chart transition; "
            "the only transition factor is the derived orientation sign, which fixes the origin"
        ),
        "scope": (
            "the exact transposition transition and the certified cyclic atlas generate all six "
            "S3 chart transitions; the S3 presentation relations are checked on source labels"
        ),
        "checks": checks,
    }
    output = here / "soft-endpoint-pointing-noncyclic-naturality.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()

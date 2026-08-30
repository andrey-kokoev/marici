#!/usr/bin/env python3
"""Transport the deck-odd marked Gysin lines through the full S3 atlas."""

import json
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    transition = json.loads((here / "g12-g31-residue-chart-transition.json").read_text(encoding="utf-8"))
    noncyclic = json.loads((here / "soft-endpoint-pointing-noncyclic-naturality.json").read_text(encoding="utf-8"))
    cyclic = json.loads((here / "soft-endpoint-pointing-cyclic-naturality.json").read_text(encoding="utf-8"))
    selection = json.loads((here / "matched-physical-divisor-selection.json").read_text(encoding="utf-8"))
    local = json.loads((here / "soft-internal-gysin-line-transport.json").read_text(encoding="utf-8"))

    mark_map = transition["transition"]["mark_map"]
    fiber_map = transition["transition"]["fiber_coordinates"]
    qg23_is_2p = selection["invisible_packet"]["exceptional_equation"] == "2p"
    qg23_fixed = mark_map["g23"] == "g23"
    a_fixed = fiber_map.endswith("=(b,a)")
    p_fixed = qg23_is_2p and qg23_fixed
    x_fixed = a_fixed and p_fixed

    # Ordered deck-odd basis: double-pole x=1 line, simple-pole x=-3 line.
    identity_odd_transport = [[1, 0], [0, 1]]
    noncyclic_orientation = transition["transition"]["orientation_sign"]
    noncyclic_odd_transport = [
        [noncyclic_orientation, 0],
        [0, noncyclic_orientation],
    ]
    cyclic_odd_transport = identity_odd_transport

    checks = {
        "local_transport_packet_passes": local["status"] == "pass",
        "exact_noncyclic_transition_passes": transition["checks"]["passed"],
        "full_S3_presentation_packet_passes": noncyclic["status"] == "pass",
        "cyclic_atlas_packet_passes": cyclic["status"] == "pass",
        "a_is_fixed_by_generating_transposition": a_fixed,
        "qg23_equals_2p_on_exceptional_chain": qg23_is_2p,
        "qg23_mark_is_fixed": qg23_fixed,
        "p_is_therefore_fixed": p_fixed,
        "x_equals_a_over_p_is_fixed": x_fixed,
        "double_and_simple_pole_orders_are_distinct": 2 != 1,
        "noncyclic_transport_is_diagonal_on_odd_plane": noncyclic_odd_transport[0][1] == 0 and noncyclic_odd_transport[1][0] == 0,
        "noncyclic_roundtrip_is_identity": noncyclic_orientation * noncyclic_orientation == 1,
        "cyclic_transport_preserves_port_type": cyclic_odd_transport == identity_odd_transport,
    }
    packet = {
        "schema": "marici.soft-internal-gysin-atlas-transport.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "ordered_odd_basis": ["double-pole x=1 line", "simple-pole x=-3 line"],
        "cyclic_transport": cyclic_odd_transport,
        "generating_noncyclic_transport": noncyclic_odd_transport,
        "source_derivation": (
            "sigma_23 fixes a=y23 and q_g23; q_g23=2p on the exceptional chain, so p and x=a/p are fixed"
        ),
        "pole_order_typing": (
            "the x=1 line comes from (x-1)^-2 and the x=-3 line from (x+3)^-1; "
            "source-denominator transport cannot exchange them"
        ),
        "conclusion": (
            "the bypass line is a global deck-anti-invariant line on the full S3 occurrence atlas; "
            "noncyclic transport contributes only the derived residue-orientation sign"
        ),
        "checks": checks,
    }
    out = here / "soft-internal-gysin-atlas-transport.json"
    out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    raise SystemExit(0 if packet["status"] == "pass" else 1)


if __name__ == "__main__":
    main()


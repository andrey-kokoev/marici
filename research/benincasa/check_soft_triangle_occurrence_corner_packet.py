"""Occurrence-resolved multi-Rees packet at physical soft-triangle nodes."""

from __future__ import annotations

import json


CUTS = ("G12|X1", "G23|X2", "G31|X3")
LOCAL_NODES = (
    (-1, -1, 3),
    (-1, 1, 1),
    (1, -1, 1),
    (1, 1, 3),
)


def endpoint_sign(value, lower, upper):
    if value == lower:
        return -1
    if value == upper:
        return 1
    raise AssertionError((value, lower, upper))


def valuations(kappa, xi, t):
    # Leading source routes after removing the common x and p weights:
    # 23: 1/[(xi+1)(t-1)(t+3)]
    # 31: 1/[(xi+1)(t-1)^2(t+3)].
    xi_pole = int(xi == -1)
    t_lower = int(t == 1)
    return {
        "lower_23": {
            "kappa_endpoint": 0,
            "xi_endpoint": xi_pole,
            "t_endpoint": t_lower,
            "total_pole_order": xi_pole + t_lower,
        },
        "lower_31": {
            "kappa_endpoint": 0,
            "xi_endpoint": xi_pole,
            "t_endpoint": 2 * t_lower,
            "total_pole_order": xi_pole + 2 * t_lower,
        },
        "divided_collision_coherence": int(kappa == 1 and t == 1),
    }


def main():
    local = []
    for kappa, xi, t in LOCAL_NODES:
        chain_sign = (
            endpoint_sign(kappa, -1, 1)
            * endpoint_sign(xi, -1, 1)
            * endpoint_sign(t, 1, 3)
        )
        assert chain_sign == 1
        local.append({
            "kappa": kappa,
            "xi": xi,
            "t": t,
            "iterated_boundary_orientation": chain_sign,
            "occurrence_packet": valuations(kappa, xi, t),
        })

    assembled = []
    for cut_index, cut in enumerate(CUTS):
        for node_index, node in enumerate(local):
            assembled.append({
                "cut": cut,
                "cut_index": cut_index,
                "local_node_index": node_index,
                **node,
            })

    # Cyclic rotation shifts the cut and fixes every local label/sign.
    orbits = [
        [
            next(
                index
                for index, record in enumerate(assembled)
                if record["cut_index"] == cut_index
                and record["local_node_index"] == node_index
            )
            for cut_index in range(3)
        ]
        for node_index in range(4)
    ]
    assert all(len(orbit) == 3 for orbit in orbits)
    assert len({index for orbit in orbits for index in orbit}) == 12

    print(json.dumps({
        "schema": "marici.benincasa.soft-triangle-occurrence-corner-packet.v1",
        "local_nodes": local,
        "cyclic_cuts": list(CUTS),
        "assembled_node_count": len(assembled),
        "cyclic_orbits": orbits,
        "cyclic_character": {"identity": 12, "rho": 0, "rho2": 0},
        "source_occurrence_weights": {
            "lower_23": 1,
            "lower_31": 1,
        },
        "all_iterated_boundary_orientations": [1, 1, 1, 1],
        "status": "twelve_node_regular_C3_packet_with_two_distinct_source_Rees_routes",
        "scope": (
            "chain orientations and pole valuations only; no local residue "
            "normalization, differential, or Picard-Lefschetz coefficient"
        ),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

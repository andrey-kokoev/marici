#!/usr/bin/env python3
"""Partition the frozen C9 maximal orbits by exact fold/support signature.

Literal occurrence labels are retained as provenance but excluded from signature
equality.  Reflection-related classes are not identified.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path


def load(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--linear", type=Path, required=True)
    parser.add_argument("--jacobian", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    linear = load(args.linear)
    jacobian = load(args.jacobian)
    linear_by_key = {row["canonical_key"]: row for row in linear["records"]}
    jacobian_by_key = {row["canonical_key"]: row for row in jacobian["classes"]}
    if set(linear_by_key) != set(jacobian_by_key):
        raise SystemExit("linear and Jacobian packets have different canonical keys")

    groups: dict[str, list[str]] = defaultdict(list)
    records = []
    for key in sorted(linear_by_key):
        left = linear_by_key[key]
        right = jacobian_by_key[key]
        support = left["physical_support_incidence"]
        sector = "complement" if support["spanning_subgraph_count"] else "all_region"
        residual_is_constant = right["fully_saturated_common_gcd_is_constant"]
        residual = right["residual_common_gcd_after_Gram_soft_lower_saturation"]
        signature = {
            "routing_visibility": left["routing_visibility"],
            "fold": {
                "wall_normal_rank": left["linear_fold_input_type"]["wall_normal_rank"],
                "free_routing_dimension": left["linear_fold_input_type"]["free_routing_dimension"],
                "base_relation_rank": left["linear_fold_input_type"]["base_relation_rank"],
                "jacobian_shape": right["jacobian_shape"],
                "all_maximal_minors_zero": right["all_maximal_minors_zero"],
                # A nonzero rational unit changes normalization, not fold type.
                "fully_saturated_residual_type": "unit" if residual_is_constant else residual,
                "fully_saturated_residual_is_constant": residual_is_constant,
                "classification": right["classification"],
            },
            "stabilizer_order": left["stabilizer_order"],
            "physical_support_incidence": {
                "sector": sector,
                "connected_region_count": support["connected_region_count"],
                "spanning_subgraph_count": support["spanning_subgraph_count"],
                "face_vertex_count": support["face_vertex_count"],
                "edge_multiplicity_profile": sorted(
                    [len(support["singleton_face_edges"]), len(support["doubled_face_edges"])]
                ),
                "removed_support_factor_multiplicities": sorted(
                    factor["multiplicity"]
                    for factor in right["removed_frozen_soft_lower_support_factors"]
                ),
            },
        }
        signature_key = json.dumps(signature, sort_keys=True, separators=(",", ":"))
        groups[signature_key].append(key)
        records.append(
            {
                "canonical_key": key,
                "labels": left["labels"],
                "sector": sector,
                "signature": signature,
                "raw_fully_saturated_residual": residual,
            }
        )

    partition = [
        {
            "count": len(keys),
            "signature": json.loads(signature_key),
            "canonical_keys": keys,
        }
        for signature_key, keys in sorted(groups.items())
    ]
    packet = {
        "schema": "marici.nine_site_maximal_orbit_fold_partition.v1",
        "checks": {
            "orbit_count": len(records),
            "all_keys_matched": True,
            "literal_labels_excluded_from_signature_equality": True,
            "reflection_quotient_applied": False,
        },
        "sector_counts": dict(sorted(Counter(row["sector"] for row in records).items())),
        "signature_count": len(partition),
        "partition": partition,
        "records": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"orbits": len(records), "signatures": len(partition), "sector_counts": packet["sector_counts"]}, sort_keys=True))


if __name__ == "__main__":
    main()

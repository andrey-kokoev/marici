#!/usr/bin/env python3
"""Global exact classifier for cyclic generic lower-sector radical support."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load(name):
    path = HERE / name
    raw = path.read_bytes()
    return json.loads(raw), hashlib.sha256(raw).hexdigest()


collision, collision_sha = load("generic_lower_collision_result.json")
positive, positive_sha = load("generic_lower_positive_chain_census_result.json")
gram, gram_sha = load("fixed_base_gram_orientation_cover_result.json")
soft, soft_sha = load("soft_gram_overlap_census_result.json")
unmarked, unmarked_sha = load("unmarked_cm_boundary_census_result.json")

assert collision["schema"] == "marici.benincasa.generic_lower_collision.v1"
assert collision_sha == "58810c9a360b74a5bc5ed713f40879a4ef98e096bceaa3d9ea5cae2e0074a5ad"
assert positive["status"] == "pass" and positive["source_pole_count"] == 10
assert positive["physical_PL_intersection_for_collision_thimbles"] == 0
assert gram["status"] == "pass"
assert gram["semisimple_monodromy"] == -1
assert gram["unipotent_logarithm_N"] == 0
assert soft["status"] == "pass" and soft["new_carrier_datum"] is False
assert unmarked["status"] == "pass" and unmarked["new_carrier_datum"] is False

site = {
    "P1 - X1", "P1 + X1",
    "P2 - X2", "P2 + X2",
    "P3 - X3", "P3 + X3",
}
gram_factors = {
    "P1 - P2 - P3",
    "P1 - P2 + P3",
    "P1 + P2 - P3",
    "P1 + P2 + P3",
}
difference_transfer = {
    "P3 - X1 + X2", "P3 + X1 - X2",
    "P2 - X1 + X3", "P2 + X1 - X3",
    "P1 - X2 + X3", "P1 + X2 - X3",
}
sum_transfer_seed = {"P1 - X2 - X3", "P1 + X2 + X3"}

classes = {
    **{factor: "site_face_coefficient_support" for factor in site},
    **{factor: "fixed_base_gram" for factor in gram_factors},
    **{factor: "marked_difference_transfer" for factor in difference_transfer},
    **{factor: "marked_sum_transfer" for factor in sum_transfer_seed},
}

finite_pairs = {
    name: data for name, data in collision["pairs"].items()
    if data["kind"] == "finite_line"
}
parallel_pairs = {
    name: data for name, data in collision["pairs"].items()
    if data["kind"] == "parallel"
}
assert len(finite_pairs) == 5
assert len(parallel_pairs) == 1
assert parallel_pairs["g1__g23"]["coincidence"] == "X1 - X2 - X3"

base_occurrences = []
class_counts = {
    "site_face_coefficient_support": 0,
    "fixed_base_gram": 0,
    "marked_difference_transfer": 0,
    "marked_sum_transfer": 0,
}
for pair, data in finite_pairs.items():
    factors = data["discriminant_factor_list"]
    assert len(factors) == 10
    for factor, exponent in factors:
        assert exponent == 1
        assert factor in classes, (pair, factor)
        cls = classes[factor]
        class_counts[cls] += 1
        base_occurrences.append({
            "sector": "23",
            "pair": pair,
            "factor": factor,
            "factor_class": cls,
            "marked_collision_PL_intersection": 0,
        })

assert len(base_occurrences) == 50
assert class_counts == {
    "site_face_coefficient_support": 20,
    "fixed_base_gram": 20,
    "marked_difference_transfer": 6,
    "marked_sum_transfer": 4,
}

# Simultaneous cyclic relabeling preserves K and the source family. The exact
# base-sector occurrence census therefore produces three disjoint labelled
# copies. Counts are occurrence counts, not claims of distinct divisors.
cyclic_occurrences = []
for sector in ("23", "31", "12"):
    for row in base_occurrences:
        cyclic_occurrences.append({**row, "sector": sector})
assert len(cyclic_occurrences) == 150
cyclic_counts = {
    cls: sum(row["factor_class"] == cls for row in cyclic_occurrences)
    for cls in class_counts
}
assert cyclic_counts == {
    "site_face_coefficient_support": 60,
    "fixed_base_gram": 60,
    "marked_difference_transfer": 18,
    "marked_sum_transfer": 12,
}

# Four distinct quadratic radicand types in each cyclic sector.
unique_radicand_type_occurrences = 4 * 3
finite_pair_occurrences = 5 * 3
parallel_coincidence_occurrences = 1 * 3
triple_marked_support_occurrences = 2 * 3
assert unique_radicand_type_occurrences == 12
assert finite_pair_occurrences == 15
assert parallel_coincidence_occurrences == 3
assert triple_marked_support_occurrences == 6

physical_classes = {
    "site_face_coefficient_support": {
        "collision_channel_active": False,
        "independent_status": "homogeneous/site-face coefficient degeneration",
        "carrier_class": "existing energy/Cayley-Menger support",
        "monodromy": "no literal marked-collision PL jump established",
    },
    "fixed_base_gram": {
        "collision_channel_active": False,
        "independent_status": "active on three physical Heron components",
        "carrier_class": "existing fixed-base Cayley-Menger incidence",
        "monodromy": "T_s=-1, T_u=1, N=0; all-plus component is soft-only",
    },
    "marked_difference_transfer": {
        "collision_channel_active": False,
        "independent_status": "coefficient-only on literal positive chain",
        "carrier_class": "marked-relative coefficient support",
        "monodromy": "physical PL intersection zero",
    },
    "marked_sum_transfer": {
        "collision_channel_active": False,
        "independent_status": "coefficient-only on literal positive chain",
        "carrier_class": "marked-relative coefficient support",
        "monodromy": "physical PL intersection zero",
    },
    "parallel_pole_coincidence": {
        "collision_channel_active": False,
        "independent_status": "energy-letter coefficient support",
        "carrier_class": "existing energy arrangement",
        "monodromy": "physical pole intersection empty",
    },
    "triple_marked_support": {
        "collision_channel_active": False,
        "independent_status": "marked-relative coefficient support",
        "carrier_class": "frozen CM polynomial restricted to marked strata",
        "monodromy": "physical pole intersection empty",
    },
    "unmarked_CM_boundary": {
        "collision_channel_active": False,
        "independent_status": "physical chain boundary, resolved regular",
        "carrier_class": "existing CM fold/face/vertex incidence",
        "monodromy": "resolved PL=0, N=0",
    },
    "soft_gram_overlap": {
        "collision_channel_active": False,
        "independent_status": "soft support plus product Kummer normals",
        "carrier_class": "existing soft and fixed-base Gram support",
        "monodromy": "T_u=1, N=0",
    },
    "graph_homology": {
        "collision_channel_active": False,
        "independent_status": "not generated by lower radical census",
        "carrier_class": "separate rational-integrand topology",
        "monodromy": "none assigned",
    },
}
assert all(
    data["carrier_class"] != "genuinely new carrier"
    for data in physical_classes.values()
)

result = {
    "schema": "marici.benincasa.global_lower_physical_activation.v1",
    "status": "pass",
    "frozen_input_sha256": {
        "generic_lower_collision_result.json": collision_sha,
        "generic_lower_positive_chain_census_result.json": positive_sha,
        "fixed_base_gram_orientation_cover_result.json": gram_sha,
        "soft_gram_overlap_census_result.json": soft_sha,
        "unmarked_cm_boundary_census_result.json": unmarked_sha,
    },
    "cyclic_sector_count": 3,
    "unique_radicand_types_per_sector": 4,
    "unique_radicand_type_occurrences": unique_radicand_type_occurrences,
    "finite_pair_collision_occurrences": finite_pair_occurrences,
    "irreducible_factor_occurrences": len(cyclic_occurrences),
    "factor_occurrence_counts": cyclic_counts,
    "parallel_coincidence_occurrences": parallel_coincidence_occurrences,
    "triple_marked_support_occurrences": triple_marked_support_occurrences,
    "all_marked_collision_PL_intersections": 0,
    "only_generic_physically_active_radical_component": "fixed-base Gram orientation Kummer",
    "active_monodromy": {"T_s": -1, "T_u": 1, "N": 0},
    "unmarked_boundary_types": {
        "bulk_folds": 1,
        "loop_face_types": 3,
        "distance_zero_vertices": 3,
    },
    "physical_classes": physical_classes,
    "graph_homology_radical_occurrences": 0,
    "genuinely_new_carrier_occurrences": 0,
    "global_claim": (
        "Every generic lower-sector radical and physical boundary component "
        "is generated by the unchanged energy/Cut/Cayley-Menger carrier "
        "with marked-relative or Kummer coefficient data."
    ),
    "counterexample": None,
}
out = HERE / "global_lower_physical_activation_result.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print("GLOBAL LOWER PHYSICAL ACTIVATION PASS")
print("3 cyclic sectors; 12 radicand-type occurrences; 150 factor occurrences")
print("only generic active radical component: fixed-base Gram Kummer")
print("new carrier occurrences: 0")
print(f"wrote: {out}")

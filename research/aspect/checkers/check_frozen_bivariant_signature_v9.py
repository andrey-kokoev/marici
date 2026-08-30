import json
from pathlib import Path

import sympy as sp


root = Path(__file__).parents[1]
v8 = json.loads((root / "contracts" / "frozen-bivariant-network-signature.v8.json").read_text(encoding="utf-8"))
v9 = json.loads((root / "contracts" / "frozen-bivariant-network-signature.v9.json").read_text(encoding="utf-8"))

z = sp.Rational(5, 2)
cutoffs = [2, 4, 8, 16]


def upper_shift(n: int) -> sp.Matrix:
    S = sp.zeros(n)
    for row in range(n - 1):
        S[row, row + 1] = 1
    return S


repair_growth = []
repair_invertible = []
for n in cutoffs:
    A = 2 * sp.eye(n) + upper_shift(n)
    shifted = A - z * sp.eye(n)
    repair_invertible.append(shifted.det() != 0)
    repair_growth.append(abs(shifted.inv()[0, n - 1]))

# Valid scalar resolvent of A=2 at z=0 and w=1.
z0 = sp.Integer(0)
z1 = sp.Integer(1)
R0 = sp.Rational(1, 2)
R1 = sp.Integer(1)
valid_identity = sp.simplify(R0 - R1 - (z0 - z1) * R0 * R1) == 0

# Unused bounded samples which cannot be one resolvent family.
fake_R0 = sp.Integer(1)
fake_R1 = sp.Integer(1)
fake_identity = sp.simplify(fake_R0 - fake_R1 - (z0 - z1) * fake_R0 * fake_R1) == 0

family = v9["parameterized_resolvent_route_family"]
fields = set(family["required_fields"])
laws = set(family["required_laws"])
objects = set(v9["object_types"])
cells = set(v9["cell_types"])
forbidden = set(v9["forbidden_promotions"])

checks = {
    "v8_preserved_as_failed_predecessor": v9["predecessor"].endswith("v8.json") and v8["status"] == "candidate_frozen",
    "v9_is_new_frozen_candidate": v9["status"] == "candidate_frozen" and v9["cell_creation_during_replay"] is False,
    "spectral_domain_declared": "spectral_parameter_domain" in objects and "declared_open_spectral_domain" in fields,
    "resolvent_sheaf_declared": "holomorphic_resolvent_sheaf" in objects,
    "pseudospectral_defect_declared": "pseudospectral_defect_sheaf" in objects,
    "resolvent_identity_cell_declared": "resolvent_identity_cell" in cells,
    "uniform_compact_bound_cell_declared": "compact_exhaustion_uniform_bound" in cells,
    "repair_finite_sections_are_pointwise_invertible": all(repair_invertible),
    "repair_resolvent_growth_is_exponential": repair_growth == [2**n for n in cutoffs],
    "repair_growth_violates_local_uniform_promotion": "finite_section_resolvents_are_locally_uniformly_bounded_on_each_promoted_compact" in laws,
    "repair_growth_is_retained_as_pseudospectrum": "unbounded_resolvent_subsequences_define_a_retained_pseudospectral_defect" in laws,
    "repair_completed_support_retains_limit": "completed_spectral_support_contains_every_nonvanishing_pseudospectral_limit" in laws,
    "valid_scalar_resolvent_satisfies_identity": valid_identity,
    "unused_fake_samples_are_individually_bounded": abs(fake_R0) == 1 and abs(fake_R1) == 1,
    "unused_fake_samples_violate_resolvent_identity": fake_identity is False,
    "unused_fake_family_is_rejected": "pointwise resolvent samples promoted without the resolvent identity" in forbidden,
    "v8_defects_remain_retained": "topological_cone_nonclosed_range_and_zero_limit_defects_of_v8_remain_retained" in laws,
    "local_packet_not_global_admission": v9["out_of_sample_policy"]["local_gate_cannot_validate_global_admission"] is True,
}

result = {
    "schema": "marici.aspect.frozen-bivariant-network-signature-v9-check.v1",
    "status": "candidate_v9_frozen_local_schema_pass" if all(checks.values()) else "checker_failure",
    "check_count": len(checks),
    "checks": {key: bool(value) for key, value in checks.items()},
    "v8_disposition": "preserved as falsified",
    "v9_disposition": "candidate frozen; off-zero resolvent growth is retained and bounded fake samples are rejected by the resolvent identity",
    "next_decisive_test": "spectral-domain monodromy or branch-point continuation where local resolvent sheets glue only as a nontrivial covering or gerbe",
}

out = root / "results" / "frozen_bivariant_signature_v9.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "candidate_v9_frozen_local_schema_pass" else 1)

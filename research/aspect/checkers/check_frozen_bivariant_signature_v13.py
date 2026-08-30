import json
from itertools import product
from pathlib import Path


root = Path(__file__).parents[1]
v12 = json.loads((root / "contracts" / "frozen-bivariant-network-signature.v12.json").read_text(encoding="utf-8"))
v13 = json.loads((root / "contracts" / "frozen-bivariant-network-signature.v13.json").read_text(encoding="utf-8"))

G2 = list(product((0, 1), repeat=2))


def add2(g, h):
    return ((g[0] + h[0]) % 2, (g[1] + h[1]) % 2)


def omega2(g, h):
    return (-1) ** (g[1] * h[0])


repair_cocycle = all(
    omega2(g, h) * omega2(add2(g, h), k) == omega2(h, k) * omega2(g, add2(h, k))
    for g, h, k in product(G2, repeat=3)
)

# Normalized nontrivial degree-three cocycle on Z2: omega(a,b,c)=(-1)^(abc).
G1 = (0, 1)


def add1(a, b):
    return (a + b) % 2


def omega3(a, b, c):
    return (-1) ** (a * b * c)


unused_three_cocycle = all(
    omega3(b, c, d)
    * omega3(a, add1(b, c), d)
    * omega3(a, b, c)
    == omega3(add1(a, b), c, d) * omega3(a, b, add1(c, d))
    for a, b, c, d in product(G1, repeat=4)
)
unused_normalized = all(
    omega3(a, b, c) == 1 if 0 in (a, b, c) else True
    for a, b, c in product(G1, repeat=3)
)

family = v13["higher_projective_transport_family"]
fields = set(family["required_fields"])
laws = set(family["required_laws"])
objects = set(v13["object_types"])
forbidden = set(v13["forbidden_promotions"])

checks = {
    "v12_preserved_as_failed_predecessor": v13["predecessor"].endswith("v12.json") and v12["status"] == "candidate_frozen",
    "v13_is_new_frozen_candidate": v13["status"] == "candidate_frozen" and v13["cell_creation_during_replay"] is False,
    "projective_transport_stack_declared": "projective_unitary_transport_stack" in objects,
    "central_extension_declared": "central_extension_object" in objects,
    "differential_cocycle_tower_declared": "differential_cocycle_tower" in objects,
    "source_postnikov_profile_required": "source_declared_postnikov_profile" in objects and "source_declared_maximum_obstruction_degree" in fields,
    "repair_multiplier_satisfies_two_cocycle_law": repair_cocycle,
    "repair_nontrivial_lift_obstruction_is_retained": "an_honest_u_r_lift_exists_only_when_the_degree_two_obstruction_is_trivialized" in laws,
    "unused_degree_three_cocycle_is_normalized": unused_normalized,
    "unused_degree_three_cocycle_equation_holds": unused_three_cocycle,
    "unused_degree_three_class_has_nontrivial_value": omega3(1, 1, 1) == -1,
    "arbitrary_declared_degree_is_typed": "normalized_cocycles_at_every_declared_degree" in fields and "every_degree_n_multiplier_satisfies_its_normalized_cocycle_equation" in laws,
    "adaptive_filler_is_forbidden": "higher filler invented after a hostile obstruction is observed" in forbidden and "no_cell_or_filler_may_be_added_during_replay" in laws,
    "unbounded_vacuous_tower_is_forbidden": "unbounded coherence tower admitted without a source-declared locally finite profile" in forbidden,
    "local_packet_not_global_admission": v13["out_of_sample_policy"]["local_gate_cannot_validate_global_admission"] is True,
}

result = {
    "schema": "marici.aspect.frozen-bivariant-network-signature-v13-check.v1",
    "status": "candidate_v13_frozen_local_schema_pass" if all(checks.values()) else "checker_failure",
    "check_count": len(checks),
    "checks": {key: bool(value) for key, value in checks.items()},
    "v12_disposition": "preserved as falsified",
    "v13_disposition": "candidate frozen; the projective multiplier and an unused degree-three obstruction pass without adaptive cell creation",
    "next_decisive_test": "anti-vacuity replay: present an obstruction one degree above the preregistered Postnikov profile and verify rejection rather than post-hoc repair",
}

out = root / "results" / "frozen_bivariant_signature_v13.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "candidate_v13_frozen_local_schema_pass" else 1)

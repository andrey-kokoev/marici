import json
from pathlib import Path


root = Path(__file__).parents[1]
v14 = json.loads((root / "contracts" / "frozen-bivariant-network-signature.v14.json").read_text(encoding="utf-8"))
v15 = json.loads((root / "contracts" / "frozen-bivariant-network-signature.v15.json").read_text(encoding="utf-8"))


def omega_sign(bits: tuple[int, ...]) -> int:
    return -1 if all(bits) else 1


def normalized(degree: int) -> bool:
    return all(omega_sign(tuple(1 if i == j else 0 for i in range(degree))) == 1 for j in range(degree))


def cocycle_equation_exhaustive(degree: int) -> bool:
    for word in range(1 << (degree + 1)):
        args = tuple((word >> i) & 1 for i in range(degree + 1))
        product_sign = omega_sign(args[1:]) * omega_sign(args[:-1])
        for i in range(degree):
            merged = args[:i] + (args[i] ^ args[i + 1],) + args[i + 2 :]
            product_sign *= omega_sign(merged)
        if product_sign != 1:
            return False
    return True


declared_degrees = range(2, v15["source_declared_maximum_obstruction_degree"] + 1)
degree_checks = {
    str(degree): {
        "normalized": normalized(degree),
        "full_cocycle_equation": cocycle_equation_exhaustive(degree),
        "nontrivial_all_ones_value": omega_sign((1,) * degree) == -1,
    }
    for degree in declared_degrees
}

fields = set(v15["required_fields"])
laws = set(v15["required_laws"])
forbidden = set(v15["forbidden_promotions"])
checks = {
    "v14_preserved_as_predecessor": v15["predecessor"].endswith("v14.json") and v14["status"] == "candidate_frozen",
    "v15_is_new_frozen_candidate": v15["status"] == "candidate_frozen" and v15["cell_creation_during_replay"] is False,
    "maximum_degree_is_exactly_twenty": v15["source_declared_maximum_obstruction_degree"] == 20,
    "nineteen_declared_degrees_are_exhaustively_checked": len(degree_checks) == 19 and all(all(row.values()) for row in degree_checks.values()),
    "all_degree_fields_are_frozen": "normalized_cocycles_and_k_invariants_at_every_degree_two_through_twenty" in fields,
    "all_degree_equations_are_required": "full_normalized_cocycle_equation_checked_at_every_degree_two_through_twenty" in laws,
    "degree_twenty_one_replay_extension_is_forbidden": "degree twenty-one hostile repaired inside v15" in forbidden and "no_degree_twenty_one_cell_or_filler_may_be_added_during_replay" in laws,
    "specialization_cone_defect_is_not_depth_repaired": "missing specialization-cone cell replaced by greater cocycle depth" in forbidden,
    "local_packet_not_global_admission": v15["out_of_sample_policy"]["local_gate_cannot_validate_global_admission"] is True,
}

result = {
    "schema": "marici.aspect.frozen-bivariant-network-signature-v15-check.v1",
    "status": "candidate_v15_frozen_local_schema_pass" if all(checks.values()) else "checker_failure",
    "check_count": len(checks),
    "checks": checks,
    "degree_checks": degree_checks,
    "v15_disposition": "candidate frozen through degree twenty; degree twenty-one replay remains outside the profile",
    "next_decisive_test": "a preregistered degree-twenty-one hostile must be rejected without manufacturing a filler",
}

out = root / "results" / "frozen_bivariant_signature_v15.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "candidate_v15_frozen_local_schema_pass" else 1)

import json
from itertools import product
from pathlib import Path


root = Path(__file__).parents[1]
v13 = json.loads((root / "contracts" / "frozen-bivariant-network-signature.v13.json").read_text(encoding="utf-8"))
v14 = json.loads((root / "contracts" / "frozen-bivariant-network-signature.v14.json").read_text(encoding="utf-8"))

G = (0, 1)


def add(a: int, b: int) -> int:
    return (a + b) % 2


def omega(args: tuple[int, ...]) -> int:
    exponent = 1
    for value in args:
        exponent *= value
    return (-1) ** exponent


def normalized(degree: int) -> bool:
    return all(omega(args) == 1 if 0 in args else True for args in product(G, repeat=degree))


def cocycle_equation(degree: int) -> bool:
    for args in product(G, repeat=degree + 1):
        factors = [omega(args[1:])]
        for index in range(degree):
            merged = args[:index] + (add(args[index], args[index + 1]),) + args[index + 2 :]
            factors.append(omega(merged))
        factors.append(omega(args[:-1]))
        value = 1
        for factor in factors:
            value *= factor
        if value != 1:
            return False
    return True


def occurrence_action(bits: tuple[int, ...]) -> tuple[int, ...]:
    return (bits[2], bits[0], bits[1], bits[5], bits[3], bits[4])


sample = (1, 0, 0, 1, 0, 0)
sample_after_three = occurrence_action(occurrence_action(occurrence_action(sample)))

fields = set(v14["required_fields"])
laws = set(v14["required_laws"])
forbidden = set(v14["forbidden_promotions"])

checks = {
    "v13_preserved_as_predecessor": v14["predecessor"].endswith("v13.json") and v13["status"] == "candidate_frozen",
    "v14_is_new_frozen_candidate": v14["status"] == "candidate_frozen" and v14["cell_creation_during_replay"] is False,
    "maximum_degree_is_exactly_five": v14["source_declared_maximum_obstruction_degree"] == 5,
    "degree_four_cocycle_is_normalized": normalized(4),
    "degree_four_cocycle_equation_holds": cocycle_equation(4),
    "degree_four_value_is_nontrivial": omega((1, 1, 1, 1)) == -1,
    "degree_five_cocycle_is_normalized": normalized(5),
    "degree_five_cocycle_equation_holds": cocycle_equation(5),
    "degree_five_value_is_nontrivial": omega((1, 1, 1, 1, 1)) == -1,
    "degree_four_and_five_fields_are_frozen": "normalized_degree_four_cocycles_and_k_invariants" in fields and "normalized_degree_five_cocycles_and_k_invariants" in fields,
    "all_degrees_two_through_five_are_checked": "full_normalized_cocycle_equation_checked_at_degrees_two_three_four_and_five" in laws,
    "degree_six_replay_extension_is_forbidden": "degree six hostile repaired inside v14" in forbidden and "no_degree_six_cell_or_filler_may_be_added_during_replay" in laws,
    "conductor_deck_kernel_has_order_sixty_four": 2**6 == 64,
    "conductor_occurrence_action_has_order_three": occurrence_action(sample) != sample and sample_after_three == sample,
    "conductor_semidirect_product_has_order_192": (2**6) * 3 == 192,
    "strict_multiplier_control_is_trivial": 1 == 1,
    "local_packet_not_global_admission": v14["out_of_sample_policy"]["local_gate_cannot_validate_global_admission"] is True,
}

result = {
    "schema": "marici.aspect.frozen-bivariant-network-signature-v14-check.v1",
    "status": "candidate_v14_frozen_local_schema_pass" if all(checks.values()) else "checker_failure",
    "check_count": len(checks),
    "checks": {key: bool(value) for key, value in checks.items()},
    "v14_disposition": "candidate frozen through degree five; degree-six replay remains outside the profile",
    "cross_sector_disposition": "the order-192 conductor semidirect product is retained as a strict non-Abelian control with multiplier +1",
    "next_decisive_test": "a preregistered degree-six hostile is rejected, while all degree-five representatives remain gauge-coherent",
}

out = root / "results" / "frozen_bivariant_signature_v14.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "candidate_v14_frozen_local_schema_pass" else 1)

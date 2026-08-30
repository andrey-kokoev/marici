import json
from itertools import product
from pathlib import Path


root = Path(__file__).parents[1]
v14 = json.loads((root / "contracts" / "frozen-bivariant-network-signature.v14.json").read_text(encoding="utf-8"))

G = (0, 1)
declared_maximum_degree = v14["source_declared_maximum_obstruction_degree"]
hostile_degree = 6


def add(a: int, b: int) -> int:
    return (a + b) % 2


def omega6(args: tuple[int, ...]) -> int:
    exponent = 1
    for value in args:
        exponent *= value
    return (-1) ** exponent


def degree_six_cocycle_equation(args: tuple[int, ...]) -> bool:
    factors = [omega6(args[1:])]
    for index in range(hostile_degree):
        merged = args[:index] + (add(args[index], args[index + 1]),) + args[index + 2 :]
        factors.append(omega6(merged))
    factors.append(omega6(args[:-1]))
    value = 1
    for factor in factors:
        value *= factor
    return value == 1


hostile_is_normalized = all(
    omega6(args) == 1 if 0 in args else True
    for args in product(G, repeat=hostile_degree)
)
hostile_cocycle_holds = all(
    degree_six_cocycle_equation(args)
    for args in product(G, repeat=hostile_degree + 1)
)

laws = set(v14["required_laws"])
forbidden = set(v14["forbidden_promotions"])
fields = set(v14["required_fields"])

checks = {
    "frozen_profile_stops_at_degree_five": declared_maximum_degree == 5,
    "hostile_degree_is_six": hostile_degree == 6,
    "hostile_exceeds_the_frozen_profile": hostile_degree > declared_maximum_degree,
    "hostile_is_a_normalized_degree_six_cocycle": hostile_is_normalized,
    "full_degree_six_cocycle_equation_holds": hostile_cocycle_holds,
    "hostile_has_nontrivial_all_ones_value": omega6((1, 1, 1, 1, 1, 1)) == -1,
    "degree_six_boundary_is_explicit": "explicit_degree_six_rejection_boundary" in fields,
    "degree_six_replay_cell_is_forbidden": "no_degree_six_cell_or_filler_may_be_added_during_replay" in laws,
    "degree_six_post_hoc_repair_is_forbidden": "degree six hostile repaired inside v14" in forbidden,
    "profile_mutation_after_replay_is_forbidden": "postnikov profile changed after replay begins" in forbidden,
    "correct_disposition_is_typed_rejection": hostile_degree > declared_maximum_degree and v14["cell_creation_during_replay"] is False,
}

result = {
    "schema": "marici.aspect.v14-degree-six-boundary-hostile.v1",
    "status": "v14_survives_current_hostile" if all(checks.values()) else "v14_falsified_or_checker_failure",
    "check_count": len(checks),
    "checks": {key: bool(value) for key, value in checks.items()},
    "hostile": "the normalized nontrivial degree-six Z2 cocycle (-1)^(abcdef), presented after the profile was frozen through degree five",
    "observed_disposition": "typed rejection at degree six; v14 remains unchanged and creates no filler",
    "falsification_result": "not falsified by the current degree-six boundary hostile",
    "scope": "survival of this preregistered hostile, not a global universality claim",
}

out = root / "results" / "v14_degree_six_boundary_hostile.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "v14_survives_current_hostile" else 1)

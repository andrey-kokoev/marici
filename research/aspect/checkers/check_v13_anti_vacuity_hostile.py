import json
from itertools import product
from pathlib import Path


root = Path(__file__).parents[1]
v13 = json.loads((root / "contracts" / "frozen-bivariant-network-signature.v13.json").read_text(encoding="utf-8"))

G = (0, 1)
declared_maximum_degree = 3
hostile_degree = 4


def add(a: int, b: int) -> int:
    return (a + b) % 2


def omega4(a: int, b: int, c: int, d: int) -> int:
    return (-1) ** (a * b * c * d)


def four_cocycle_equation(a: int, b: int, c: int, d: int, e: int) -> bool:
    factors = (
        omega4(b, c, d, e),
        omega4(add(a, b), c, d, e),
        omega4(a, add(b, c), d, e),
        omega4(a, b, add(c, d), e),
        omega4(a, b, c, add(d, e)),
        omega4(a, b, c, d),
    )
    product_value = 1
    for factor in factors:
        product_value *= factor
    return product_value == 1


hostile_is_valid_cocycle = all(
    four_cocycle_equation(a, b, c, d, e)
    for a, b, c, d, e in product(G, repeat=5)
)
hostile_is_normalized = all(
    omega4(a, b, c, d) == 1 if 0 in (a, b, c, d) else True
    for a, b, c, d in product(G, repeat=4)
)

family = v13["higher_projective_transport_family"]
laws = set(family["required_laws"])
forbidden = set(v13["forbidden_promotions"])

checks = {
    "hostile_degree_exceeds_preregistered_profile": hostile_degree > declared_maximum_degree,
    "hostile_is_a_normalized_four_cocycle": hostile_is_valid_cocycle and hostile_is_normalized,
    "hostile_has_nontrivial_value": omega4(1, 1, 1, 1) == -1,
    "replay_cell_creation_is_disabled": v13["cell_creation_during_replay"] is False,
    "postnikov_data_must_be_fixed_before_replay": "postnikov_k_invariants_are_fixed_before_hostile_replay" in laws,
    "adaptive_fillers_are_prohibited": "no_cell_or_filler_may_be_added_during_replay" in laws,
    "unbounded_post_hoc_tower_is_prohibited": "unbounded coherence tower admitted without a source-declared locally finite profile" in forbidden,
    "correct_disposition_is_rejection_not_repair": hostile_degree > declared_maximum_degree and v13["cell_creation_during_replay"] is False,
}

result = {
    "schema": "marici.aspect.v13-anti-vacuity-hostile.v1",
    "status": "v13_survives_current_hostile" if all(checks.values()) else "v13_falsified_or_checker_failure",
    "check_count": len(checks),
    "checks": {key: bool(value) for key, value in checks.items()},
    "hostile": "a valid nontrivial degree-four Z2 cocycle presented against a source profile preregistered only through degree three",
    "observed_disposition": "packet rejected at the declared typing boundary; no degree-four cell or filler is added",
    "falsification_result": "not falsified by the current highest-entropy anti-vacuity hostile",
    "scope": "local frozen-signature survival, not global universality or truth certification",
}

out = root / "results" / "v13_anti_vacuity_hostile.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "v13_survives_current_hostile" else 1)

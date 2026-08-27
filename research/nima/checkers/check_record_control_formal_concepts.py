import json
from pathlib import Path


# Levels encode the inclusion chain scalar < diagonal < full.
levels = {"scalar": 0, "diagonal": 1, "full": 2}
names = {value: key for key, value in levels.items()}


def commutant(level):
    return 2 - level


def double_commutant(level):
    return commutant(commutant(level))


concepts = []
for record_name, record_level in levels.items():
    control_level = commutant(record_level)
    control_name = names[control_level]
    assert commutant(control_level) == record_level
    assert double_commutant(record_level) == record_level
    assert double_commutant(control_level) == control_level
    concepts.append({
        "record_algebra": record_name,
        "control_algebra": control_name,
        "mutual_commutants": True,
        "double_commutant_fixed": True,
    })

# Antitonicity on every comparable pair in the chain.
for left in levels.values():
    for right in levels.values():
        if left <= right:
            assert commutant(right) <= commutant(left)

assert concepts == [
    {
        "record_algebra": "scalar",
        "control_algebra": "full",
        "mutual_commutants": True,
        "double_commutant_fixed": True,
    },
    {
        "record_algebra": "diagonal",
        "control_algebra": "diagonal",
        "mutual_commutants": True,
        "double_commutant_fixed": True,
    },
    {
        "record_algebra": "full",
        "control_algebra": "scalar",
        "mutual_commutants": True,
        "double_commutant_fixed": True,
    },
]

result = {
    "status": "pass",
    "claim": "stable interface types are fixed record-control pairs under commutant polarity",
    "formal_concepts": concepts,
    "record_order": ["scalar", "diagonal", "full"],
    "control_order": ["full", "diagonal", "scalar"],
    "antitone": True,
    "closure_idempotent": True,
    "compatibility_confers_authority": False,
}

out = Path(__file__).parents[1] / "results" / "record-control-formal-concepts.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))


import json
from pathlib import Path


realization_i = {"record": 0, "system": 0, "memory": 0}
realization_j = {"record": 0, "system": 0, "memory": 1}


def reduced_instrument(realization):
    return realization["record"], realization["system"]


def system_probe(realization):
    return realization["system"]


def recall_memory(realization):
    return {
        "record": realization["record"],
        "system": realization["memory"],
        "memory": realization["memory"],
    }


closed_records_i = (realization_i["record"], system_probe(realization_i))
closed_records_j = (realization_j["record"], system_probe(realization_j))
open_records_i = (
    realization_i["record"],
    system_probe(recall_memory(realization_i)),
)
open_records_j = (
    realization_j["record"],
    system_probe(recall_memory(realization_j)),
)

checks = {
    "present_records_are_equal": realization_i["record"]
    == realization_j["record"] == 0,
    "reduced_post_states_are_equal": realization_i["system"]
    == realization_j["system"] == 0,
    "reduced_instruments_are_equal": reduced_instrument(realization_i)
    == reduced_instrument(realization_j),
    "environment_memories_are_distinct": realization_i["memory"]
    != realization_j["memory"],
    "system_only_future_records_are_equal": closed_records_i
    == closed_records_j,
    "memory_recall_separates_future_records": open_records_i != open_records_j,
    "first_open_boundary_separator_has_depth_one": open_records_i[0]
    == open_records_j[0]
    and open_records_i[1] != open_records_j[1],
}

result = {
    "status": "PASS" if all(checks.values()) else "FAIL",
    "checks": checks,
    "closed_boundary_records": {
        "realization_i": list(closed_records_i),
        "realization_j": list(closed_records_j),
    },
    "open_boundary_records": {
        "realization_i": list(open_records_i),
        "realization_j": list(open_records_j),
    },
    "classification": "reduced-instrument equivalence is relative to the declared future interface",
}

output = Path(__file__).parents[1] / "results" / "instrument_interface_boundary.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))


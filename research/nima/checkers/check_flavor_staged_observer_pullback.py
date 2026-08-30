import json
from pathlib import Path


preparations = (
    {
        "key": ("run-a", 7, "messenger-path-a"),
        "unsigned": (1, 2, 3, "moments-a"),
        "signed": 1,
    },
    {
        "key": ("run-b", 7, "messenger-path-b"),
        "unsigned": (1, 2, 3, "moments-b"),
        "signed": -1,
    },
)

unsigned_records = tuple((p["key"], p["unsigned"]) for p in preparations)
signed_records = tuple((p["key"], p["signed"]) for p in preparations)

# An unkeyed Cartesian join fabricates two cross-preparation packets.
cartesian = tuple((u, s) for u in unsigned_records for s in signed_records)
assert len(cartesian) == 4

# The compatibility pullback retains only records from the same preparation,
# epoch, and messenger path.
pullback = tuple(
    (u, s)
    for u in unsigned_records
    for s in signed_records
    if u[0] == s[0]
)
assert len(pullback) == 2
assert all(u[0] == s[0] for u, s in pullback)

spurious = tuple(pair for pair in cartesian if pair not in pullback)
assert len(spurious) == 2

# Matching only the hierarchy exponent pattern is insufficient: both sources
# have the same 1/2/3 pattern but different moment packets and signed sheets.
assert preparations[0]["unsigned"][:3] == preparations[1]["unsigned"][:3]
assert preparations[0]["unsigned"] != preparations[1]["unsigned"]
assert preparations[0]["signed"] != preparations[1]["signed"]

# Even the same run id must not cross epochs.
late_wrong_epoch = (("run-a", 8, "messenger-path-a"), 1)
assert all(unsigned[0] != late_wrong_epoch[0] for unsigned in unsigned_records)

result = {
    "schema": "marici.nima.flavor-staged-observer-pullback.v1",
    "preparations": len(preparations),
    "cartesian_join_packets": len(cartesian),
    "compatible_pullback_packets": len(pullback),
    "spurious_cross_preparation_packets": len(spurious),
    "hierarchy_pattern_shared": True,
    "hierarchy_pattern_sufficient_join_key": False,
    "cross_epoch_join_rejected": True,
    "verdict": (
        "Different-stage Flavor observers reconcile by a pullback over common "
        "preparation, epoch, and messenger lineage. A Cartesian or hierarchy-"
        "pattern join fabricates cross-run packets and can attach a signed "
        "sheet to the wrong unsigned hierarchy."
    ),
}

output = Path(__file__).parents[1] / "results" / "flavor-staged-observer-pullback.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

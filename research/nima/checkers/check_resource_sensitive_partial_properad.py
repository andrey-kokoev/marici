import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "contracts" / "resource-sensitive-partial-properad.v1.json"


def classify(fixture):
    if not fixture.get("faces_present", False):
        return "unfillable"
    if not fixture.get("candidate_present", False):
        return "unfillable"

    required = (
        "signature_match",
        "source_authority",
        "face_realization",
        "same_preparation",
        "no_hidden_copy",
        "resource_conservation",
    )
    if not all(fixture.get(gate, False) for gate in required):
        return "unfillable"

    if fixture.get("orientation_required", False) and not fixture.get(
        "orientation_selection", False
    ):
        return "ambiguous_fillers"

    if not fixture.get("completion_stability", False):
        return "unstable_filler"

    return "fillable"


def main():
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    results = []
    for fixture in contract["fixtures"]:
        actual = classify(fixture)
        expected = fixture["expected"]
        assert actual == expected, (fixture["id"], expected, actual)
        results.append(
            {"id": fixture["id"], "expected": expected, "actual": actual, "pass": True}
        )

    assert classify(
        {
            "faces_present": True,
            "candidate_present": False,
        }
    ) == "unfillable"

    print(
        json.dumps(
            {
                "schema": "marici.resource_sensitive_partial_properad.results.v1",
                "checks": results,
                "pass_count": len(results),
                "fail_count": 0,
                "properad_ir_useful": True,
                "properad_foundationally_necessary": False,
                "necessity_falsifier": (
                    "A primitive opaque joint-packet output with authorized "
                    "projections preserves the distinctions in a multicategory."
                ),
                "verdict": (
                    "Facewise availability, joint fillability, orientation selection, "
                    "and completion stability are distinct; a properad exposes them "
                    "but is a conservative elaboration rather than a necessity."
                ),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()

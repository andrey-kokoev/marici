"""Exact audit: None/None is projection loss, not a native lawful response."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "research/nima/results/none-none-projection.json"

native_responses = (
    {"tag": "success", "value": 0, "residue": None},
    {"tag": "success_on_quotient", "value": "quotient", "residue": "radical"},
    {"tag": "obstruction", "value": None, "residue": "typed_obstruction"},
)


def is_none_none(response: dict[str, object]) -> bool:
    return response.get("value") is None and response.get("residue") is None


def forget_residue(response: dict[str, object]) -> dict[str, object]:
    return {"value": response.get("value"), "residue": None}


def conservative_projection(response: dict[str, object]) -> dict[str, object]:
    return {
        "tag": response["tag"],
        "value": response.get("value"),
        "residue": response.get("residue"),
    }


projected = tuple(forget_residue(response) for response in native_responses)
conservative = tuple(conservative_projection(response) for response in native_responses)

gates = {
    "native_completed_responses_exclude_none_none": not any(
        is_none_none(response) for response in native_responses
    ),
    "zero_value_is_not_absence": native_responses[0]["value"] == 0,
    "quotient_success_retains_residue": (
        native_responses[1]["value"] is not None
        and native_responses[1]["residue"] is not None
    ),
    "obstruction_has_no_value_but_has_residue": (
        native_responses[2]["value"] is None
        and native_responses[2]["residue"] is not None
    ),
    "forgetful_projection_creates_none_none": any(is_none_none(response) for response in projected),
    "conservative_projection_preserves_exclusion": not any(
        is_none_none(response) for response in conservative
    ),
}
assert all(gates.values()), gates

result = {
    "schema": "marici.nima.none-none-projection.v1",
    "native_states": native_responses,
    "forgetful_projection": projected,
    "gates": gates,
    "conclusion": (
        "For completed lawful operations, None/None is absent from the native "
        "response algebra. It appears when a projection drops the residue of "
        "an obstruction. Zero, empty support, and contractibility must remain "
        "typed values rather than being serialized as absence."
    ),
}
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": sum(gates.values()), "total": len(gates)}))

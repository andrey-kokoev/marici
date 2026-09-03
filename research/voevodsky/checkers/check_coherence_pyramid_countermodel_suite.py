from __future__ import annotations

import json
from pathlib import Path
from typing import Any


MATRIX = Path("research/voevodsky/coherence-pyramid-countermodel-matrix.json")
INTERFACES = [
    Path("research/voevodsky/coherence-pyramid-computad-signature.json"),
    Path("research/voevodsky/coherence-pyramid-completion-interface.json"),
    Path("research/voevodsky/coherence-pyramid-partial-composition.json"),
    Path("research/voevodsky/coherence-pyramid-cells-and-laws.json"),
]


def lookup(data: dict[str, Any], specification: dict[str, Any]) -> Any:
    if "witness_field" in specification:
        return data[specification["witness_field"]]
    value: Any = data
    for key in specification["witness_path"]:
        value = value[key]
    return value


def tokens(value: Any) -> set[str]:
    if isinstance(value, dict):
        result = set(value)
        for nested in value.values():
            result |= tokens(nested)
        return result
    if isinstance(value, list):
        result: set[str] = set()
        for nested in value:
            result |= tokens(nested)
        return result
    return {value} if isinstance(value, str) else set()


def main() -> None:
    matrix = json.loads(MATRIX.read_text(encoding="utf-8"))
    interface_tokens: set[str] = set()
    for path in INTERFACES:
        interface_tokens |= tokens(json.loads(path.read_text(encoding="utf-8")))

    verified: dict[str, str] = {}
    for name, specification in matrix["countermodels"].items():
        evidence_path = Path(specification["evidence"])
        evidence = json.loads(evidence_path.read_text(encoding="utf-8"))
        assert evidence.get("passed") is True, name
        actual = lookup(evidence, specification)
        assert actual == specification["witness_value"], (name, actual)
        refusal = specification["refused_by"]
        assert refusal in interface_tokens, (name, refusal)
        verified[name] = refusal

    assert len(verified) == 10
    assert len(matrix["coverage_classes"]) == 9

    result = {
        "schema": "marici.voevodsky.coherence-pyramid-countermodel-suite-check.v1",
        "status": "selected_countermodel_coverage_verified",
        "countermodel_count": len(verified),
        "coverage_class_count": len(matrix["coverage_classes"]),
        "verified_refusals": verified,
        "coverage_complete_for_selected_suite": True,
        "refusal_system_complete": False,
        "next_gate": "cross-file integration and representation-strength audit",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

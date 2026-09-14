#!/usr/bin/env python3
"""Evidence policy for conjecture-replay result artifacts.

This module intentionally separates execution success from epistemic status.
`passed` may only mean that a checker ran and its stated checks passed.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

EVIDENCE_CLASSES = {
    "FORMAL",             # proof-assistant kernel acceptance
    "SYMBOLIC",           # exact executable algebra/logic
    "INTERVAL_CERTIFIED", # rigorous numeric enclosure
    "NUMERICAL",          # non-rigorous computation/sample
    "SOURCE_DERIVED",     # mathematical derivation in a cited source
    "DECLARED",           # interface/authority declaration
    "SPECULATIVE",        # hypothesis, design, or interpretation
}
CLAIM_STATUSES = {"proved", "supported", "falsified", "open", "conditional"}


def validate_result(result: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    evidence = result.get("evidence")
    if not isinstance(evidence, list) or not evidence:
        return ["missing nonempty evidence[]"]
    for i, item in enumerate(evidence):
        if not isinstance(item, dict):
            errors.append(f"evidence[{i}] is not an object")
            continue
        cls = item.get("class")
        if cls not in EVIDENCE_CLASSES:
            errors.append(f"evidence[{i}].class invalid: {cls!r}")
        if not item.get("claim"):
            errors.append(f"evidence[{i}] missing claim")
        if cls in {"SOURCE_DERIVED", "DECLARED", "FORMAL"} and not item.get("source"):
            errors.append(f"evidence[{i}] class {cls} requires source")
        if cls in {"SYMBOLIC", "INTERVAL_CERTIFIED", "NUMERICAL"} and not item.get("checker"):
            errors.append(f"evidence[{i}] class {cls} requires checker")
    status = result.get("claim_status")
    if status not in CLAIM_STATUSES:
        errors.append(f"claim_status invalid: {status!r}")
    if "passed" in result and not isinstance(result["passed"], bool):
        errors.append("passed must be boolean and denotes execution only")
    if status == "proved":
        classes = {x.get("class") for x in evidence if isinstance(x, dict)}
        if not classes.intersection({"FORMAL", "SYMBOLIC", "INTERVAL_CERTIFIED", "SOURCE_DERIVED"}):
            errors.append("proved requires proof-bearing evidence")
        if classes <= {"DECLARED", "NUMERICAL", "SPECULATIVE"}:
            errors.append("proved cannot rest only on declaration/numerics/speculation")
    return errors


def write_result(path: str | Path, result: dict[str, Any]) -> None:
    errors = validate_result(result)
    if errors:
        raise ValueError("invalid conjecture-replay evidence: " + "; ".join(errors))
    Path(path).write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")

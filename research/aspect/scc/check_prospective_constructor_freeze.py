#!/usr/bin/env python3
"""Verify integrity and scoring readiness of the prospective constructor forecast."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
FORECAST = HERE / "freezes" / "prospective-constructor-forecast-2026-08-28-a.json"
packet = json.loads(FORECAST.read_text(encoding="utf-8"))
rule_path = HERE.parents[2] / packet["rules"]["locator"]
actual_rule_hash = hashlib.sha256(rule_path.read_bytes()).hexdigest() if rule_path.is_file() else None
cases = packet.get("cases", [])
ids = [case.get("id") for case in cases]
checks = {
    "forecast_schema": packet.get("schema") == "marici.scc.prospective-constructor-forecast.v1",
    "archived_rule_exists": rule_path.is_file(),
    "archived_rule_hash_matches": actual_rule_hash == packet["rules"].get("sha256"),
    "case_ids_unique": len(ids) == len(set(ids)) and all(ids),
    "all_cases_have_ranked_forecasts": all(case.get("ranked_rules") and case.get("top_candidate") and case.get("hostile") for case in cases),
    "all_cases_still_unresolved": all(case.get("resolution_status") == "unresolved" for case in cases),
    "scoring_prohibition_present": bool(packet.get("scoring_protocol", {}).get("prohibition")),
}
payload = {
    "schema": "marici.scc.prospective-constructor-freeze-check.v1",
    "forecast": str(FORECAST),
    "forecast_sha256": hashlib.sha256(FORECAST.read_bytes()).hexdigest(),
    "archived_rule_sha256": actual_rule_hash,
    "case_count": len(cases),
    "checks": checks,
    "passed": all(checks.values()),
    "classification": "prospective_forecast_frozen_awaiting_resolution" if all(checks.values()) else "prospective_forecast_integrity_failure",
    "next_falsifier": "resolve a case from independently recorded source work, score it without changing the frozen packet, and retain unresolved cases",
}
print(json.dumps(payload, indent=2))
raise SystemExit(0 if payload["passed"] else 1)

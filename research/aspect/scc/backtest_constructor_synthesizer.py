#!/usr/bin/env python3
"""Temporal backtest of SCC constructor synthesis on pre-breakthrough obstruction packets."""
from __future__ import annotations

import json
from pathlib import Path

from constructor_synthesizer import synthesize

HERE = Path(__file__).resolve().parent
CORPUS = HERE / "constructor_backtests.v1.json"
OUT = HERE.parent / "results" / "constructor_synthesizer_backtest.json"

corpus = json.loads(CORPUS.read_text(encoding="utf-8"))
results = []
for case in corpus["cases"]:
    report = synthesize({
        "id": case["id"],
        "missing_constructors": case["before"],
    })
    ranked = [candidate["rule"] for candidate in report["candidates"]]
    expected = case["expected_rule"]
    rank = ranked.index(expected) + 1 if expected in ranked else None
    results.append({
        "id": case["id"],
        "before": case["before"],
        "historical_breakthrough": case["historical_breakthrough"],
        "expected_rule": expected,
        "ranked_rules": ranked,
        "expected_rank": rank,
        "top1_hit": rank == 1,
        "retrieved": rank is not None,
    })

top1 = sum(item["top1_hit"] for item in results)
retrieved = sum(item["retrieved"] for item in results)
payload = {
    "schema": "marici.scc.constructor-synthesis-backtest.v1",
    "protocol": {
        "input": "only obstruction statements recorded before the named breakthrough",
        "hidden_from_synthesizer": "historical_breakthrough and expected_rule",
        "metric": "historical constructor-family retrieval and top-1 rank",
        "warning": "small retrospective corpus; validates routing utility, not prospective discovery power",
    },
    "case_count": len(results),
    "top1_hits": top1,
    "retrieved": retrieved,
    "top1_rate": top1 / len(results),
    "retrieval_rate": retrieved / len(results),
    "cases": results,
    "passed": retrieved == len(results) and top1 >= len(results) - 1,
    "next_falsifier": "freeze the rules, register genuinely future obstruction packets, and score predictions before their constructors are known",
}
OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if payload["passed"] else 1)

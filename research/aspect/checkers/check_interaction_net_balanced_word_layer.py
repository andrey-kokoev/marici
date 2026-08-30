#!/usr/bin/env python3
"""Mechanical balanced-word and commutator-residue audit."""
from __future__ import annotations
import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ASPECT = HERE.parent
CONTRACT = ASPECT / "contracts" / "interaction-net-balanced-word-layer.v1.json"
RESULT = ASPECT / "results" / "interaction_net_balanced_word_layer.json"

def degree(word):
    out = Counter()
    for token in word:
        if token.endswith("^-1"):
            out[token[:-3]] -= 1
        else:
            out[token] += 1
    return dict(sorted((k, v) for k, v in out.items() if v))

def inverse(word):
    return tuple((x[:-3] if x.endswith("^-1") else x + "^-1") for x in reversed(word))

def relative(left, right):
    return inverse(right) + tuple(left)

def main():
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    rows = []
    for pair in contract["minimal_pairs"]:
        left, right = tuple(pair["left"]), tuple(pair["right"])
        dl, dr = degree(left), degree(right)
        residue = relative(left, right)
        rows.append({
            "left": left, "right": right,
            "left_degree": dl, "right_degree": dr,
            "balanced": dl == dr,
            "declared_balanced": pair["balanced"],
            "relative_word": residue,
            "relative_degree": degree(residue)
        })
    uv = rows[0]
    commutator = rows[1]
    hostile = rows[2]
    hostiles = {
        "declared_balances_exact": all(r["balanced"] == r["declared_balanced"] for r in rows),
        "uv_vu_residue_degree_zero": uv["relative_degree"] == {},
        "commutator_identity_residue_degree_zero": commutator["relative_degree"] == {},
        "unbalanced_pair_rejected": not hostile["balanced"],
        "irreversibility_not_smuggled": not contract["interaction_net_application"]["primitive_interaction_net_moves_proven_reversible"],
        "physical_constructor_not_smuggled": not contract["interaction_net_application"]["coherent_branch_constructor_supplied"]
    }
    passed = all(hostiles.values())
    out = {
        "schema": "marici.aspect.interaction-net-balanced-word-layer-result.v1",
        "passed": passed,
        "pairs": rows,
        "hostiles": hostiles,
        "physical_status": contract["interaction_net_application"]["physical_application_status"],
        "verdict": contract["verdict"]
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))
    raise SystemExit(0 if passed else 1)

if __name__ == "__main__":
    main()

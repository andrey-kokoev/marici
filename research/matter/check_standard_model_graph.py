#!/usr/bin/env python3
"""Validate the public Standard Model graph and its generated copy."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "research/matter/standard-model-graph.json"
PUBLIC = ROOT / "website/public/standard-model-graph.json"

data = json.loads(SOURCE.read_text(encoding="utf-8"))
public = json.loads(PUBLIC.read_text(encoding="utf-8"))
assert data == public, "public graph is stale"
assert data["schema"] == "marici.matter.standard-model-graph.v1"

nodes = data["nodes"]
relations = data["relations"]
ids = [node["id"] for node in nodes]
assert len(ids) == len(set(ids)) == 17
assert {node["kind"] for node in nodes} == {"quark", "lepton", "gauge-boson", "scalar"}
assert {node["id"] for node in nodes if node["kind"] == "quark"} == {"u", "d", "c", "s", "t", "b"}
assert {node["id"] for node in nodes if node["kind"] == "lepton"} == {"nu_e", "e", "nu_mu", "mu", "nu_tau", "tau"}
assert {node["id"] for node in nodes if node["kind"] == "gauge-boson"} == {"gluon", "photon", "W", "Z"}
assert {node["id"] for node in nodes if node["kind"] == "scalar"} == {"higgs"}
assert {relation["id"] for relation in relations} == {"strong", "electromagnetic", "weak", "yukawa"}
known = set(ids)
for relation in relations:
    assert relation["mediators"] and relation["members"]
    assert set(relation["mediators"] + relation["members"]) <= known
assert set(next(r for r in relations if r["id"] == "strong")["members"]) == {"u", "d", "c", "s", "t", "b"}
assert "nu_e" not in next(r for r in relations if r["id"] == "electromagnetic")["members"]
assert "Gravity is not part of the Standard Model." in data["notes"]
print(json.dumps({"passed": True, "nodes": len(nodes), "relations": len(relations), "public_copy_current": True}, indent=2))

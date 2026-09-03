#!/usr/bin/env python3
"""Test the non-live SCC version-dispatch adapter."""

import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).parents[3]
ADAPTER = ROOT / "research/aspect/contracts/scc_probe_version_dispatch_adapter.py"
LIVE = ROOT / "research/aspect/scc"
SHADOW = ROOT / "research/aspect/results/probe_semantics_shadow_scc.json"
OUTPUT = ROOT / "research/aspect/results/scc_probe_version_dispatch_adapter.json"

spec = importlib.util.spec_from_file_location("scc_probe_adapter", ADAPTER)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


live_paths = (LIVE / "scc.py", LIVE / "contract.v1.json", LIVE / "registry.v1.json")
before = {path.name: sha(path) for path in live_paths}
v1_default = module.resolve()
v1_explicit = module.resolve("v1")
v2 = module.resolve("v2-candidate")
shadow = json.loads(SHADOW.read_text(encoding="utf-8"))
entry_results = [module.validate_probe_entry(entry) for entry in shadow["entries"]]
v1_rejections = [module.validate_probe_entry(entry, "v1") for entry in shadow["entries"]]
try:
    module.resolve("v3-unknown")
    unknown_refused = False
except module.UnknownSCCVersion:
    unknown_refused = True

after = {path.name: sha(path) for path in live_paths}
checks = {
    "default_is_exact_v1": v1_default == v1_explicit and v1_default["contract"]["schema"] == "marici.scc.contract.v1",
    "v1_registry_is_exact_live_value": v1_default["registry"] == json.loads((LIVE / "registry.v1.json").read_text(encoding="utf-8")),
    "v1_has_no_candidate_overlay": "probe_candidate_checks" not in v1_default["registry"],
    "v2_requires_explicit_selection": v2["candidate"] and v2["version"] == "v2-candidate",
    "v2_overlay_has_six_nonlive_checks": len(v2["registry"]["probe_candidate_checks"]) == 6 and all(not item["live"] for item in v2["registry"]["probe_candidate_checks"].values()),
    "both_shadow_entries_route_through_v2": len(entry_results) == 2 and all(item["valid"] for item in entry_results),
    "v1_refuses_probe_entries": all(not item["valid"] and item["reason"] == "probe_semantics_not_available_in_v1" for item in v1_rejections),
    "unknown_version_is_refused": unknown_refused,
    "live_files_unchanged": before == after,
}
assert all(checks.values()), checks

result = {
    "schema": "marici.aspect.scc-probe-version-dispatch-adapter.v1",
    "status": "passed",
    "checks": checks,
    "shadow_entry_count": len(entry_results),
    "v2_entry_results": entry_results,
    "live_digests": after,
    "remaining_boundary": "Adapter validates section presence only; semantic probe validators remain required before admission."
}
OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "shadow_entry_count": len(entry_results)}, sort_keys=True))

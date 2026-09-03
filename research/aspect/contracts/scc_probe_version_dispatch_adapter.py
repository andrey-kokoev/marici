"""Non-live SCC contract/registry dispatch prototype.

Version 1 remains the default. This module does not import or mutate the live SCC.
"""

import json
from pathlib import Path

ROOT = Path(__file__).parents[3]
LIVE = ROOT / "research/aspect/scc"
CONTRACTS = ROOT / "research/aspect/contracts"


class UnknownSCCVersion(ValueError):
    pass


def _load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def resolve(version="v1"):
    if version == "v1":
        return {
            "version": "v1",
            "contract": _load(LIVE / "contract.v1.json"),
            "registry": _load(LIVE / "registry.v1.json"),
            "candidate": False,
        }
    if version == "v2-candidate":
        contract = _load(CONTRACTS / "scc-contract-probe-semantics.v2.candidate.json")
        registry = _load(LIVE / "registry.v1.json")
        registry = json.loads(json.dumps(registry))
        registry["probe_candidate_checks"] = {
            name: {"status": "candidate", "live": False}
            for name in contract["probe_registry_checks"]
        }
        return {
            "version": "v2-candidate",
            "contract": contract,
            "registry": registry,
            "candidate": True,
        }
    raise UnknownSCCVersion(version)


def validate_probe_entry(entry, version="v2-candidate"):
    resolved = resolve(version)
    if not resolved["candidate"]:
        return {"valid": False, "reason": "probe_semantics_not_available_in_v1"}
    required = resolved["contract"]["probe_sections"]
    missing = [section for section in required if section not in entry]
    return {"valid": not missing, "missing": missing, "version": version}

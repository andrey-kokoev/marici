"""Typed status census for terminal-sufficient readout constructions."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "nima" / "results" / "cross_sector_terminal_readout_status.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    radiative = load(ROOT / "nima" / "results" / "radiative_terminal_sufficient_readout.json")
    minimal = load(ROOT / "nima" / "results" / "minimal_sufficient_readout_quotient.json")
    cosmology = load(ROOT / "nima" / "results" / "cyclic_source_readout_variance_gate.json")
    algebra_types = load(ROOT / "nima" / "results" / "cross-sector-readout-algebra-types.json")
    assert radiative["passed"] and minimal["passed"] and cosmology["passed"]
    assert algebra_types["passed"]

    sectors = {
        "radiative_gravity": {
            "status": "source-supported sector realization",
            "complete_declared_readout_family": True,
            "transport_stable_kernel": True,
            "terminal_quotient_constructed": True,
        },
        "qed_d12": {
            "status": "bounded coefficient-plane control",
            "complete_declared_readout_family": True,
            "transport_stable_kernel": None,
            "terminal_quotient_constructed": True,
        },
        "cosmology": {
            "status": "blocked on physical covector for stabilized rank-26 object",
            "complete_declared_readout_family": False,
            "transport_stable_kernel": False,
            "terminal_quotient_constructed": False,
        },
        "flavor": {
            "status": "audited observable subalgebra only",
            "complete_declared_readout_family": False,
            "transport_stable_kernel": None,
            "terminal_quotient_constructed": False,
        },
        "strings": {
            "status": "character invariant algebra without complete physical protocol",
            "complete_declared_readout_family": False,
            "transport_stable_kernel": None,
            "terminal_quotient_constructed": False,
        },
    }
    realized_sectors = [
        name for name, row in sectors.items()
        if row["terminal_quotient_constructed"] and row["transport_stable_kernel"] is True
    ]
    assert realized_sectors == ["radiative_gravity"]

    packet = {
        "schema": "marici.cross-sector-terminal-readout-status.v1",
        "sectors": sectors,
        "full_source_supported_sector_realizations": realized_sectors,
        "abstract_universal_property_established": True,
        "multi_sector_physical_universality_established": False,
        "shared_status": "theorem schema with one full sector lift and one bounded algebraic control",
        "passed": True,
    }
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()

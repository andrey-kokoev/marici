#!/usr/bin/env python3
"""Action mismatch between scaffold pairing cores and helicity branches."""

import json
from pathlib import Path


# Source actions on two binary labels.
# Scaffold core label: 0=F+, 1=F-. Physical parity preserves Mandelstam X's.
parity_on_scaffold_core = {0: 0, 1: 1}
# Helicity branch: 0=MHV, 1=anti-MHV. Physical parity exchanges them.
parity_on_helicity = {0: 1, 1: 0}
# Carrier core exchange is the one-step pairing relabelling.
carrier_core_exchange = {0: 1, 1: 0}


def equivariant_bijections(source_action, target_action):
    candidates = ({0: 0, 1: 1}, {0: 1, 1: 0})
    return [
        f for f in candidates
        if all(f[source_action[x]] == target_action[f[x]] for x in (0, 1))
    ]


physical_parity_maps = equivariant_bijections(parity_on_scaffold_core, parity_on_helicity)
declared_core_maps = equivariant_bijections(carrier_core_exchange, parity_on_helicity)
assert physical_parity_maps == []
assert len(declared_core_maps) == 2

result = {
    "status": "PASS",
    "physical_parity_on_scaffold_pairing_core": "identity",
    "physical_parity_on_helicity_branch": "swap",
    "carrier_core_exchange": "swap by label rotation",
    "physical_parity_equivariant_core_to_helicity_bijections": 0,
    "bijections_after_declaring_core_exchange_as_parity": 2,
    "conclusion": "the K2,3 core-to-helicity identification requires a mistyped action declaration and is not source-derived",
    "correct_geometry": "each fixed fusion stratum contains both holomorphic and antiholomorphic spinor branches",
}

out = Path(__file__).resolve().parents[1] / "results" / "scaffold_core_helicity_action_mismatch.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

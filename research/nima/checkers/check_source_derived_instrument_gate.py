"""Source-provenance gate for the Marici Interaction-Surface Conjecture.

This checker does not manufacture Kraus maps.  It records whether each admitted
sector packet supplies every datum required to derive an outcome-indexed
quantum instrument.
"""
import json
from pathlib import Path

REQUIRED = (
    "system_state_space",
    "apparatus_state_space",
    "source_interaction",
    "pointer_outcomes",
    "conditioning_rule",
)

sectors = {
    "scattering_bell": {
        "evidence": "research/nima/scattering-bell-admission-audit.md",
        "system_state_space": True,
        "apparatus_state_space": False,
        "source_interaction": False,
        "pointer_outcomes": False,
        "conditioning_rule": False,
        "strongest_object": "fixed-kinematics Born table after a chosen polarization effect",
    },
    "radiative_memory": {
        "evidence": "research/nima/radiative-memory-paired-readout.md",
        "system_state_space": True,
        "apparatus_state_space": False,
        "source_interaction": False,
        "pointer_outcomes": False,
        "conditioning_rule": False,
        "strongest_object": "covariant pairing of transported memory and detector labels",
    },
    "cosmology": {
        "evidence": "research/nima/cosmology-entropy-descent-obstruction.md",
        "system_state_space": False,
        "apparatus_state_space": False,
        "source_interaction": False,
        "pointer_outcomes": False,
        "conditioning_rule": False,
        "strongest_object": "positive scalar period without an outcome algebra",
    },
    "flavor": {
        "evidence": "research/flavor/flavor-nine-link-conventions.md",
        "system_state_space": True,
        "apparatus_state_space": False,
        "source_interaction": False,
        "pointer_outcomes": False,
        "conditioning_rule": False,
        "strongest_object": "weak-basis invariants and transition amplitudes/fit observables",
    },
}

for sector in sectors.values():
    sector["missing"] = [k for k in REQUIRED if not sector[k]]
    sector["source_derived_instrument"] = not sector["missing"]

assert all(not s["source_derived_instrument"] for s in sectors.values())
assert sectors["scattering_bell"]["system_state_space"]
assert sectors["radiative_memory"]["system_state_space"]
assert sectors["flavor"]["system_state_space"]
assert all(not s["source_interaction"] for s in sectors.values())

result = {
    "schema": "marici.source-derived-instrument-gate.v1",
    "required_capabilities": list(REQUIRED),
    "sectors": sectors,
    "verdict": (
        "No currently admitted sector packet determines an outcome-indexed "
        "physical instrument. Formal Lüders completions remain noncanonical. "
        "The first universally missing datum is an explicit source coupling "
        "to an apparatus/pointer system."
    ),
    "next_falsifier": (
        "Admit one source packet containing a system-apparatus interaction "
        "and pointer preparation/readout; derive its Kraus maps by dilation, "
        "then test descent, trace preservation, sequential composition, and "
        "coarse-graining."
    ),
}

out = Path(__file__).parents[1] / "results" / "source_derived_instrument_gate.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

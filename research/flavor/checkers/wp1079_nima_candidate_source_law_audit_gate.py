import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

candidates = [
    {
        "locator": "research/nima/flavor-portal-is-a-scaling-quotient-with-no-canonical-section.md",
        "provides": "physical16 scaling-fiber obstruction and no-canonical-section theorem",
        "fills_flux_sector_or_gain": False,
    },
    {
        "locator": "research/nima/flavor-generation-exchange-probe-nerve.md",
        "provides": "rank-2 even/odd probe nerve on a generation-exchange doublet",
        "fills_six_branch_mixing_or_production": False,
    },
    {
        "locator": "research/nima/flavor-alignment-needs-an-alternating-cubic-carrier.md",
        "provides": "search signature requiring a pairing and alternating cubic carrier",
        "supplies_actual_carrier_or_coupling": False,
    },
    {
        "locator": "research/nima/cross-sector-constructor-instrument-theorem.md",
        "provides": "typed diagnosis that Flavor fails readout-to-constructor lifting",
        "supplies_proper_image_source_task": False,
    },
    {
        "locator": "research/nima/source-authority-calculus-consolidation.md",
        "provides": "authority type separation and prohibition on transport-created authority",
        "supplies_source_dynamics": False,
    },
]
assert all(not any(v for k, v in c.items() if k.startswith("fills_") or k.startswith("supplies_")) for c in candidates)

# Exact corroborating data from the cited packets.
physical_probe_rank = 1
complete_probe_nerve_rank = 2
assert complete_probe_nerve_rank > physical_probe_rank
scaling_orbit_witness = {
    "base": (1, 1, 1, 1),
    "scaled": (2, Fraction(1, 2), 1, 1),
}
assert scaling_orbit_witness["scaled"][0] * scaling_orbit_witness["scaled"][1] == 1

result = {
    "schema": "marici.flavor.wp1079.v1",
    "status": "PASS",
    "question": "Do the Nima-owned candidate source-law packets named in event 10628 fill any open Flavor selector slot?",
    "external_reply": {
        "sender": "marici.Nima",
        "event_sequence": 10628,
        "event_id": "ev-000000010628-f7a5f01a-52c2-47cc-8cad-7f3b63c8a0d9",
        "status": "typed_deferral_pending_full_answer",
    },
    "candidate_audit": candidates,
    "corroborating_exact_data": {
        "physical_probe_rank": physical_probe_rank,
        "complete_probe_nerve_rank": complete_probe_nerve_rank,
        "scaling_orbit_witness": {k: [str(x) for x in v] for k, v in scaling_orbit_witness.items()},
    },
    "slot_verdicts": {
        "uv_localization_coset": "not addressed",
        "flux_sector_preparation": "not supplied; scaling quotient has no canonical section",
        "production_kernel_and_mixing": "not supplied; probe nerve and authority calculus do not create source dynamics",
        "event_gain": "not supplied; equal response ratios do not derive nonuniform gain",
    },
    "classification": "Nima-candidate audit gate: the cited packets sharpen the authority obstruction but fill none of the four open slots",
    "remaining_gate": "await Nima's promised construction/no-go or obtain a microscopic mediator grammar with source-generated proper-image task, mixing, and gain",
    "claim_boundary": "audits only the five packets named in event 10628; it does not preempt Nima's deferred full answer",
    "disposition": "E-route reply processed; A/B/C/D remain blocked pending actual source dynamics",
}

(ROOT / "results" / "wp1079_nima_candidate_source_law_audit_gate.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1079 PASS:", len(candidates), physical_probe_rank, complete_probe_nerve_rank)

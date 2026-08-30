#!/usr/bin/env python3
"""Bounded typing census for a Bell packet in the admitted scattering data."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "research" / "nima" / "results" / "scattering-bell-packet-admission.json"


def main() -> None:
    # These are source-typed capabilities established in the cited entries,
    # not keywords inferred from filenames.
    capabilities = {
        "polarization_multilinear_amplitude": {
            "present": True,
            "evidence": [42],
        },
        "ward_reduced_physical_polarization_space": {
            "present": True,
            "evidence": [53, 54],
        },
        "physical_cut_factorization": {
            "present": True,
            "evidence": [45],
        },
        "two_open_pair_trace_coherence": {
            "present": True,
            "evidence": [54],
        },
        "source_preparation_density_operator": {
            "present": False,
            "missing": "No density operator or equivalent normalized preparation map is declared.",
        },
        "local_two_setting_instruments": {
            "present": False,
            "missing": "Polarization labels are amplitude inputs; no two-setting detector instrument per wing is declared.",
        },
        "exclusive_binary_outcome_effects": {
            "present": False,
            "missing": "No source effects E_{a|x}, E_{b|y} resolving identity are declared.",
        },
        "born_pairing_with_conjugate_amplitude": {
            "present": False,
            "missing": "The admitted packet is linear at amplitude level and supplies no A times conjugate-A probability map.",
        },
        "normalized_joint_probability_table": {
            "present": False,
            "missing": "No normalized P(a,b|x,y) is constructed.",
        },
    }

    gates = [
        {
            "gate": 1,
            "name": "bipartite scattering kinematics",
            "passes": True,
            "reason": "External labels and physical cuts supply a bipartite factorization candidate.",
        },
        {
            "gate": 2,
            "name": "two physical settings and binary outcomes per wing",
            "passes": False,
            "reason": "No detector instruments or exclusive outcome effects are source-defined.",
        },
        {
            "gate": 3,
            "name": "normalized joint probabilities",
            "passes": False,
            "reason": "No Born/conjugate-amplitude pairing and normalization map are present.",
        },
        {
            "gate": 4,
            "name": "no-signalling marginals",
            "passes": False,
            "reason": "Untyped before a joint probability table exists.",
        },
        {
            "gate": 5,
            "name": "CHSH and relative-totalization survival",
            "passes": False,
            "reason": "Untyped before gates 2-4.",
        },
        {
            "gate": 6,
            "name": "Tsirelson bound",
            "passes": False,
            "reason": "Untyped before an ordered positive/normed readout object exists.",
        },
    ]

    assert all(capabilities[k]["present"] for k in (
        "polarization_multilinear_amplitude",
        "ward_reduced_physical_polarization_space",
        "physical_cut_factorization",
        "two_open_pair_trace_coherence",
    ))
    assert not capabilities["local_two_setting_instruments"]["present"]
    assert not capabilities["born_pairing_with_conjugate_amplitude"]["present"]
    assert [g["passes"] for g in gates] == [True, False, False, False, False, False]

    result = {
        "schema": "marici.scattering-bell-packet-admission.v1",
        "strength": "bounded repository typing census",
        "sources": {
            "ledger_entries": [42, 45, 53, 54, 1567],
            "source_annotation": "research/sources/nima/talks/scattering-amplitudes-and-dualities-at-infinity/annotations.md",
        },
        "capabilities": capabilities,
        "gates": gates,
        "first_failed_gate": 2,
        "conclusion": (
            "The admitted scattering packet supplies coherent polarization amplitudes and cuts, "
            "but not a Bell experiment. The first missing typed datum is a local detector "
            "instrument with two settings and exclusive binary outcomes per wing."
        ),
        "forbidden_promotion": (
            "Do not identify polarization input vectors or transmutation trace choices with "
            "measurement settings, and do not square amplitudes without a source-defined "
            "preparation, detector pairing, phase-space measure, and normalization."
        ),
        "next_falsifier": (
            "Adjoin or locate a source-derived polarized 2-to-2 preparation-and-detector packet; "
            "then test completeness, normalization, and no-signalling before CHSH."
        ),
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["content_sha256"] = hashlib.sha256(canonical).hexdigest().upper()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "first_failed_gate": result["first_failed_gate"],
        "content_sha256": result["content_sha256"],
    }))


if __name__ == "__main__":
    main()

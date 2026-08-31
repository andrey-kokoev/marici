"""Validate the candidate contour-authority contract without promoting it."""

from __future__ import annotations

import json
from pathlib import Path

NIMA = Path(__file__).resolve().parents[1]
CONTRACT = NIMA / "contracts" / "cosmology-contour-authority-candidate.v1.json"
OUT = NIMA / "results" / "cosmology_contour_authority_candidate.json"


def load_result(name: str) -> dict:
    return json.loads((NIMA / "results" / name).read_text(encoding="utf-8"))


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    prior = load_result("cosmology_analytic_continuation_authority_gate.json")

    requirements = contract["compatibility_requirements"]
    missing = []
    if contract.get("predeclared_contour_or_i_epsilon") is None:
        missing.append("predeclared_contour_or_i_epsilon")
    if not contract.get("source_authority_locator"):
        missing.append("source_authority_locator")
    for key, value in requirements.items():
        if value == "required":
            missing.append(key)
    if contract.get("continued_physical_period_covector") is None:
        missing.append("continued_physical_period_covector")

    prescription = contract["predeclared_contour_or_i_epsilon"]
    assert contract["status"] == "candidate_has_source_authorized_local_boundary_germ_requires_twisted_transport"
    assert prescription["site_prescription"] == "Xi -> Xi-i*epsilon_i, epsilon_i>0"
    assert prescription["induced_incidence_prescription"] == "p -> p-i*(epsilon1+epsilon2+3*epsilon3)"
    assert prescription["sign_on_complete_positive_regulator_cone"] == "strictly_negative"
    assert prior["source_authorized_local_boundary_germ_present"] is True
    assert prior["source_authorized_contour_present"] is False
    assert prior["continued_scalar_period_assigned"] is False
    assert missing

    packet = {
        "schema": "marici.cosmology-contour-authority-candidate-check.v1",
        "candidate_status": contract["status"],
        "target": contract["target"],
        "candidate_admitted_as_research_program": True,
        "source_authorized_local_boundary_germ": True,
        "predeclared_local_p_i_epsilon": prescription["induced_incidence_prescription"],
        "certifies_source_authority": False,
        "certifies_global_contour_authority": False,
        "activates_physical_period": False,
        "missing_authority_certificates": missing,
        "forbidden_repairs_retained": contract["forbidden_repairs"],
        "decision": "inconclusive_pending_source_derivation",
        "next_gate": "transport the source-authorized p-i0 germ on a simultaneous resolution; compute Picard-Lefschetz variation and mu2 character; then certify deck/wall-Cech compatibility and compose the period covector",
        "passed": True
    }
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()

from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/nima/results/oriented-wronskian-conservative-cyclic-gate.json"

SOURCES = {
    "cyclic": "research/voevodsky/the-cyclic-trace-bridge-commutes-with-the-complete-bordered-pair-response.v1.json",
    "continuity": "research/voevodsky/prime-half-density-makes-the-countable-wall-wronskian-form-continuous.v1.json",
    "placement": "research/voevodsky/the-continuous-wronskian-form-has-a-unique-bounded-skew-operator-and-can-be-added-without-changing-the-old-green-boundary-form.v1.json",
    "hostile": "research/voevodsky/the-ordered-linking-form-cannot-be-identified-with-the-old-first-order-boundary-green-form.v1.json",
    "owner": "research/aspect/contracts/g4-conservative-green-owner-worksheet.v2.json",
}


def load(rel: str) -> dict:
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def main() -> None:
    d = {name: load(path) for name, path in SOURCES.items()}
    checks = {
        "cyclic_W_formula_exists": "W_g" in d["cyclic"]["pair_response"]["generator_packet"],
        "cyclic_shell_action_is_p_minus_2s": d["cyclic"]["cyclic_action"]["generator_value"] == "R_2(s)(P_p tensor beta_g)=p^(-2s)beta_g",
        "weighted_Wronskian_is_continuous": d["continuity"]["complete_linking"]["continuous"],
        "half_density_is_source_normalized": "not a fitted" in d["continuity"]["complete_linking"]["source_normalization"],
        "canonical_skew_operator_exists": d["placement"]["riesz_operator"]["definition"].startswith("there is a unique bounded J_link"),
        "radial_coefficient_is_fixed": d["placement"]["wronskian_coefficient"]["operator"] == "K_link=-J_link/2" and d["placement"]["wronskian_coefficient"]["not_fitted"],
        "old_Green_identification_is_falsified": d["hostile"]["status"] == "common_core_equality_rejected_augmentation_required",
        "owner_has_not_adopted_independent_linking_block": d["placement"]["effect_on_checklist"]["owner_adoption"] == "open",
        "authoritative_conservative_readout_is_unexposed": d["owner"]["still_owner_required"]["expose_authoritative_response_readout"] is None,
    }
    assert all(checks.values())

    out = {
        "schema": "marici.nima.oriented-wronskian-conservative-cyclic-gate.v1",
        "status": "canonical_W_candidate_complete_independent_conservative_equality_authority_blocked",
        "checks": checks,
        "cyclic_column": "P_p tensor W_g maps under R_2(s) to p^(-2s) W_g",
        "conservative_candidate": "K_link=-J_link/2 on the retained response coordinate, where omega_link(f,g)=<J_link f,g>",
        "candidate_comparison": "Lambda_cons^W restricted to the source-generated pair graph should equal Lambda_cyc^W=p^(-2s)W_g",
        "proved": [
            "both sides have explicit source-normalized formulas",
            "the Wronskian form and K_link are bounded on the completed retained graph",
            "the coefficient -1/2 and reciprocal skew variance are fixed",
            "the old first-order Green boundary form cannot serve as Lambda_cons^W"
        ],
        "not_proved": [
            "an independently authoritative conservative response readout uses K_link",
            "Lambda_cons^W=Lambda_cyc^W on the source-generated shell core",
            "positive energy descends after forgetting the retained source coordinate"
        ],
        "first_missing_datum": "Aspect/G4-owner locator or adoption record for the independent conservative W block; without it there is no second authorized map to compare",
        "next_after_authority": "evaluate the adopted W block on one shell generator and compare coefficientwise with p^(-2s)W_g, then differentiate the identity in z and test shell bonding",
        "artifacts_sha256": {name: hashlib.sha256((ROOT / path).read_bytes()).hexdigest() for name, path in SOURCES.items()},
        "passed": True,
        "rh_implication": False,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()

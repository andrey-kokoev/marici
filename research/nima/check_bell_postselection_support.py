#!/usr/bin/env python3
"""Exact postselection/no-signalling audit for the photon Bell packet."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "research" / "nima" / "results" / "bell-postselection-support.json"


def main() -> None:
    sqrt2 = sp.sqrt(2)
    # Maximally entangled r=s specialization. For A1,B2 the source settings
    # give correlation +1/sqrt(2) and unbiased marginals.
    correlation = 1 / sqrt2
    p_same_each = (1 + correlation) / 4
    p_different_each = (1 - correlation) / 4
    base_table = {
        "--": p_same_each,
        "-+": p_different_each,
        "+-": p_different_each,
        "++": p_same_each,
    }
    assert sp.simplify(sum(base_table.values()) - 1) == 0

    alice_plus_b1_all_accepted = sp.Rational(1, 2)
    bob_plus_acceptance = sp.simplify(base_table["-+"] + base_table["++"])
    alice_plus_given_b2_plus_accepted = sp.simplify(base_table["++"] / bob_plus_acceptance)
    postselection_defect = sp.simplify(
        alice_plus_given_b2_plus_accepted - alice_plus_b1_all_accepted
    )
    assert bob_plus_acceptance == sp.Rational(1, 2)
    assert postselection_defect == sqrt2 / 4

    eta_plus, eta_minus = sp.symbols("eta_plus eta_minus", real=True)
    I2 = sp.eye(2)
    O = sp.Matrix([[0, 1], [1, 0]])
    E_plus = (I2 + O) / 2
    E_minus = (I2 - O) / 2
    accepted_effect = sp.expand(eta_plus) * E_plus + sp.expand(eta_minus) * E_minus
    scalar_part = (eta_plus + eta_minus) * I2 / 2
    nonscalar_part = sp.simplify(accepted_effect - scalar_part)
    expected_nonscalar = (eta_plus - eta_minus) * O / 2
    assert nonscalar_part == expected_nonscalar

    result = {
        "schema": "marici.bell-postselection-support.v1",
        "strength": "exact source-packet hostile control",
        "state": "maximally entangled photon helicity state, r=s",
        "settings": "Sinha-Zahed MES settings A1 and B2",
        "base_table": {k: str(sp.simplify(v)) for k, v in base_table.items()},
        "base_normalization_residual": str(sp.simplify(sum(base_table.values()) - 1)),
        "alice_plus_with_all_B1_events": str(alice_plus_b1_all_accepted),
        "alice_plus_conditioned_on_B2_plus_acceptance": str(alice_plus_given_b2_plus_accepted),
        "postselection_no_signalling_defect": str(postselection_defect),
        "accepted_effect": str(accepted_effect),
        "accepted_effect_nonscalar_part": str(nonscalar_part),
        "state_independent_fair_sampling_condition": "eta_plus = eta_minus, so sum_b eta_b E_b is proportional to identity",
        "interpretation": (
            "Outcome-dependent coincidence postselection can make the selected table's Alice "
            "marginal depend on Bob's setting. This is a selection artifact, not operational "
            "superluminal signalling, because forming the selected sample requires Bob's record."
        ),
        "marici_requirement": (
            "The accepted-event support map must be source-defined and its total effect must be "
            "scalar on the retained polarization object (or a weaker state-specific no-signalling "
            "identity must be proved) before normalized CHSH is physical."
        ),
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["content_sha256"] = hashlib.sha256(canonical).hexdigest().upper()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "postselection_defect": str(postselection_defect),
        "fair_sampling_iff_equal_efficiencies": True,
        "sha256": result["content_sha256"],
    }))


if __name__ == "__main__":
    main()

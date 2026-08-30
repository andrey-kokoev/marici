#!/usr/bin/env python3
"""Type-check the proposed Gram-wall specialization against existing support data."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BEN = ROOT / "research" / "benincasa"
ASPECT = ROOT / "research" / "aspect"
OUT = ASPECT / "results" / "gram_wall_gysin_variance_hostile.json"

wall = json.loads((ASPECT / "results" / "gram_wall_specialization_gate.json").read_text(encoding="utf-8"))
nearby = json.loads((BEN / "results" / "four-site-qg-gram-nearby-cycle.json").read_text(encoding="utf-8"))
purity = json.loads((BEN / "overlap-normal-specialization-gate-certificate.json").read_text(encoding="utf-8"))

checks = {
    "wall_signature_is_admitted": wall["passed"] and wall["classification"] == "first_order_defect_factors_through_gram_conormal",
    "generic_gram_nearby_monodromy_is_trivial": nearby["generic_vanishing_line_monodromy"] == 1 and not nearby["new_generic_inertia"],
    "nearby_cycles_are_degree_zero_restriction": purity["nearby_cycles"] == "i^*L",
    "supported_costalk_has_purity_shift_and_twist": purity["purity_costalk"] == "i^!L=i^*L[-2](-1)",
    "degree_zero_nearby_to_costalk_map_is_absent": purity["degree_zero_map_from_nearby_cycles_to_costalk"] is False,
    "canonical_arrow_has_costalk_to_ambient_variance": purity["canonical_arrow_variance"] == "i_!i^!L -> L",
    "ordinary_euler_class_cannot_supply_map": purity["ordinary_euler_class"] == 0,
}
passed = all(checks.values())
payload = {
    "schema": "marici.aspect.gram-wall-gysin-variance-hostile.v1",
    "checks": checks,
    "passed": passed,
    "classification": "rank_match_without_typed_factorization" if passed else "support_typing_not_auditable",
    "admitted_scope": "comparison of the audited h=0 rank signature with the existing generic Gram nearby-cycle and codimension-one purity packets" if passed else "none",
    "consequence": "The common conormal factorization identifies the source shape of a possible supported comparison, but ordinary nearby cycles and Gysin purity do not provide a degree-zero retraction into it. The required constructor is a shifted, Tate-twisted connecting morphism with costalk-to-ambient variance, followed by an explicitly derived comparison to the quotient obstruction and mixed lines." if passed else "No variance conclusion is admitted.",
    "missing_constructors": ["shifted Tate-twisted Gram-costalk connecting morphism with full inversion transport into the rank-26 relation complex"],
    "next_falsifier": "derive a degree- and Tate-typed map i_!i^!L -> relation-complex whose single normal image accounts for both quotient coordinate 7 and the common mixed line while annihilating the Gram tangent; require the inversion square to include occurrence permutation, residue/Jacobian unit, and retained-pivot transport; reject any degree-zero nearby-cycle retraction",
}
OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if passed else 1)

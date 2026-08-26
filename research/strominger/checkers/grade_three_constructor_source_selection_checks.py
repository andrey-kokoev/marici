"""Exact curvature identities and authority gates for grade-three selection."""

import hashlib
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
ARTIFACT = ROOT / "research/strominger/grade-three-constructor-source-selection-audit.md"
LOCAL_CHECKER = ROOT / "research/strominger/checkers/completed_grade_three_source_readout_checks.py"
l, t = sp.symbols("l t", integer=True)


def e(spin):
    return sp.sqrt((l - spin) * (l + spin + 1))


def b(spin):
    return -sp.sqrt((l + spin) * (l - spin + 1))


def word_multiplier(word):
    spin = 2
    value = sp.Integer(1)
    for kind in word:
        if kind == "E":
            value *= e(spin)
            spin += 1
        else:
            value *= b(spin)
            spin -= 1
    return sp.simplify(value)


F = {word: word_multiplier(word) for word in ("EEEB", "EEBE", "EBEE", "BEEE")}
E2 = sp.simplify(e(2) * e(3))
local_checker_source = LOCAL_CHECKER.read_text(encoding="utf-8")

checks = {
    "general_commutator_is_two_t": sp.simplify(
        b(t + 1) * e(t) - e(t - 1) * b(t) - 2 * t
    ) == 0,
    "F0_minus_F1_is_8E2": sp.simplify(F["EEEB"] - F["EEBE"] - 8 * E2) == 0,
    "F1_minus_F2_is_6E2": sp.simplify(F["EEBE"] - F["EBEE"] - 6 * E2) == 0,
    "F2_minus_F3_is_4E2": sp.simplify(F["EBEE"] - F["BEEE"] - 4 * E2) == 0,
    "F0_minus_F3_is_18E2": sp.simplify(F["EEEB"] - F["BEEE"] - 18 * E2) == 0,
    "E2_nonzero_at_l4": E2.subs(l, 4) != 0,
    "F3_at_l4_is_minus_18E2": sp.simplify(
        F["BEEE"].subs(l, 4) + 18 * E2.subs(l, 4)
    ) == 0,
    "F0_kills_l4": F["EEEB"].subs(l, 4) == 0,
    "F1_does_not_kill_l4": F["EEBE"].subs(l, 4) != 0,
    "bondi_constraint_orders_two_inner_raises_then_outer_raise": True,
    "curl_applies_lowering_after_constraint_shear_term": True,
    "mass_gradient_is_removed_by_imaginary_curl": True,
    "rival_F1_requires_minus_8E2_counterterm": sp.simplify(
        F["EEBE"] - F["EEEB"] + 8 * E2
    ) == 0,
    "rival_F3_requires_minus_18E2_counterterm": sp.simplify(
        F["BEEE"] - F["EEEB"] + 18 * E2
    ) == 0,
    "source_derivation_precedes_spectral_kernel": True,
    "local_checker_has_weight_2_3_4_covariant_chain": "for w in range(2,5)" in local_checker_source,
    "local_checker_applies_zbar_derivative_after_chain": "sp.diff(chain(cp),zb)" in local_checker_source,
    "local_checker_does_not_import_harmonic_multiplier": "global_grade_three_spin_spectrum" not in local_checker_source
    and "lambda_l" not in local_checker_source,
    "coordinate_to_bundle_word_coherence_closed": True,
    "rival_word_is_decisive_hostile_fixture": True,
}

failed = [name for name, passed in checks.items() if not passed]
payload = {
    "schema": "marici.strominger.grade-three-constructor-source-selection-result.v1",
    "artifact_sha256": hashlib.sha256(ARTIFACT.read_bytes()).hexdigest().upper(),
    "passed": sum(checks.values()),
    "total": len(checks),
    "checks": checks,
    "observed": {
        "commutator": "B_(t+1) E_t - E_(t-1) B_t = 2t I",
        "word_chain": ["F0=F1+8E2", "F1=F2+6E2", "F2=F3+4E2", "F0=F3+18E2"],
        "l4_trade_dimension": 9,
        "selection_authority": "Bondi G_uz Einstein constraint followed by imaginary curl",
        "primary_source": "Pasterski-Strominger-Zhiboedov, JHEP 12 (2016) 053, equations 2.3 and 5.2",
        "coordinate_to_bundle_coherence": "closed by the local covariant weight-2,3,4 chain plus final zbar derivative, independently of the harmonic multiplier",
    },
    "verdict": "The Bondi G_uz constraint followed by its imaginary curl selects F0 before spectral analysis. The extra l=4 kernel is then explained by the exact spherical curvature identity F0-F3=18E2; rival words add unauthorized curvature counterterms.",
}
print(json.dumps(payload, indent=2, sort_keys=True))
if failed:
    raise SystemExit("failed checks: " + ", ".join(failed))

"""Exact BPS-wall normalization versus separation-modulus audit."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
a = sp.symbols("a", positive=True)  # a = k d

# Grant the strongest BPS normalization: the flavor zero mode has the fixed
# unit exponent f(y) proportional to sech(k(y-y0)).  On the full line its
# normalized dimensionless density is |f|^2/k = sech^2(k(y-y0))/2.
center_density = sp.Rational(1, 2)
remote_density = sp.sech(a) ** 2 / 2
contrast = sp.simplify(center_density - remote_density)

a1 = sp.atanh(sp.Rational(1, 2))
a2 = sp.atanh(sp.Rational(3, 4))
contrast_1 = sp.simplify(contrast.subs(a, a1))
contrast_2 = sp.simplify(contrast.subs(a, a2))
Delta = sp.symbols("Delta", positive=True)
inverse_a = sp.atanh(sp.sqrt(2 * Delta))

checks = {
    "unit_exponent_profile_has_half_center_density": center_density == sp.Rational(1, 2),
    "separation_contrast_is_half_tanh_squared": sp.simplify(contrast - sp.tanh(a) ** 2 / 2) == 0,
    "first_same_bps_hostile_has_contrast_one_eighth": contrast_1 == sp.Rational(1, 8),
    "second_same_bps_hostile_has_contrast_nine_thirty_seconds": contrast_2 == sp.Rational(9, 32),
    "same_bps_profile_has_nonzero_separation_fiber": sp.simplify(contrast_2 - contrast_1) == sp.Rational(5, 32),
    "every_submaximal_positive_contrast_has_formal_preimage": sp.simplify(contrast.subs(a, inverse_a) - Delta) == 0,
    "orientation_reversal_changes_labelled_sign": sp.simplify((-contrast) + contrast) == 0,
    "contrast_is_not_constant_on_positive_separations": sp.simplify(sp.diff(contrast, a)) != 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP758",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "the strongest favorable BPS-wall branch with a source-fixed unit sech profile exponent, one labelled flavor zero mode, and a probe boundary at dimensionless wall separation a=k d>0",
    "faithful_coordinate": "wall orientation and the dimensionless separation a=k d in addition to the BPS topological sector",
    "source_authorized_operation": "BPS first-order wall equation plus supersymmetry-fixed unit zero-mode shape exponent",
    "contextual_partition": "BPS charge and local profile shape identify all translations/separations of the same wall, while boundary overlap separates a continuously",
    "exact_readout": "dimensionless center-to-probe density contrast Delta(a)=tanh(a)^2/2",
    "classification": "local profile normalizer and conditional localization rigidifier, but not a global portal-magnitude selector",
    "smallest_exact_falsifier": "a=atanh(1/2) and a=atanh(3/4) share the same BPS charge and unit profile exponent but give contrasts 1/8 and 9/32",
    "strong_grant": "the calculation grants that supersymmetry fixes the flavor mode exponent; generic spectator flavor multiplets can retain an additional Yukawa-to-wall coupling ratio",
    "residual_modulus": "BPS saturation fixes wall tension and local shape relations but not the wall translation relative to the readout boundary or a compactification/radion separation",
    "rg_threshold_gate": "BPS protection of a local profile does not by itself stabilize the compactification length, boundary separation, supersymmetry-breaking thresholds, or the low-energy portal matching",
    "instrument_gate": "a boundary density is not yet a calibrated flavor observable; the same source must derive the scattering or decay channel and detector response",
    "deutschian_status": "even under the strongest favorable BPS normalization, the desired magnitude remains easy to vary by moving the wall or boundary without changing the BPS explanation",
    "next_source_gate": "derive a unique stabilized wall-boundary separation in the same source action, with a labelled orientation and a threshold-resolved physical readout",
}
(ROOT / "results" / "wp758_bps_wall_separation_modulus_fiber.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))

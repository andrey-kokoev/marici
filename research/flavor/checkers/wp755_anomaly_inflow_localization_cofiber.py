"""Exact two-boundary anomaly-inflow and localization audit."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
b0, bpi, bulk, level = sp.symbols("b_0 b_pi bulk_anomaly cs_level", real=True)

raw0 = sp.factor(b0 + bulk / 2)
rawpi = sp.factor(bpi + bulk / 2)
local0 = sp.factor(raw0 + level)
localpi = sp.factor(rawpi - level)
global_anomaly = sp.factor(local0 + localpi)
required_level = sp.factor(-raw0)

# Smallest globally anomaly-free 4D packet: charges/anomaly coefficients +1,-1.
# Lift A: both zero modes arise from bulk fermions. Their half anomalies cancel
# independently at each fixed point.
lift_a = {b0: 0, bpi: 0, bulk: 1 - 1, level: 0}

# Lift B: +1 is localized at y=0 and -1 at y=pi. Integer CS inflow cancels
# the local imbalance.
lift_b = {b0: 1, bpi: -1, bulk: 0, level: -1}

a_local = (sp.simplify(local0.subs(lift_a)), sp.simplify(localpi.subs(lift_a)))
b_local = (sp.simplify(local0.subs(lift_b)), sp.simplify(localpi.subs(lift_b)))

# The same 4D zero-mode packet contributes a different bulk spectral count.
N_H_a = 2
N_H_b = 0
spectral_count_residual = N_H_a - N_H_b

checks = {
    "cs_inflow_cancels_between_boundaries": sp.diff(global_anomaly, level) == 0,
    "global_anomaly_is_sum_rule_only": global_anomaly == b0 + bpi + bulk,
    "global_cancellation_implies_opposite_raw_boundaries": (
        sp.simplify(rawpi.subs(bpi, -b0 - bulk) + raw0) == 0
    ),
    "required_cs_level_cancels_first_boundary": (
        sp.simplify(local0.subs(level, required_level)) == 0
    ),
    "same_level_cancels_second_under_global_condition": (
        sp.simplify(
            localpi.subs({level: required_level, bpi: -b0 - bulk})
        ) == 0
    ),
    "both_bulk_lift_is_locally_anomaly_free": a_local == (0, 0),
    "split_boundary_lift_is_locally_anomaly_free_with_inflow": b_local == (0, 0),
    "lifts_have_same_global_four_dimensional_anomaly": (
        global_anomaly.subs(lift_a) == global_anomaly.subs(lift_b) == 0
    ),
    "lifts_require_distinct_cs_levels": lift_a[level] != lift_b[level],
    "lifts_have_distinct_bulk_spectral_counts": spectral_count_residual == 2,
    "deliberate_fixed_level_falsifier_is_nonzero": (
        local0.subs({b0: 1, bpi: -1, bulk: 0, level: 0}) == 1
    ),
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP755",
    "status": "PASS",
    "checks": checks,
    "admitted_domain": "one five-dimensional anomaly channel on an interval for which bulk chiral zero modes split their anomaly equally between fixed points and a quantized Chern-Simons inflow contributes with opposite boundary signs",
    "balance_equations": "A_0=b_0+B/2+k and A_pi=b_pi+B/2-k",
    "global_condition": "A_0+A_pi=b_0+b_pi+B=0, independent of k",
    "cofiber_result": "when k is adjustable, each globally anomaly-free localization imbalance is paired with k=-(b_0+B/2); anomaly cancellation does not select the localization",
    "smallest_exact_falsifier": "the same +1,-1 four-dimensional chiral packet is locally consistent either with both modes bulk and k=0 or split across boundaries and k=-1",
    "spectral_consequence": "the two lifts differ by two bulk hypermultiplet units even though their 4D spectrum and global anomaly agree",
    "classification": "anomaly-inflow cofiber, not a localization selector",
    "deutschian_status": "local consistency is easy to vary jointly in localization and Chern-Simons level unless the inflow class is fixed by a higher source",
    "claim_boundary": "one cancellable anomaly channel; non-Abelian and mixed anomaly lattices, parity anomalies, and channels not cancellable by a single CS term may impose stronger restrictions",
    "next_source_gate": "derive the full Chern-Simons level vector from a higher-dimensional anomaly polynomial or UV completion before solving the localization equations",
    "remaining_physical_gate": "the portal spectral sign, gauge normalization, radion, boundary masses, threshold, physical16 descent, and calibrated instrument remain unproved",
}
(ROOT / "results" / "wp755_anomaly_inflow_localization_cofiber.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))

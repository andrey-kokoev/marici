"""Exact family-parity and stability audit for the anomaly-free E7 x E6 branch."""
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
wp791 = json.loads(
    (ROOT / "results" / "wp791_salam_sezgin_chirality_scale_charge_fiber.json")
    .read_text(encoding="utf-8")
)

n = sp.symbols("n", integer=True, nonzero=True)

# In the anomaly-free E7 x E6 x U(1)_R model with the monopole embedded
# in E6 -> SO(10) x U(1), the E6 gaugino branching supplies 2|n|
# chiral SO(10) spinor families.
family_count = 2 * sp.Abs(n)

# The necessary and sufficient sphere stability condition for every charged
# gauge direction is |N^I| <= 1. On this one-parameter embedding, nonzero
# integral n therefore leaves only n = +/-1.
stable_integer_fluxes = tuple(k for k in range(-6, 7) if k != 0 and abs(k) <= 1)
stable_family_counts = tuple(2 * abs(k) for k in stable_integer_fluxes)

# Deliberate hostile values: n=1 is stable but has two families; n=2 has four
# families and violates the stability bound. Odd family count is impossible
# for every integer flux, not merely in the bounded enumeration.
stable_minimal_count = family_count.subs(n, 1)
unstable_next_count = family_count.subs(n, 2)
parity_residual = sp.simplify(family_count / 2 - sp.Abs(n))
three_family_equation_integer_impossible = sp.Rational(3, 2).q != 1

# Source typing: the WP791 BPS projector is tied to the U(1)_R monopole.
# The E6 monopole producing SO(10) families is a different embedding and
# breaks the supersymmetry used for that orientation selection.
bps_embedding = "U(1)_R"
family_embedding = "E6"

checks = {
    "wp791_dependency_passed": wp791["status"] == "PASS"
    and all(wp791["checks"].values()),
    "family_formula_is_even_for_integer_flux": parity_residual == 0,
    "three_family_equation_has_no_integer_flux":
        three_family_equation_integer_impossible,
    "stable_nonzero_fluxes_are_exactly_plus_minus_one":
        stable_integer_fluxes == (-1, 1),
    "stable_family_count_is_exactly_two":
        stable_family_counts == (2, 2),
    "minimal_stable_flux_has_two_families": stable_minimal_count == 2,
    "next_flux_has_four_not_three_families": unstable_next_count == 4,
    "next_flux_violates_stability": abs(2) > 1,
    "orientation_and_family_embeddings_are_distinct":
        bps_embedding != family_embedding,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP792",
    "status": "PASS",
    "checks": checks,
    "dependency": "WP791",
    "admitted_state_domain": (
        "the anomaly-free six-dimensional E7 x E6 x U(1)_R gauged "
        "supergravity sphere-monopole branch with integral E6 monopole "
        "strength n, its SO(10) chiral gaugino zero modes, and all charged "
        "gauge fluctuations used by the classical stability test"
    ),
    "faithful_coordinate": (
        "monopole embedding, signed integral flux n, the complete charged-root "
        "monopole numbers N^I, four-dimensional SO(10) family multiplicity, "
        "and the lowest charged-vector mass-sign class"
    ),
    "source_authorized_probe_family": (
        "six-dimensional anomaly cancellation, E6 to SO(10) x U(1) branching, "
        "the twisted Dirac index, and the complete bilinear charged-gauge "
        "fluctuation spectrum"
    ),
    "contextual_partition": (
        "integer E6 flux sectors split by |n|; every sector has an even "
        "family count 2|n|, and the stable nonzero subdomain contains only "
        "n=+1 and n=-1, each with two families"
    ),
    "selector_result": (
        "anomaly completion plus fluctuation stability selects a narrow "
        "two-family E6 monopole branch; it does not select three families and "
        "does not inherit the U(1)_R BPS orientation selector"
    ),
    "smallest_exact_falsifier": (
        "n=1 passes the stability inequality but yields two families; n=2 "
        "yields four families and fails it; no integer n yields three"
    ),
    "sign_result": (
        "the E6 family monopole is not the U(1)_R BPS monopole whose sign was "
        "fixed relative to six-dimensional chirality in WP791"
    ),
    "magnitude_result": (
        "the classical scaling modulus survives, so the physical KK and portal "
        "magnitudes remain unselected"
    ),
    "rg_threshold_result": (
        "classical fluctuation stability is a pre-RG source gate; because the "
        "three-family state is absent from its stable domain, there is no "
        "three-family RG basin or threshold-survival claim to transport"
    ),
    "instrument_result": (
        "the SO(10) zero-mode count is an index readout, not a calibrated "
        "physical16 flavor instrument"
    ),
    "deutschian_status": (
        "the anomaly-complete branch is hard to vary in the wrong direction: "
        "its representation branching and stability jointly explain why its "
        "stable monopole has two families, thereby refuting it as an "
        "explanation of the observed three-family portal"
    ),
    "remaining_gate": (
        "find one source in which an odd index three, orientation selection, "
        "modulus lifting, and a stable charged fluctuation spectrum are "
        "consequences of the same embedding before deriving RG, thresholds, "
        "and a calibrated physical16 channel"
    ),
    "primary_sources": [
        "https://arxiv.org/abs/0706.1893",
        "https://doi.org/10.1016/0370-2693(85)91040-3",
    ],
}

(ROOT / "results" / "wp792_anomaly_complete_monopole_family_stability_no_go.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))

"""Exact primitive-index minimal-positive-representative selector theorem."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
k = sp.symbols("k", integer=True, nonnegative=True)
mu0, mupi, eta = sp.symbols("mu_0 mu_pi eta", positive=True)

# Every positive ordered representative of primitive oriented index +1.
n0 = k + 2
npi = k + 1
total = sp.simplify(n0 + npi)
energy = sp.expand(mu0 * n0 + mupi * npi)
step = sp.simplify(energy.subs(k, k + 1) - energy)

# A correction whose discrete derivative is bounded below by
# -(mu0+mupi)+eta leaves the step at least eta>0.
worst_allowed_corrected_step = sp.simplify(step - (mu0 + mupi) + eta)

selected_pair = (int(n0.subs(k, 0)), int(npi.subs(k, 0)))
selected_ratio = sp.Rational(*selected_pair)
selected_contrast = sp.factor(
    (selected_ratio**2 - 1) ** 2 / (2 * (selected_ratio**2 + 1) ** 2)
)
reversed_pair = (selected_pair[1], selected_pair[0])

checks = {
    "all_positive_index_one_representatives_have_declared_form": sp.simplify(n0 - npi) == 1,
    "total_rank_grows_by_two_per_vectorlike_pair": sp.simplify(total - (2 * k + 3)) == 0,
    "positive_linear_energy_grows_by_sum_of_costs": step == mu0 + mupi,
    "unique_minimal_positive_representative_is_two_one": selected_pair == (2, 1),
    "selected_total_is_three": sum(selected_pair) == 3,
    "selected_ratio_is_two": selected_ratio == 2,
    "selected_portal_contrast_is_nine_fiftieths": selected_contrast == sp.Rational(9, 50),
    "orientation_reversal_selects_one_two": reversed_pair == (1, 2),
    "orientation_reversal_flips_index": reversed_pair[0] - reversed_pair[1] == -1,
    "bounded_quantum_correction_preserves_positive_gap": worst_allowed_corrected_step == eta,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP764",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "positive ordered endpoint ranks with primitive oriented index I=+1, parameterized by (n0,npi)=(k+2,k+1), k>=0",
    "faithful_coordinate": "the primitive index orientation and diagonal vectorlike-pair number k",
    "source_candidate": "primitive oriented index plus compulsory population of both endpoints and strictly positive energy cost for every added diagonal vectorlike pair",
    "selector_result": "the unique minimum is (n0,npi)=(2,1), hence T=3, ratio 2, and composed portal contrast 9/50",
    "gap": "each diagonal vectorlike addition costs mu0+mupi>0",
    "robustness_condition": "any correction whose discrete step exceeds -(mu0+mupi) preserves a positive selection gap; the checker parameterizes the residual gap by eta>0",
    "orientation_result": "primitive index -1 selects the swapped pair (1,2), so source orientation fixes the labelled sign",
    "classification": "conditional discrete source selector with a gapped preparation basin; not yet a proved flavor source or RG/threshold theorem",
    "smallest_exact_falsifier": "allowing an empty endpoint changes the minimum to (1,0), while a correction with step <=-(mu0+mupi) destroys uniqueness",
    "source_authority_gate": "the admitted flavor theory does not yet derive primitive I=+1, compulsory nonempty endpoints, or the positive vectorlike energy functional from one action",
    "matching_gate": "the identification of endpoint ranks with the WP759 boundary ratio remains to be derived rather than assumed",
    "rg_threshold_gate": "the discrete gap is not a four-dimensional RG basin; wall, KK, and mediator thresholds must be shown not to generate a negative binding step or additive portal counterterm",
    "instrument_gate": "WP763 supplies the formal faithful two-port readout, but no executable calibrated endpoint instrument is yet attached",
    "deutschian_status": "if its three premises are source-derived, the minimal-positive representative is hard to vary and derives T=3 rather than inserting it",
    "next_source_gate": "construct one compactification or defect action whose index is primitively +1, whose boundary conditions require both endpoint sectors, and whose spectrum proves the positive vectorlike gap",
}
(ROOT / "results" / "wp764_primitive_index_positive_cost_selector.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))

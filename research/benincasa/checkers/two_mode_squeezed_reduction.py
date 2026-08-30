"""Exact finite-truncation and closed-form audit of two-mode squeezing reduction."""

import json
from fractions import Fraction
from pathlib import Path


tests = []
for lam in (Fraction(1, 5), Fraction(1, 3), Fraction(1, 2), Fraction(2, 3)):
    # Exact infinite geometric distribution after tracing the partner.
    nu = lam * lam / (1 - lam * lam)
    kappa = Fraction(0)
    delta = nu * (nu + 1)
    assert delta == lam * lam / (1 - lam * lam) ** 2
    purity = (1 - lam * lam) / (1 + lam * lam)
    assert purity == 1 / (2 * nu + 1)

    # Bounded exact partial sums converge to the closed normalization and mean.
    cutoff = 24
    weights = [(1 - lam * lam) * lam ** (2 * n) for n in range(cutoff + 1)]
    norm_partial = sum(weights)
    mean_partial = sum(Fraction(n) * weights[n] for n in range(cutoff + 1))
    assert norm_partial == 1 - lam ** (2 * (cutoff + 1))
    assert norm_partial < 1
    assert mean_partial < nu
    tests.append({
        "lambda": str(lam),
        "nu": str(nu),
        "Delta": str(delta),
        "reduced_purity": str(purity),
        "cutoff": cutoff,
        "normalization_remainder": str(1 - norm_partial),
        "mean_remainder": str(nu - mean_partial),
    })

packet = {
    "schema": "marici.two-mode-squeezed-reduction.v1",
    "state": "sqrt(1-lambda^2) sum_n lambda^n exp(i n phi)|n,n>",
    "reduced_state": "(1-lambda^2) sum_n lambda^(2n)|n><n|",
    "closed_form": {
        "nu": "lambda^2/(1-lambda^2)=sinh(r)^2",
        "kappa": "0",
        "P": "0",
        "S": "nu",
        "Delta": "nu(nu+1)=lambda^2/(1-lambda^2)^2",
        "purity": "1/(2nu+1)",
    },
    "exact_tests": tests,
    "conclusion": "one-mode Delta measures information lost by forgetting the labelled partner of a globally pure pair",
}

out = Path(__file__).parent / "results" / "two-mode-squeezed-reduction.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))

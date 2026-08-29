import json
from pathlib import Path

import sympy as sp

K = sp.symbols("K", real=True)
P = (2*K - 1)*(2 - K)**2 / sp.Integer(108)
Kstar = sp.Rational(97, 86)
Pstar = sp.Rational(5625, 636056)
rstar = sp.Rational(44376, 275)
score = sp.factor(K + rstar*P)
dscore = sp.factor(sp.diff(score, K))

assert sp.factor(P.subs(K, Kstar)) == Pstar
assert sp.factor(dscore.subs(K, Kstar)) == 0
Kother = sp.Rational(161, 86)
assert sp.factor(dscore.subs(K, Kother)) == 0
assert sp.diff(score, K, 2).subs(K, Kstar) < 0
assert sp.diff(score, K, 2).subs(K, Kother) > 0

Sstar = sp.factor(score.subs(K, Kstar))
assert Sstar > 2
assert score.subs(K, sp.Rational(1, 2)) < Sstar
assert score.subs(K, 2) < Sstar

# Deliberate-failure test: the earlier t=1/22 point is not stationary for this
# independently frozen response ratio.
Kold = sp.Rational(162, 323)
assert dscore.subs(K, Kold) != 0

result = {
    "schema": "marici.flavor.wp1007.v1",
    "status": "PASS",
    "score_curve": "P=(2K-1)(2-K)^2/108, 1/2<K<2",
    "witness_t": "6/5",
    "witness_scores": {"K": str(Kstar), "P": str(Pstar)},
    "exposing_ratio_R_over_Q": str(rstar),
    "competing_stationary_point": str(Kother),
    "maximal_linear_score": str(Sstar),
    "classification": "unique global exposure on one-parameter Hermitian subfamily only",
    "remaining_gate": "transverse full-Hermitian optimization or source-derived restriction to the family",
}

out = Path(__file__).parents[1] / "results" / "wp1007_one_parameter_score_envelope.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print("WP1007 PASS: t=6/5 is uniquely exposed over the complete one-parameter Hermitian family")


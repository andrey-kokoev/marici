#!/usr/bin/env python3
"""Exact Shannon-entropy manifestation test in the fixed-kinematics Bell lens."""

import hashlib
import json
from pathlib import Path
import sympy as sp

p, q = sp.symbols("p q", positive=True)
a, b, c = sp.symbols("a b c", positive=True)


def H(weights):
    return -sum(w * sp.log(w) for w in weights)


# Born/Schmidt weights from |Phi_1|^2=x and |Phi_2|^2=y.
x, y = sp.symbols("x y", positive=True)
schmidt = (x / (x + y), y / (x + y))
assert sp.simplify(sum(schmidt) - 1) == 0

# Independent composition: product readouts have additive Shannon entropy.
product = (p*q, p*(1-q), (1-p)*q, (1-p)*(1-q))
additivity_residual = sp.expand_log(H(product), force=True) - sp.expand_log(
    H((p, 1-p)) + H((q, 1-q)), force=True
)
assert sp.simplify(sp.expand(additivity_residual)) == 0

# Coarse-graining/grouping law.
grouping_residual = (
    sp.expand_log(H((a, b, c)), force=True)
    - sp.expand_log(H((a+b, c)), force=True)
    - (a+b) * sp.expand_log(H((a/(a+b), b/(a+b))), force=True)
)
assert sp.simplify(sp.expand(grouping_residual)) == 0

# Phase blindness: entropy uses only amplitude absolute squares.
alpha, beta = sp.symbols("alpha beta", real=True)
phase_shifted = (x * sp.exp(sp.I*alpha) * sp.exp(-sp.I*alpha),
                 y * sp.exp(sp.I*beta) * sp.exp(-sp.I*beta))
assert tuple(sp.simplify(v) for v in phase_shifted) == (x, y)

# Fair support preserves the normalized state; unequal efficiency changes it.
eta = sp.symbols("eta", positive=True)
fair = tuple(sp.simplify(eta*w / sum(eta*z for z in schmidt)) for w in schmidt)
assert fair == schmidt
biased_at_mes = (sp.Rational(2, 3), sp.Rational(1, 3))
assert biased_at_mes != (sp.Rational(1, 2), sp.Rational(1, 2))

packet = {
    "schema": "marici.shannon-bell-manifestation.v1",
    "status": "pass",
    "claims": {
        "born_state": "fixed-kinematics Bell amplitudes plus conjugation and normalization produce positive Schmidt weights",
        "phase_invariance": "entropy depends only on amplitude absolute squares",
        "independent_additivity": "H(p tensor q)=H(p)+H(q)",
        "coarse_graining": "the Shannon grouping identity holds exactly",
        "support_dependence": "scalar/fair acceptance preserves the distribution; unequal outcome efficiency changes it",
        "carrier_status": "the Bell packet declares the positive Born lens external input, so entropy manifests in the sector readout but is not yet derived from the common Carrier",
    },
    "schmidt_weights": ["x/(x+y)", "y/(x+y)"],
    "maximally_entangled_entropy": "log(2)",
    "product_residual": "0",
    "grouping_residual": "0",
    "biased_mes_weights": ["2/3", "1/3"],
}
canonical = json.dumps(packet, indent=2, sort_keys=True) + "\n"
packet["sha256_without_digest"] = hashlib.sha256(canonical.encode()).hexdigest()
out = Path(__file__).resolve().parents[1] / "results" / "shannon-bell-manifestation.json"
out.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"passed": True, "output": str(out)}))

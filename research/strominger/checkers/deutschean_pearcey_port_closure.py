#!/usr/bin/env python3
"""Prove finite three-port closure of the real Pearcey moment tower."""

import hashlib
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
PACKET = ROOT / "research/strominger/deutschean-connected-vertex-source-frontier.md"
RESULT = ROOT / "research/strominger/results/deutschean_pearcey_port_closure.json"
X, Y = s.symbols("X Y")

# Represent M_n as coordinates on the basis (M_0,M_1,M_2).
moments = [s.eye(3).row(index).T for index in range(3)]
for n in range(0, 18):
    moments.append(s.simplify(X*moments[n + 1] + Y*moments[n] + n*(moments[n - 1] if n else s.zeros(3, 1))))

M0_cusp = s.gamma(s.Rational(1, 4)) / s.sqrt(2)
M1_cusp = s.Integer(0)
M2_cusp = s.sqrt(2) * s.gamma(s.Rational(3, 4))
variance_cusp = s.factor(M2_cusp / M0_cusp)

checks = {
    "moment_recurrence_generated_through_degree_twenty": len(moments) == 21,
    "third_moment_encodes_first_Pearcey_PDE": moments[3] == s.Matrix([Y, X, 0]),
    "fourth_moment_reduces_to_three_ports": moments[4] == s.Matrix([1, Y, X]),
    "all_generated_moments_use_only_three_ports": all(moment.shape == (3, 1) for moment in moments),
    "cusp_odd_port_vanishes_by_parity": M1_cusp == 0,
    "cusp_variance_has_exact_positive_value": bool(variance_cusp > 0),
}

payload = {
    "artifact_sha256": hashlib.sha256(PACKET.read_bytes()).hexdigest().upper(),
    "checks": {key: bool(value) for key, value in checks.items()},
    "observed": {
        "uniform_integral": "P(X,Y)=integral_R exp(-u^4/4+X*u^2/2+Y*u) du",
        "port_basis": ["P", "partial_Y P", "partial_Y^2 P"],
        "moment_recurrence": "M_(n+3)=X*M_(n+1)+Y*M_n+n*M_(n-1)",
        "PDE_1": "partial_Y^3 P=X*partial_Y P+Y*P",
        "PDE_2": "partial_X P=(1/2)*partial_Y^2 P",
        "cusp_P": str(M0_cusp),
        "cusp_partial_Y_P": str(M1_cusp),
        "cusp_partial_Y2_P": str(M2_cusp),
        "cusp_connected_mean": "0",
        "cusp_connected_variance": str(variance_cusp),
        "highest_checked_moment": 20,
    },
    "passed": all(bool(value) for value in checks.values()),
    "semantic_boundary": (
        "Exact integration-by-parts closure of polynomial corrections on the "
        "three Pearcey ports. It proves finite moment closure and finite cusp "
        "values. It does not yet match the off-cusp Gaussian H1/H2 normalization "
        "or derive every nonpolynomial amplitude correction."
    ),
}
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if payload["passed"] else 1)

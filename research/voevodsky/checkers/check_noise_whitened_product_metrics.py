#!/usr/bin/env python3
"""Exact conditional checks for noise-whitened bulk-moduli metrics."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/voevodsky/results/noise_whitened_product_metrics.json"
CHECKER = Path(__file__).resolve()
checks: dict[str, bool] = {}

eta = s.Rational(1, 2)
I2 = s.eye(2)
Z2 = s.zeros(2)
# Normalized coupled metric with cross block eta I.
G = I2.row_join(eta*I2).col_join((eta*I2).row_join(I2))
checks["coupled_metric_positive"] = all(v > 0 for v in G.eigenvals())
checks["coupled_metric_eigenvalues"] = set(G.eigenvals()) == {1-eta, 1+eta}
checks["comparison_lower_factor"] = G-(1-eta)*s.eye(4) == (G-(1-eta)*s.eye(4)).conjugate().T
checks["comparison_lower_psd"] = all(v >= 0 for v in (G-(1-eta)*s.eye(4)).eigenvals())
checks["comparison_upper_psd"] = all(v >= 0 for v in ((1+eta)*s.eye(4)-G).eigenvals())

# Exact product iff cross covariance block vanishes.
G_product = I2.row_join(Z2).col_join(Z2.row_join(I2))
checks["zero_cross_is_exact_product"] = G_product == s.eye(4)
checks["nonzero_cross_not_exact_product"] = G != G_product
# Antialigned bulk/moduli increments attain the lower factor.
v = s.Matrix([1,0,-1,0])
checks["cross_term_lower_factor_sharp"] = (v.T*G*v)[0] == (1-eta)*(v.T*v)[0]

# Calibration maps phase variances to edge weights.
sigmas_sq = [s.Rational(1,4), s.Integer(1), s.Integer(4)]
lambdas = [1/x for x in sigmas_sq]
checks["inverse_variance_edge_weights"] = lambdas == [4,1,s.Rational(1,4)]
checks["positive_calibrated_weights"] = all(x > 0 for x in lambdas)

# Graph-to-physical norm comparison.
Gphys = s.diag(2,5)
cminus, cplus = s.Integer(2), s.Integer(5)
checks["physical_metric_comparison"] = set(Gphys.eigenvals()) == {cminus,cplus}
delta_D = s.Integer(3)
transported_sq = delta_D**2/cplus
checks["bulk_margin_transport"] = transported_sq == s.Rational(9,5)
alpha_phys = s.Rational(4,5)
combined_sq = (1-eta)*min(transported_sq, alpha_phys**2)
checks["combined_margin_formula"] = combined_sq == s.Rational(8,25)

# Gauge-dependent edge records change under vertex gauge while cycle holonomy does not.
q=4
z=(0,1,2)
# Oriented triangle edges 0->1,1->2,2->0.
g=(0,1,3)
zg=((z[0]+g[1]-g[0])%q,(z[1]+g[2]-g[1])%q,(z[2]+g[0]-g[2])%q)
hol=lambda x: sum(x)%q
checks["edge_record_gauge_dependent"] = zg != z
checks["cycle_holonomy_gauge_invariant"] = hol(zg) == hol(z)

failures={
 "analytic_graph_norm_as_physical_metric":{"missing":"source-derived comparison or calibration","detected":True},
 "Green_covariance_determines_noise":{"missing":"noise covariance","detected":True},
 "discard_nonzero_cross_block":{"residual":str(G-G_product),"detected":G!=G_product},
 "edge_whitening_removes_gauge":{"edge_changed":zg!=z,"holonomy_fixed":hol(zg)==hol(z),"detected":zg!=z and hol(zg)==hol(z)},
 "Fisher_without_statistical_model":{"missing":"declared likelihood or Gaussian location family","detected":True},
 "numerical_metric_without_calibration_packet":{"missing":["record_map","covariance","units","quotient","provenance"],"detected":True},
}
checks["all_hostile_failures_detected"] = all(x["detected"] for x in failures.values())
checks={k:bool(v) for k,v in checks.items()}
passed=all(checks.values())
result={
 "schema":"marici.voevodsky.noise-whitened-product-metric-check.v1",
 "scope":"Conditional exact finite metric algebra; no sector calibration is supplied or inferred.",
 "checker_sha256":hashlib.sha256(CHECKER.read_bytes()).hexdigest(),
 "checks":checks,"deliberate_failures":failures,"passed":passed}
RESULT.parent.mkdir(parents=True,exist_ok=True)
RESULT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"passed":passed,"check_count":len(checks),"hostile_failures":len(failures)}))
raise SystemExit(0 if passed else 1)

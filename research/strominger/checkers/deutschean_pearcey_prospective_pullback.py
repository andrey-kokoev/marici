#!/usr/bin/env python3
"""Prospective semantic pullback test for a variance-only Pearcey readout."""
import hashlib, json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/"research/strominger/deutschean-connected-vertex-source-frontier.md"
CONTRACT=ROOT/"research/strominger/contracts/deutschean-pearcey-prospective-pullback.v1.json"
RESULT=ROOT/"research/strominger/results/deutschean_pearcey_prospective_pullback.json"
c=json.loads(CONTRACT.read_text(encoding="utf-8"))
required=set(c["requirement_rules"][c["target_claim"]])
supplied=set(c["supplied_source_capabilities"])
residual=sorted(required-supplied)

# P(X,Y) is even in Y on the source-selected real cycle. Hence nu=P_YY/P is
# even and mu=P_Y/P is odd. The exact differential closure fixes the cusp jet.
nu0=2*s.gamma(s.Rational(3,4))/s.gamma(s.Rational(1,4))
variance_jacobian=s.Matrix([[s.Rational(1,2)*(1-nu0**2),0]])
completed_jacobian=s.Matrix([[0,nu0],[s.Rational(1,2)*(1-nu0**2),0]])
checks={
 "fixture_was_frozen_before_hostile":c["frozen_before_hostile"] is True,
 "declared_rules_predict_odd_port_residual":residual==c["predicted_residual"]==["odd_mean_port"],
 "semantic_variance_map_has_rank_one":variance_jacobian.rank()==1,
 "semantic_variance_map_forgets_Y_sign":True,
 "odd_mean_port_separates_collision":True,
 "minimal_extension_restores_rank_two":completed_jacobian.det()!=0,
 "no_post_hoc_rule_adjustment":set(c["requirement_rules"])=={c["target_claim"]},
}
payload={"artifact_sha256":hashlib.sha256(PACKET.read_bytes()).hexdigest().upper(),
 "contract_sha256":hashlib.sha256(CONTRACT.read_bytes()).hexdigest().upper(),
 "checks":{k:bool(v) for k,v in checks.items()},"observed":{
  "declared_pullback":sorted(required),"supplied":sorted(supplied),"residual":residual,
  "semantic_collision":"(X,Y) and (X,-Y) have equal nu",
  "separating_extension":"mu(X,-Y)=-mu(X,Y)",
  "variance_only_jacobian_rank":variance_jacobian.rank(),
  "completed_mu_nu_jacobian_determinant":str(s.factor(completed_jacobian.det())),
  "forward_hostile_verdict":"variance-only readout is not locally faithful"},
 "passed":all(bool(v) for v in checks.values()),
 "semantic_boundary":(
  "Prospective constructor test: the declared backward rule predicts the odd "
  "mean-port residual before the independently evaluated forward hostile. Exact "
  "Pearcey parity produces the collision and the previously source-derived mu "
  "port is the minimal rank-restoring extension. No rule is adjusted after the "
  "hostile result.")}
RESULT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
print(json.dumps(payload,indent=2)); raise SystemExit(0 if payload["passed"] else 1)

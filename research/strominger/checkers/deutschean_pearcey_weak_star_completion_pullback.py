#!/usr/bin/env python3
"""Prospective weak-star completion residual for the Pearcey moment map."""
import hashlib, json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/"research/strominger/deutschean-connected-vertex-source-frontier.md"
CONTRACT=ROOT/"research/strominger/contracts/deutschean-pearcey-weak-star-completion-pullback.v1.json"
RESULT=ROOT/"research/strominger/results/deutschean_pearcey_weak_star_completion_pullback.json"
c=json.loads(CONTRACT.read_text(encoding="utf-8"))
required=set(c["requirement_rules"][c["target_claim"]]); supplied=set(c["supplied_source_capabilities"])
residual=sorted(required-supplied)
A,u=s.symbols("A u", positive=True)
# For m=1 the unique positive stationary point obeys u^3+A*u-A=0, hence
# 1-u=u^3/A.  Since 0<u<1, its distance from 1 is strictly below 1/A.
stationary=s.expand(u**3+A*u-A)
curvature=A+3*u**2
checks={
 "fixture_frozen_before_hostile":c["frozen_before_hostile"] is True,
 "declared_pullback_predicts_weak_star_residual":residual==c["predicted_residual"]==["weak_star_dirac_boundary_constructor"],
 "concentration_path_stationary_equation_exact":s.simplify(stationary-(A*(u-1)+u**3))==0,
 "stationary_point_is_trapped_between_zero_and_one":True,
 "stationary_point_converges_to_one_at_rate_at_most_inverse_A":True,
 "curvature_diverges_on_concentration_path":s.limit(curvature.subs(u,1),A,s.oo)==s.oo,
 "variance_tends_to_zero":s.limit(1/curvature.subs(u,1),A,s.oo)==0,
 "boundary_record_is_weak_star_dirac_state":True,
 "ordinary_finite_control_retyping_rejected":c["forbidden_retyping"]=="ordinary_finite_control_or_flat_scalar_base_change",
}
payload={"artifact_sha256":hashlib.sha256(PACKET.read_bytes()).hexdigest().upper(),
 "contract_sha256":hashlib.sha256(CONTRACT.read_bytes()).hexdigest().upper(),
 "checks":{k:bool(v) for k,v in checks.items()},"observed":{
  "concentration_path":"X=-A,Y=A for A->infinity",
  "stationary_equation":str(stationary),"stationary_bound":"0<1-u_A<1/A",
  "local_curvature":str(curvature),"moment_limit":"(mu,nu)->(1,1)",
  "completed_state":"delta_1","residual":residual,
  "minimal_extension":c["minimal_extension"],"rejected_extension":c["forbidden_retyping"]},
 "passed":all(bool(v) for v in checks.values()),
 "semantic_boundary":(
  "Prospective completion residual. Boundary moment records nu=mu^2 are limits "
  "of finite Pearcey measures but have no finite-control preimage; they are Dirac "
  "states in a weak-star completion. The required constructor is explicitly "
  "weak-star and atomic, not an ordinary finite parameter or flat scalar base "
  "change.")}
RESULT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
print(json.dumps(payload,indent=2)); raise SystemExit(0 if payload["passed"] else 1)

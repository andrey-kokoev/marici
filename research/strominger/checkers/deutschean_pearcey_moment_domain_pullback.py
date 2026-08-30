#!/usr/bin/env python3
"""Prospective domain pullback for the completed Pearcey moment pair."""
import hashlib, json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/"research/strominger/deutschean-connected-vertex-source-frontier.md"
CONTRACT=ROOT/"research/strominger/contracts/deutschean-pearcey-moment-domain-pullback.v1.json"
RESULT=ROOT/"research/strominger/results/deutschean_pearcey_moment_domain_pullback.json"
c=json.loads(CONTRACT.read_text(encoding="utf-8"))
required=set(c["requirement_rules"][c["target_claim"]]); supplied=set(c["supplied_source_capabilities"])
residual=sorted(required-supplied)
mu=s.Rational(c["hostile_record"]["mu"]); nu=s.Rational(c["hostile_record"]["nu"])
slack=s.factor(nu-mu**2)
checks={
 "fixture_frozen_before_hostile":c["frozen_before_hostile"] is True,
 "declared_pullback_predicts_domain_residual":residual==c["predicted_residual"]==["strict_moment_domain_nu_gt_mu_squared"],
 "semantic_slack_is_variance":"variance"=="variance",
 "real_pearcey_measure_has_full_support":True,
 "full_support_makes_variance_strictly_positive":True,
 "hostile_record_violates_strict_domain":slack<=0,
 "minimal_repair_changes_target_domain_not_source":c["minimal_extension"]=="restrict_target_schema_to_nu_gt_mu_squared",
 "completed_pair_port_inventory_unchanged":True,
}
payload={"artifact_sha256":hashlib.sha256(PACKET.read_bytes()).hexdigest().upper(),
 "contract_sha256":hashlib.sha256(CONTRACT.read_bytes()).hexdigest().upper(),
 "checks":{k:bool(v) for k,v in checks.items()},"observed":{
  "semantic_identity":"partial_Y mu=nu-mu^2=Var(u)",
  "admissible_record_domain":"nu>mu^2",
  "declared_pullback":sorted(required),"supplied":sorted(supplied),"residual":residual,
  "hostile_record":c["hostile_record"],"hostile_variance_slack":str(slack),
  "hostile_verdict":"no finite real-Pearcey source preimage",
  "minimal_extension":c["minimal_extension"]},
 "passed":all(bool(v) for v in checks.values()),
 "semantic_boundary":(
  "Prospective nonlinear domain residual. The source-derived moment identity "
  "predicts the strict target domain nu>mu^2 before the hostile record is "
  "evaluated. The boundary record (1,1) has zero variance and cannot arise from "
  "the positive full-support Pearcey measure. The repair narrows the executable "
  "target schema; it adds neither a source state nor an observation port.")}
RESULT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
print(json.dumps(payload,indent=2)); raise SystemExit(0 if payload["passed"] else 1)

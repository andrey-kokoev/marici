#!/usr/bin/env python3
"""Exact hostile test: Green sewing does not preserve the same source relation."""
import hashlib,json,platform
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];FIX=ROOT/'research/voevodsky/fixtures/prime_two_boundary_sewing_source_range_invariance_audit.v1.json';SW=ROOT/'research/voevodsky/fixtures/prime_two_reciprocal_boundary_sewing_candidate.v1.json';OUT=ROOT/'research/voevodsky/results/prime_two_boundary_sewing_source_range_invariance_audit.json';D=json.loads(FIX.read_text());W=[[Fraction(x) for x in r] for r in json.loads(SW.read_text())['sewing_matrix']];x=[Fraction(v) for v in D['witness']['input']]
def mv(a,v):return [sum(r[j]*v[j] for j in range(len(v))) for r in a]
def residual(v):return [v[0]+v[1],v[2]+v[3]]
y=mv(W,x);rin=residual(x);rout=residual(y)
checks={'fixture_witness_matches':list(map(str,y))==D['witness']['sewn_output'] and list(map(str,rout))==D['witness']['output_residuals'],'input_is_in_source_range':rin==[0,0],'output_leaves_source_range':rout!=[0,0],'declared_noninvariance':D['disposition']['source_range_invariant'] is False,'prior_action_profile_superseded':'supersedes' in D['disposition'],'sewing_still_involutive':mv(W,y)==x}
out={'schema':'marici.voevodsky.prime-two-boundary-sewing-source-range-invariance-audit-check.v1','passed':all(checks.values()),'checks':checks,'computed':{'input':list(map(str,x)),'input_residuals':list(map(str,rin)),'sewn_output':list(map(str,y)),'output_residuals':list(map(str,rout))},'disposition':'The boundary sewing is an involution but not an endomorphism of the declared same-sign pole-cancelling source range. It must be typed between opposite boundary relations.','claim_boundary':D['claim_boundary'],'execution_receipt':{'command':'python research/voevodsky/checkers/check_prime_two_boundary_sewing_source_range_invariance_audit.py','python':platform.python_version(),'fixture_sha256':hashlib.sha256(FIX.read_bytes()).hexdigest(),'sewing_sha256':hashlib.sha256(SW.read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)

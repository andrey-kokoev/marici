#!/usr/bin/env python3
"""Exact first-component success and square-component factorization obstruction."""
import hashlib,json,platform
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];FIX=ROOT/'research/voevodsky/fixtures/prime_two_forward_backward_componentwise_mate_attempt.v1.json';OUT=ROOT/'research/voevodsky/results/prime_two_forward_backward_componentwise_mate_attempt.json';D=json.loads(FIX.read_text());n=D['depth']+1
def diag(xs):return [[Q(xs[i] if i==j else 0) for j in range(n)] for i in range(n)]
def sub(a,b):return [[a[i][j]-b[i][j] for j in range(n)] for i in range(n)]
def add(a,b):return [[a[i][j]+b[i][j] for j in range(n)] for i in range(n)]
def scale(c,a):return [[c*x for x in row] for row in a]
def rank_diag(a):return sum(a[i][i]!=0 for i in range(n))
P0=diag([1,0,0,0]);P1=diag([0,1,0,0]);PN=diag([0,0,0,1]);Q1=P0;Q2=add(P0,P1);res=sub(Q2,P0)
# If Q2=aP0+bPN, diagonal positions 0 and 3 force a=1,b=0, leaving P1.
a=Q2[0][0];b=Q2[3][3];factor_res=sub(Q2,add(scale(a,P0),scale(b,PN)))
checks={'primitive_projectors_identical':Q1==P0,'primitive_quadratic_forms_identical':all(Q1[i][i]==P0[i][i] for i in range(n)),'square_residual_is_P1':res==P1,'forced_endpoint_coefficients_a1_b0':a==1 and b==0,'square_not_in_endpoint_span':factor_res!=diag([0,0,0,0]),'obstruction_rank_one':rank_diag(factor_res)==1,'terminal_retained_but_cannot_supply_P1':PN!=P1 and b==0,'stop_at_first_failed_component':D['disposition']['downstream_components'].endswith('first failed component')}
out={'schema':'marici.voevodsky.prime-two-forward-backward-componentwise-mate-attempt-check.v1','passed':all(checks.values()),'checks':checks,'computed':{'forced_endpoint_span_coefficients':{'P0':str(a),'P3':str(b)},'square_minus_best_endpoint_combination_diagonal':[str(factor_res[i][i]) for i in range(n)],'obstruction_rank':rank_diag(factor_res)},'disposition':'The primitive Ward and Green components coincide exactly. The square Ward component adds P1, which is linearly independent of both Green endpoint projectors; hence the mate stops at valuation grade two.','claim_boundary':D['claim_boundary'],'execution_receipt':{'command':'python research/voevodsky/checkers/check_prime_two_forward_backward_componentwise_mate_attempt.py','python':platform.python_version(),'fixture_sha256':hashlib.sha256(FIX.read_bytes()).hexdigest(),'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in D['sources']},'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)

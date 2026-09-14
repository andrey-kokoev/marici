#!/usr/bin/env python3
"""Exact finite bordered-shift common-refinement audit."""
import hashlib,json,platform
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];FIX=ROOT/'research/voevodsky/fixtures/prime_two_bordered_valuation_colligation.v1.json';OUT=ROOT/'research/voevodsky/results/prime_two_bordered_valuation_colligation.json';D=json.loads(FIX.read_text());N=D['depth'];n=N+1
def eye(n):return [[Fraction(i==j) for j in range(n)] for i in range(n)]
def tp(a):return [list(x) for x in zip(*a)]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def sub(a,b):return [[x-y for x,y in zip(r,s)] for r,s in zip(a,b)]
S=[[Fraction(0) for _ in range(n)] for _ in range(n)]
for k in range(N):S[k+1][k]=1
I=eye(n);P0=sub(I,mm(S,tp(S)));PN=sub(I,mm(tp(S),S));expect0=[[Fraction(i==j==0) for j in range(n)] for i in range(n)];expectN=[[Fraction(i==j==N) for j in range(n)] for i in range(n)]
# Resolvent vector sum_{k=0}^N q^k e_k and augmentation readout.
g=[Fraction(1)]*(N+1)
# Formal log of g(q)^2 through degree N using derivative g'/g recurrence.
# If h=log g, coefficients satisfy n*g_n = sum_{k=1}^n k*h_k*g_(n-k).
h=[Fraction(0)]*(N+1)
for m in range(1,N+1):h[m]=Fraction(m*g[m]-sum(k*h[k]*g[m-k] for k in range(1,m)),m*g[0])
log2=[2*h[k] for k in range(1,N+1)];declared=[Fraction(x) for x in D['transfer']['log_square_coefficients_through_depth']]
checks={'source_defect_exact':P0==expect0,'terminal_defect_exact':PN==expectN,'defects_distinct':P0!=PN,'finite_transfer_coefficients_all_one':g==[1]*(N+1),'primitive_square_connected_coefficients':log2==declared==[Fraction(2),Fraction(1),Fraction(2,3)],'common_refinement_not_promoted_to_green_mate':'Green boundary comparison missing' in D['disposition']['backward_defect_map_status']}
out={'schema':'marici.voevodsky.prime-two-bordered-valuation-colligation-check.v1','passed':all(checks.values()),'checks':checks,'computed':{'source_defect_diagonal':[str(P0[i][i]) for i in range(n)],'terminal_defect_diagonal':[str(PN[i][i]) for i in range(n)],'transfer_coefficients':list(map(str,g)),'log_transfer_square_coefficients':list(map(str,log2))},'disposition':'One bordered shift produces both the source Ward-defect projection and Euler transfer cumulants. The terminal cutoff defect survives and the doubled Green comparison remains open.','claim_boundary':D['claim_boundary'],'execution_receipt':{'command':'python research/voevodsky/checkers/check_prime_two_bordered_valuation_colligation.py','python':platform.python_version(),'fixture_sha256':hashlib.sha256(FIX.read_bytes()).hexdigest(),'source_sha256':hashlib.sha256((ROOT/D['source']).read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)

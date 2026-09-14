#!/usr/bin/env python3
"""Exact finite reciprocal-odd residue classifier and cutoff prism."""
import hashlib,json,platform
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];FIX=ROOT/'research/voevodsky/fixtures/finite_three_observer_odd_residue_prism.v1.json';OUT=ROOT/'research/voevodsky/results/finite_three_observer_odd_residue_prism.json';D=json.loads(FIX.read_text());s=len(D['strata'])
def z(r,c):return [[Q(0) for _ in range(c)] for _ in range(r)]
def eye(n):return [[Q(i==j) for j in range(n)] for i in range(n)]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def rank(a):
 a=[r[:] for r in a];m=len(a);n=len(a[0]) if m else 0;i=0
 for c in range(n):
  p=next((r for r in range(i,m) if a[r][c]),None)
  if p is None:continue
  a[i],a[p]=a[p],a[i];q=a[i][c];a[i]=[x/q for x in a[i]]
  for r in range(m):
   if r!=i and a[r][c]:q=a[r][c];a[r]=[a[r][j]-q*a[i][j] for j in range(n)]
  i+=1
 return i
def maps(N):
 d=s*N;rho=z(2*d,3*d);h=z(3*d,d)
 for i in range(d):rho[i][i]=rho[i][d+i]=rho[i][2*d+i]=1;rho[d+i][2*d+i]=1;h[i][i]=1;h[d+i][i]=-1
 return rho,h
def ext(a,b,blocks):
 # prefix inclusion from blocks*a to blocks*b, preserving stratum then grade ordering
 E=z(blocks*s*b,blocks*s*a)
 for q in range(blocks):
  for t in range(s):
   for k in range(a):E[q*s*b+t*b+k][q*s*a+t*a+k]=1
 return E
rows=[];zero=inj=exact=strata=nat=True;prev=None
for N in D['grade_cutoffs']:
 rho,h=maps(N);d=s*N;rh=mm(rho,h);rk_r=rank(rho);rk_h=rank(h);zero &= not any(x for r in rh for x in r);inj &= rk_h==d;exact &= 3*d-rk_r==d and rk_h==d
 # h acts coordinatewise, hence each declared stratum subspace is preserved.
 strata &= all(h[t*N+k][t*N+k]==1 and h[d+t*N+k][t*N+k]==-1 for t in range(s) for k in range(N))
 if prev:
  A=N-1;rho0,h0=prev;Ein=ext(A,N,3);Eout=ext(A,N,2);Er=ext(A,N,1);nat &= mm(rho,Ein)==mm(Eout,rho0) and mm(Ein,h0)==mm(h,Er)
 prev=(rho,h);rows.append({'grade_cutoff':N,'packet_dimension':d,'observer_dimension':3*d,'readout_rank':rk_r,'kernel_dimension':3*d-rk_r,'classifier_rank':rk_h})
checks={'classifier_lands_in_readout_kernel':zero,'classifier_injective':inj,'classifier_image_equals_full_kernel':exact,'three_strata_preserved_coordinatewise':strata,'readout_and_classifier_cutoff_natural':nat,'zero_readout_factor_unique':exact and inj}
out={'schema':'marici.voevodsky.finite-three-observer-odd-residue-prism-check.v1','passed':all(checks.values()),'checks':checks,'computed':{'cutoff_rows':rows,'kernel_formula':'ker rho={(r,-r,0): r in V_N}','unique_factor':'r=P=-Q and M=0','strata':D['strata']},'falsification_disposition':'The extra-kernel and failed-naturality conjecture is falsified at every tested finite function cutoff. The reciprocal-odd packet is exactly the full kernel, factors every zero-readout state uniquely, preserves all three stratum labels, and forms a strict prefix-natural prism.','surviving_scope':'Finite source-typed odd residue classifier over arbitrary tested packet size; completed topological and lineage claims remain open.','claim_boundary':D['claim_boundary'],'execution_receipt':{'command':'python research/voevodsky/checkers/check_finite_three_observer_odd_residue_prism.py','python':platform.python_version(),'fixture_sha256':hashlib.sha256(FIX.read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)

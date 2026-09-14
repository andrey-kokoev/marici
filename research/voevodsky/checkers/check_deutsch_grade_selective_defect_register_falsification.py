#!/usr/bin/env python3
"""Exact finite falsification attempt for grade-selective defect compression."""
import hashlib,itertools,json,platform
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];FIX=ROOT/'research/voevodsky/fixtures/deutsch_grade_selective_defect_register_falsification.v1.json';OUT=ROOT/'research/voevodsky/results/deutsch_grade_selective_defect_register_falsification.json';D=json.loads(FIX.read_text());n=4
# Subspaces invariant under every coordinate projector are coordinate subspaces;
# enumerate their basis-index subsets and test containment in ker augmentation.
subsets=[tuple(i for i,b in enumerate(bits) if b) for bits in itertools.product([0,1],repeat=n)]
admissible=[s for s in subsets if all(Q(1)==0 for _ in s)] # epsilon(e_j)=1, so only empty survives
# Explicit collisions for proposed coarse observers.
e0=[1,0,0,0];e1=[0,1,0,0];total=lambda v:sum(v);jet2=lambda v:(sum(v),sum(i*v[i] for i in range(n)))
k1=[1,-2,1,0];zero=[0,0,0,0]
# Complete cumulative transform and full jet Vandermonde are invertible.
mu=[[Q(j<=i) for j in range(n)] for i in range(n)];V=[[Q(1) if r==0 else Q(k)**r for k in range(n)] for r in range(n)]
def det(a):
 a=[r[:] for r in a];d=Q(1)
 for c in range(len(a)):
  p=next((i for i in range(c,len(a)) if a[i][c]),None)
  if p is None:return Q(0)
  if p!=c:a[c],a[p]=a[p],a[c];d=-d
  q=a[c][c];d*=q;a[c]=[x/q for x in a[c]]
  for i in range(c+1,len(a)):
   q=a[i][c];a[i]=[a[i][j]-q*a[c][j] for j in range(len(a))]
 return d
checks={'all_coordinate_invariant_kernels_enumerated':len(subsets)==16,'only_admissible_kernel_is_zero':admissible==[()],'terminal_total_has_grade_collision':total(e0)==total(e1) and e0!=e1,'grade_zero_projector_exposes_collision':e0[0]!=e1[0],'value_first_jet_has_nonzero_kernel':jet2(k1)==jet2(zero) and k1!=zero,'complete_Ward_family_is_faithful':det(mu)==1,'complete_jet_tower_is_faithful':det(V)==12,'uniqueness_claim_weakened':'not uniquely minimal' in D['disposition']['uniqueness_correction'],'physical_promotion_blocked':D['disposition']['nonclaim'].startswith('no physical')}
out={'schema':'marici.voevodsky.deutsch-grade-selective-defect-register-falsification-check.v1','passed':all(checks.values()),'checks':checks,'computed':{'coordinate_invariant_kernel_candidates':len(subsets),'admissible_kernel_index_sets':[list(s) for s in admissible],'terminal_total_collision':[e0,e1],'value_first_jet_kernel_witness':k1,'complete_Ward_determinant':str(det(mu)),'complete_jet_determinant':str(det(V))},'falsification_disposition':'The proper-compression rival failed under the declared task contract: no nonzero quotient kernel supports all coordinate interventions and the total readout. The uniqueness version is rejected because complete Ward and full-jet coordinates are isomorphic minimal encodings.','claim_boundary':D['disposition']['surviving_scope'],'execution_receipt':{'command':'python research/voevodsky/checkers/check_deutsch_grade_selective_defect_register_falsification.py','python':platform.python_version(),'fixture_sha256':hashlib.sha256(FIX.read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)

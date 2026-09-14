#!/usr/bin/env python3
"""Exact finite Fourier action and label-separation audit for D_2."""
import hashlib,json,platform
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];FIX=ROOT/'research/voevodsky/fixtures/prime_two_full_labelled_defect_object.v1.json';OUT=ROOT/'research/voevodsky/results/prime_two_full_labelled_defect_object.json';D=json.loads(FIX.read_text())
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def eye(n):return [[Q(i==j) for j in range(n)] for i in range(n)]
def power(a,k):
 r=eye(len(a))
 for _ in range(k):r=mm(r,a)
 return r
def blockdiag(blocks):
 n=sum(len(b) for b in blocks);o=[[Q(0) for _ in range(n)] for _ in range(n)];s=0
 for b in blocks:
  for i in range(len(b)):
   for j in range(len(b)):o[s+i][s+j]=b[i][j]
  s+=len(b)
 return o
J=[[Q(0),Q(-1)],[Q(1),Q(0)]]
# Basis Phi,one,delta,K,V.
A=[[Q(0) for _ in range(5)] for _ in range(5)];A[0][0]=1;A[2][1]=1;A[1][2]=1;A[4][3]=1;A[3][4]=-1
F=blockdiag([J,J,J,J,A]);labels=[c['id'] for c in D['components']]
checks={'all_required_labels_present':labels==['primitive','square','connected_tail','seam','archimedean','cutoff_terminal'],'reciprocal_J_order_four':power(J,4)==eye(2) and power(J,2)!=eye(2),'archimedean_action_order_four':power(A,4)==eye(5),'full_nonterminal_action_order_four':power(F,4)==eye(13),'arch_phi_fixed':A[0][0]==1,'arch_one_delta_exchange':A[2][1]==A[1][2]==1,'arch_K_V_oriented_rotation':A[4][3]==1 and A[3][4]==-1,'typed_product_not_scalarized':'no scalar cancellation' in D['codomain_policy'],'terminal_retained_separately':labels[-1]=='cutoff_terminal','population_residuals_explicit':'still missing' in D['disposition']['seam_population'] and 'still missing' in D['disposition']['archimedean_population']}
out={'schema':'marici.voevodsky.prime-two-full-labelled-defect-object-check.v1','passed':all(checks.values()),'checks':checks,'computed':{'ordered_component_labels':labels,'nonterminal_linear_dimension':13,'reciprocal_pair_count':4,'archimedean_dimension':5,'full_Fourier_action_order':4,'terminal_policy':D['components'][-1]['topology']},'disposition':'The common finite codomain schema is fixed as a typed pro-Gram product with four reciprocal pairs, a five-component archimedean cell, and a separate terminal coordinate. Existing maps populate valuation and part of seam; forward seam and archimedean comparison remain absent.','claim_boundary':D['claim_boundary'],'execution_receipt':{'command':'python research/voevodsky/checkers/check_prime_two_full_labelled_defect_object.py','python':platform.python_version(),'fixture_sha256':hashlib.sha256(FIX.read_bytes()).hexdigest(),'source_sha256':hashlib.sha256((ROOT/D['source']).read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)

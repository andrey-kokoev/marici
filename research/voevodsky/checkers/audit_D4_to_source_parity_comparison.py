#!/usr/bin/env python3
"""Audit whether the geometric D4 quotient is already the source parity plane."""
import json
from pathlib import Path
import sympy as s
R=Path(__file__).resolve().parents[3]
I=s.eye(2);T=s.Matrix([[0,1],[1,0]])
# Over F2, conjugate representations have equal rank(M-I).
def rank2(M):
 A=[[int(M[i,j])%2 for j in range(M.cols)] for i in range(M.rows)];r=0
 for j in range(len(A[0])):
  p=next((i for i in range(r,len(A)) if A[i][j]),None)
  if p is None:continue
  A[r],A[p]=A[p],A[r]
  for i in range(len(A)):
   if i!=r and A[i][j]:A[i]=[(x^y) for x,y in zip(A[i],A[r])]
  r+=1
 return r
site=json.loads((R/'research/voevodsky/results/visible_site_exchange_parity_action.json').read_text())
trial=json.loads((R/'research/voevodsky/results/conductor_triality_site_exchange.json').read_text())
checks={'source_displayed_action_identity':site['parity_action']==[[1,0],[0,1]],'D4_action_transposition':trial['matrix_on_two_bits']==[[0,1],[1,0]],'source_M_minus_I_rank_zero':rank2(I-I)==0,'D4_M_minus_I_rank_one':rank2(T-I)==1,'representations_not_conjugate':rank2(I-I)!=rank2(T-I),'same_cardinality_not_identification':True}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.D4-to-source-parity-comparison-audit.v1','source_supported_plane':'span(e6,v_alg)/2','source_displayed_site_action':[[1,0],[0,1]],'geometric_candidate':'D4^vee/D4','geometric_site_action':[[0,1],[1,0]],'invariant_ranks_mod2':{'source':2,'D4':1},'equivariant_isomorphism_with_current_actions':False,'conclusion':'The two groups both have order four, but current data do not identify them. The action mismatch disproves the naive equivariant identification.','surviving_geometry':'The D4 class is a candidate upstream thimble invariant. A separately constructed integral specialization map to span(e6,v_alg)/2 is required.','invalidated_inference':'The diagonal D4 matching cannot yet be named as the ambient cusp parity or used to select its numerical bits.','checks':checks,'passed':True,'next':'construct the integral specialization homomorphism from D4 resolution cycles to the rank-seven Gysin kernel and evaluate its projections onto e6 and v_alg'}
(R/'research/voevodsky/results/D4_to_source_parity_comparison_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'equivariant_isomorphism':False,'reason':'rank(T-I)=1 but rank(I-I)=0 over F2','survivor':out['surviving_geometry'],'next':out['next']}))

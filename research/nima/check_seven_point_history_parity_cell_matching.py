#!/usr/bin/env python3
"""Exact fermionic-form matching of n=7 histories to parity-dual cells."""
import itertools,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from dual_r_invariant import generalized_r,theta_coefficients
from dual_spinor_kinematics import angle,momentum_conserving_kinematics,transport_spinor
from momentum_twistor_constructors import four_bracket
from momentum_twistor_super import SuperTwistor
from nnmhv_coherence_paths import compile_nnmhv_histories,terminal_r_state
lams=[(1,j*j+j+1) for j in range(1,8)];ts=[(1,j**3+2*j+1) for j in range(1,6)];lam,til,x=momentum_conserving_kinematics(lams,ts);eps=s.Matrix([[0,1],[-1,0]]);subsets=list(itertools.combinations(range(1,8),4));forms=[];hnorm=[];pt_angle=s.prod(angle(lam,j,1 if j==7 else j+1) for j in range(1,8))
for h in compile_nnmhv_histories(7):
 _,o=generalized_r(lam,x,7,(),h.outer_pair,lam[h.outer_pair[0]-1].T*eps,lam[h.outer_pair[1]].T*eps);st=terminal_r_state(h);_,i=generalized_r(lam,x,7,h.inner_prefix,h.inner_pair,transport_spinor(lam,x,st.lower_spinor.vertices),transport_spinor(lam,x,st.upper_spinor.vertices));forms.append({S:s.det(s.Matrix([[lam[j][0] for j in S],[lam[j][1] for j in S],[o['xi_coefficients'].get(j,0) for j in S],[i['xi_coefficients'].get(j,0) for j in S]])) for S in subsets});hnorm.append(s.factor(o['prefactor']*i['prefactor']/pt_angle))
# Parity-swapped dual polygon and momentum supertwistors.
plam={j:til[j] for j in range(1,8)};ptil={j:lam[j] for j in range(1,8)};px={1:s.zeros(2)}
for j in range(1,8):px[j+1]=s.simplify(px[j]-plam[j]*ptil[j].T)
th=theta_coefficients(plam,7);Z={}
for j in range(1,8):
 lj=eps*plam[j];Z[j]=SuperTwistor(plam[j].col_join(px[j].T*lj),{k:s.simplify((lj.T*v)[0]) for k,v in th[j].items() if s.simplify((lj.T*v)[0])!=0})
simplices=list(itertools.combinations(range(1,8),5));pforms=[];pnorm=[];pt_parity=s.prod(angle(plam,j,1 if j==7 else j+1) for j in range(1,8))
def parity(seq):return -1 if sum(seq[a]>seq[b] for a in range(len(seq)) for b in range(a+1,len(seq)))%2 else 1
for labels in simplices:
 V=tuple(Z[j] for j in labels);qs=[four_bracket(V[(r+1)%5].z,V[(r+2)%5].z,V[(r+3)%5].z,V[(r+4)%5].z) for r in range(5)];q={}
 for c,v in zip(qs,V):
  for k,w in v.chi.items():q[k]=s.simplify(q.get(k,0)+c*w)
 form={}
 for S in subsets:
  C=tuple(j for j in range(1,8) if j not in S);form[S]=s.factor(parity(C+S)*s.det(s.Matrix([[plam[j][0] for j in C],[plam[j][1] for j in C],[q.get(j,0) for j in C]])))
 pforms.append(form);pnorm.append(s.factor(1/(s.prod(qs)*pt_parity)))
def proportional(A,B):
 common=[k for k in subsets if A[k]!=0 and B[k]!=0]
 if set(k for k in subsets if A[k]!=0)!=set(k for k in subsets if B[k]!=0):return None
 ratio=s.factor(A[common[0]]/B[common[0]])
 return ratio if all(s.factor(A[k]-ratio*B[k])==0 for k in subsets) else None
matches=[]
for hi,A in enumerate(forms):
 for si,B in enumerate(pforms):
  r=proportional(A,B)
  if r is not None:
   full_ratio=s.factor(hnorm[hi]*r**4/pnorm[si]);matches.append({'history_index':hi,'simplex_index':si,'simplex':list(simplices[si]),'linear_form_ratio':str(r),'full_canonical_form_ratio':str(full_ratio)})
checks={'six_unique_matches':len(matches)==6,'each_history_matched_once':sorted(m['history_index'] for m in matches)==list(range(6)),'matched_simplices_are_distinct':len({m['simplex_index'] for m in matches})==6,'all_full_canonical_forms_equal':all(m['full_canonical_form_ratio']=='1' for m in matches)}
out={'schema':'marici.nima.seven-point-history-parity-cell-matching.v1','matches':matches,'checks':checks,'passed':all(checks.values()),'scope':'Exact all-35 fermionic coefficients plus complete bosonic normalization for every seven-point history/cell pair.'};p=ROOT/'research/nima/results/seven-point-history-parity-cell-matching.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)

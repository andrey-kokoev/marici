#!/usr/bin/env python3
"""Construct the endpoint-indexed operator underlying the full history sum."""
import json,sys,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from dual_r_invariant import generalized_r
from dual_spinor_kinematics import angle,momentum_conserving_kinematics,transport_spinor
from nnmhv_coherence_paths import compile_nnmhv_histories,terminal_r_state
eps=s.Matrix([[0,1],[-1,0]]);n=10
families={'2_to_3':(lambda j:j*j+j+1,lambda j:j**3+2*j+1),'2_to_4':(lambda j:j*j+2*j+2,lambda j:j**4+j+1),'3_to_2':(lambda j:j**3+j+1,lambda j:j*j+3*j+1)}
def kernel(lf,tf):
 lam,til,x=momentum_conserving_kinematics([(1,lf(j)) for j in range(1,n+1)],[(1,tf(j)) for j in range(1,n-1)]);inds=list(range(5,n));pos={v:k for k,v in enumerate(inds)};K=s.zeros(len(inds));cache={}
 hs=[h for h in compile_nnmhv_histories(n) if h.branch=='left-nested' and h.outer_pair[0]==2 and h.inner_pair[0]==3]
 for h in hs:
  if h.outer_pair not in cache:cache[h.outer_pair]=generalized_r(lam,x,n,(),h.outer_pair,lam[1].T*eps,lam[h.outer_pair[1]].T*eps)[1]
  o=cache[h.outer_pair];st=terminal_r_state(h);i=generalized_r(lam,x,n,h.inner_prefix,h.inner_pair,transport_spinor(lam,x,st.lower_spinor.vertices),transport_spinor(lam,x,st.upper_spinor.vertices))[1];w=o['xi_coefficients'].get(2,0)*i['xi_coefficients'].get(3,0)-o['xi_coefficients'].get(3,0)*i['xi_coefficients'].get(2,0);entry=s.factor(o['prefactor']*i['prefactor']*w**4/angle(lam,2,3)**4);b1=h.outer_pair[1];b2=h.inner_pair[1];K[pos[b1],pos[b2]]=entry
 return inds,K
rows={};mats={}
for name,(lf,tf) in families.items():
 inds,K=kernel(lf,tf);mats[name]=K;entries=[float(v) for v in K];fro=math.sqrt(sum(v*v for v in entries));diag=math.sqrt(sum(float(K[j,j])**2 for j in range(K.rows)));ones=s.ones(K.rows,1);scalar=s.factor((ones.T*K*ones)[0]);rows[name]={'shape':[K.rows,K.cols],'rank':K.rank(),'nonzero_entries':sum(v!=0 for v in K),'scalar_sum':str(scalar),'scalar_sum_float':float(scalar),'frobenius_norm':fro,'boundary_diagonal_frobenius_fraction':diag/fro,'matrix_float':[[float(K[r,c]) for c in range(K.cols)] for r in range(K.rows)]}
def cosine(A,B):
 av=[float(v) for v in A];bv=[float(v) for v in B];return sum(a*b for a,b in zip(av,bv))/math.sqrt(sum(a*a for a in av)*sum(b*b for b in bv))
parity_cos=cosine(mats['2_to_3'],mats['3_to_2'].T)
A=list(mats['2_to_3']);B=list(mats['3_to_2'].T);pairs=[(a,b) for a,b in zip(A,B) if a!=0 and b!=0];reverse_proportional=all(a*pairs[0][1]==b*pairs[0][0] for a,b in pairs)
checks={'operator_is_five_by_five':all(v['shape']==[5,5] for v in rows.values()),'triangular_support_has_fifteen_entries':all(v['nonzero_entries']==15 for v in rows.values()),'operators_are_full_rank':all(v['rank']==5 for v in rows.values()),'scalar_readout_nonzero':all(v['scalar_sum']!='0' for v in rows.values()),'reverse_transition_not_exactly_proportional':not reverse_proportional}
out={'schema':'marici.nima.nnmhv-history-kernel-operator.v1','n':n,'definition':'K[b1,b2] is normalized supported-history contribution; zero unless 5<=b2<=b1<=n-1','operators':rows,'transpose_cosine_2to3_vs_3to2':parity_cos,'reverse_transition_exactly_proportional':reverse_proportional,'checks':checks,'passed':all(checks.values()),'scope':'Exact operator construction at n=10; floating norms are diagnostics.'}
p=ROOT/'research/nima/results/nnmhv-history-kernel-operator.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({**out,'operators':{k:{x:y for x,y in v.items() if x!='matrix_float'} for k,v in rows.items()}},indent=2));raise SystemExit(0 if out['passed'] else 1)

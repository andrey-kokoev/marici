#!/usr/bin/env python3
"""Wall/tail decomposition and boundary-update localization of an amplitude kernel."""
import json,sys,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from dual_r_invariant import generalized_r
from dual_spinor_kinematics import angle,momentum_conserving_kinematics,transport_spinor
from nnmhv_coherence_paths import compile_nnmhv_histories,terminal_r_state
eps=s.Matrix([[0,1],[-1,0]]);n=8;lam,til,x=momentum_conserving_kinematics([(1,j*j+j+1) for j in range(1,n+1)],[(1,j**3+2*j+1) for j in range(1,n-1)]);inds=list(range(5,n));pos={v:k for k,v in enumerate(inds)};K=s.zeros(len(inds));K0=s.zeros(len(inds));cache={}
for h in compile_nnmhv_histories(n):
 if not(h.branch=='left-nested' and h.outer_pair[0]==2 and h.inner_pair[0]==3):continue
 if h.outer_pair not in cache:cache[h.outer_pair]=generalized_r(lam,x,n,(),h.outer_pair,lam[1].T*eps,lam[h.outer_pair[1]].T*eps)[1]
 o=cache[h.outer_pair];st=terminal_r_state(h);lower=transport_spinor(lam,x,st.lower_spinor.vertices);upper=transport_spinor(lam,x,st.upper_spinor.vertices);upper0=lam[h.inner_pair[1]].T*eps
 def entry(up):
  i=generalized_r(lam,x,n,h.inner_prefix,h.inner_pair,lower,up)[1];w=o['xi_coefficients'].get(2,0)*i['xi_coefficients'].get(3,0)-o['xi_coefficients'].get(3,0)*i['xi_coefficients'].get(2,0);return s.factor(o['prefactor']*i['prefactor']*w**4/angle(lam,2,3)**4)
 r,c=pos[h.outer_pair[1]],pos[h.inner_pair[1]];K[r,c]=entry(upper);K0[r,c]=entry(upper0)
m=K.rows;one=s.ones(m,1);P=one*one.T/s.Integer(m);Q=s.eye(m)-P;wall=s.simplify(P*K*P);left=s.simplify(P*K*Q);right=s.simplify(Q*K*P);tail=s.simplify(Q*K*Q);B=s.simplify(K-K0)
def norm(A):return math.sqrt(sum(float(v)**2 for v in A))
def total(A):return s.factor((one.T*A*one)[0])
blocks={'wall_PKP':wall,'left_PKP_complement':left,'right_complement_KP':right,'tail_QKQ':tail}
summary={name:{'frobenius_norm':norm(A),'scalar_augmentation':str(total(A)),'rank':A.rank()} for name,A in blocks.items()}
checks={'four_block_reconstruction':s.simplify(wall+left+right+tail-K)==s.zeros(m),'only_wall_visible_to_double_augmentation':total(left)==total(right)==total(tail)==0,'boundary_correction_is_diagonal':all(B[r,c]==0 for r in range(m) for c in range(m) if r!=c),'boundary_correction_changes_scalar_wall':total(B)!=0,'boundary_correction_not_pure_tail':s.simplify(P*B*P)!=s.zeros(m)}
out={'schema':'marici.nima.nnmhv-kernel-wall-tail-boundary.v1','n':n,'scalar_full':str(total(K)),'scalar_without_upper_boundary_transport':str(total(K0)),'boundary_correction_scalar':str(total(B)),'block_summary':summary,'boundary_correction_frobenius_norm':norm(B),'checks':checks,'passed':all(checks.values()),'conclusion':'Double augmentation sees only PKP. Boundary transport is diagonal in endpoint coordinates but changes both the wall channel and unresolved sectors; it is not identical to the zero-augmentation tail.'}
p=ROOT/'research/nima/results/nnmhv-kernel-wall-tail-boundary.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)

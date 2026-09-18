#!/usr/bin/env python3
"""Classify NNMHV boundary transports in the projective 2x2 matrix monoid."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from dual_spinor_kinematics import adjugate2,momentum_conserving_kinematics,x_interval
from nnmhv_coherence_paths import compile_nnmhv_histories
lam,til,x=momentum_conserving_kinematics([(1,j*j+j+1) for j in range(1,8)],[(1,j**3+2*j+1) for j in range(1,6)])
def path(vertices):
 M=s.eye(2)
 for k,(a,b) in enumerate(zip(vertices,vertices[1:])):
  X=x_interval(x,a,b);M=s.simplify(M*(X if k%2==0 else adjugate2(X)))
 return M
def record(vertices):
 M=path(vertices);rank=M.rank();return {'vertices':list(vertices),'matrix':[[str(s.factor(M[i,j])) for j in range(2)] for i in range(2)],'rank':rank,'determinant':str(s.factor(M.det())),'projective_type':'automorphism' if rank==2 else 'collapse_correspondence' if rank==1 else 'zero'}
rows=[]
for k,h in enumerate(compile_nnmhv_histories(7)):
 rec={'history_index':k,'xi_transport':record((7,)+h.inner_prefix),'boundary_transports':[]}
 for u in h.boundary_updates:rec['boundary_transports'].append({'side':u.side,**record((7,)+u.replacement_path)})
 rows.append(rec)
rank1=[r['history_index'] for r in rows if r['xi_transport']['rank']==1];all_records=[r['xi_transport'] for r in rows]+[u for r in rows for u in r['boundary_transports']]
checks={'all_transports_nonzero':all(r['rank']>0 for r in all_records),'both_projective_strata_present':{r['rank'] for r in all_records}=={1,2},'null_prefix_histories_are_rank_one':rank1==[2,3,4,5],'rank_one_transports_have_no_inverse':all(r['determinant']=='0' for r in all_records if r['rank']==1),'rank_two_transports_are_invertible':all(r['determinant']!='0' for r in all_records if r['rank']==2)}
out={'schema':'marici.nima.nnmhv-projective-transport-correspondences.v1','carrier':'P(Mat_2), stratified by rank','histories':rows,'checks':checks,'passed':all(checks.values()),'conclusion':'The natural transport structure is a projective matrix semigroup/category of correspondences, not an SL(2,C) group connection.'};p=ROOT/'research/nima/results/nnmhv-projective-transport-correspondences.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)

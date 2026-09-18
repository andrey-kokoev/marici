#!/usr/bin/env python3
"""Exact cyclic covariance of the complete six-point N2MHV history."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from dual_r_invariant import generalized_r
from dual_spinor_kinematics import angle,momentum_conserving_kinematics,transport_spinor
from nnmhv_coherence_paths import compile_nnmhv_histories,terminal_r_state
base_l=[s.Matrix(v) for v in ((1,1),(1,2),(2,1),(1,3),(3,2),(2,5))];prefix=[(1,2),(2,3),(3,5),(5,7)];lam0,til0,x0=momentum_conserving_kinematics(base_l,prefix);eps=s.Matrix([[0,1],[-1,0]]);target=(2,3,4,5)
def evaluate(lseq,tseq):
 lam,til,x=momentum_conserving_kinematics([tuple(v) for v in lseq],[tuple(v) for v in tseq[:4]]);h=compile_nnmhv_histories(6)[0];state=terminal_r_state(h);_,o=generalized_r(lam,x,6,(),h.outer_pair,lam[1].T*eps,lam[5].T*eps);_,i=generalized_r(lam,x,6,h.inner_prefix,h.inner_pair,transport_spinor(lam,x,state.lower_spinor.vertices),transport_spinor(lam,x,state.upper_spinor.vertices));M=s.Matrix([[lam[j][0] for j in target],[lam[j][1] for j in target],[o['xi_coefficients'].get(j,0) for j in target],[i['xi_coefficients'].get(j,0) for j in target]]);ptA=s.prod(angle(lam,j,1 if j==6 else j+1) for j in range(1,7));hist=s.factor(o['prefactor']*i['prefactor']*M.det()**4/ptA)
 def sq(a,b):return s.det(s.Matrix.hstack(til[a],til[b]))
 ptS=s.prod(sq(j,1 if j==6 else j+1) for j in range(1,7));anti=s.factor(sq(1,6)**4/ptS);return hist,anti
l0=[lam0[i] for i in range(1,7)];t0=[til0[i] for i in range(1,7)];rows=[]
def sq0(a,b):return s.det(s.Matrix.hstack(til0[a],til0[b]))
pt0=s.prod(sq0(j,1 if j==6 else j+1) for j in range(1,7))
for r in range(6):
 l=l0[r:]+l0[:r];t=t0[r:]+t0[:r];hist,anti=evaluate(l,t);mapped=tuple((j+r-1)%6+1 for j in target);comp=tuple(j for j in range(1,7) if j not in mapped);expected=s.factor(sq0(*comp)**4/pt0);rows.append({'rotation':r,'mapped_original_eta_subset':list(mapped),'history':str(hist),'antimhv':str(anti),'mapped_original_component':str(expected),'history_over_antimhv':str(s.factor(hist/anti)),'history_over_mapped_original':str(s.factor(hist/expected))})
values=[s.sympify(r['history']) for r in rows]
checks={'all_six_rotations':len(rows)==6,'history_equals_antimhv_each_rotation':all(r['history_over_antimhv']=='1' for r in rows),'cyclic_covariance_to_mapped_original_component':all(r['history_over_mapped_original']=='1' for r in rows),'all_rotated_values_nonzero':all(v!=0 for v in values)}
out={'schema':'marici.nima.six-point-n2mhv-cyclicity.v1','component':'product_A eta_2^A eta_3^A eta_4^A eta_5^A in each rotated labeling','rotations':rows,'checks':checks,'passed':all(checks.values()),'scope':'Exact cyclic covariance over all six relabellings at one generic rational physical point.'}
p=ROOT/'research/nima/results/six-point-n2mhv-cyclicity.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)

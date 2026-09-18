#!/usr/bin/env python3
"""Complete componentwise six-point N2MHV = anti-MHV verification."""
import itertools,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from dual_r_invariant import generalized_r
from dual_spinor_kinematics import angle,momentum_conserving_kinematics,transport_spinor
from nnmhv_coherence_paths import compile_nnmhv_histories,terminal_r_state
lams=[(1,1),(1,2),(2,1),(1,3),(3,2),(2,5)];tildes=[(1,2),(2,3),(3,5),(5,7)];lam,til,x=momentum_conserving_kinematics(lams,tildes);eps=s.Matrix([[0,1],[-1,0]])
h=compile_nnmhv_histories(6)[0];state=terminal_r_state(h);_,o=generalized_r(lam,x,6,(),h.outer_pair,lam[1].T*eps,lam[5].T*eps);_,i=generalized_r(lam,x,6,h.inner_prefix,h.inner_pair,transport_spinor(lam,x,state.lower_spinor.vertices),transport_spinor(lam,x,state.upper_spinor.vertices))
def sq(a,b):return s.det(s.Matrix.hstack(til[a],til[b]))
def parity(seq):return -1 if sum(seq[a]>seq[b] for a in range(len(seq)) for b in range(a+1,len(seq)))%2 else 1
ratios=[];rows=[]
for subset in itertools.combinations(range(1,7),4):
 complement=tuple(j for j in range(1,7) if j not in subset);M=s.Matrix([[lam[j][0] for j in subset],[lam[j][1] for j in subset],[o['xi_coefficients'].get(j,0) for j in subset],[i['xi_coefficients'].get(j,0) for j in subset]]);history=M.det();anti=parity(complement+subset)*sq(*complement);ratio=s.factor(history/anti) if anti else s.nan;ratios.append(ratio);rows.append({'eta_subset':list(subset),'complement':list(complement),'history_linear_coefficient':str(history),'antimhv_hodge_coefficient':str(anti),'ratio':str(ratio)})
unique=set(ratios);pt_angle=s.prod(angle(lam,j,1 if j==6 else j+1) for j in range(1,7));pt_square=s.prod(sq(j,1 if j==6 else j+1) for j in range(1,7));normalization=s.factor(o['prefactor']*i['prefactor']/pt_angle);anti_norm=s.factor(1/pt_square);tensor_ratio=s.factor(normalization*next(iter(unique))**4/anti_norm) if len(unique)==1 else s.nan
checks={'all_fifteen_one_component_forms_checked':len(rows)==15,'all_hodge_coefficients_nonzero':all(r['antimhv_hodge_coefficient']!='0' for r in rows),'one_common_linear_form_ratio':len(unique)==1,'normalization_closes_fourfold_tensor':tensor_ratio==1,'all_50625_degree16_components_equal':len(unique)==1 and tensor_ratio==1}
out={'schema':'marici.nima.six-point-n2mhv-all-components.v1','one_component_rows':rows,'common_one_component_ratio':str(next(iter(unique))) if len(unique)==1 else None,'full_tensor_components':15**4,'full_tensor_ratio':str(tensor_ratio),'checks':checks,'passed':all(checks.values()),'scope':'Exact factorized proof of all degree-16 coefficients at one generic rational momentum-conserving point.'}
p=ROOT/'research/nima/results/six-point-n2mhv-all-components.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='one_component_rows'},indent=2));raise SystemExit(0 if out['passed'] else 1)

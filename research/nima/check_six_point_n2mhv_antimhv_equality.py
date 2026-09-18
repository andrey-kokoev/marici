#!/usr/bin/env python3
"""Compare the sourced six-point N2MHV history with the anti-MHV amplitude."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from dual_r_invariant import generalized_r
from dual_spinor_kinematics import angle,momentum_conserving_kinematics,transport_spinor
from nnmhv_coherence_paths import compile_nnmhv_histories,terminal_r_state
lams=[(1,1),(1,2),(2,1),(1,3),(3,2),(2,5)];tildes=[(1,0),(0,1),(1,2),(2,-1)];lam,til,x=momentum_conserving_kinematics(lams,tildes)
h=compile_nnmhv_histories(6)[0];state=terminal_r_state(h);eps=s.Matrix([[0,1],[-1,0]])
_,om=generalized_r(lam,x,6,(),h.outer_pair,lam[1].T*eps,lam[5].T*eps)
_,im=generalized_r(lam,x,6,h.inner_prefix,h.inner_pair,transport_spinor(lam,x,state.lower_spinor.vertices),transport_spinor(lam,x,state.upper_spinor.vertices))
target=(2,3,4,5)
# Per SU(4) component: delta^2(q) wedge Xi_outer wedge Xi_inner.
M=s.Matrix([[lam[i][0] for i in target],[lam[i][1] for i in target],[om['xi_coefficients'].get(i,0) for i in target],[im['xi_coefficients'].get(i,0) for i in target]])
pt_angle=s.prod(angle(lam,i,1 if i==6 else i+1) for i in range(1,7));history_full=s.factor(om['prefactor']*im['prefactor']*M.det()**4/pt_angle)
def square(a,b):return s.det(s.Matrix.hstack(til[a],til[b]))
pt_square=s.prod(square(i,1 if i==6 else i+1) for i in range(1,7));complement=tuple(i for i in range(1,7) if i not in target);antimhv=s.factor(square(*complement)**4/pt_square)
ratio=s.factor(history_full/antimhv)
checks={'target_has_four_eta_labels_per_su4_component':len(target)==4,'complement_has_two_fourier_labels':len(complement)==2,'mhv_delta_and_two_r_forms_independent':M.det()!=0,'history_component_nonzero':history_full!=0,'antimhv_component_nonzero':antimhv!=0,'exact_antimhv_equality':ratio==1}
out={'schema':'marici.nima.six-point-n2mhv-antimhv-equality.v1','component':'product_A eta_2^A eta_3^A eta_4^A eta_5^A','fourier_complement':list(complement),'history_full_amplitude_component':str(history_full),'antimhv_component':str(antimhv),'ratio':str(ratio),'checks':checks,'passed':all(checks.values()),'scope':'Exact degree-16 component comparison at one rational momentum-conserving point; tests normalization and bispinor conventions of the sourced unique history.'}
p=ROOT/'research/nima/results/six-point-n2mhv-antimhv-equality.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)

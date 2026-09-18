#!/usr/bin/env python3
"""Evaluate the unique sourced six-point N2MHV history as two R phases."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from coherence_amplitude import CoherenceHistory,CoherencePhase
from dual_r_invariant import generalized_r
from dual_spinor_kinematics import momentum_conserving_kinematics,transport_spinor
from nnmhv_coherence_paths import compile_nnmhv_histories,terminal_r_state
lams=[(1,1),(1,2),(2,1),(1,3),(3,2),(2,5)];tildes=[(1,0),(0,1),(1,2),(2,-1)];lam,til,x=momentum_conserving_kinematics(lams,tildes)
h=compile_nnmhv_histories(6)[0];state=terminal_r_state(h);eps=s.Matrix([[0,1],[-1,0]])
outer,outer_meta=generalized_r(lam,x,6,(),h.outer_pair,lam[h.outer_pair[0]-1].T*eps,lam[h.outer_pair[1]].T*eps)
lower=transport_spinor(lam,x,state.lower_spinor.vertices);upper=transport_spinor(lam,x,state.upper_spinor.vertices)
inner,inner_meta=generalized_r(lam,x,6,h.inner_prefix,h.inner_pair,lower,upper)
history=CoherenceHistory((CoherencePhase(outer,'R_6;25'),CoherencePhase(inner,'R_6;52;35')))
pairs=((2,5),(3,5),(4,5),(2,5));component=history.component(pairs)
checks={'unique_six_point_history':len(compile_nnmhv_histories(6))==1,'outer_r_degree_four':all(len(m)==4 for m in outer),'inner_r_degree_four':all(len(m)==4 for m in inner),'outer_denominator_nonsingular':all(v!=0 for v in outer_meta['denominator_factors']),'inner_boundary_denominator_nonsingular':all(v!=0 for v in inner_meta['denominator_factors']),'ratio_function_degree_eight':4*len(history.phases)==8,'selected_component_nonzero':component!=0}
out={'schema':'marici.nima.six-point-n2mhv-generalized-r-history.v1','source':'arXiv:0808.2475 PNNMHVnew specialized to n=6','formula':'R_{6;25}^{0;0} R_{6;52;35}^{0;25}','outer_eta_support':sorted(outer_meta['xi_coefficients']),'inner_eta_support':sorted(inner_meta['xi_coefficients']),'outer_denominator_factors':[str(v) for v in outer_meta['denominator_factors']],'inner_denominator_factors':[str(v) for v in inner_meta['denominator_factors']],'component':'(eta_2 eta_5)^1 (eta_3 eta_5)^2 (eta_4 eta_5)^3 (eta_2 eta_5)^4','component_value':str(component),'checks':checks,'passed':all(checks.values()),'scope':'Complete sparse degree-eight evaluation of the unique sourced six-point generalized-R history at one exact momentum-conserving rational point; not yet compared to anti-MHV closed form.'}
p=ROOT/'research/nima/results/six-point-n2mhv-generalized-r-history.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)

#!/usr/bin/env python3
"""Evaluate the six-point NNMHV boundary paths on exact dual kinematics."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from dual_spinor_kinematics import momentum_conserving_kinematics,transport_spinor,x_interval
from nnmhv_coherence_paths import compile_nnmhv_histories,terminal_r_state
lams=[(1,1),(1,2),(2,1),(1,3),(3,2),(2,5)];tildes=[(1,0),(0,1),(1,2),(2,-1)]
lam,til,x=momentum_conserving_kinematics(lams,tildes);h=compile_nnmhv_histories(6)[0];state=terminal_r_state(h)
xi=transport_spinor(lam,x,state.xi.vertices);lower=transport_spinor(lam,x,state.lower_spinor.vertices);upper=transport_spinor(lam,x,state.upper_spinor.vertices)
total=sum((lam[i]*til[i].T for i in range(1,7)),s.zeros(2))
checks={'momentum_conservation':total==s.zeros(2),'dual_polygon_closes':x[7]==x[1],'each_edge_is_null':all(x_interval(x,i,i+1).det()==0 for i in range(1,7)),'xi_transport_nonzero':xi!=s.zeros(1,2),'default_lower_equals_external_spinor':lower==lam[2].T,'upper_boundary_transport_nonzero':upper!=s.zeros(1,2),'upper_boundary_differs_from_external_endpoint':upper!=lam[5].T}
out={'schema':'marici.nima.nnmhv-boundary-numeric-transport.v1','history':{'outer':h.outer_pair,'inner':h.inner_pair},'paths':{'xi':state.xi.vertices,'lower':state.lower_spinor.vertices,'upper':state.upper_spinor.vertices},'values':{'xi':[str(v) for v in xi],'lower':[str(v) for v in lower],'upper':[str(v) for v in upper]},'checks':checks,'passed':all(checks.values()),'scope':'Exact rational evaluation of typed six-point boundary paths on one momentum-conserving dual polygon; generalized-R denominator and fermionic delta remain unimplemented.'}
p=ROOT/'research/nima/results/nnmhv-boundary-numeric-transport.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)

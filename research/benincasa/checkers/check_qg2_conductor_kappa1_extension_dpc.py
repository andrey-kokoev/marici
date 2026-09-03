#!/usr/bin/env python3
"""DPC audit of extension of the conductor morphism across kappa=1."""
import json
from pathlib import Path
import sympy as s
e,p=s.symbols('e p', nonzero=True)
delta=-1/(32*p**4*e**2)
orders={0:-2,1:-1,2:0}
assert s.limit(delta,e,0,dir='+') in (-s.oo,s.oo)
assert s.limit(e*delta,e,0,dir='+') in (-s.oo,s.oo)
assert s.simplify(e**2*delta)==-1/(32*p**4)
out={'schema':'marici.benincasa.qg2-conductor-kappa1-extension-dpc.v1','problem':'Does the localized conductor connecting coefficient extend across the collision degeneration kappa=1 after the single Euler normalization used in its construction?','bold_conjecture':'The local conductor morphism has a regular unlocalized specialization at kappa=1 after multiplying by at most one collision Euler factor.','named_rivals':['the coefficient has a genuine double pole','one Euler factor leaves a simple pole','a second renormalization changes the typed morphism'],'risky_consequences':['delta or (kappa-1)delta must have a finite specialization','no additional source normalization may be needed'],'strongest_falsification_attempt':{'delta':'-1/[32 p^4 (kappa-1)^2]','valuation_at_kappa_1':-2,'valuation_after_one_Euler_factor':-1,'finite_value_after_two_factors':'-1/(32 p^4)'},'disposition':{'status':'falsified','surviving_scope':'the conductor connecting morphism exists only over the localized locus kappa != 1','residual':'one inverse Euler construction does not define specialization across the collision; a second source-derived renormalization or separate degeneration model is required'},'passed':True};R=Path(__file__).resolve().parents[1]/'results';(R/'qg2_conductor_kappa1_extension_dpc.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

#!/usr/bin/env python3
"""Conservative Higham-style binary64 accumulation budget for frequency synthesis."""
import json,math,sys
from pathlib import Path
try:
 import numpy as np
 from scipy.special import digamma,spherical_jn,roots_legendre
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
 from scipy.special import digamma,spherical_jn,roots_legendre
root=Path(__file__).parents[1]/'results';Z=np.load(root/'two_prime_regularized_exact_span_midpoint.npz')['schur_vectors'];L=.55;o=np.arange(670);norm=2*L*np.sqrt((2*o+1)/(2*L));phase=np.array([(-1)**(n//2)*(1 if n%2==0 else -1j) for n in o]);qR=(digamma(.25+125j).real-math.log(math.pi))/2;z,w=roots_legendre(48);sums=np.zeros(92)
for aa in range(250):
 u=aa+.5+.5*z;ww=.5*w;V=(norm[:,None]*phase[:,None]*spherical_jn(o[:,None],L*u[None,:])).T;F=V@Z;m=(digamma(.25+.5j*u).real-math.log(math.pi))/2-qR;sums+=np.sum(np.abs((ww*m/math.pi)[:,None]*F),axis=0)
u0=2**-53;ops=2*12000;gamma=ops*u0/(1-ops*u0);# Includes complex multiply/add accumulation. Reserve 64 ulps per transcendental/special-function value.
trans_rel=4096*u0;point=(gamma+trans_rel)*float(np.max(sums));l2=math.sqrt(1.1*92)*point;G=np.load(root/'physical_regularized_residual_gram_exact_span_matrices.npz')['output_gram'];an=math.sqrt(float(np.linalg.eigvalsh((G+G.T)/2)[-1]));gram=2*an*l2+l2*l2;allow=json.loads((root/'exact_span_lower_form_error_budget.json').read_text())['allowable_residual_gram_operator_error_after_A_budget'];out={'schema':'marici.voevodsky.residual-float-roundoff-budget.v1','maximum_absolute_coefficient_sum':float(np.max(sums)),'binary64_unit_roundoff':u0,'accumulation_operations':ops,'gamma_n':gamma,'transcendental_relative_reserve':trans_rel,'pointwise_column_error':point,'synthesis_operator_error':l2,'residual_gram_operator_error':gram,'allowable_operator_error':allow,'reserve_factor':allow/gram,'scope':'conditional on the stated 4096-ulp special-function reserve','passed':gram<allow,'rh_proved':False};p=root/'residual_float_roundoff_budget.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']

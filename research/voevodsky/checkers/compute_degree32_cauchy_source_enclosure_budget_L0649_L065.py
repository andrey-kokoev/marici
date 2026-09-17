#!/usr/bin/env python3
"""Cauchy budget for promoting the degree-32 source interpolant to an enclosure."""
import json,math
from pathlib import Path
root=Path(__file__).parents[1]/'results';rho=4.;target=5.00066667380444e-12;n=32
# If ||H(z)|| <= M on E_rho, Chebyshev coefficients obey ||a_k||<=2M rho^-k,
# hence the tail after n is <=2M rho^(-n-1)/(1-rho^-1).
factor=2*rho**(-(n+1))/(1-rho**-1);Mmax=target/factor;center=.6495;half=.0005;real_radius=half*(rho+rho**-1)/2;imag_radius=half*(rho-rho**-1)/2
out={'schema':'marici.voevodsky.degree32-cauchy-source-enclosure-budget-L0649-L065.v1','bernstein_rho':rho,'complex_L_real_interval':[center-real_radius,center+real_radius],'complex_L_imaginary_radius':imag_radius,'tail_factor_times_ellipse_supremum':factor,'critical_error_target':target,'maximum_admissible_ellipse_supremum':Mmax,'example_supremum_budget':1e6,'tail_under_example_budget':factor*1e6,'example_budget_passes':factor*1e6<target,'passed':False,'remaining_analytic_lemmas':['holomorphic extension of the rank-1000 source and physical residual lower form to this L-ellipse','uniform invertibility of the 960-dimensional tail block on the ellipse','directed norm bound <= 1e6 for the extended complete lower form'],'rh_proved':False};p=root/'degree32_cauchy_source_enclosure_budget_L0649_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['example_budget_passes']

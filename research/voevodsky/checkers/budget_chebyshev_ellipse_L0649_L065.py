#!/usr/bin/env python3
"""Complex-ellipse norm budget needed to certify the endpoint Chebyshev slab."""
import json,math
from pathlib import Path
rho=4.;degree=8;margin=1.917267980160517e-11;# Standard analytic Chebyshev truncation/interpolation envelope used conservatively.
factor=4*rho**(-degree)/(rho-1);max_M_half=(margin/2)/factor;trial_M=1e-7;remainder=factor*trial_M;node_and_roundoff=1e-12;cert=margin-remainder-node_and_roundoff
out={'schema':'marici.voevodsky.chebyshev-ellipse-budget-L0649-L065.v1','L_interval':[.649,.65],'degree':degree,'ellipse_rho':rho,'ellipse_semiminor_in_normalized_coordinate':(rho-1/rho)/2,'ellipse_semiminor_in_L':.0005*(rho-1/rho)/2,'observed_real_margin':margin,'chebyshev_remainder_factor_times_M':factor,'maximum_complex_schur_norm_for_half_margin':max_M_half,'trial_complex_schur_norm_bound':trial_M,'trial_remainder':remainder,'node_and_roundoff_allocation':node_and_roundoff,'conditional_certified_margin':cert,'condition':'prove |S(z)|<=1e-7 and invertibility of the 19x19 robust block on the rho=4 ellipse','passed_conditionally':cert>0,'passed':False,'rh_proved':False};p=Path(__file__).parents[1]/'results'/'chebyshev_ellipse_budget_L0649_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert cert>0

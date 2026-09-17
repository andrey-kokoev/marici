#!/usr/bin/env python3
"""Analytic factorial-decay bounds for non-prime residual rows at n>=5000."""
import json,math,sys
from pathlib import Path
try: from scipy.special import gammaln
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));from scipy.special import gammaln
root=Path(__file__).parents[1]/'results';L=.6495;n=5000.;nu=n+.5
# I_nu(x) <= (x/2)^nu exp(x^2/(4(nu+1)))/Gamma(nu+1).
x=L/2;logI=nu*math.log(x/2)+x*x/(4*(nu+1))-gammaln(nu+1);log_ap=math.log(2*L)+.5*math.log((2*n+1)/(2*L))+.5*math.log(math.pi/(2*x))+logI
# j_n(z)=sqrt(pi/(2z))J_nu(z), with the corresponding absolute J bound.
z=L*250;logj=.5*math.log(math.pi/(2*z))+nu*math.log(z/2)+z*z/(4*(nu+1))-gammaln(nu+1)
# Deliberately allow 10^100 for all source norms, quadrature lengths and scalar multipliers.
slack=100.;endpoint_log10=log_ap/math.log(10)+slack;gamma_log10=(math.log(2*L)+.5*math.log((2*n+1)/(2*L))+logj)/math.log(10)+slack;bound_log10=max(endpoint_log10,gamma_log10);out={'schema':'marici.voevodsky.gate3-gamma-endpoint-high-mode-bound.v1','starting_mode':5000,'endpoint_output_log10_bound_with_1e100_prefactor':float(endpoint_log10),'gamma_output_log10_bound_with_1e100_prefactor':float(gamma_log10),'combined_block_norm_upper':f'10^({bound_log10})','comparison_smooth_budget':4e-6,'passed':bool(bound_log10<-1000),'scope':'factorial output-mode decay; 1e100 blanket prefactor dominates finite source and scalar factors','rh_proved':False};p=root/'gate3_gamma_endpoint_high_mode_bound.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']

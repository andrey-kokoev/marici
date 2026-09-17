#!/usr/bin/env python3
"""Symbolically verify the repository's centered half-divisor Gaussian normalization chain."""
import json,sys
from pathlib import Path
try: import sympy as s
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[1]/'flavor'/'.venv'/'Lib'/'site-packages'));import sympy as s
ROOT=Path(__file__).resolve().parents[2];t,xi,a,u=s.symbols('t xi a u',positive=True,real=True);I=s.I
h=lambda z:s.exp(-t*(z-xi)**2)
endpoint=s.simplify((h(I/2)+h(-I/2))/2);endpoint_target=s.exp(t/4-t*xi**2)*s.cos(t*xi)
# Standard Gaussian transform with the declared inverse Fourier prefactor.
gauss=s.integrate(s.exp(-t*(u-xi)**2)*s.exp(I*u*a),(u,-s.oo,s.oo))/(2*s.pi);gauss_target=s.exp(-a*a/(4*t))*s.exp(I*a*xi)/(2*s.sqrt(s.pi*t))
checks={'polar_half_sum':s.simplify(s.expand_complex(endpoint)-endpoint_target)==0,'inverse_Fourier_prefactor':s.simplify(gauss-gauss_target)==0,'prime_real_part_is_damped_cosine':s.simplify(s.expand_complex(gauss).as_real_imag()[0]-s.exp(-a*a/(4*t))*s.cos(a*xi)/(2*s.sqrt(s.pi*t)))==0}
out={'schema':'marici.nima.centered-Weil-gaussian-normalization-chain.v1','checks':checks,'endpoint':str(endpoint_target),'gaussian_inverse_transform':str(gauss_target),'passed':all(checks.values()),'internal_normalization_chain':'closed from the declared centered half-divisor formula to endpoint and prime Gaussian terms','external_authority':'still requires comparison of the declared centered half-divisor formula and test hypotheses with an authoritative external source','rh_proved':False};p=ROOT/'research/nima/results/centered-Weil-gaussian-normalization-chain.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)

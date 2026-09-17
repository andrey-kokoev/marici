#!/usr/bin/env python3
"""Explicit Fourier-Linf edge coercivity collar for every prime-power threshold."""
import json,math,sys
from pathlib import Path
try: from scipy.special import digamma
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));from scipy.special import digamma
q0=(digamma(.25)-math.log(math.pi))/2;c=2/math.e
def q(u):return (digamma(.25+.5j*u).real-math.log(math.pi))/2
def lower(delta):
 # At most half the Fourier probability lies in |u|<pi/(2 delta).
 return .5*(q0+q(math.pi/(2*delta)))-2*math.sinh(delta/2)-c
lo,hi=1e-16,1.
for _ in range(100):
 mid=(lo+hi)/2
 if lower(mid)>0:lo=mid
 else:hi=mid
safe=lo;out={'schema':'marici.voevodsky.uniform-threshold-edge-collar.v1','q_zero':q0,'uniform_prime_power_coefficient':c,'fourier_split_radius_formula':'pi/(2 delta)','endpoint_norm_penalty_formula':'2 sinh(delta/2)','largest_safe_overlap_width':safe,'lower_bound_at_99_percent_safe_width':lower(.99*safe),'proof_inputs':['Plancherel','|fhat(u)|<=sqrt(delta)||f||','monotonicity of q(|u|)','Lambda(n)/sqrt(n)<=2/e'],'passed':bool(safe>0 and lower(.99*safe)>0),'rh_proved':False};p=Path(__file__).parents[1]/'results'/'uniform_threshold_edge_collar.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']

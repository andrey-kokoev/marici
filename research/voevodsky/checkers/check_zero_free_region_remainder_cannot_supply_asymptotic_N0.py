#!/usr/bin/env python3
"""Exact asymptotic obstruction for classical zero-free-region PNT input."""
import json,sys
from pathlib import Path
try: import sympy as s
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import sympy as s
x=s.symbols('x',positive=True);# Representative constants suffice for executable symbolic regression; proof note records arbitrary c,k.
f=s.exp(x/s.Integer(2)-s.sqrt(x))/x**4;lim=s.limit(f,x,s.oo);der=s.factor(s.diff(x/s.Integer(2)-s.sqrt(x),x));checks={'ratio_to_log_power_diverges':lim==s.oo,'exponent_eventually_increasing':s.solve_univariate_inequality(der>0,x).as_set().contains(s.Integer(5))==True};out={'schema':'marici.voevodsky.zero-free-region-remainder-no-asymptotic-N0.v1','weighted_remainder_in_x_logN':'exp(x/2-c sqrt(x))','representative_ratio':'exp(x/2-sqrt(x))/x^4','representative_limit':str(lim),'exponent_derivative_c1':str(der),'checks':checks,'passed':all(checks.values()),'general_statement':'for every c>0 and k>=0, exp(x/2-c sqrt(x))/x^k tends to infinity','conclusion':'a classical zero-free-region PNT remainder cannot eventually lie below any polylogarithmic edge coercivity, hence supplies no asymptotic N0 for this route','rh_proved':False};p=Path(__file__).parents[1]/'results'/'zero_free_region_remainder_no_asymptotic_N0.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']

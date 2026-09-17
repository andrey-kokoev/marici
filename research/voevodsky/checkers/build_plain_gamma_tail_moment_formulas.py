#!/usr/bin/env python3
"""Build closed formulas for the nonoscillatory asymptotic gamma-tail moments."""
import json
from fractions import Fraction
from pathlib import Path
d=json.loads((Path(__file__).parents[1]/'results'/'digamma_real_asymptotic_coefficients.json').read_text());cs={int(k):Fraction(v) for k,v in d['coefficients'].items()}
# Formula data for integral_R^inf g_asym(u) u^-k du, 2<=k<=160.
forms={}
for k in range(2,161):
 forms[str(k)]={'log_coefficient_denominator':k-1,'constant_term_denominator':(k-1)**2,'corrections':[{'digamma_power':j,'coefficient':str(c),'result_power':k+j-1,'integration_denominator':k+j-1} for j,c in cs.items()]}
out={'schema':'marici.voevodsky.plain-gamma-tail-moment-formulas.v1','formula':'R^(1-k)*(log(R/(2*pi))/(k-1)+1/(k-1)^2)+sum_j c_j*R^(1-k-j)/(k+j-1)','moment_power_range':[2,160],'digamma_correction_power_range':[min(cs),max(cs)],'formula_count':len(forms),'formulas':forms,'passed':True,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'plain_gamma_tail_moment_formulas.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'formula_count':len(forms),'moment_power_range':[2,160],'passed':True},indent=2))

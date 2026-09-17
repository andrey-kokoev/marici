#!/usr/bin/env python3
"""Numerically evaluate the explicit smooth logarithmic IMS constant."""
import json,math,sys
from pathlib import Path
try: from scipy.integrate import quad
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));from scipy.integrate import quad
def weight(t):return math.exp(-t/4)/(-math.expm1(-t))
def C(K):
 split=4/math.sqrt(K)
 f=lambda t:.25*weight(t)*min(4,K*t*t/4)
 a,ea=quad(f,0,split,epsabs=1e-12,limit=300);b,eb=quad(f,split,200,epsabs=1e-12,limit=300)
 return a+b,ea+eb
rows=[]
for delta in (1,.1,.01,.001,6.11758525067988e-5):
 # Representative sin/cos partition varying on scale delta: sum derivative squares <= (pi/(2 delta))^2.
 K=(math.pi/(2*delta))**2;c,e=C(K);rows.append({'transition_width':delta,'K':K,'C_IMS':c,'quadrature_error_estimate':e,'C_minus_log_inverse_width':c-math.log(1/delta)})
out={'schema':'marici.voevodsky.logarithmic-ims-constants.v1','partition_model':'sine/cosine transition','rows':rows,'passed':all(math.isfinite(r['C_IMS']) for r in rows),'rh_proved':False};p=Path(__file__).parents[1]/'results'/'logarithmic_ims_constants.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']

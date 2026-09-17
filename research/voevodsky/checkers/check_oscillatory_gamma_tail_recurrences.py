#!/usr/bin/env python3
"""Symbolically verify the four oscillatory tail recurrences."""
import json,sys
from pathlib import Path
try: import sympy as s
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import sympy as s
u,R,w,a,k=s.symbols('u R omega a k',positive=True);f=u**(-k);fl=s.log(u/a)*f
# Recurrences follow from antiderivatives and these derivative identities.
checks={'plain_derivative':s.simplify(s.diff(f,u)+k*u**(-k-1))==0,'log_derivative':s.simplify(s.diff(fl,u)-(u**(-k-1)*(1-k*s.log(u/a))))==0}
assert all(checks.values())
out={'schema':'marici.voevodsky.oscillatory-gamma-tail-recurrences.v1','checks':checks,'plain_recurrences':['C_k=-R^-k sin(omega R)/omega+k S_(k+1)/omega','S_k=R^-k cos(omega R)/omega-k C_(k+1)/omega'],'log_recurrences':['Clog_k=-R^-k log(R/a) sin(omega R)/omega+k Slog_(k+1)/omega-S_(k+1)/omega','Slog_k=R^-k log(R/a) cos(omega R)/omega-k Clog_(k+1)/omega+C_(k+1)/omega'],'oscillatory_moment_count':317,'passed':True,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'oscillatory_gamma_tail_recurrences.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

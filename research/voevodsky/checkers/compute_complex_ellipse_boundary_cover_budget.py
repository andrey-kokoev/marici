#!/usr/bin/env python3
"""Boundary covering budget from the 64 complex Schur samples."""
import json,math
from pathlib import Path
root=Path(__file__).parents[1]/'results';d=json.loads((root/'complex_schur_ellipse_L0649_L065_scout64.json').read_text());r=d['samples'];n=len(r);z=[complex(x['L_real'],x['L_imag']) for x in r];s=[complex(x['schur_real'],x['schur_imag']) for x in r];der=[]
for i in range(n):der.append(abs((s[(i+1)%n]-s[i])/(z[(i+1)%n]-z[i])))
maxd=max(der);half_chord=max(abs(z[(i+1)%n]-z[i]) for i in range(n))/2;sample=max(abs(x) for x in s);# allocate a factor four above observed secant derivative for a future directed derivative enclosure
der_target=4*maxd;cover=sample+der_target*half_chord;target=1e-8
out={'schema':'marici.voevodsky.complex-ellipse-boundary-cover-budget.v1','samples':n,'maximum_sample_abs':sample,'maximum_secant_derivative':maxd,'adopted_derivative_target':der_target,'maximum_half_chord':half_chord,'conditional_full_boundary_abs':cover,'target_boundary_abs':target,'condition':'directed bound |S prime(z)| <= adopted_derivative_target on each boundary arc','passed_conditionally':cover<target,'passed':False,'rh_proved':False};p=root/'complex_ellipse_boundary_cover_budget.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

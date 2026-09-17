#!/usr/bin/env python3
"""Cauchy magnitude cover for pivot17 on E8 from E10."""
import json
from pathlib import Path
root=Path(__file__).parents[1]/'results';r8=json.loads((root/'complex_schur_ellipse_L0649_L065_rho8_scout128.json').read_text())['samples'];r10=json.loads((root/'complex_schur_ellipse_L0649_L065_rho10_scout64.json').read_text())['samples'];h=.0005
def axes(r):return h*(r+r**-1)/2,h*(r-r**-1)/2
a8,b8=axes(8);a10,b10=axes(10);sep=min(a10-a8,b10-b8);M=1e-5;der=M/sep;half=max(abs(complex(r8[(i+1)%128]['L_real'],r8[(i+1)%128]['L_imag'])-complex(r8[i]['L_real'],r8[i]['L_imag'])) for i in range(128))/2;p8=max(abs(complex(x['strong_ldl_pivot_real'][17],x['strong_ldl_pivot_imag'][17])) for x in r8);bound=p8+der*half;out={'schema':'marici.voevodsky.gate3-E8-pivot17-from-E10.v1','sampled_E10_pivot17_max':max(abs(complex(x['strong_ldl_pivot_real'][17],x['strong_ldl_pivot_imag'][17])) for x in r10),'adopted_E10_bound':M,'separation':sep,'derivative_E8':der,'E8_half_chord_128':half,'sampled_E8_max':p8,'conditional_E8_full_bound':bound,'target_E8_bound':8e-6,'passed_conditionally':bound<8e-6,'passed':False,'next':'double E8 contour resolution','rh_proved':False};p=root/'gate3_E8_pivot17_from_E10.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

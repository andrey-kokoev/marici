#!/usr/bin/env python3
"""Degree-16 rho=4 tail-map remainder budget after degree-8 rho=5 failure."""
import json
from pathlib import Path
rho=4.;degree=16;M=1.;factor=4*rho**(-degree)/(rho-1);remainder=factor*M;An=2.292255400523168;alpha=1.067569476012246;margin=1.918863145047285e-11;res=An*remainder;correction=res*res/alpha;out={'schema':'marici.voevodsky.degree16-tail-map-budget-L0649-L065.v1','rho':rho,'degree':degree,'complex_tail_map_norm_target':M,'remainder_factor':factor,'tail_map_remainder':remainder,'residual_norm':res,'schur_correction':correction,'regularized_margin':margin,'lower_after_correction':margin-correction,'passed_conditionally':correction<margin/2,'condition':'directed true tail-map norm <=1 on rho=4 ellipse','passed':False,'rh_proved':False};p=Path(__file__).parents[1]/'results'/'degree16_tail_map_budget_L0649_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_conditionally']

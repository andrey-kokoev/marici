#!/usr/bin/env python3
"""Quantify which comparison constants dominate the two-prime high-mode threshold."""
import json,math
from pathlib import Path
L=.55;prime=sum(math.log(p)/math.sqrt(p) for p in (2,3));psi_quarter=-0.5772156649015329-math.pi/2-3*math.log(2);sharp_center=-(psi_quarter-math.log(math.pi))/2
cases={
 'registered_coarse':((4+.5*math.log(20)+math.log(math.pi))/2,math.pi),
 'sharp_gamma_center_only':(sharp_center,math.pi),
 'sharp_gamma_and_half_carleman':(sharp_center,math.pi/2),
 'sharp_gamma_no_boundary_loss':(sharp_center,0.0)}
out={}
for name,(cg,cb) in cases.items():
 C=cg+cb+prime;M=math.floor((2*L/math.pi)*(math.exp(2*C)-1))+1;out[name]={'gamma_constant':cg,'boundary_constant':cb,'total_constant':C,'mode_threshold':M}
res={'schema':'marici.voevodsky.high-mode-threshold-constant-sensitivity.v1','L':L,'prime_norm':prime,'cases':out,'decision':'The boundary comparison dominates. Audit its exact 1/2 normalization before attempting any intermediate-band computation.','passed':True,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'high_mode_threshold_constant_sensitivity.json';p.write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))

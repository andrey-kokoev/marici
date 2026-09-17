#!/usr/bin/env python3
"""Combine the directed digamma constant with the two-endpoint Schur bound."""
import json,math,hashlib
from pathlib import Path
root=Path(__file__).parents[1]/'results';gp=root/'sharp_half_normalized_digamma_constant.json';g=json.loads(gp.read_text());L=.55;cg=g['certified_global_upper'];cb=math.pi/math.sqrt(3);cp=sum(math.log(p)/math.sqrt(p) for p in (2,3));C=cg+cb+cp;M=math.floor((2*L/math.pi)*(math.exp(2*C)-1))+1;margin=.5*math.log(1+math.pi*M/(2*L))-C
out={'schema':'marici.voevodsky.sharpened-direct-interval-threshold.v1','L':L,'constants':{'directed_gamma':cg,'two_endpoint_boundary':cb,'prime':cp,'total':C},'sufficient_dirichlet_mode':M,'strict_margin':margin,'remaining_band':f'160..{M-1}','dependency_sha256':hashlib.sha256(gp.read_bytes()).hexdigest(),'passed':margin>0,'rh_proved':False}
p=root/'sharpened_direct_interval_threshold.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

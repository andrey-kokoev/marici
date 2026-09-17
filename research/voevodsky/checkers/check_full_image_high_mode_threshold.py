#!/usr/bin/env python3
"""Certified high-mode threshold from sharp gamma and full image budget."""
import json,math,hashlib
from pathlib import Path
root=Path(__file__).parents[1]/'results';gp=root/'sharp_half_normalized_digamma_constant.json';bp=root/'full_image_boundary_budget.json';g=json.loads(gp.read_text());b=json.loads(bp.read_text());L=.55;cg=g['certified_global_upper'];cb=b['full_boundary_budget'];cp=sum(math.log(p)/math.sqrt(p) for p in (2,3));C=cg+cb+cp;M=math.floor((2*L/math.pi)*(math.exp(2*C)-1))+1;margin=.5*math.log(1+math.pi*M/(2*L))-C
out={'schema':'marici.voevodsky.full-image-high-mode-threshold.v1','L':L,'constants':{'gamma':cg,'full_image_boundary':cb,'prime':cp,'total':C},'sufficient_dirichlet_mode':M,'strict_margin':margin,'remaining_band':f'160..{M-1}','dependencies':{'gamma_sha256':hashlib.sha256(gp.read_bytes()).hexdigest(),'boundary_sha256':hashlib.sha256(bp.read_bytes()).hexdigest()},'passed':margin>0,'rh_proved':False}
p=root/'full_image_high_mode_threshold.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

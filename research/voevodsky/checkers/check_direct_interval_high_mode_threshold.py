#!/usr/bin/env python3
"""High-mode threshold using the direct two-endpoint Schur bound."""
import json,math
from pathlib import Path
L=.55;cg=(4+.5*math.log(20)+math.log(math.pi))/2;cb=math.pi/math.sqrt(3);cp=sum(math.log(p)/math.sqrt(p) for p in (2,3));C=cg+cb+cp;M=math.floor((2*L/math.pi)*(math.exp(2*C)-1))+1;margin=.5*math.log(1+math.pi*M/(2*L))-C
out={'schema':'marici.voevodsky.direct-interval-high-mode-threshold.v1','L':L,'constants':{'gamma':cg,'two_endpoint_boundary':cb,'prime':cp,'total':C},'sufficient_dirichlet_mode':M,'strict_margin':margin,'ims_localization_used':False,'endpoint_representers_must_be_adjoined':True,'remaining_band':f'160..{M-1}','passed':margin>0,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'direct_interval_high_mode_threshold.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

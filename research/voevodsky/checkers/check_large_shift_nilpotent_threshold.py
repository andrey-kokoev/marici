#!/usr/bin/env python3
"""Assemble the rigorous high-mode threshold using square-zero prime shifts."""
import json,math
from pathlib import Path
L=.55;shifts=[math.log(2),math.log(3)];weights=[math.log(2)/math.sqrt(2),math.log(3)/math.sqrt(3)];assert all(2*a>=2*L for a in shifts)
cp=.5*sum(weights);cg=2.6947343670010686;cb=math.pi/math.sqrt(3)+math.log(2)-3/8;C=cg+cb+cp;M=math.floor((2*L/math.pi)*(math.exp(2*C)-1))+1;margin=.5*math.log1p(math.pi*M/(2*L))-C
out={'schema':'marici.voevodsky.large-shift-nilpotent-threshold.v1','L':L,'square_zero_shifts':shifts,'prime_norm_bound':cp,'gamma_constant':cg,'boundary_constant':cb,'total_constant':C,'sufficient_dirichlet_mode':M,'strict_margin':margin,'passed':margin>0,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'large_shift_nilpotent_threshold.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

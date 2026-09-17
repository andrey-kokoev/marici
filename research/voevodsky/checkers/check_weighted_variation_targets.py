#!/usr/bin/env python3
"""Variation caps sufficient to close residuals beyond Legendre mode 4999."""
import json,math
from pathlib import Path
L=.55;N=5000;bud=[7.233397108631436e-5,0.0011857561820853655,0.011859194030218644,0.08631608590010617];finite_1000_1999=[2.6006767471288582e-6,3.2281721049510936e-5,0.00035010785909424713,0.0021187291984118414];finite_2000_4999=[1.7450214140890782e-6,2.9330094212102474e-5,0.00023510218643718798,0.0019295025469033007];factor=math.sqrt(2*L/(math.pi*(N-1)));caps=[]
for b,a,c in zip(bud,finite_1000_1999,finite_2000_4999):
 used=math.hypot(a,c);remaining=math.sqrt(max(0,b*b-used*used));caps.append(remaining/factor)
out={'schema':'marici.voevodsky.weighted-variation-targets.v1','tail_start':N,'legendre_tail_factor':factor,'sufficient_weighted_variation_caps':caps,'finite_residuals_combined':[math.hypot(a,c) for a,c in zip(finite_1000_1999,finite_2000_4999)],'passed':min(caps)>0,'rh_proved':False};p=Path(__file__).parents[1]/'results'/'weighted_variation_targets.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

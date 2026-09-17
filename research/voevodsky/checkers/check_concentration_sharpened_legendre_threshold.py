#!/usr/bin/env python3
"""Combine exterior gamma and negligible low-band concentration leakage."""
import json,math
from pathlib import Path
L=.55;cg=0.9701921794495408;cb=math.pi/math.sqrt(3)+math.log(2)-3/8;cp=.4504638081309234;leak=10**(-421.4519334719844)*(2.6947343670010686-cg);C=cg+cb+cp+leak;N=160
while .5*math.log1p(math.sqrt(N*(N+1))/L)<=C:N+=1
margin=.5*math.log1p(math.sqrt(N*(N+1))/L)-C
out={'schema':'marici.voevodsky.concentration-sharpened-legendre-threshold.v1','L':L,'constants':{'exterior_gamma':cg,'boundary':cb,'exact_prime':cp,'low_band_leak_upper':leak,'total':C},'sufficient_legendre_rank':N,'strict_margin':margin,'passed':margin>0,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'concentration_sharpened_legendre_threshold.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

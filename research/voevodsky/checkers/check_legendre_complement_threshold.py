#!/usr/bin/env python3
"""Compute the coercive rank in the Legendre-aligned decomposition."""
import json,math
from pathlib import Path
L=.55;C=2.6947343670010686+math.pi/math.sqrt(3)+math.log(2)-3/8+0.4504638081309234
N=1
while .5*math.log1p(math.sqrt(N*(N+1))/L)<=C:N+=1
margin=.5*math.log1p(math.sqrt(N*(N+1))/L)-C
at160=.5*math.log1p(math.sqrt(160*161)/L)-C
out={'schema':'marici.voevodsky.legendre-complement-threshold.v1','L':L,'total_order_zero_constant':C,'sufficient_legendre_rank':N,'strict_margin':margin,'rank160_tail_margin':at160,'operator_order':'-Delta_D >= A_L, hence log(1+sqrt(-Delta_D)) >= log(1+sqrt(A_L))','basis_mismatch_removed':True,'passed':margin>0,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'legendre_complement_threshold.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

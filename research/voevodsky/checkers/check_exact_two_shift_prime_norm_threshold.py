#!/usr/bin/env python3
"""Exact 2-by-2 overlap-graph norm and resulting coercive threshold."""
import json,math
from pathlib import Path
L=.55;a=math.log(2);b=math.log(3);delta=b-a;u=a/(2*math.sqrt(2));v=b/(2*math.sqrt(3));cp=math.sqrt(u*u+v*v/2+v*math.sqrt(v*v+4*u*u)/2)
# Geometry checks for exactly the length-two overlap component.
geom={'both_cross_midpoint':min(a,b)>L,'b_domain_shifted_by_delta_lies_in_a_domain':(-L+delta)>=-L and (L-b+delta)<=L-a,'second_delta_exits_a_domain':(-L+2*delta)>L-a}
assert all(geom.values());cg=2.6947343670010686;cb=math.pi/math.sqrt(3)+math.log(2)-3/8;C=cg+cb+cp;M=math.floor((2*L/math.pi)*(math.exp(2*C)-1))+1;margin=.5*math.log1p(math.pi*M/(2*L))-C
out={'schema':'marici.voevodsky.exact-two-shift-prime-norm-threshold.v1','L':L,'edge_weights':{'u':u,'v':v},'geometry_checks':geom,'exact_prime_norm':cp,'previous_triangle_bound':u+v,'total_constant':C,'sufficient_dirichlet_mode':M,'strict_margin':margin,'passed':margin>0,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'exact_two_shift_prime_norm_threshold.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

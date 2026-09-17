#!/usr/bin/env python3
"""Quantify the Green-recursion geometric factor for degree 999 and n>=5000."""
import json,math
from pathlib import Path
d=999;N=5000;rho=d*(d+1)/(N*(N+1));rows=[]
for r in (1,2,3,4,5,6,8,10):rows.append({'iterations':r,'relative_bulk_remainder':rho**r})
out={'schema':'marici.voevodsky.legendre-green-geometric-remainder.v1','maximum_piece_degree':d,'tail_start_degree':N,'geometric_ratio':rho,'rows':rows,'iterations_for_1e_minus_12':math.ceil(math.log(1e-12)/math.log(rho)),'passed':rho<.04,'rh_proved':False};p=Path(__file__).parents[1]/'results'/'legendre_green_geometric_remainder.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']

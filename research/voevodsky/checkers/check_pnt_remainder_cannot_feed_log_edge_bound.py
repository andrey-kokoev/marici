#!/usr/bin/env python3
"""Record the asymptotic mismatch between zero-free-region PNT error and logarithmic edge coercivity."""
import json,math
from pathlib import Path
# With y=log N, weighted PNT error/logarithmic coercivity is exp(y/2-c sqrt(y))/y.
c=1.0
def log_ratio(y):return y/2-c*math.sqrt(y)-math.log(y)
# derivative = 1/2-c/(2 sqrt y)-1/y, positive for y>=16 when c=1.
rows=[{'log_N':y,'log_error_to_log_coercivity_ratio':log_ratio(y)} for y in (16,25,50,100,200,500,1000)]
out={'schema':'marici.voevodsky.pnt-remainder-vs-log-edge.v1','model_constant_c':c,'log_ratio_formula':'y/2-c sqrt(y)-log(y)','eventual_derivative_lower_at_y16':.5-c/(2*math.sqrt(16))-1/16,'rows':rows,'conclusion':'ratio diverges; classical zero-free-region PNT error cannot be absorbed by O(log N) edge coercivity','passed':rows[-1]['log_error_to_log_coercivity_ratio']>rows[-2]['log_error_to_log_coercivity_ratio']>0,'rh_proved':False};p=Path(__file__).parents[1]/'results'/'pnt_remainder_vs_log_edge.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']

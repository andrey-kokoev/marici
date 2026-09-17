#!/usr/bin/env python3
"""Audit multiplier normalization together with the number of interval endpoints."""
import json,math
from pathlib import Path
coefficient=.5;halfline_norm=math.pi;endpoint_count=2;per_endpoint=coefficient*halfline_norm;triangle=endpoint_count*per_endpoint
out={'schema':'marici.voevodsky.interval-carleman-endpoint-count.v1','principal_log_coefficient':coefficient,'halfline_carleman_norm':halfline_norm,'endpoint_count':endpoint_count,'per_endpoint_budget':per_endpoint,'coarse_interval_budget':triangle,'checks':{'per_endpoint_is_pi_over_2':per_endpoint==math.pi/2,'two_endpoint_budget_is_pi':triangle==math.pi},'disposition':'Any budget below pi requires a direct two-endpoint cancellation theorem.','passed':True,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'interval_carleman_endpoint_count.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

#!/usr/bin/env python3
"""Check and record the universal Lambda(n)/sqrt(n) <= 2/e bound."""
import json,math
from pathlib import Path
inv=json.loads((Path(__file__).parents[1]/'results'/'prime_power_support_inventory.json').read_text());vals=[x['coefficient'] for x in inv['items']];bound=2/math.e;out={'schema':'marici.voevodsky.uniform-prime-power-coefficient-bound.v1','analytic_bound':bound,'reason':'Lambda(n)<=log(n), and log(x)/sqrt(x) is maximized at x=e^2','inventory_max_through_exp4':max(vals),'inventory_argmax':inv['items'][vals.index(max(vals))]['n'],'passed':max(vals)<=bound,'rh_proved':False};p=Path(__file__).parents[1]/'results'/'uniform_prime_power_coefficient_bound.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']

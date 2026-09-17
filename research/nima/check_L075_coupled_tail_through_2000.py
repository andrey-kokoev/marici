#!/usr/bin/env python3
"""Aggregate ten directed complete-source residual blocks on modes 1000..1998."""
import json,sys
from pathlib import Path
try:
 import flint
 from flint import arb
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[1]/'flavor'/'.venv'/'Lib'/'site-packages'));import flint
 from flint import arb
flint.ctx.prec=256;ROOT=Path(__file__).resolve().parents[2];V=ROOT/'research/voevodsky/results';N=ROOT/'research/nima/results';sq=arb(0);rows=[]
for a in range(1000,2000,100):
 d=json.loads((V/f'L075_residual_cached_chunk_{a}_{a+100}.json').read_text());z=arb(d['squared_norm']);sq+=z;rows.append({'range':[a,a+100],'norm':str(z.sqrt())})
norm=sq.sqrt();allow=arb('4.267829461527579e-9');remaining=(allow*allow-sq).sqrt()
out={'schema':'marici.nima.L075-coupled-tail-through-2000.v1','blocks':rows,'degree_range':[1000,2000],'even_mode_count':500,'coupled_norm':str(norm),'tail_allowance':str(allow),'allowance_fraction_upper':float(norm.upper()/allow.lower()),'orthogonal_allowance_for_modes_2000_to_infinity':str(remaining),'directed_prefix_below_allowance':norm.upper()<allow.lower(),'infinite_tail_certified':False,'next_obligation':'bound the complete coupled coefficient tail from degree 2000 onward; no geometric extrapolation is used','rh_proved':False,'passed':norm.upper()<allow.lower()}
p=N/'L075-coupled-tail-through-2000.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)

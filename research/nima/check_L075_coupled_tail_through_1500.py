#!/usr/bin/env python3
"""Aggregate five directed full-source L=.75 tail blocks, preserving source cancellation."""
import json,sys
from pathlib import Path
try:
 import flint
 from flint import arb
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[1]/'flavor'/'.venv'/'Lib'/'site-packages'));import flint
 from flint import arb
flint.ctx.prec=256;ROOT=Path(__file__).resolve().parents[2];V=ROOT/'research/voevodsky/results';N=ROOT/'research/nima/results';rows=[];sq=arb(0)
for a in range(1000,1500,100):
 d=json.loads((V/f'L075_residual_cached_chunk_{a}_{a+100}.json').read_text());z=arb(d['squared_norm']);sq+=z*z*0+z;rows.append({'range':[a,a+100],'squared_norm':str(z),'norm':str(z.sqrt())})
norm=sq.sqrt();allow=arb('4.267829461527579e-9');remaining=(allow*allow-sq).sqrt()
out={'schema':'marici.nima.L075-coupled-tail-through-1500.v1','blocks':rows,'degree_range':[1000,1500],'even_mode_count':250,'coupled_norm':str(norm),'tail_allowance':str(allow),'allowance_fraction_upper':float(norm.upper()/allow.lower()),'orthogonal_allowance_for_modes_1500_to_infinity':str(remaining),'directed_prefix_below_allowance':norm.upper()<allow.lower(),'infinite_tail_certified':False,'finding':'block norms are not monotonically geometric; extrapolation is prohibited','next_obligation':'bound the complete coupled coefficient tail from degree 1500 onward by the orthogonal remaining allowance','rh_proved':False,'passed':norm.upper()<allow.lower()}
p=N/'L075-coupled-tail-through-1500.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)

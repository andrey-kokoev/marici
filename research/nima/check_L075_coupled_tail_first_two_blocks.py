#!/usr/bin/env python3
"""Directed coupled full-source residual norm on L=.75 modes 1000..1198."""
import json,sys
from pathlib import Path
try:
 import flint
 from flint import arb
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[1]/'flavor'/'.venv'/'Lib'/'site-packages'));import flint
 from flint import arb
flint.ctx.prec=256;ROOT=Path(__file__).resolve().parents[2];V=ROOT/'research/voevodsky/results';N=ROOT/'research/nima/results'
a=json.loads((V/'L075_residual_cached_chunk_1000_1100.json').read_text());b=json.loads((V/'L075_residual_cached_chunk_1100_1200.json').read_text());sa=arb(a['squared_norm']);sb=arb(b['squared_norm']);norm=(sa+sb).sqrt();allow=arb('4.267829461527579e-9')
# Block contraction is diagnostic only; it cannot certify the unsampled infinite tail.
ratio=sb/sa
out={'schema':'marici.nima.L075-coupled-tail-first-two-blocks.v1','degree_range':[1000,1200],'even_mode_count':a['count']+b['count'],'first_block_squared_norm':str(sa),'second_block_squared_norm':str(sb),'coupled_block_norm':str(norm),'full_tail_allowance':str(allow),'fraction_of_allowance_upper':float(norm.upper()/allow.lower()),'second_to_first_squared_norm_ratio':str(ratio),'directed_coupled_block_below_allowance':norm.upper()<allow.lower(),'cross_terms_retained':'inside each full source coefficient before squaring','infinite_tail_certified':False,'next_obligation':'derive a directed envelope for the complete coupled coefficients from degree 1200 to infinity; block contraction alone is not such a theorem','rh_proved':False,'passed':norm.upper()<allow.lower()}
p=N/'L075-coupled-tail-first-two-blocks.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)

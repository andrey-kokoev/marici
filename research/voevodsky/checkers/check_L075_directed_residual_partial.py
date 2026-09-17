#!/usr/bin/env python3
"""Register the first successful directed chunk of the L=.75 residual."""
import json,sys
from pathlib import Path
try:
 import flint
 from flint import arb
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import flint
 from flint import arb
root=Path(__file__).parents[1]/'results';d=json.loads((root/'L075_residual_chunk_150_160.json').read_text());sq=arb(d['squared_norm']);out={'schema':'marici.voevodsky.L075-directed-residual-partial.v1','certified_even_modes':[150,152,154,156,158],'directed_squared_norm':str(sq),'directed_norm_upper':float(sq.sqrt().upper()),'remaining_even_modes':420,'full_residual_certified':False,'performance_finding':'independent wide chunks time out because each recomputes 18000-node Arb transforms; production implementation must cache F_w nodes and use a vectorized/order recurrence transform','passed_partial':sq.lower()>0,'rh_proved':False};p=root/'L075_directed_residual_partial.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_partial'] and not out['full_residual_certified']

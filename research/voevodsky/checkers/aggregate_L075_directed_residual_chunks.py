#!/usr/bin/env python3
"""Aggregate all available disjoint directed L=.75 residual chunks."""
import glob,json,sys
from pathlib import Path
try:
 import flint
 from flint import arb
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import flint
 from flint import arb
root=Path(__file__).parents[1]/'results';rows=[]
paths=list(root.glob('L075_residual_chunk_*_*.json'))+list(root.glob('L075_residual_cached_chunk_*_*.json'))
for p in sorted(paths):
 d=json.loads(p.read_text());rows.append((d['start'],d['stop'],d['count'],arb(d['squared_norm']),p.name))
rows.sort();assert all(rows[i][1]<=rows[i+1][0] for i in range(len(rows)-1));sq=sum((x[3] for x in rows),arb(0));count=sum(x[2] for x in rows);out={'schema':'marici.voevodsky.L075-directed-residual-chunk-aggregate.v1','chunks':[{'start':x[0],'stop':x[1],'count':x[2],'squared_norm':str(x[3]),'artifact':x[4]} for x in rows],'certified_even_mode_count':count,'certified_through_exclusive':max(x[1] for x in rows),'squared_norm_sum':str(sq),'partial_norm_upper':float(sq.sqrt().upper()),'remaining_even_modes':425-count,'full_residual_certified':count==425,'passed_partial':sq.lower()>0,'rh_proved':False};p=root/'L075_directed_residual_chunk_aggregate.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_partial']

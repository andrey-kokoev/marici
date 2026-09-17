#!/usr/bin/env python3
"""Merge and validate all resumable R=250 gamma-tail moment chunks."""
import json,glob,hashlib
from pathlib import Path
root=Path(__file__).parents[1]/'results';files=sorted(root.glob('gamma_tail_moments_250_*_*.json'));mom={};deps=[]
for p in files:
 d=json.loads(p.read_text());
 if d.get('schema')!='marici.voevodsky.gamma-tail-moment-chunk.v1':continue
 for k,v in d['moments'].items():
  if k in mom:assert mom[k]==v
  mom[k]=v
 deps.append({'file':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
missing=[k for k in range(2,161) if str(k) not in mom];assert not missing and len(mom)==159
out={'schema':'marici.voevodsky.gamma-tail-moments-250-merged.v1','R':250,'precision_digits':70,'power_range':[2,160],'moment_triples':mom,'dependencies':deps,'complete':True,'passed':True,'rh_proved':False}
p=root/'gamma_tail_moments_250_merged.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'chunk_count':len(deps),'moment_count':len(mom),'missing':missing,'passed':True},indent=2))

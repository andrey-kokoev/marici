#!/usr/bin/env python3
"""Compare source and one-grade-delayed square persistence in degree two."""
from hashlib import sha256
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3];PACKET=ROOT/'research/voevodsky/filler_delay_breaks_persistence_synchronization.md';RESULT=ROOT/'research/voevodsky/results/filler_delay_persistence.json'
# Reuse the audited degree-two enumerator and reducer definitions without executing its report block.
BASE=ROOT/'research/voevodsky/checkers/check_degree_two_persistent_h1.py';scope={'__file__':str(BASE)};exec(BASE.read_text(encoding='utf-8').split("ints={str(p):intervals(p) for p in MODS}")[0],scope)
cells=scope['cells'];source_birth=scope['birth'];boundary=scope['boundary'];MODS=scope['MODS'];LIMIT=scope['LIMIT']
def reduce_with(grades,p):
 ordered=sorted(cells,key=lambda c:(grades[c],len(c[1]),c[1],c[0]));index={c:i for i,c in enumerate(ordered)};basis={};reduced={};pairs={}
 for c in ordered:
  col={index[f]:a%p for f,a in boundary(c).items()}
  while col:
   low=max(col)
   if low not in basis:break
   q=col[low]*pow(basis[low][low],p-2,p)%p
   for i,a in basis[low].items():
    z=(col.get(i,0)-q*a)%p
    if z:col[i]=z
    else:col.pop(i,None)
  reduced[c]=col
  if col:low=max(col);basis[low]=col;pairs[ordered[low]]=c
 return reduced,pairs
def bars(grades,p):
 reduced,pairs=reduce_with(grades,p);out=[]
 for c in cells:
  if len(c[1])!=1 or reduced[c]:continue
  death=pairs.get(c);out.append({'edge':[c[0],c[1][0]],'birth':grades[c],'death':grades[death] if death else None,'lifetime':grades[death]-grades[c] if death else None})
 return sorted(out,key=lambda x:(x['birth'],x['edge']))
original=dict(source_birth);delayed={c:g+(1 if len(c[1])==2 else 0) for c,g in source_birth.items()}
face_monotone=all(delayed[f]<=delayed[c] for c in cells for f in boundary(c))
barcodes={}
for name,grades in (('original',original),('delayed',delayed)):
 barcodes[name]={str(p):bars(grades,p) for p in MODS}
def summary(xs):return {'births':len(xs),'zero_length':sum(x['lifetime']==0 for x in xs),'positive_length':sum(x['lifetime'] is not None and x['lifetime']>0 for x in xs),'right_censored':sum(x['lifetime'] is None for x in xs),'lifetime_histogram':{str(d):sum(x['lifetime']==d for x in xs) for d in sorted({x['lifetime'] for x in xs if x['lifetime'] is not None})}}
os=summary(barcodes['original'][str(MODS[0])]);ds=summary(barcodes['delayed'][str(MODS[0])])
checks={'face_monotone':face_monotone,'original_fields_agree':barcodes['original'][str(MODS[0])]==barcodes['original'][str(MODS[1])],'delayed_fields_agree':barcodes['delayed'][str(MODS[0])]==barcodes['delayed'][str(MODS[1])],'original_73_zero':os['births']==os['zero_length']==73,'delayed_73_length_one':ds['births']==ds['positive_length']==73 and ds['lifetime_histogram']=={'1':73},'scope_retained':'not asserted to be source-derived or physical' in PACKET.read_text(encoding='utf-8')};checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.filler-delay-persistence.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'limit':LIMIT,'intervention':'add one grade to every square; retain vertex/edge grades and all boundaries','original':os,'delayed':ds,'first_ten_delayed':barcodes['delayed'][str(MODS[0])][:10],'checks':checks,'passed':all(checks.values()),'disposition':{'prediction':'survives','inference':'same-grade filler alignment, not incidence alone, suppresses positive persistence','authority':'counterfactual filtration only'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'original':os,'delayed':ds,'checks':checks}));raise SystemExit(0 if result['passed'] else 1)

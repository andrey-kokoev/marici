#!/usr/bin/env python3
"""Test positive-same-grade reservations before vertex-edge matching."""
from hashlib import sha256
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3];PACKET=ROOT/'research/voevodsky/same_grade_first_global_morse_preflight.md';RESULT=ROOT/'research/voevodsky/results/same_grade_first_global_morse_preflight.json'
BASE=ROOT/'research/voevodsky/checkers/check_global_filtered_morse_preflight.py';scope={'__file__':str(BASE)};exec(BASE.read_text(encoding='utf-8').split('predictions={};sectors={}')[0],scope)
build=scope['build'];has_cycle=scope['cycle'];LIMIT=scope['LIMIT']
def test(D):
 birth,cells,faces=build(D);matched=set();pairs=[]
 # Reserve equal-grade positive pairs first.
 for d in range(1,D):
  co={f:[] for f in cells[d]}
  for c in cells[d+1]:
   for f in faces[c]:co[f].append(c)
  for f in cells[d]:
   if f in matched:continue
   options=sorted((c for c in co[f] if c not in matched and birth[c]==birth[f]),key=lambda c:(c[1],c[0]))
   if options:c=options[0];matched|={f,c};pairs.append((f,c))
 # Only then match vertices to unused edges.
 co={v:[] for v in cells[0]}
 for e in cells[1]:
  for v in faces[e]:co[v].append(e)
 for v in cells[0]:
  if v in matched:continue
  options=sorted((e for e in co[v] if e not in matched),key=lambda e:(birth[e],e[1],e[0]))
  if options:e=options[0];matched|={v,e};pairs.append((v,e))
 nodes=[c for d in cells for c in cells[d]];unmatched=[c for c in nodes if c not in matched];positive=[c for c in unmatched if c[1]];pairset=set(pairs);arrows=[]
 for d in range(1,D+1):
  for c in cells[d]:
   for f in faces[c]:arrows.append((f,c) if (f,c) in pairset else (c,f))
 parent={v:v for v in cells[0]}
 def find(x):
  while parent[x]!=x:parent[x]=parent[parent[x]];x=parent[x]
  return x
 for e in cells[1]:
  vs=list(faces[e])
  if len(vs)==2:
   a,b=map(find,vs)
   if a!=b:parent[a]=b
 h0=len({find(v) for v in cells[0]});critical_vertices=sum(not c[1] for c in unmatched)
 return {'cell_counts':[len(cells[d]) for d in range(D+1)],'pair_counts':{f'{d}-{d+1}':sum(len(f[1])==d for f,c in pairs) for d in range(D)},'unmatched_positive_count':len(positive),'first_unmatched_positive':([positive[0][0],list(positive[0][1])] if positive else None),'critical_vertices':critical_vertices,'absolute_h0':h0,'cross_grade_positive_pairs':sum(bool(f[1]) and birth[f]!=birth[c] for f,c in pairs),'gradient_cycle':has_cycle(nodes,arrows)}
sectors={str(D):test(D) for D in range(2,6)};predictions={}
for D,r in ((int(k),v) for k,v in sectors.items()):
 predictions[f'only_vertices_D{D}']=r['unmatched_positive_count']==0;predictions[f'critical_vertices_equal_h0_D{D}']=r['critical_vertices']==r['absolute_h0'];predictions[f'equal_grade_positive_D{D}']=r['cross_grade_positive_pairs']==0;predictions[f'acyclic_D{D}']=not r['gradient_cycle']
checks={'all_sectors_enumerated':set(sectors)=={'2','3','4','5'},'scope_retained':'does not yet prove global synchronization' in PACKET.read_text(encoding='utf-8')};checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.same-grade-first-morse-preflight.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'limit':LIMIT,'sectors':sectors,'predictions':predictions,'checks':checks,'passed':all(checks.values()),'disposition':{'constructor':'survives bounded test' if all(predictions.values()) else 'fails','residual':'prove general rule or refine from exact first failures'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'sectors':sectors,'prediction_failures':[k for k,v in predictions.items() if not v]}));raise SystemExit(0 if result['passed'] else 1)

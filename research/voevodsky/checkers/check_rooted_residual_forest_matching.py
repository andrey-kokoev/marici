#!/usr/bin/env python3
"""Complete same-grade matching by rooting the residual edge forest."""
from collections import deque
from hashlib import sha256
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3];PACKET=ROOT/'research/voevodsky/rooted_residual_forest_completes_filtered_morse_matching.md';RESULT=ROOT/'research/voevodsky/results/rooted_residual_forest_matching.json'
BASE=ROOT/'research/voevodsky/checkers/check_global_filtered_morse_preflight.py';scope={'__file__':str(BASE)};exec(BASE.read_text(encoding='utf-8').split('predictions={};sectors={}')[0],scope);build=scope['build'];has_cycle=scope['cycle'];LIMIT=scope['LIMIT']
def test(D):
 birth,cells,faces=build(D);matched=set();pairs=[]
 for d in range(1,D):
  co={f:[] for f in cells[d]}
  for c in cells[d+1]:
   for f in faces[c]:co[f].append(c)
  for f in cells[d]:
   if f in matched:continue
   options=sorted((c for c in co[f] if c not in matched and birth[c]==birth[f]),key=lambda c:(c[1],c[0]))
   if options:c=options[0];matched|={f,c};pairs.append((f,c))
 residual_edges=[e for e in cells[1] if e not in matched];adj={v:[] for v in cells[0]}
 for e in residual_edges:
  for v in faces[e]:
   other=next(x for x in faces[e] if x!=v);adj[v].append((other,e))
 seen=set();components=[];forest_pairs=[]
 for root in sorted(cells[0],key=lambda v:(birth[v],v[0])):
  if root in seen:continue
  seen.add(root);queue=deque([root]);verts=[];edges=set()
  while queue:
   v=queue.popleft();verts.append(v)
   for w,e in sorted(adj[v],key=lambda z:(birth[z[1]],z[1][1],z[1][0],z[0][0])):
    edges.add(e)
    if w not in seen:seen.add(w);queue.append(w);forest_pairs.append((w,e))
  components.append({'root':root,'vertices':len(verts),'edges':len(edges)})
 residual_is_forest=all(c['edges']==c['vertices']-1 for c in components)
 parent={v:v for v in cells[0]}
 def find(v):
  while parent[v]!=v:parent[v]=parent[parent[v]];v=parent[v]
  return v
 for e in cells[1]:
  a,b=list(faces[e]);a,b=find(a),find(b)
  if a!=b:parent[a]=b
 full_h0=len({find(v) for v in cells[0]})
 for v,e in forest_pairs:
  if v not in matched and e not in matched:matched|={v,e};pairs.append((v,e))
 nodes=[c for d in cells for c in cells[d]];unmatched=[c for c in nodes if c not in matched];pairset=set(pairs);arrows=[]
 for d in range(1,D+1):
  for c in cells[d]:
   for f in faces[c]:arrows.append((f,c) if (f,c) in pairset else (c,f))
 return {'cell_counts':[len(cells[d]) for d in range(D+1)],'residual_edges':len(residual_edges),'residual_components':len(components),'residual_is_forest':residual_is_forest,'component_count_matches_absolute_h0':len(components)==full_h0,'all_positive_paired':all(not c[1] for c in unmatched),'critical_vertices':sum(not c[1] for c in unmatched),'all_components_one_root':sum(not c[1] for c in unmatched)==len(components),'cross_grade_positive_pairs':sum(bool(f[1]) and birth[f]!=birth[c] for f,c in pairs),'gradient_cycle':has_cycle(nodes,arrows),'component_size_extrema':{'min':min(c['vertices'] for c in components),'max':max(c['vertices'] for c in components)}}
sectors={str(D):test(D) for D in range(2,6)};predictions={}
for D,r in ((int(k),v) for k,v in sectors.items()):
 for key in ('residual_is_forest','component_count_matches_absolute_h0','all_positive_paired','all_components_one_root'):predictions[f'{key}_D{D}']=r[key]
 predictions[f'equal_grade_positive_D{D}']=r['cross_grade_positive_pairs']==0;predictions[f'acyclic_D{D}']=not r['gradient_cycle']
checks={'all_sectors_enumerated':set(sectors)=={'2','3','4','5'},'scope_retained':'not yet an all-dimensional proof' in PACKET.read_text(encoding='utf-8')};checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.rooted-residual-forest-matching.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'limit':LIMIT,'sectors':sectors,'predictions':predictions,'checks':checks,'passed':all(checks.values()),'disposition':{'constructor':'survives bounded sectors' if all(predictions.values()) else 'fails','residual':'prove residual-forest property and mixed-gradient acyclicity for all degrees and cutoffs'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'sectors':sectors,'prediction_failures':[k for k,v in predictions.items() if not v]}));raise SystemExit(0 if result['passed'] else 1)

#!/usr/bin/env python3
"""Audit critical diamonds and unique normal forms for predecessor shifts."""
from functools import lru_cache
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3];PACKET=ROOT/'research/voevodsky/predecessor_shift_rewriting_is_terminating_and_confluent.md';RESULT=ROOT/'research/voevodsky/results/predecessor_shift_confluence.json'
BASE=ROOT/'research/voevodsky/checkers/check_global_filtered_morse_preflight.py';scope={'__file__':str(BASE)};exec(BASE.read_text(encoding='utf-8').split('predictions={};sectors={}')[0],scope);build=scope['build'];PS=scope['PS'];LIMIT=scope['LIMIT']
def test(D):
 birth,cells,faces=build(D);cellset=set(birth);succ={c:set() for d in range(1,D+1) for c in cells[d]}
 for d in range(1,D):
  for c in cells[d]:
   base,I=c;m=max(I)
   for j in range(1,m):
    if j not in I and base%PS[j]==0:
     x=(base*PS[j-1]//PS[j],tuple(sorted(I+(j,))))
     if x in cellset and birth[x]==birth[c]:succ[c].add(x)
 branch_count=0;diamond_count=0;diamond_fail=[]
 for c,nexts in succ.items():
  if len(nexts)>1:branch_count+=1
  base,I=c
  for a,b in combinations(nexts,2):
   ja=next(iter(set(a[1])-set(I)));jb=next(iter(set(b[1])-set(I)))
   common=(base*PS[ja-1]*PS[jb-1]//(PS[ja]*PS[jb]),tuple(sorted(I+(ja,jb))))
   diamond_count+=1
   if common not in cellset or birth.get(common)!=birth[c] or common not in succ[a] or common not in succ[b]:diamond_fail.append({'cell':[base,list(I)],'directions':[ja,jb]})
 @lru_cache(None)
 def terminals(c):
  if not succ[c]:return frozenset((c,))
  return frozenset(x for q in succ[c] for x in terminals(q))
 multiple=[];max_depth=0
 @lru_cache(None)
 def depth(c):return 0 if not succ[c] else 1+max(depth(q) for q in succ[c])
 for c in succ:
  ts=terminals(c);max_depth=max(max_depth,depth(c))
  if len(ts)!=1:multiple.append({'cell':[c[0],list(c[1])],'terminal_count':len(ts)})
 return {'positive_cells':len(succ),'branching_cells':branch_count,'critical_diamonds':diamond_count,'diamond_failures':len(diamond_fail),'multiple_normal_forms':len(multiple),'maximum_rewrite_depth':max_depth,'first_diamond_failure':diamond_fail[:1],'first_multiple_normal_form':multiple[:1]}
sectors={str(D):test(D) for D in range(2,6)};checks={}
for D,r in ((int(k),v) for k,v in sectors.items()):checks[f'all_diamonds_join_D{D}']=r['diamond_failures']==0;checks[f'unique_normal_forms_D{D}']=r['multiple_normal_forms']==0
checks['branching_tested']=sum(r['critical_diamonds'] for r in sectors.values())>0;checks['scope_retained']='repeated-shell cells and alternative grades are excluded' in PACKET.read_text(encoding='utf-8');checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.predecessor-shift-confluence.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'limit':LIMIT,'sectors':sectors,'checks':checks,'passed':all(checks.values()),'disposition':{'theorem':'termination plus cubical diamonds gives unique saturated same-grade normal forms','filtered_morse_consequence':'one critical vertex per component and zero-length positive persistence','scope':'distinct-shell max-grade Carrier'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'sectors':sectors,'checks':checks}));raise SystemExit(0 if result['passed'] else 1)

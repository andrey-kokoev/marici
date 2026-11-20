"""Test pure complementary channel explanation at Hall root0 of type191 (its unique center)."""
from pathlib import Path
from itertools import combinations
import json
from ramsey_hall_center_conjecture import decode
from ramsey_mutual_repair_conjecture import switches,repairs,apply
def independent_sets(A,mask,chosen=()):
 yield chosen
 while mask:
  bit=mask&-mask;mask^=bit;i=bit.bit_length()-1
  yield from independent_sets(A,mask&~A[i],chosen+(i,))
data=json.loads(Path(__file__).with_name('ramsey_hall_center_conjecture.json').read_text());r=next(r for r in data['regular'] if r['record']==191);assert r['centers']==[0];A=decode(r['graph6'].encode());moves=list(switches(A));out=[]
for s,t in combinations(moves,2):
 if s['support']&t['support'] or not(repairs(s,t) and repairs(t,s)):continue
 pair=[]
 for move in (s,t):
  B=apply(A,move['removed'],move['added']);assert B[0]==A[0];W=((1<<22)-1)^B[0]^1;alpha=0;deficits=[]
  for J in independent_sets(B,W):
   alpha=max(alpha,len(J));union=0
   for w in J:union|=B[w]&B[0]
   if union.bit_count()<len(J):deficits.append(J)
  pair.append({'removed':move['removed'],'added':move['added'],'external_alpha':alpha,'hall_deficiencies':deficits})
 out.append(pair)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print('channel profiles',[[ (x['external_alpha'],len(x['hall_deficiencies'])) for x in pair] for pair in out])

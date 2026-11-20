"""Exact valid two-edge-switch graph of regular catalogue types. No external graph libraries; retain concrete switches and verified isomorphisms."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json
from ramsey_hall_center_conjecture import decode,independent

def relation(A):
 R=[[(A[i]>>j&1,(A[i]&A[j]).bit_count()) for j in range(22)] for i in range(22)]
 S=[tuple(sorted(row)) for row in R];return R,S,tuple(sorted(S))

def iso(A,B,ra,rb):
 R,S,key=ra;T,Q,other=rb
 if key!=other:return None
 def search(m,used):
  if len(m)==22:return m
  options=[]
  for i in range(22):
   if i in m:continue
   opts=[j for j in range(22) if j not in used and S[i]==Q[j] and all(R[i][a]==T[j][b] for a,b in m.items())]
   if not opts:return None
   options.append((len(opts),i,opts))
  _,i,opts=min(options)
  for j in opts:
   ans=search(m|{i:j},used|{j})
   if ans is not None:return ans
  return None
 ans=search({},set())
 if ans is not None:assert all(((A[i]>>j)&1)==((B[ans[i]]>>ans[j])&1) for i,j in combinations(range(22),2))
 return ans

if __name__=='__main__':
 data=json.loads(Path(__file__).with_name('ramsey_hall_center_conjecture.json').read_text());graphs={r['record']:decode(r['graph6'].encode()) for r in data['regular']};relations={k:relation(A) for k,A in graphs.items()};counts=Counter();witness={};attempts=Counter()
 for source,A in graphs.items():
  edges=[(i,j) for i,j in combinations(range(22),2) if A[i]>>j&1]
  for (a,b),(c,d) in combinations(edges,2):
   if len({a,b,c,d})!=4:continue
   for added in [((a,c),(b,d)),((a,d),(b,c))]:
    if any(A[i]>>j&1 for i,j in added):continue
    attempts['legal_switches']+=1;B=A[:]
    for i,j in [(a,b),(c,d),*added]:B[i]^=1<<j;B[j]^=1<<i
    if any(B[i]&B[j] for i,j in added):continue
    attempts['triangle_free']+=1
    if independent(B,(1<<22)-1,7):continue
    attempts['valid']+=1;rb=relation(B);hits=[]
    for target,C in graphs.items():
     mapping=iso(B,C,rb,relations[target])
     if mapping is not None:hits.append((target,mapping))
    assert len(hits)==1,('unclassified or duplicate catalogue type',source,added,hits)
    target,mapping=hits[0];counts[source,target]+=1;witness.setdefault((source,target),{'source':source,'target':target,'removed':[(a,b),(c,d)],'added':added,'isomorphism':mapping})
  print('source',source,'targets',{t:n for (s,t),n in counts.items() if s==source},flush=True)
 todo=set(graphs);components=[]
 while todo:
  seen=set();stack=[min(todo)]
  while stack:
   s=stack.pop()
   if s in seen:continue
   seen.add(s);stack.extend(t for a,t in counts if a==s and t not in seen)
  todo-=seen;components.append(sorted(seen))
 result={'attempts':dict(attempts),'components':components,'transitions':[dict(witness[k],count=n) for k,n in sorted(counts.items())]};Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print('components',components,'attempts',dict(attempts))

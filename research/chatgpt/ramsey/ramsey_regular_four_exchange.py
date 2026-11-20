"""Exhaust all exact four-edge exchanges from both Hall types, without fixing any root. Prune only monotone triangle obstructions after removing all four edges."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json,time
from ramsey_hall_center_conjecture import decode,independent,root_profile
from ramsey_regular_two_switch import relation,iso

def completions(A,B,stubs,added=()):
 if not stubs:yield tuple(sorted(added));return
 a=stubs[0];seen=set()
 for j in range(1,len(stubs)):
  b=stubs[j]
  if b in seen:continue
  seen.add(b)
  if a==b or (A[a]>>b&1) or (B[a]>>b&1) or B[a]&B[b]:continue
  B[a]|=1<<b;B[b]|=1<<a
  yield from completions(A,B,stubs[1:j]+stubs[j+1:],added+(tuple(sorted((a,b))),))
  B[a]^=1<<b;B[b]^=1<<a

if __name__=='__main__':
 data=json.loads(Path(__file__).with_name('ramsey_hall_center_conjecture.json').read_text());graphs={r['record']:decode(r['graph6'].encode()) for r in data['regular']};rels={k:relation(A) for k,A in graphs.items()};report=[];start=time.time()
 for source in (190,191):
  A=graphs[source];edges=[e for e in combinations(range(22),2) if A[e[0]]>>e[1]&1];stats=Counter();counts=Counter();witnesses={};center_stats=Counter()
  for removed in combinations(edges,4):
   stats['removed_quadruples']+=1;B=A[:]
   for i,j in removed:B[i]^=1<<j;B[j]^=1<<i
   additions=set(completions(A,B,tuple(sorted(x for e in removed for x in e))))
   for added in additions:
    stats['triangle_free']+=1;C=B[:]
    for i,j in added:C[i]|=1<<j;C[j]|=1<<i
    assert all(x.bit_count()==6 for x in C)
    if independent(C,(1<<22)-1,7):continue
    stats['valid']+=1;rc=relation(C);hits=[]
    for target,D in graphs.items():
     mapping=iso(C,D,rc,rels[target])
     if mapping is not None:hits.append((target,mapping))
    assert len(hits)==1;target,mapping=hits[0];counts[target]+=1;centers=[v for v in range(22) if root_profile(C,v)['hall_center']];center_stats[target,tuple(centers)]+=1
    witnesses.setdefault(target,{'target':target,'removed':removed,'added':added,'isomorphism':mapping,'output_hall_centers':centers})
  result={'source':source,'stats':dict(stats),'targets':dict(counts),'center_patterns':[{'target':t,'centers':c,'count':n} for (t,c),n in sorted(center_stats.items())],'witnesses':list(witnesses.values())};report.append(result);Path(__file__).with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n');print('source',source,'stats',dict(stats),'targets',dict(counts),'seconds',round(time.time()-start,2),flush=True)

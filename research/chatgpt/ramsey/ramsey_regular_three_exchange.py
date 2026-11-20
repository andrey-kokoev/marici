"""Exhaust all exact three-red-edge exchanges from Hall-center types. Endpoint multiset pairing includes exchanges with shared endpoints, not just three disjoint removed edges."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json
from ramsey_hall_center_conjecture import decode,independent,root_profile
from ramsey_regular_two_switch import relation,iso

def pairings(stubs):
 if not stubs:yield ();return
 a=stubs[0]
 for j in range(1,len(stubs)):
  b=stubs[j]
  if a==b:continue
  for tail in pairings(stubs[1:j]+stubs[j+1:]):yield tuple(sorted((tuple(sorted((a,b))),)+tail))

if __name__=='__main__':
 data=json.loads(Path(__file__).with_name('ramsey_hall_center_conjecture.json').read_text());graphs={r['record']:decode(r['graph6'].encode()) for r in data['regular']};rels={k:relation(A) for k,A in graphs.items()};report=[]
 for source in (190,191):
  A=graphs[source];edges=[e for e in combinations(range(22),2) if A[e[0]]>>e[1]&1];stats=Counter();counts=Counter();witnesses={}
  for removed in combinations(edges,3):
   stats['removed_triples']+=1
   for added in set(pairings(tuple(x for e in removed for x in e))):
    if len(set(added))!=3 or any(A[i]>>j&1 for i,j in added):continue
    stats['legal_exchanges']+=1;B=A[:]
    for i,j in (*removed,*added):B[i]^=1<<j;B[j]^=1<<i
    assert all(x.bit_count()==6 for x in B)
    if any(B[i]&B[j] for i,j in added):continue
    stats['triangle_free']+=1
    if independent(B,(1<<22)-1,7):continue
    stats['valid']+=1;rb=relation(B);hits=[]
    for target,C in graphs.items():
     mapping=iso(B,C,rb,rels[target])
     if mapping is not None:hits.append((target,mapping))
    assert len(hits)==1;target,mapping=hits[0];counts[target]+=1
    witnesses.setdefault(target,{'target':target,'removed':removed,'added':added,'isomorphism':mapping,'output_hall_centers':[v for v in range(22) if root_profile(B,v)['hall_center']]})
  result={'source':source,'stats':dict(stats),'targets':dict(counts),'witnesses':list(witnesses.values())};report.append(result);print(result,flush=True)
 Path(__file__).with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n')

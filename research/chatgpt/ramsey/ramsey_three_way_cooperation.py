"""Exhaust vertex-disjoint triples of individually invalid triangle-free two-edge switches on all ten regular catalogue types. Require all three pairs invalid and the full triple valid."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json
from ramsey_hall_center_conjecture import decode,independent
from ramsey_mutual_repair_conjecture import switches,apply,sevens
from ramsey_regular_two_switch import relation,iso

if __name__=='__main__':
 data=json.loads(Path(__file__).with_name('ramsey_hall_center_conjecture.json').read_text());graphs={r['record']:decode(r['graph6'].encode()) for r in data['regular']};rels={k:relation(A) for k,A in graphs.items()};report=[]
 for source,A in graphs.items():
  moves=list(switches(A));stats=Counter();examples={};counts=Counter();pair_cache={}
  for ids in combinations(range(len(moves)),3):
   selected=[moves[i] for i in ids]
   if any(s['support']&t['support'] for s,t in combinations(selected,2)):continue
   stats['disjoint_triples']+=1;B=A[:]
   for s in selected:B=apply(B,s['removed'],s['added'])
   if independent(B,(1<<22)-1,7):continue
   stats['valid_joint_triples']+=1;valid_pair=False
   for i,j in combinations(ids,2):
    if (i,j) not in pair_cache:
     C=apply(apply(A,moves[i]['removed'],moves[i]['added']),moves[j]['removed'],moves[j]['added']);pair_cache[i,j]=not independent(C,(1<<22)-1,7)
    if pair_cache[i,j]:valid_pair=True;break
   if valid_pair:continue
   stats['irreducible_triples']+=1;rb=relation(B);hits=[]
   for target,C in graphs.items():
    mapping=iso(B,C,rb,rels[target])
    if mapping is not None:hits.append((target,mapping))
   assert len(hits)==1;target,mapping=hits[0];counts[target]+=1
   if target not in examples:
    subset_evidence=[]
    for mask in range(1,8):
     C=A[:]
     for k,s in enumerate(selected):
      if mask>>k&1:C=apply(C,s['removed'],s['added'])
     bad=list(sevens(C));assert bool(bad)==(mask!=7);assert all(not(C[i]&C[j]) for i,j in combinations(range(22),2) if C[i]>>j&1);subset_evidence.append({'mask':mask,'independent_sevens':len(bad),'first':bad[:1]})
    examples[target]={'switches':selected,'subset_evidence':subset_evidence,'isomorphism':mapping}
  row={'source':source,'individually_invalid_switches':len(moves),'stats':dict(stats),'targets':dict(counts),'examples':examples};report.append(row);Path(__file__).with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n');print({k:v for k,v in row.items() if k!='examples'},flush=True)

"""Freeze the early signatures; hold out the complete late covers. Compare like named inputs, including comparator kind, across sampling times."""
import itertools,json
from collections import defaultdict,Counter
from pathlib import Path
D=Path(__file__).resolve().parents[1]/'results'
load=lambda k:json.loads((D/(k+'.json')).read_text())
red=set(map(tuple,load('pne_ramsey_comparison_refinement')['redSignatures']))
g=[defaultdict(dict),defaultdict(dict)];examples=[]
for (late,index),row in {(v['late'],v['index']):v for v in load('pne_four_cover_realizations')}.items():
 for perm in itertools.permutations('01234'):
  cs=[tuple(''.join(sorted(perm[int(i)] for i in pair)) for pair in c) for c in row['contacts']]
  for t in range(0,10,2):
   for j,other in enumerate(cs):
    if j in (t,t+1):continue
    key=(cs[t],j%2,other);ex=cs[t+1];truth=all(set(a).isdisjoint(b) for a,b in zip(ex,other));g[late][key].setdefault(truth,dict(index=index,perm=''.join(perm),tick=t//2,comparatorIndex=j,exit=ex))
counts=Counter();overlap=Counter();sigs=defaultdict(set)
for key,bits in g[1].items():
 entry,kind,other=key;sig=(kind,)+tuple(len(set(a)&set(b)) for a in entry for b in other);pred=sig in red;sigs[sig].update(bits)
 for bit in bits:counts[str((pred,bit))]+=1
 if key in g[0]:
  overlap[str(set(bits)==set(g[0][key]))]+=1
  if set(bits)!=set(g[0][key]) and len(examples)<2:examples.append(dict(entry=entry,kind=kind,other=other,early=g[0][key],late=bits))
out=dict(lateInputs=len(g[1]),ambiguous=sum(len(v)>1 for v in g[1].values()),counts=counts,sharedInputsSameTruth=overlap,lateSignatures=[(s,sorted(v)) for s,v in sorted(sigs.items())],examples=examples);print(out);(D/'pne_ramsey_late_exit_transfer.json').write_text(json.dumps(out,indent=2)+'\n')

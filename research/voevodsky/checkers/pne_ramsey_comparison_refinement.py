"""Compare only co-occurring contacts in realized early-exit covers. Freeze the comparison contact's two named pairs and kind, not a vertex chosen after observing adjacency. Enumerate coefficient renamings consistently on each whole cover."""
import itertools,json
from collections import defaultdict,Counter
from pathlib import Path
D=Path(__file__).resolve().parents[1]/'results'
covers=json.loads((D/'pne_four_cover_realizations.json').read_text());groups=defaultdict(dict)
for row in {v['index']:v for v in covers if not v['late']}.values():
 for perm in itertools.permutations('01234'):
  contacts=[tuple(''.join(sorted(perm[int(i)] for i in pair)) for pair in c) for c in row['contacts']]
  for t in range(0,10,2):
   for j,other in enumerate(contacts):
    if j in (t,t+1):continue
    key=(contacts[t],j%2,other);ex=contacts[t+1];red=all(set(a).isdisjoint(b) for a,b in zip(ex,other));groups[key].setdefault((ex,red),dict(index=row['index'],perm=''.join(perm),tick=t//2,comparatorIndex=j,exit=ex,red=red))
hist=Counter();example=None
for k,v in groups.items():
 bits={b for _,b in v};hist[(len(v),len(bits))]+=1
 if len(bits)==2 and example is None:
  example=dict(entry=k[0],comparisonKind=('PN','NE')[k[1]],comparison=k[2],witnesses=[next(x for x in v.values() if x['red']==b) for b in [False,True]])
signatures=defaultdict(set)
for (entry,kind,other),v in groups.items():
 sig=(kind,)+tuple(len(set(a)&set(b)) for a in entry for b in other);signatures[sig].update(bit for _,bit in v)
assert all(len(bits)==1 for bits in signatures.values())
out=dict(redSignatures=sorted(s for s,bits in signatures.items() if True in bits),signatureCount=len(signatures),groups=len(groups),hist=[dict(distinctExits=k[0],distinctBits=k[1],groups=n) for k,n in sorted(hist.items())],example=example); print(out);(D/'pne_ramsey_comparison_refinement.json').write_text(json.dumps(out,indent=2)+'\n')

"""Ignore global cover labels. Apply each local advance+column exchange to the multiset of marked contact records. Test closure with multiplicity; keep PN and NE distinct."""
import json
from pathlib import Path
from collections import Counter
D=Path(__file__).resolve().parents[1]/'results';data=json.loads((D/'pne_center_local_advance.json').read_text())['rows'];runs={}
for x in data:runs.setdefault((tuple(x['perm']),x['prep'],x['late']),[]).append(x)
out=[];hist=Counter()
for (perm,prep,late),early in runs.items():
 if late:continue
 other=runs[perm,prep,True];early=sorted(early,key=lambda x:x['j']);other=sorted(other,key=lambda x:x['j']);assert all(x['rename']==y['rename'] for x,y in zip(early,other))
 for mask in range(32):
  xs=[other[j] if j%2 and mask>>(j//2)&1 else e for j,e in enumerate(early)];C=Counter((x['j']%2,*x['contact']) for x in xs);accepted=[]
  for x in xs:
   p=x['rename'];f=lambda s:''.join(sorted(p[int(v)] for v in s));assert [f(x['contact'][1]),f(x['contact'][0])]==x['contact'];T=Counter()
   for (k,a,b),n in C.items():T[k,f(b),f(a)]+=n
   if T==C:accepted.append(x['j'])
  balanced=all(len({x['contact'][k] for x in xs})==10 for k in (0,1));hist[balanced,len(accepted),len({xs[j]['rename'] for j in accepted})]+=1;out.append(dict(perm=perm,prep=prep,mask=mask,balanced=balanced,accepted=accepted))
print(hist);print(out[:4]);(D/'pne_period_occurrence_symmetry.json').write_text(json.dumps(out,indent=2)+'\n')

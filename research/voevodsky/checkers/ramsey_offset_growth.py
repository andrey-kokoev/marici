"""Scan SAME cyclic offset rule on two predecessor orders and every allowed positive root degree. Tests whole Cayley completion (including J-J edges), not endpoint catalogue. Empty degree skipped: cannot improve on best. Purely retrospective family selection."""
import json,itertools,collections
from ramsey_retention_slice import D,check
P=D.parent;out={}
for k,maximum in [(4,8),(5,13),(6,17),(7,22),(8,27)]:
 runs=[]
 for n in (maximum-1,maximum):
  for d in range(1,k+1):
   m=n+d+1
   if m%2 and d%2:continue
   good=[];tested=0
   for ds in itertools.combinations(range(1,(m+1)//2),d//2):
    J=set(ds)|{m-v for v in ds}|({m//2} if d%2 else set());tested+=1
    if any((u-v)%m in J for u,v in itertools.combinations(J,2)):continue
    C=sorted(set(range(m))-{0}-J);a=[sum(1<<i for i,y in enumerate(C) if (y-x)%m in J) for x in C];assert len(C)==n
    if not check(a,(1<<n)-1,3,k):continue
    # A blue (k+1)-clique anywhere can be translated to contain 0, contradicting legality of the blue core. Replay directly.
    g=[sum(1<<((x+j)%m) for j in J) for x in range(m)];assert check(g,(1<<m)-1,3,k+1);good.append(sorted(J))
   runs.append(dict(n=n,d=d,m=m,tested=tested,successful=good))
 out[k]=runs;print(k,max((r['m'] for r in runs if r['successful']),default=None),[(r['n'],r['d'],len(r['successful'])) for r in runs if r['successful']],flush=True)
(P/'ramsey_offset_growth.json').write_text(json.dumps(out)+'\n')

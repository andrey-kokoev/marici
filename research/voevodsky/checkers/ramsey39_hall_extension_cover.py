"""Screen all eight-regular circulants on Z/35 and test one per multiplier orbit. Hall-lift six of every retained eight, then check the other 13 pairs."""
from itertools import combinations
from math import gcd
from pathlib import Path
import runpy,json
root=Path(__file__).resolve().parents[2];h=runpy.run_path(str(root/'chatgpt/ramsey/ramsey_cyclic_quotient_constructor.py'));P=h['P'];bundles=[b for b in h['B'] if b<=h['outputs'][0]];N=35;full=(1<<N)-1;out=[];passed=0
for ds in combinations(range(1,18),4):
 S=set(ds)|{35-d for d in ds};orbit={tuple(sorted(min(k*d%35,(-k*d)%35) for d in ds)) for k in range(1,35) if gcd(k,35)==1}
 if ds!=min(orbit) or any((a+b)%35 in S for a in S for b in S):continue
 adj=[sum(1<<((i+d)%35) for d in S) for i in range(35)];ss=[]
 def walk(a,c,d):
  if d==8:ss.append(a);return not c
  while c.bit_count()>=8-d:
   b=c&-c;c-=b
   if not walk(a|b,c&~adj[b.bit_length()-1],d+1):return False
  return True
 if not walk(0,full,0):continue
 passed+=len(orbit);allbits=(1<<len(ss))-1
 incident=[sum(1<<j for j,s in enumerate(ss) if s>>i&1) for i in range(35)];covers=[]
 for s in ss:
  m=allbits
  while s:
   b=s&-s;s-=b;m&=~incident[b.bit_length()-1]
  covers.append(m)
 left=allbits;keep=[];pairs=set()
 while left:
  j=max(range(len(ss)),key=lambda j:(covers[j]&left).bit_count());assert covers[j]&left;left&=~covers[j];v=[i for i in range(35) if ss[j]>>i&1];keep.append(v);checks={(v[P[i][0]],v[P[i][1]]) for b in bundles for i,_ in b}|{(v[i],v[j]) for j in (6,7) for i in range(j)};assert len(checks)==28 and all(not(adj[i]>>j&1) for i,j in checks);pairs.update(checks)
 out.append(dict(distances=ds,orbit=len(orbit),eights=len(ss),cover=keep,distinctPairs=len(pairs)))
print('systems',passed,[(x['distances'],x['orbit'],x['eights'],len(x['cover']),x['distinctPairs']) for x in out]);(root/'voevodsky/results/ramsey39_hall_extension_cover.json').write_text(json.dumps(out,indent=1)+'\n')

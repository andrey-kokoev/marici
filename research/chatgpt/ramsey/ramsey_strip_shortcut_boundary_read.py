"""Does a compressed square run touch zero, one or both endpoint columns at its bounding midpoints? Verify the local rule across all four pole frames using actual matching signs as ground truth, retaining failures and ambiguous completions."""
from ramsey_strip_prism_proof import labels,rep,E,r
from ramsey_strip_witness_orbits import fill,edges
from pathlib import Path
from collections import Counter
from functools import lru_cache
from itertools import combinations
import json
records=json.loads(Path(__file__).with_name('ramsey_strip_length_control.json').read_text());words={tuple(labels[rep(x)] for x in z['path'][1:-1]):tuple(z['path']) for z in records};assert len(words)==96
@lru_cache(None)
def signs(w):
 p=words[w];c=p+tuple(r[x] for x in p[-2:0:-1]);out=set()
 for e in fill(set(range(30))-set(c)):
    for a in (0,1):
        m=e|{edges(c[i],c[(i+1)%len(c)]) for i in range(a,len(c),2)};out.add((-1)**sum((i-k)*(j-l)<0 for (i,j),(k,l) in combinations(m,2)))
 return tuple(sorted(out))
H=Counter();local={}
for w in words:
 for i in range(len(w)-3):
    if tuple(sorted((w[i],w[i+3]))) not in E:continue
    v=w[:i+1]+w[i+3:];ends={w[0],w[-1]};lft,right=w[i-1],w[i+4];assert lft.isupper() and right.isupper();n=int(lft in ends)+int(right in ends);s,t=signs(w),signs(v);H[n,s,t]+=1
    assert bool(s)==bool(t)
    if s:assert (s,t)==[((1,),(1,)),((1,),(-1,)),((-1,),(-1,1))][n]
    local.setdefault((w[i:i+4],lft,right),set()).add((s,t))
print('endpoint contacts, long types, short types:',H);print('same flanked arc with success and failure:',sum(len(x)>1 for x in local.values()))

"""Pure-integer replay; test every multiset of six inclusion-maximal columns."""
from itertools import combinations_with_replacement
from pathlib import Path
from fractions import Fraction
import json
r=json.loads((Path(__file__).resolve().parents[1]/'results/ramsey_split_fractional_gap.json').read_text());n=r['n'];edges=[1<<u|1<<v for u,v in r['edges']];assert all(sum(e&t==e for e in edges)<3 for t in range(1<<n) if t.bit_count()==3);I=[s for s in range(1,1<<n) if not any(e&s==e for e in edges)];F=[s for s in I if not any(s!=t and s&t==s for t in I)];assert F==r['fac'];w=list(map(Fraction,r['weights']));a=r['a'];assert sum(w)==a and all(sum(v for f,v in zip(F,w) if f&s)>=s.bit_count() for s in I);req=[sum(1<<i for i,s in enumerate(I) if s.bit_count()==k) for k in range(7)];masks=[sum(1<<i for i,s in enumerate(I) if f&s) for f in F];alpha=max(map(int.bit_count,I));assert alpha<a and a==6

def valid(fs):
    h=[0]*(alpha+1);h[0]=(1<<len(I))-1
    for f in fs:
        for j in range(alpha,0,-1):h[j]|=h[j-1]&f
    return all(h[j]&req[j]==req[j] for j in range(1,alpha+1))
count=0
for fs in combinations_with_replacement(masks,a):assert not valid(fs);count+=1
witness=next(fs for fs in combinations_with_replacement(range(len(F)),a+1) if valid([masks[i] for i in fs]));print('alpha',alpha,'rows',len(I),'fractional mass',sum(w),'rejected multisets',count,'seven columns',[F[i] for i in witness])

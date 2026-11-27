"""Minimal multi-link repairs from parent exclusions. Check each minimal repair on full graph constraints via port subsets."""
from itertools import combinations
from functools import reduce
from collections import Counter
from pathlib import Path
import json


def run(k, on_two=None):
    full=(1<<k)-1;rows=[sum(1<<i for i in s) for s in combinations(range(k),3) if min(s[1]-s[0],s[2]-s[1])>=2];R=set(rows);pos=lambda x:[i+1 for i in range(k) if x>>i&1];caps=[]
    for x in range(full+1):
        n=0
        while x:b=x&-x;n+=1;x&=~(b|b<<1)
        caps.append(n)
    counts=Counter();ex={}
    for c in rows:
        moves=[3<<i for i in range(k-1) if (c&(3<<i)).bit_count()==1 and c^(3<<i) in R]
        for a,b in combinations(moves,2):
            if a&b or c^a^b not in R:continue
            p=(c,c^a,c^b);sub=[(sum(1<<i for i in z),reduce(int.__or__,(p[i] for i in z),0)) for n in range(4) for z in combinations(range(3),n)]
            if any(h.bit_count()+caps[full^u]>=7 for h,u in sub):continue
            singles=[v for v in rows if v not in p and all(h.bit_count()+1+caps[full&~(u|v)]<7 for h,u in sub)]
            for s,t in combinations(singles,2):
                mask=full&~(s|t);bad=[h for h,u in sub if h.bit_count()+caps[mask&~u]>=5];
                if not bad:continue
                opts={i:[j for j,v in enumerate((s,t),3) if not row&v] for i,row in enumerate(p)};available=[i for i,js in opts.items() if js];ss=(*p,s,t)
                if not s&t:cost=1;links=[(3,4)]
                else:
                    for n in range(1,len(available)+1):
                        cut=next((z for z in combinations(available,n) if all(any(h>>i&1 for i in z) for h in bad)),None)
                        if cut is not None:break
                    else:cut=None
                    cost=len(cut) if cut else 'impossible';links=[(i,opts[i][0]) for i in (cut if cut else available)]
                if cost==2 and on_two is not None:on_two(ss,bad,opts)
                # Test witness links, or saturate every eligible link for an impossibility certificate.
                if cost=='impossible':links=[(i,j) for i in available for j in opts[i]]
                assert all(not ss[i]&ss[j] for i,j in links) and not any(all(e in links for e in combinations(tri,2)) for tri in combinations(range(5),3))
                survivors=[]
                for m in range(32):
                    if any((m>>i)&(m>>j)&1 for i,j in links):continue
                    u=reduce(int.__or__,(v for i,v in enumerate(ss) if m>>i&1),0)
                    if caps[full^u]+m.bit_count()>=7:survivors.append(m)
                assert bool(survivors)==(cost=='impossible');counts[str(cost)]+=1
                if cost!=1 and (str(cost) not in ex or (cost=='impossible' and not ex[str(cost)]['links'] and links)):
                    ex[str(cost)]=dict(rows=list(map(pos,ss)),links=[(i+1,j+1) for i,j in links],surviving_port_masks=survivors)
    return dict(width=k,counts=counts,examples=ex)
if __name__=='__main__':
    D=Path(__file__).resolve().parents[1]/'results';data=[run(k) for k in range(7,13)];prev=json.loads((D/'ramsey_corner_essential.json').read_text());assert all(sum(x['counts'].values())==y['counts'].get('fail',0) and x['counts']['1']==y['counts'].get('has_single_repair',0) for x,y in zip(data,prev));print(data);(D/'ramsey_corner_joint_repairs.json').write_text(json.dumps(data,indent=2)+'\n')

"""Leave-one-corner-out path capacity; compare one-link predictions to direct clique enumeration on examples and earlier full census totals."""
from functools import reduce
from itertools import combinations
from collections import Counter
from pathlib import Path
import json


def run(k):
    F=(1<<k)-1; rows=[sum(1<<i for i in q) for q in combinations(range(k),3) if min(q[1]-q[0],q[2]-q[1])>=2];R=set(rows);out=Counter();examples={};caps=[];pos=lambda x:[i+1 for i in range(k) if x>>i&1]
    for x in range(F+1):
        n=0
        while x:b=x&-x;n+=1;x&=~(b|b<<1)
        caps.append(n)
    for c in rows:
        moves=[3<<i for i in range(k-1) if (c&(3<<i)).bit_count()==1 and c^(3<<i) in R]
        for i,j in combinations(moves,2):
            if i&j or c^i^j not in R:continue
            p=(c,c^i,c^j);U=p[0]|p[1]|p[2];subs=[(sum(1<<h for h in hs), reduce(int.__or__,(p[h] for h in hs),0)) for d in range(4) for hs in combinations(range(3),d)]
            if any(h.bit_count()+caps[F^u]>=7 for h,u in subs):continue
            singles=[s for s in rows if s not in p and all(h.bit_count()+1+caps[F&~(u|s)]<7 for h,u in subs)]
            for s,t in combinations(singles,2):
                V=F&~(s|t);trial=lambda u:caps[V&~u];base=trial(0);one=[1+trial(r) for r in p];two={(a,b):2+trial(p[a]|p[b]) for a,b in combinations(range(3),2)};assert two[1,2]==2+trial(U)<5
                drop=[]
                for a,b in ((1,2),(0,2),(0,1)):drop.append(max(base,one[a],one[b],two[a,b]))
                if max(*drop,3+trial(U))<5:continue
                essential=[z for z,v in enumerate(drop) if v<5]+[3,4];ss=(*p,s,t);allowed=[(a,b) for a,b in combinations(range(5),2) if not ss[a]&ss[b]];rep=[e for e in allowed if all(h in essential for h in e)]
                # Independent subset test for every allowed link, not just total repair counts.
                for a,b in allowed:
                    safe=all(h.bit_count()+2+trial(u)<7 for h,u in subs if (h|24)&((1<<a)|(1<<b))!=((1<<a)|(1<<b)))
                    assert safe==((a,b) in rep)
                out['fail']+=1;out['has_single_repair']+=bool(rep);out['all_three_essential']+=len(essential)==5;out['no_parent_essential']+=len(essential)==2;out['elbow_essential']+=0 in essential;out['nonessential_only_via_two_remaining']+=sum(v>=5 and max(base,*[one[z] for z in range(3) if z!=d])<5 for d,v in enumerate(drop))
                if rep and len(rep)<len(allowed) and not examples:examples=dict(rows=list(map(pos,ss)),scores=drop,essential=essential,repairs=rep,zero_based=True)
    return dict(width=k,counts=out,example=examples)
if __name__=='__main__':
    D=Path(__file__).resolve().parents[1]/'results';prev=json.loads((D/'ramsey_partial_square_bound.json').read_text());res=[run(z['width']) for z in prev];assert all(all(n['counts'].get(key,0)==o['counts'].get(key,0) for key in ('fail','has_single_repair')) for n,o in zip(res,prev));print(res);(D/'ramsey_corner_essential.json').write_text(json.dumps(res,indent=2)+'\n')

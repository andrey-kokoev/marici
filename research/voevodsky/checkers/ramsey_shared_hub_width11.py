"""Test the width-ten W rule out of chart against a destination test on arbitrary path runs."""
from collections import Counter
from functools import lru_cache, reduce
from itertools import combinations
from pathlib import Path
import json


def run(k):
    full=(1<<k)-1;rows=[sum(1<<i for i in q) for q in combinations(range(k),3) if min(q[1]-q[0],q[2]-q[1])>=2];R=set(rows);cap=[];must=[];fmt=lambda x:[i+1 for i in range(k) if x>>i&1]
    for m in range(full+1):
        n=0;required=0;i=0
        while i<k:
            if not (m>>i&1):i+=1;continue
            j=i+1
            while m>>j&1:j+=1
            n+=(j-i+1)//2
            if (j-i)%2:required|=sum(1<<v for v in range(i,j,2))
            i=j
        cap.append(n);must.append(required)
    @lru_cache(None)
    def safe(ss):return all(n+cap[full&~reduce(int.__or__,q,0)]<7 for n in range(len(ss)+1) for q in combinations(ss,n))
    counts=Counter();seen=set();ex={}
    for C in rows:
        moves=[3<<i for i in range(k-1) if (C&(3<<i)).bit_count()==1 and C^(3<<i) in R]
        for a in moves:
            B=C^a;M=C&B
            for b in moves:
                if a&b or C^a^b not in R:continue
                E=C^b;y=C&b;Y=E&b;fixed=C^y
                singles=[u for u in rows if u not in (C,B,E) and safe(tuple(sorted((C,B,E,u))))]
                for T in singles:
                    if T&(C|B):continue
                    for S in singles:
                        if S==T or not S&T:continue
                        V=full&~(S|T);W=V&~(C|B);Z=M&~S
                        if min(cap[V&~C],cap[V&~B])<4:continue
                        # Count each seed orientation once; the corner and its neighbor force links to T.
                        old=bool(Y&W) and all((((1<<(i+1))|((1<<i)>>1))&W).bit_count()>=1+int(y==(1<<i)) for i in range(k) if Z>>i&1)
                        H=V&~fixed;pred=cap[V]<5 and (cap[H]<4 or (cap[H]==4 and bool(Y&must[H])));actual=cap[V]<5 and cap[V&~E]<4;assert pred==actual
                        counts['seeds']+=1;counts['success']+=int(actual);counts['false_accept']+=int(old and not actual);counts['false_reject']+=int(not old and actual)
                        if actual:seen.add((C,frozenset((B,E)),frozenset((S,T))))
                        tag='false_accept' if old and not actual else 'false_reject' if actual and not old else ('pass' if actual else 'blocked');ex.setdefault(tag,dict(C=fmt(C),B=fmt(B),S=fmt(S),T=fmt(T),E=fmt(E),W=fmt(W),V=fmt(V),H=fmt(H),required=fmt(must[H]),y=fmt(y),Y=fmt(Y)))
    assert len(seen)==(456 if k==10 else 24);return dict(width=k,counts=dict(counts),examples=ex)
if __name__=='__main__':
    data=[run(k) for k in (10,11)];print(data);(Path(__file__).resolve().parents[1]/'results/ramsey_shared_hub_width11.json').write_text(json.dumps(data,indent=2)+'\n')

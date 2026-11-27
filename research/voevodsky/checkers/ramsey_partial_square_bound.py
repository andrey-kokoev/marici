"""Delete one corner of literal Excel squares. Test the inside-union capacity bound."""
from itertools import combinations
from collections import Counter
from pathlib import Path
import json


def run(k):
    rows=[sum(1<<i for i in s) for s in combinations(range(k),3) if min(s[1]-s[0],s[2]-s[1])>=2];R=set(rows);parents=set();sites=lambda x:[i+1 for i in range(k) if x>>i&1]
    for s in rows:
        mv=[3<<i for i in range(k-1) if (s&(3<<i)).bit_count()==1 and s^(3<<i) in R]
        for a,b in combinations(mv,2):
            if not a&b and s^a^b in R:parents.update(combinations(sorted([s,s^a,s^b,s^a^b]),3))
    full=(1<<k)-1;cap=[]
    for u in range(1<<k):
        v=u;n=0
        while v:bit=v&-v;v&=~(bit|bit<<1);n+=1
        cap.append(n)
    counts=Counter();examples={}
    for p in sorted(parents):
        H=[(0,0,0)]
        for i,r in enumerate(p):H+=[(b|1<<i,u|r,h+1) for b,u,h in H]
        U=H[-1][1];m=len(p)
        if any(h+cap[full^u]>=7 for b,u,h in H):continue
        singles=[r for r in rows if r not in p and all(h+1+cap[full^(u|r)]<7 for b,u,h in H)]
        for s,t in combinations(singles,2):
            counts['trials']+=1;V=full^(s|t);cl=[b|24 for b,u,h in H if h+2+cap[V&~u]>=7];assert all(cap[U&V&~u]>=m-h for b,u,h in H if b|24 in cl);assert cap[V&~U]<=5-m
            if not cl:continue
            counts['fail']+=1;proper=any(b!=31 for b in cl);counts['proper_subset_witness']+=proper
            ss=(*p,s,t);edges=[(i,j) for i,j in combinations(range(5),2) if not ss[i]&ss[j]];good=[(i,j) for i,j in edges if all((b>>i)&(b>>j)&1 for b in cl)];bad=[e for e in edges if e not in good];counts['has_ineffective_allowed_link']+=bool(bad);counts['has_single_repair']+=bool(good)
            label='both' if good and bad else 'only_ineffective' if bad else 'other'
            if bad and label not in examples:
                i,j=bad[0];b=next(b for b in cl if not ((b>>i)&(b>>j)&1));u=0
                for n,r in enumerate(ss):
                    if b>>n&1:u|=r
                avail=full^u;chosen=[]
                while avail and len(chosen)<7-b.bit_count():v=avail&-avail;chosen.append(v.bit_length());avail&=~(v|v<<1)
                examples[label]=dict(ports=list(map(sites,ss)),ineffective_pair=[i+1,j+1],effective_pairs=[(x+1,y+1) for x,y in good],surviving_ports=[x+1 for x in range(5) if b>>x&1],surviving_sites=chosen)
    return dict(width=k,counts=counts,examples=examples)
if __name__=='__main__':
    out=[run(k) for k in (7,8,9)];print(out);(Path(__file__).resolve().parents[1]/'results/ramsey_partial_square_bound.json').write_text(json.dumps(out,indent=2)+'\n')

"""All proper prefix cuts, all live equal-future classes. Compare local blocker guard,
exact one-edge moves and smallest simultaneous-move radius connecting each class.
Finite oracle only: futures obtained independently from full labeled colorings."""
import json
from collections import defaultdict,Counter
from itertools import combinations
from pathlib import Path

def run(n,k):
    E=[(i,j) for j in range(n) for i in range(j)];m=len(E)
    pats=[(v,sum(1<<E.index(e) for e in combinations(t,2))) for r,v in ((3,1),(k,0)) for t in combinations(range(n),r)];poss=[x for x in range(1<<m) if all((x&s!=s if v else x&s!=0) for v,s in pats)]
    per=[];example=None
    for cut in range(1,m):
        mask=(1<<cut)-1;f=defaultdict(list)
        for x in poss:f[x&mask].append(x>>cut)
        groups=defaultdict(list)
        for x,s in f.items():groups[tuple(s)].append(x)
        exact=guard=0;radius=Counter();miss=None
        for suffix,g in groups.items():
            G=set(g);nearest=[]
            for x in g:
                for i in range(cut):
                    b=1<<i;y=x^b
                    if x>=y:continue
                    ok=all((mask&~b&s&(~x if v else x))!=0 for v,s in pats if s&b)
                    if ok:assert y in G;guard+=1
                    if y in G:
                        exact+=1
                        if not ok and miss is None:miss=(x,y,len(suffix))
            if len(g)<2:continue
            # Kruskal on the Hamming metric; maximal edge of a minimum spanning tree.
            parent={x:x for x in g}
            def root(x):
                while parent[x]!=x:parent[x]=parent[parent[x]];x=parent[x]
                return x
            cnt=len(g);buckets=defaultdict(list)
            for x,y in combinations(g,2):buckets[(x^y).bit_count()].append((x,y))
            for d in sorted(buckets):
                for x,y in buckets[d]:
                    a,b=root(x),root(y)
                    if a!=b:parent[a]=b;cnt-=1
                    if cnt==1:break
                if cnt==1:break
            radius[d]+=1
            if d>1 and (example is None or d>example['radius']):example=dict(cut=cut,group=sorted(g)[:15],size=len(g),suffix=list(suffix)[:15],radius=d)
        per.append(dict(cut=cut,exact=exact,guard=guard,radius=dict(radius),first_missed=miss))
    totals=Counter();
    for t in per:totals.update(t['radius'])
    return dict(n=n,k=k,models=len(poss),guard=sum(t['guard'] for t in per),exact=sum(t['exact'] for t in per),group_radius=dict(sorted(totals.items())),example=example,cuts=per)
if __name__=='__main__':
    out=[run(n,k) for n,k in ((5,3),(5,4),(6,4))];print(json.dumps([{k:v for k,v in r.items() if k!='cuts'} for r in out],indent=1));(Path(__file__).resolve().parents[1]/'results/ramsey_guard_connectivity.json').write_text(json.dumps(out,indent=1)+'\n')

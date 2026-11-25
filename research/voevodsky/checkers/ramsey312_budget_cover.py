"""Exact total-budget-six cover search. Every class of capacity k contains one common red neighbor and misses an independent (11-k)-set. Six restored originals saturate every budget-six cover, hence classes partition the originals."""
from ramsey312_google_two_step import *
from itertools import combinations
from functools import lru_cache,reduce
from operator import and_,or_

def run(d,s):
 h=F^sum(1<<i for i in d);A=[adj[i]&h for i in d];assert len(A)==len(set(A))==6 and set(A)<=set(s);full=(1<<len(s))-1;col=[sum(1<<j for j,x in enumerate(s) if x>>v&1) for v in range(52)];orig=sum(1<<s.index(x) for x in A);blocks={};T=sum(1<<i for i in [1,9,12,31,33,45,49,50,51]);known=(1<<14,T)
 for m in range(1,64):
    aa=[A[i] for i in bits(m)];k=len(aa);b=reduce(and_,aa);p=h&~reduce(or_,aa);choices={};
    if b:
        for t in sets(p,11-k):
            miss=full
            for v in bits(t):miss&=~col[v]
            for v in bits(b):
                row=miss&col[v];assert (row&orig).bit_count()==k;choices.setdefault(row,(1<<v,t))
    mx={}
    for row in sorted(choices,key=int.bit_count,reverse=True):
        if not any(row&~z==0 for z in mx):mx[row]=choices[row]
    blocks[m]=mx
 def rec(groups,rem):
    if not groups:return [] if not rem else None
    poss=[reduce(or_,blocks[m],0) for m in groups];
    if rem&~reduce(or_,poss,0):return None
    opts=[]
    for i,m in enumerate(groups):
        need=rem&~reduce(or_,poss[:i]+poss[i+1:],0);cands=[z for z in blocks[m] if not need&~z];opts.append((len(cands),i,cands))
    _,i,cands=min(opts);m=groups[i]
    for z in sorted(cands,key=lambda z:(z&rem).bit_count(),reverse=True):
        sol=rec(groups[:i]+groups[i+1:],rem&~z)
        if sol is not None:return [(m,*blocks[m][z])]+sol
    return None
 fixed=col[14]&~reduce(or_,(col[v] for v in bits(T)),0);m=sum(1<<i for i,x in enumerate(A) if x&known[0] and not x&T);fixedsol=None
 if m.bit_count()==2 and not T&~h:
    fixedsol=rec([1<<i for i in range(6) if not m>>i&1],full&~fixed)
    if fixedsol is not None:fixedsol=[(m,*known)]+fixedsol
 def partitions(mask):
    if not mask:yield [];return
    b=mask&-mask;m=mask
    while m:
        if m&b and blocks[m]:
            for rest in partitions(mask^m):yield [m,*rest]
        m=(m-1)&mask
 sol=fixedsol;tested=0
 if sol is None:
    for gs in sorted(partitions(63),key=lambda gs:(6-len(gs),gs)):
        tested+=1;sol=rec(gs,full)
        if sol is not None:break
 if sol is not None:
    assert sum(m.bit_count() for m,b,t in sol)==6 and all(any(x&b and not x&t for m,b,t in sol) for x in s);assert all(t.bit_count()==11-m.bit_count() and not (b|t)&~h and all(not adj[v]&t for v in bits(t)) for m,b,t in sol)
 return dict(d=d,supports=len(s),fixed=fixedsol is not None,cert=sol,partitions_tried=tested,maximal_class_counts={str(m):len(v) for m,v in blocks.items() if v})
if __name__=='__main__':
 out=[]
 for f in sys.argv[1:]:
    for l in open(f):
        z=list(map(int,l.split()));r=run(list(bits(z[0])),z[1:]);out.append(r);print(r['d'],r['supports'],r['fixed'],r['cert'],r['partitions_tried'],flush=True)
 (D/'ramsey312_budget_cover.json').write_text(json.dumps(out))

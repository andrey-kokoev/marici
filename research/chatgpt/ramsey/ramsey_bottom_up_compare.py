"""Grow all (3,k) graphs from empty; use the reverse map only after generating a level."""
from ramsey_border_order import graph,key
import gzip,sys
from pathlib import Path

def children(n,m,k):
    g=graph(n,m);ind=[0];adj=g.get_adjlist()
    for i in range(n):
        mask=sum(1<<j for j in adj[i]);ind += [s|1<<i for s in ind if not s&mask]
    must=[s for s in ind if s.bit_count()==k-1];offset=n*(n-1)//2
    for p in ind:
        if all(p&s for s in must):yield key(graph(n+1,m|(p<<offset)))

def audit(k,limit):
    pool={0};eligible={}
    if k==5:
        with gzip.open(Path(__file__).with_name('ramsey_border_35_13_to_0.tsv.gz'),'rt') as f:
            next(f)
            for row in f:
                n,c,p,_=row.split();n=int(n);eligible.setdefault(n,set()).add(int(c,16));eligible.setdefault(n+1,set()).add(int(p,16))
    for n in range(limit+1):
        if n in eligible:assert eligible[n]<=pool
        print(n,len(pool),len(eligible[n]) if n in eligible else '-',flush=True)
        if n in eligible and pool-eligible[n] and n<=5:print('excluded:',[graph(n,m).get_edgelist() for m in pool-eligible[n]])
        if n<limit:pool={c for m in pool for c in children(n,m,k)}
if __name__=='__main__':audit(*map(int,sys.argv[1:]))

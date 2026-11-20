"""Exact border/orbit audit for a fixed sample of unmarked 26-address bases.
Select 8 maximum hosts uniformly without replacement, all 27 one-vertex deletions.
No restriction to returns to the eight input hosts. Run with igraph.
"""
from ramsey_border_order import unpack,key,graph
from collections import Counter,defaultdict
from random import Random
from urllib.request import urlopen
import gzip

def main():
    lines=gzip.decompress(urlopen('https://users.cecs.anu.edu.au/~bdm/data/r38_27.g6.gz',timeout=30).read()).splitlines();assert len(lines)==477142
    ids=sorted(Random(38).sample(range(len(lines)),8));sources=defaultdict(set)
    for i in ids:
        g=unpack(lines[i]);p=key(g)
        for v in range(27):
            h=g.copy();h.delete_vertices(v);sources[key(h)].add(p)
    totals=Counter();all_out=set();example=None
    for m,src in sources.items():
        g=graph(26,m);ind=[0]
        for i,nb in enumerate(g.get_adjlist()):
            a=sum(1<<j for j in nb);ind.extend([x|(1<<i) for x in ind if not x&a])
        assert max(x.bit_count() for x in ind)==7
        opts=ind
        for seven in ind:
            if seven.bit_count()==7:opts=[x for x in opts if x&seven]
        # Canonical child mask from every actual border (also checks symmetry pruning).
        children={p:key(graph(27,m|(p<<325))) for p in opts};distinct=set(children.values());assert src<=distinct
        G=g.get_automorphisms_vf2();rem=set(opts);out=set();orbits=0
        while rem:
            p=next(iter(rem));vs=[i for i in range(26) if p>>i&1];orb={sum(1<<a[i] for i in vs) for a in G};assert orb<=rem and {children[q] for q in orb}=={children[p]};rem-=orb;out.add(children[p]);orbits+=1
        assert out==distinct;all_out.update(out);totals.update(dict(raw=len(opts),orbits=orbits,links=len(out),before=int(len(opts)>orbits),after=int(orbits>len(out))))
        if orbits>len(out) and example is None:example=(hex(m),len(opts),orbits,len(out))
    print('source records (1-based)',[i+1 for i in ids]);print('unique bases',len(sources),'counts',totals,'distinct final states',len(all_out),'within-base example',example)
if __name__=='__main__':main()

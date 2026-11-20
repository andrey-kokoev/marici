"""Exact state-orbit tests for known order-22 hosts and eligible order-21 bases.
Run: uv run --with igraph python research/chatgpt/ramsey/ramsey_37_state_symmetry.py
"""
from collections import Counter,defaultdict
from pathlib import Path
import gzip
from ramsey_border_order import graph,key

def main():
    expected=defaultdict(set)
    with gzip.open(Path(__file__).with_name('ramsey_border_37_22_to_20.tsv.gz'),'rt') as f:
        next(f)
        for row in f:
            n,c,p,_=row.split()
            if n=='21':expected[int(c,16)].add(int(p,16))
    hosts=set.union(*expected.values());raw=red=0;ranges=[];asym=0
    for p in hosts:
        g=graph(22,p);G=g.get_automorphisms_vf2();arcs={(i,j) for i in range(22) for j in g.neighbors(i)};raw+=len(arcs);count=0
        while arcs:
            i,j=next(iter(arcs));arcs.difference_update((a[i],a[j]) for a in G);count+=1
        red+=count;ranges.append(count);asym+=len(G)==1
    print('first arrows: hosts/raw/classes/range/asymmetric',len(hosts),raw,red,(min(ranges),max(ranges)),asym,flush=True)
    raw=red=reduced=0
    for m,want in expected.items():
        g=graph(21,m);I=[0]
        for i,nb in enumerate(g.get_adjlist()):
            adj=sum(1<<j for j in nb);I.extend([s|1<<i for s in I if not s&adj])
        six=[s for s in I if s.bit_count()==6];opts={s for s in I if all(t&s for t in six)};before=len(opts);raw+=before
        G=g.get_automorphisms_vf2();actual=set();cnt=0
        while opts:
            p=next(iter(opts));digits=[i for i in range(21) if p>>i&1];orb={sum(1<<a[i] for i in digits) for a in G};assert orb<=opts;opts-=orb;cnt+=1
            h=g.copy();h.add_vertices(1);h.add_edges([(i,21) for i in digits]);actual.add(key(h))
        assert actual==want;red+=cnt;reduced+=cnt<before
    print('borders: bases/raw/classes/reduced bases/distinct base-to-host links',len(expected),raw,red,reduced,sum(map(len,expected.values())))
if __name__=='__main__':main()

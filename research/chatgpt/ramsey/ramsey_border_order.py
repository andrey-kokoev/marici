"""uv run --with igraph python ramsey_border_order.py K ORDER LOWEST
Nodes: canonical adjacency bit strings. Edge (child,parent,v): delete parent v.
The saved edges allow exact upward traversal over the materialized levels.
"""
import sys,gzip,urllib.request
from pathlib import Path
from itertools import combinations
import igraph as ig

def edges(n):return [(i,j) for j in range(n) for i in range(j)]
def unpack(s):
    n=s[0]-63;b=''.join(f'{x-63:06b}' for x in s[1:]);return ig.Graph(n,[e for e,v in zip(edges(n),b) if v=='1'])
def key(g):
    h=g.permute_vertices(g.canonical_permutation());n=h.vcount();m=sum(1<<(j*(j-1)//2+i) for i,j in map(sorted,h.get_edgelist()));return m

def graph(n,m):return ig.Graph(n,[e for i,e in enumerate(edges(n)) if m>>i&1])
def build(k,n,stop):
    raw=urllib.request.urlopen(f'https://users.cecs.anu.edu.au/~bdm/data/r3{k}_{n}.g6',timeout=20).read().splitlines();parents={key(unpack(s)) for s in raw};assert len(parents)==len(raw)
    path=Path(__file__).with_name(f'ramsey_border_3{k}_{n}_to_{stop}.tsv.gz')
    with gzip.open(path,'wt') as f:
        f.write('child_order\tchild_hex\tparent_hex\tdeleted_vertex_zero_based\n')
        while n>stop:
            incoming={};count=0
            for p in sorted(parents):
                g=graph(n,p);assert key(g)==p
                seen=set()
                for v in range(n):
                    h=g.copy();h.delete_vertices(v);c=key(h)
                    if c in seen:continue
                    seen.add(c);incoming[c]=incoming.get(c,0)+1;count+=1
                    f.write(f'{n-1}\t{c:x}\t{p:x}\t{v}\n')
            print(f'{n}->{n-1}: parents={len(parents)} children={len(incoming)} edges={count} max_upward_choices={max(incoming.values())}',flush=True)
            n-=1;parents=incoming
if __name__=='__main__':build(*map(int,sys.argv[1:]))

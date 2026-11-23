"""Independently replay the first held-out positive hit: rebuild the boundary vertices and check shortest non-square return, its isometry and opposite cuts."""
from pathlib import Path
import json,networkx as nx
from itertools import combinations
D=Path(__file__).parent;r=json.loads((D/'ramsey_long_circuit_2.json').read_text());g=nx.from_graph6_bytes((D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines()[r['record']-1]);g.remove_nodes_from(r['deleted']);I=[0]
for v in g:
    h=sum(1<<i for i in g[v]);I += [s|1<<v for s in I if not s&h]
T=[s for s in I if s.bit_count()==6];B={s for s in I if all(s&t for t in T)};assert B==set(r['component']);G=nx.Graph();G.add_nodes_from(sorted(B));G.add_edges_from((x,y) for x,y in combinations(sorted(B),2) if (x^y).bit_count()==1);E={tuple(sorted(e)):i for i,e in enumerate(G.edges)};C=sorted(nx.simple_cycles(G),key=len);code=lambda c:sum(1<<E[tuple(sorted(e))] for e in zip(c,c[1:]+c[:1]));basis={}
def residual(x):
    for k in sorted(basis,reverse=True):
        if x>>(k-1)&1:x^=basis[k]
    return x
for c in C:
    if len(c)==4:
        v=residual(code(c))
        if v:basis[v.bit_length()]=v
c=next(c for c in C if residual(code(c)));d=dict(nx.all_pairs_shortest_path_length(G));N=len(c);assert all(d[x][y]==min((i-j)%N,(j-i)%N) for i,x in enumerate(c) for j,y in enumerate(c));cut=lambda u,v:frozenset(x for x in B if d[x][u]<d[x][v]);ts=[cut(x,y) for x,y in zip(c,c[1:]+c[:1])];assert all(ts[i]==B-ts[(i+N//2)%N] for i in range(N));o=dict(vertices=len(B),square_rank=len(basis),shortest_non_square_length=N,walk=c,site_changes=[(x^y).bit_length()-1 for x,y in zip(c,c[1:]+c[:1])],opposite_cuts_verified=True);print(o);(D/'ramsey_long_circuit_certificate.json').write_text(json.dumps(o,indent=2)+'\n')

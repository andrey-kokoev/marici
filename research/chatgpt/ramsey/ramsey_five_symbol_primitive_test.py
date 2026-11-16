#!/usr/bin/env python3
"""Exact seed-only orbit test for RGR00, and subsequent fixed-k Ramsey extensions.

First part uses no known Ramsey graph as construction input. The 13-vertex
circulant appears only afterward, as an independently supplied comparison.
"""
from collections import deque
from itertools import combinations
import networkx as nx

SEED = 'RGR00'
n=5
shift = tuple((i+1)%n for i in range(n))
root = (3,1,4,2,0)  # root^2: i -> (2-i) mod 5
reflect = tuple((2-i)%n for i in range(n))

def compose(f,g):
    return tuple(f[g[i]] for i in range(len(f)))

def orbit(gens):
    id_=tuple(range(n))
    result={id_}
    queue=deque([id_])
    while queue:
        f=queue.popleft()
        for g in gens:
            h=compose(g,f)
            if h not in result:
                result.add(h)
                queue.append(h)
    return result

def act(row,g):
    out=['']*len(g)
    for i,c in enumerate(row):
        out[g[i]]=c
    return ''.join(out)

assert compose(root,root)==reflect
assert act(SEED,reflect)==SEED
O_shift={act(SEED,g) for g in orbit([shift])}
O_ref={act(SEED,g) for g in orbit([shift,reflect])}
O_turn={act(SEED,g) for g in orbit([root])}
G=orbit([shift,root])
O={act(SEED,g) for g in G}
assert (len(O_shift),len(O_ref),len(O_turn),len(G),len(O))==(5,5,2,20,10)
R_pairs={tuple(i for i,c in enumerate(row) if c=='R'):row for row in O}
assert len(R_pairs)==10
assert set(R_pairs)==set(combinations(range(5),2))

KG=nx.Graph()
KG.add_nodes_from(R_pairs)
for a,b in combinations(R_pairs,2):
    if set(a).isdisjoint(b):KG.add_edge(a,b)
assert KG.number_of_nodes()==10 and KG.number_of_edges()==15
assert set(dict(KG.degree()).values())=={3}
assert nx.is_isomorphic(KG,nx.petersen_graph())
assert sum(1 for _ in nx.algorithms.isomorphism.GraphMatcher(KG,KG).isomorphisms_iter())==120

def independent(G,S):
    return all(not G.has_edge(a,b) for a,b in combinations(S,2))

def alpha(G):
    vv=list(G)
    for n_ in range(len(vv),-1,-1):
        for S in combinations(vv,n_):
            if independent(G,S):return n_
    return 0
assert alpha(KG)==4

def admissible_neighborhoods(G,k):
    V=list(G)
    for m in range(1<<len(V)):
        S={V[i] for i in range(len(V)) if (m>>i)&1}
        if independent(G,S) and alpha(G.subgraph(set(V)-S))<=k-2:
            yield S

def extend(G,S):
    H=nx.convert_node_labels_to_integers(G)
    v=H.number_of_nodes()
    H.add_node(v)
    # S is pre-conversion! convert canonical 0..n-1 first.
    H.add_edges_from((v,i) for i in S)
    return H

K5=nx.convert_node_labels_to_integers(KG)
branches={10:[K5]}
for order in (10,11,12):
    out=[]
    total=0
    for old in branches.get(order,[]):
        for S in admissible_neighborhoods(old,5):
            total+=1
            H=extend(old,S)
            assert nx.triangles(H)=={i:0 for i in H}
            assert alpha(H)<=4
            if not any(nx.is_isomorphic(H,R) for R in out):out.append(H)
    branches[order+1]=out
    print('extensions',order,'to',order+1,'labelled proposals',total,'nonisomorphic descendants',len(out))

G13=nx.Graph()
G13.add_nodes_from(range(13))
for i in range(13):
    for d in (1,5,-1,-5):G13.add_edge(i,(i+d)%13)
assert alpha(G13)==4
cycles4={frozenset((i,i+1,i+5,i+6) if i+6<13 else ((i)%13,(i+1)%13,(i+5)%13,(i+6)%13)) for i in range(13)}
assert len(cycles4)==13 and all(all(G13.has_edge((i+o)%13,(i+o2)%13) for o,o2 in ((0,1),(1,6),(6,5),(5,0))) for i in range(13) if frozenset((i)%13 for i in (i,i+1,i+5,i+6)) in cycles4) # awkward independent check
assert all(sum(v in c for c in cycles4)==4 for v in G13)
assert all(any(c.isdisjoint(set(rem)) for c in cycles4) for rem in combinations(G13,3))
print('SEED=',SEED)
print('raw shift orbit',sorted(O_shift))
print('root alone',sorted(O_turn))
print('group order',len(G),'combined orbit',sorted(O))
print('red pair labels',sorted(R_pairs))
print('Petersen vertices',KG.number_of_nodes(),'edges',KG.number_of_edges(),'alpha',alpha(KG),'automorphisms',120)
print('13-vertex comparison:',G13.number_of_nodes(),'four-cycles',len(cycles4))
print('PASS')

# Determine all graph edge relations preserved by the generated 20-element group.
red_pair_labels=sorted(R_pairs)
label_index={p:i for i,p in enumerate(red_pair_labels)}
all_edges=set(combinations(range(10),2))
edge_orbits=[]
while all_edges:
    i,j=next(iter(all_edges))
    E={tuple(sorted((label_index[tuple(sorted(g[a] for a in red_pair_labels[i]))],
                     label_index[tuple(sorted(g[a] for a in red_pair_labels[j]))])))
       for g in G}
    edge_orbits.append(E)
    all_edges-=E
assert sum(map(len,edge_orbits))==45
print('F20 pair-orbit sizes:',[len(o) for o in edge_orbits])
valid_graphs=[]
for mask in range(1<<len(edge_orbits)):
    H=nx.Graph(); H.add_nodes_from(range(10))
    for j,E in enumerate(edge_orbits):
        if mask&(1<<j): H.add_edges_from(E)
    if any(nx.triangles(H).values()):continue
    if alpha(H)>4:continue
    valid_graphs.append((mask,H.number_of_edges(),alpha(H),H))
print('F20-invariant triangle-free alpha<=4 relations:',
      [(mask,e,a) for mask,e,a,_ in valid_graphs])
print('all Petersen?', all(nx.is_isomorphic(H,KG) for _,_,_,H in valid_graphs))
for i,E in enumerate(edge_orbits):
    d=sum(set(red_pair_labels[u]).isdisjoint(red_pair_labels[v]) for u,v in E)
    print(f'orbital {i}: size {len(E)}, disjoint={d}, intersecting={len(E)-d}')
for mask,e,a,H in valid_graphs:
    cycles=[len(c) for c in nx.connected_components(H)]
    print(f'valid mask={mask}, edges={e}, component sizes={cycles}, Petersen={nx.is_isomorphic(H,KG)}, '
          f'degrees={sorted(set(dict(H.degree()).values()))}, girth={min((len(c) for c in nx.cycle_basis(H)), default=None)}')
# Complete fixed-k=5 extension test for every AGL(1,5)-invariant red decoder.
for mask,e,a,H in valid_graphs:
    H0=nx.convert_node_labels_to_integers(H)
    first=[extend(H0,S) for S in admissible_neighborhoods(H0,5)]
    second=sum(1 for H1 in first for _ in admissible_neighborhoods(H1,5))
    print(f'decoder mask={mask} edges={e} first_extensions={len(first)} second_extensions={second}')
    assert len(first)==(5 if nx.is_isomorphic(H,KG) else 0)
    assert second==0
print('All invariant seed-decoder branches terminal by 11 vertices.')

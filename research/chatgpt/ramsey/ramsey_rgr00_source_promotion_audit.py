#!/usr/bin/env python3
"""Source-level audit of the RGR00 orbit against existing Marici promotion types.
No Ramsey target size or adjacency supplied to construct the pair data.
Graph with 13 vertices used only for separate equivariance obstruction.
"""
from collections import Counter, defaultdict
from itertools import combinations, product
import networkx as nx

SEED = 'RGR00'
N=5
T=tuple((j+1)%N for j in range(N))
P=tuple((1+3*(j-1))%N for j in range(N))

def compose(g,h): return tuple(g[h[j]] for j in range(N))
def act(w,g):
    result=['']*N
    for i,ch in enumerate(w): result[g[i]]=ch
    return ''.join(result)

G={tuple(range(N))}
while True:
    new=G|{compose(g,h) for g in G for h in [T,P]}
    if new==G: break
    G=new
assert len(G)==20
X=sorted({act(SEED,g) for g in G})
assert len(X)==10
supports={w:frozenset(i for i,ch in enumerate(w) if ch=='R') for w in X}
assert len(set(supports.values()))==10
assert set(supports.values())=={frozenset(x) for x in combinations(range(N),2)}

# One-to-one source promotion: labels and histories, no new independent states.
assert len(X)==10

# Explicit independent (ordered) pair construction: records are different,
# but adding a second independent operand is a new input rule.
ordered=list(product(X,repeat=2))
assert len(ordered)==100
categories=Counter(len(supports[x]&supports[y]) for x,y in ordered)
assert categories=={2:10,1:60,0:30},categories

# Quotient by factor-exchange preserves 55 distinct unordered paired records.
exchange_quotient={tuple(sorted((x,y))) for x,y in ordered}
assert len(exchange_quotient)==55

# Optional support-union readout (a specific, not source-forced quotient)
union_images={supports[x]|supports[y] for x,y in ordered}
assert Counter(map(len,union_images))=={2:10,3:10,4:5}
union_fibers=Counter(supports[x]|supports[y] for x,y in ordered)
assert set(union_fibers.values())=={1,6}

# Pair overlap = line graph of K5, and its complement is Petersen.
source=nx.Graph(); source.add_nodes_from(range(5)); source.add_edges_from(combinations(range(5),2))
line=nx.line_graph(source)
assert len(line)==10 and line.number_of_edges()==30
assert nx.triangles(line) != {v:0 for v in line}
disjoint=nx.complement(line)
assert disjoint.number_of_edges()==15 and nx.is_isomorphic(disjoint,nx.petersen_graph())
secondline=nx.line_graph(line)
assert secondline.number_of_nodes()==30

# Recover primitive translation orbit decomposition on X.
X_set=set(X)
seen=set(); t_orbits=[]
for w in X:
    if w in seen: continue
    oo={w}; a=w
    for _ in range(4):
        a=act(a,T); oo.add(a)
    assert len(oo)==5
    seen |= oo; t_orbits.append(oo)
assert len(t_orbits)==2

# The known 13-vertex extremal graph enters only as an external target
# for a symmetry-equivariance impossibility theorem.
G13=nx.Graph(); G13.add_nodes_from(range(13))
for i in range(13):
    for d in (-5,-1,1,5): G13.add_edge(i,(i+d)%13)
assert sum(nx.triangles(G13).values())==0
Aut13=sum(1 for _ in nx.algorithms.isomorphism.GraphMatcher(G13,G13).isomorphisms_iter())
assert Aut13==52,Aut13
# If F20 acts via a homomorphism on this target, the 5-subgroup is killed:
# 5 does not divide 52. Thus each C5 orbit in X collapses under every
# F20-equivariant X -> V(G13) map, making the image <=2.
assert 52%5!=0
print('F20 group:',len(G))
print('RGR00 row states:',len(X))
print('C5 translation orbit sizes:',sorted(map(len,t_orbits)))
print('Promote record (same operand):',len(X))
print('Independent ordered pair records:',len(ordered), 'overlap categories:',dict(categories))
print('Swap-quotiented unordered pair records:',len(exchange_quotient))
print('Support union quotient:',len(union_images), 'sizes:',dict(Counter(map(len,union_images))))
print('Shared-endpoint line graph:',len(line),'edges',line.number_of_edges(),'contains triangle',any(nx.triangles(line).values()))
print('Disjointness complement:',len(disjoint),'edges',disjoint.number_of_edges(),'alpha',nx.algorithms.approximation.maximum_independent_set(disjoint) is not None)
print('Second line-graph promotion:',len(secondline))
print('Comparison 13-vertex automorphism order:',Aut13)
print('Equivariant image from 10-state source to this 13-vertex graph: at most TWO points, if full F20 preserved')
print('PASS')

# Speculative but sharply testable: promote the three pair-intersection types
# into THREE NEW RECORD VERTICES, fixed by the original F20 action.
# This gives 10+3=13 without using a Ramsey number, but does it admit
# an invariant triangle-free graph of independence < 5?
source_pairs=[frozenset(x) for x in combinations(range(5),2)]
pair_index={x:i for i,x in enumerate(source_pairs)}
actions=[]
for g in G:
    act13=[pair_index[frozenset(g[i] for i in x)] for x in source_pairs] + [10,11,12]
    actions.append(act13)
all_e=set(combinations(range(13),2)); edge_orbits=[]
while all_e:
    i,j=min(all_e)
    E={tuple(sorted((act[i],act[j]))) for act in actions}
    edge_orbits.append(sorted(E)); all_e-=E
print('10+3 phase-relation promoted-state edge-orbit sizes:',list(map(len,edge_orbits)))
assert len(edge_orbits)==10

def contains_ind_set_size5(neigh):
    # Search 5-subsets directly and test all ten pairs.
    for c in combinations(range(13),5):
        if all(not (neigh[i] & (1<<j)) for i,j in combinations(c,2)):
            return True
    return False

valid=[]; triangfree=0
for mask in range(1<<len(edge_orbits)):
    adj=[0]*13
    for z,E in enumerate(edge_orbits):
        if mask & (1<<z):
            for i,j in E:
                adj[i]|=1<<j;adj[j]|=1<<i
    triangles=any((adj[j]&adj[i]) for i in range(13)
                  for j in range(i+1,13) if (adj[i]>>j)&1)
    if triangles:continue
    triangfree+=1
    if not contains_ind_set_size5(adj):valid.append(mask)
print('10+3 invariant graph candidates:', 1<<len(edge_orbits),
      'triangle-free:',triangfree,
      'triangle-free alpha<=4:',len(valid))
assert not valid
print('PASS (10+3 canonical relation role experiment)')

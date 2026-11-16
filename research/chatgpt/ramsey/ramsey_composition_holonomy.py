"""Exact elementary check: same local A/B composition, different global closure."""
from collections import Counter
from itertools import combinations

N = 12

def prism():
    E = set()
    for i in range(6):
        for row in (0, 6):
            E.add(frozenset((row+i, row+(i+1)%6)))
        E.add(frozenset((i, i+6)))
    return E

def mobius():
    E = {frozenset((i, (i+1)%12)) for i in range(12)}
    E |= {frozenset((i, i+6)) for i in range(6)}
    return E

def get_adj(E):
    adj = [set() for _ in range(N)]
    for edge in E:
        a,b=tuple(edge)
        adj[a].add(b)
        adj[b].add(a)
    return adj

def alpha(adj):
    for k in range(N,0,-1):
        for nodes in combinations(range(N),k):
            if all(v not in adj[u] for u,v in combinations(nodes,2)):
                return k,nodes
    return 0,()

def bipartite_on(adj, nodes):
    nodes=set(nodes)
    colors={}
    for root in nodes:
        if root in colors: continue
        colors[root]=0
        stack=[root]
        while stack:
            u=stack.pop()
            for v in adj[u] & nodes:
                if v not in colors:
                    colors[v]=1-colors[u]
                    stack.append(v)
                elif colors[v]==colors[u]:return False
    return True

def odd_cycle_transversal(adj):
    for k in range(N+1):
        for deleted in combinations(range(N),k):
            remaining=set(range(N))-set(deleted)
            if bipartite_on(adj,remaining):return k,deleted
    raise AssertionError

def verify_cycle(cycle,adj,complement=False):
    assert sorted(cycle)==list(range(N))
    for a,b in zip(cycle,cycle[1:]+cycle[:1]):
        assert (b not in adj[a]) if complement else (b in adj[a])

for name,edge_set,a_cycle,b_cycle,expected_alpha,expected_tau in [
    ('Hexagonal prism',prism(),[0,1,2,3,4,5,11,10,9,8,7,6],
     [0,2,4,1,3,5,6,8,10,7,9,11],6,0),
    ('Möbius ladder',mobius(),list(range(12)),
     [0,2,4,1,3,5,7,9,6,11,8,10],5,2),
]:
    adj=get_adj(edge_set)
    assert len(edge_set)==18
    assert all(len(row)==3 for row in adj)
    assert all(not (adj[i]&adj[j]) for i,j in combinations(range(N),2) if j in adj[i])
    verify_cycle(a_cycle,adj)
    verify_cycle(b_cycle,adj,complement=True)
    degree_two_local=[]
    for i in range(N):
        counts=Counter(len(adj[i]&adj[j]) for j in range(N) if j!=i and j not in adj[i])
        degree_two_local.append(tuple(counts.get(v,0) for v in range(3)))
    assert all(profile==(4,2,2) for profile in degree_two_local)
    global_counts=Counter(len(adj[i]&adj[j]) for i,j in combinations(range(N),2) if j not in adj[i])
    assert tuple(global_counts.get(v,0) for v in range(3))==(24,12,12)
    a,witness=alpha(adj)
    tau,removed=odd_cycle_transversal(adj)
    assert a==expected_alpha and tau==expected_tau
    print(name, 'N=12 E=18 local B-pair A² counts=(4,2,2)',
          'alpha=',a,'witness=',witness,'odd_cycle_transversal=',tau,
          'delete=',removed)

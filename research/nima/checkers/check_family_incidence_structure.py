"""Derive mean compatibility and hidden edits from retained family incidence.

Each leaf is an edge between its source family and target family. A spanning
forest gives independent compatibility conditions and an explicit cycle basis.
Integer checks; no numerical rank calculation or external dependencies.
"""
from itertools import product
from collections import defaultdict, deque
from fractions import Fraction as F

V=range(4)
edges=[e for e in product(V,repeat=2) if e[0]!=e[1] and e!=(0,1)]
slots=[('arrow',a,b) for a,b in product(edges,repeat=2)]
slots += [('state',a,b) for a,b in product(V,repeat=2)]
ends=[]
adjacency=defaultdict(list)
for i,(kind,a,b) in enumerate(slots):
    s=(kind,a[0],b[0]) if kind=='arrow' else (kind,a,b)
    t=(kind,a[1],b[1]) if kind=='arrow' else (kind,a,b)
    u=('source',s); v=('target',t)
    ends.append((u,v)); adjacency[u].append((v,i)); adjacency[v].append((u,i))

parent={v:v for v in adjacency}
def root(v):
    while parent[v]!=v: v=parent[v]
    return v

forest=defaultdict(list); chords=[]
for i,(u,v) in enumerate(ends):
    a,b=root(u),root(v)
    if a==b: chords.append(i)
    else:
        parent[b]=a
        forest[u].append((v,i)); forest[v].append((u,i))
components=defaultdict(set)
for v in adjacency: components[root(v)].add(v)
assert len(adjacency)==64 and len(ends)==137 and len(components)==17
assert len(chords)==90
assert sorted(map(len,components.values()))==[2]*16+[32]


def divergence(flow):
    out={v:F(0) for v in adjacency}
    for amount,(u,v) in zip(flow,ends):
        out[u]+=amount; out[v]-=amount
    return out


cycles=[]
for chord in chords:
    u,v=ends[chord]
    # Chord oriented u->v, then the unique forest path v->u.
    previous={v:None}; todo=deque([v])
    while u not in previous:
        at=todo.popleft()
        for nxt,edge in forest[at]:
            if nxt not in previous:
                previous[nxt]=(at,edge); todo.append(nxt)
    cycle=[0]*len(ends); cycle[chord]=1
    at=u
    while at!=v:
        before,edge=previous[at]
        cycle[edge]=1 if ends[edge]==(before,at) else -1
        at=before
    assert all(value==0 for value in divergence(cycle).values())
    assert all(cycle[c]==(c==chord) for c in chords)
    cycles.append(cycle)
# Unique unit chord coordinates prove all 90 cycle vectors independent.


def solve_means(request):
    # Convert mean increments to signed incidence divergence.
    remaining={v:F(request[v])*len(adjacency[v])*(1 if v[0]=='source' else -1)
               for v in adjacency}
    if any(sum((remaining[v] for v in component),F(0))!=0 for component in components.values()):
        return None
    result=[F(0)]*len(ends)
    for component in components.values():
        start=min(component,key=repr); previous={start:None}; order=[start]
        for at in order:
            for nxt,edge in forest[at]:
                if nxt not in previous:
                    previous[nxt]=(at,edge); order.append(nxt)
        for at in reversed(order[1:]):
            before,edge=previous[at]
            sign=1 if ends[edge][0]==at else -1
            result[edge]=remaining[at]*sign
            remaining[before]+=remaining[at]
            remaining[at]=0
        assert remaining[start]==0
    return result

flow=[F((i%7)-3,5) for i in range(len(ends))]
div=divergence(flow)
means={v:div[v]*(1 if v[0]=='source' else -1)/len(adjacency[v]) for v in adjacency}
lift=solve_means(means)
assert lift is not None and divergence(lift)==div
residual=[x-y for x,y in zip(flow,lift)]
reconstructed=[sum((residual[chord]*cycle[i] for chord,cycle in zip(chords,cycles)),F(0))
               for i in range(len(ends))]
assert reconstructed==residual
# Each component provides an independently detectable incompatible request.
for component in components.values():
    bad=dict(means); at=next(iter(component)); bad[at]+=1
    assert solve_means(bad) is None
# Shared-member connected-component promotion closes after one step.
component_relations={(root(u),root(v)) for u,v in ends}
assert all(a==b for a,b in component_relations)
assert len(component_relations)==17
print('Incidence: 64 family vertices, 137 retained leaf edges, 17 connected components (one 32-vertex arrow block + 16 state pairs).')
print('Mean-readout rank = 64-17 = 47; hidden edit dimension = 137-47 = 90.')
print('90 explicit independent integer cycle vectors preserve every source/target mean.')
print('Exact forest solver realizes compatible requests; 17 componentwise incompatibility controls rejected.')
print('Arbitrary tested leaf edit decomposes into its forest lift plus the explicit cycle residual.')
print('Connected-component promotion yields 17 nodes with only self-relations: further component promotion is stationary.')

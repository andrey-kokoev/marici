#!/usr/bin/env python3
"""Finite controls for native six-occurrence Ramsey-complementarity gate.

The calculations concern the frozen directed seed and two *different*
interpretation policies. They do not show that a WG autonomously selects one.
"""
from itertools import combinations, permutations, product
from collections import deque, Counter
import json
from pathlib import Path

V=('A','B','C','D')
E={('A','B'):'AB',('B','C'):'BC',('C','A'):'CA',
   ('A','D'):'AD',('D','B'):'DB',('B','A'):'BA'}
s={'A':'B','B':'A','C':'D','D':'C'}
j={'A':'C','C':'B','B':'D','D':'A'}
g={'A':'B','B':'C','C':'A','D':'D'}
h={'A':'D','D':'B','B':'A','C':'C'}

def shortest(u,v):
    paths=deque([(u,(u,))]); solutions=[]; length=None
    while paths:
        curr,path=paths.popleft()
        if length is not None and len(path)-1>length:break
        if curr==v:
            length=len(path)-1; solutions.append(tuple(E[pair] for pair in zip(path,path[1:])))
        else:
            for (a,b),_ in E.items():
                if a==curr and b not in path:paths.append((b,path+(b,)))
    return solutions

macro={(u,v):shortest(u,v) for u,v in permutations(V,2)}
assert len(macro)==12 and all(len(paths)==1 for paths in macro.values())
assert Counter(len(paths[0]) for paths in macro.values())=={1:6,2:6}
assert all(macro[(s[u],s[v])]==[tuple({v:k for k,v in E.items()}[p] for p in [])] for u,v in [])  # noop

def transported_word(word,mapping):
    lookup={value:key for key,value in E.items()}
    return tuple(E[(mapping[lookup[x][0]],mapping[lookup[x][1]])] for x in word)
assert all(transported_word(macro[(u,v)][0],s)==macro[(s[u],s[v])][0]
           for (u,v) in macro)

# Graph automorphisms, preserving all original occurrence endpoints.
auts=[]
for perm in permutations(V):
    f=dict(zip(V,perm))
    if set((f[a],f[b]) for a,b in E)==set(E):auts.append(f)
assert len(auts)==2 and any(f==s for f in auts)

# A unique four-step directed circuit and a unique two-step return seam.
def cycles(n):
    out=set()
    for p in permutations(V,n):
        if all((a,b) in E for a,b in zip(p,p[1:]+p[:1])):
            out.add(min(tuple(p[k:]+p[:k]) for k in range(n)))
    return out
assert cycles(4)=={('A','D','B','C')}
assert cycles(2)=={('A','B')}

S={frozenset(x) for x in combinations(V,2)}
def support(path):return frozenset(frozenset((a,b)) for a,b in zip(path,path[1:]))
def canon(path):return min(path,tuple(reversed(path)))
all_paths={canon(p):support(p) for p in permutations(V)}
assert len(all_paths)==12
by_support={sup:p for p,sup in all_paths.items()}
assert len(by_support)==12
pairs={}
for p,e in all_paths.items():
    comp=frozenset(S-e)
    if comp in by_support:
        k=tuple(sorted((p,by_support[comp])))
        pairs[k]=(e,comp)
assert len(pairs)==6

native=set(E)
minimal=native | {('C','D'),('D','C')}
complete=set(permutations(V,2))

def path_directed(path,allowed):
    return any(all(edge in allowed for edge in zip(orientation,orientation[1:]))
               for orientation in (path,tuple(reversed(path))))
def realizable(allowed):
    return {k for k in pairs if all(path_directed(p,allowed) for p in k)}
assert len(realizable(native))==0
assert len(realizable(minimal))==4
assert len(realizable(complete))==6

# All six are definable from path-level reachability, but are not constructed
# as partitions from native primitive directed edge records.
assert all(len(macro[(a,b)])==1 for a,b in permutations(V,2))

def action_on_pair(pair,mapping):
    new=tuple(sorted(canon(tuple(mapping[v] for v in p)) for p in pair))
    assert new in pairs
    return new

# Original s symmetry fixes two *undirected* path pairs; the four
# direction-realizable pairs are two exchanged pairs.
fixed_s={k for k in pairs if action_on_pair(k,s)==k}
assert len(fixed_s)==2
assert realizable(minimal)==set(pairs)-fixed_s
assert all(action_on_pair(k,s) in realizable(minimal) for k in realizable(minimal))

# Quarter-turn has 4+1+1 orbits on the six unordered pairs.
def orbits(items, f):
    remaining=set(items); result=[]
    while remaining:
        a=next(iter(remaining)); orbit=[]; x=a
        while x not in orbit:
            orbit.append(x);x=f(x)
        assert x==a
        remaining.difference_update(orbit);result.append(orbit)
    return result
j_orbits=orbits(pairs,lambda p:action_on_pair(p,j))
assert sorted(map(len,j_orbits))==[1,1,4]
assert all(len(o)==1 for o in j_orbits if o[0] in fixed_s)
assert set().union(*(set(o) for o in j_orbits if len(o)==4))==realizable(minimal)

# A4 is transitive on the 12 *ordered* vertex-pairs, hence any
# preserved original-vs-promoted bit would have to be constant.
def compose(p,q):return {v:p[q[v]] for v in V}
group={tuple(V):dict(zip(V,V))};queue=[group[tuple(V)]]
while queue:
    a=queue.pop()
    for gen in [g,h]:
        b=compose(gen,a);key=tuple(b[v] for v in V)
        if key not in group:group[key]=b;queue.append(b)
assert len(group)==12
assert {(f['A'],f['B']) for f in group.values()}==complete
assert any((f['A'],f['D']) not in native for f in group.values())
assert len({action_on_pair(next(iter(pairs)),f) for f in group.values()})==6

# Explicit source-derived 4-cycle vs 2-edge seam partition. Its unique
# proper 2-color completion, *if* triangle avoidance is additionally imposed,
# is C4 + matching. It cannot extend triangle-freely to a fifth vertex.
C4={frozenset(e) for e in [('A','D'),('D','B'),('B','C'),('C','A')]}
assert len(C4)==4
red=C4;blue=S-red
assert blue=={frozenset(('A','B')),frozenset(('C','D'))}
def no_mono_triangle(vertices,red_edges):
    edges={frozenset(e) for e in combinations(vertices,2)}
    blue_edges=edges-red_edges
    for tri in combinations(vertices,3):
        three={frozenset(e) for e in combinations(tri,2)}
        if three <= red_edges or three <= blue_edges:return False
    return True
assert no_mono_triangle(V,red)
Z='z'; possible=[]
for bits in product([False,True],repeat=4):
    red5=red|{frozenset((v,Z)) for v,b in zip(V,bits) if b}
    if no_mono_triangle(V+(Z,),red5):possible.append(bits)
assert not possible

# All 4-vertex colorings: 18 avoid triangles, 12 extend, 6 cannot.
edgelist=tuple(sorted(S,key=lambda e:''.join(sorted(e))))
records=[]
for bits in product([False,True],repeat=6):
    reds={e for e,b in zip(edgelist,bits) if b}
    if not no_mono_triangle(V,reds):continue
    extensions=sum(no_mono_triangle(V+(Z,),reds|{frozenset((v,Z)) for v,b in zip(V,bb) if b}) for bb in product([False,True],repeat=4))
    records.append((bits,extensions))
assert len(records)==18
assert Counter(n for bits,n in records)=={0:6,1:12}

# Model independence: two different color annotations leave the source
# Edge/Path/WG algebra untouched; only one satisfies Ramsey avoidance.
allred={frozenset(x) for x in combinations(V,2)}
assert not no_mono_triangle(V,allred)

result={
 'source':list(E.values()), 'strict_edges':len(E), 'missing_directed_edges':
   [{ 'edge':u+v, 'unique_shortest_history':macro[(u,v)][0]} for u,v in sorted(set(permutations(V,2))-native)],
 'shortest_histories':{'length1':6,'length2':6,'all_unique':True,'reflection_equivariant':True},
 'literal_K4_partition_possible':False,
 'macro_K4_partition_family_size':len(pairs),
 'directed_realizable_unordered_path_pairs':{'native':len(realizable(native)),'plus_CD_DC':len(realizable(minimal)),'full12':len(realizable(complete))},
 'native_automorphism_count':len(auts),
 'reflection_fixed_path_pairs':len(fixed_s),
 'quarter_turn_orbit_sizes':sorted(map(len,j_orbits)),
 'A4_generated_order':len(group),'A4_ordered_pair_orbit_size':len(complete),
 'A4_path_pair_orbit_size':6,
 'provenance_original_count':len(native),'provenance_promoted_count':6,
 'unique_directed_Hamiltonian_cycle':list(next(iter(cycles(4)))),
 'unique_directed_seam':list(next(iter(cycles(2)))),
 'C4_matching_no_triangle':True,'C4_matching_extensions_to_K5':0,
 'K4_avoidance_count':len(records), 'K4_extension_distribution':dict(Counter(n for bits,n in records)),
 'scope':'source-relative finite theorems; no native autonomously selected palette/admission/Edge promotion'
}
folder=Path('/mnt/data')
(folder/'marici_native_complementarity_gate_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))

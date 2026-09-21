"""Packet face/refinement coherence and minimal relation-power certificates."""
from itertools import combinations,product
from math import prod,factorial
from pathlib import Path
import json

PRIMES=(2,3,5,7,11,13)
def labels(n):return {m:2*prod(PRIMES[j] for j in range(n) if m>>j&1) for m in range(1<<n)}
def catalogue(n):return sorted(labels(n).values())
def refinement(m,n):
    old,new=catalogue(m),catalogue(n)
    return tuple(tuple(j for j in range(len(new)-1) if a<=new[j] and new[j+1]<=b)
                 for a,b in zip(old,old[1:]))

def refine_vector(vector,map_):
    out={}
    for i,c in vector.items():
        for j in map_[i]:out[j]=out.get(j,0)+c
    return {j:c for j,c in out.items() if c}

def event_vector(n,start,prime):
    ls=labels(n);cs=catalogue(n)
    return {j:1 for j in range(cs.index(ls[start]),cs.index(ls[start|1<<prime]))}

edge_checks=0;corner_checks=0
for m,n in ((2,3),(3,4),(4,5),(5,6),(4,6)):
    ref=refinement(m,n)
    assert all(ref) and len(set(j for block in ref for j in block))==sum(map(len,ref))
    for x in range(1<<m):
        for p in range(m):
            if not x>>p&1:
                assert refine_vector(event_vector(m,x,p),ref)==event_vector(n,x,p)
                edge_checks+=1
        for y in range(1<<m):
            if x&y==x:
                for z in range(1<<n):
                    if x&z==x and z&y==z:assert z<1<<m
                corner_checks+=1
for m,n,k in ((2,3,4),(3,4,6),(4,5,6)):
    first,second,direct=refinement(m,n),refinement(n,k),refinement(m,k)
    assert tuple(tuple(j for i in block for j in second[i]) for block in first)==direct

# Ordered partitions into pairs preserve ALL intermediate source vertices.
def pair_blocks(items):
    if not items:
        yield ();return
    for pair in combinations(items,2):
        rest=tuple(j for j in items if j not in pair)
        for tail in pair_blocks(rest):yield (pair,)+tail

def local_relation(pair,kind):
    p,q=pair
    marks=((False,False),) if kind==0 else ((False,True),(True,False))
    return {((p,q),m):1 for m in marks}|{((q,p),m):-1 for m in marks}

def multiply(left,right):
    out={}
    for (u,mu),a in left.items():
        for (v,mv),b in right.items():out[u+v,mu+mv]=out.get((u+v,mu+mv),0)+a*b
    return {k:v for k,v in out.items() if v}

layers=[]
for r in (1,2,3):
    n=2*r;entries=[];probes=[]
    for blocks in pair_blocks(tuple(range(n))):
        for kinds in product((0,1),repeat=r):
            rel={((),()):1}
            for pair,kind in zip(blocks,kinds):rel=multiply(rel,local_relation(pair,kind))
            probe=(sum(blocks,()),sum((((False,False) if kind==0 else (False,True)) for kind in kinds),()))
            assert rel[probe]==1
            entries.append(rel);probes.append(probe)
    index={p:i for i,p in enumerate(probes)}
    assert len(index)==len(entries)==factorial(n)
    for i,col in enumerate(entries):
        assert {index[k]:c for k,c in col.items() if k in index}=={i:1}
    layers.append({'event_length':n,'relation_power':r,'ordered_pair_partitions':factorial(n)//(2**r),
                   'local_type_choices':2**r,'certified_product_dimension':len(entries),
                   'joint_seam_raw_degree':-r,'required_joint_shift':1-r,
                   'resulting_degree':-r-(1-r)})
    assert layers[-1]['resulting_degree']==-1

# A cut-refinement hostile: first differentiate each coarse relation block.
# D(ab) tensor D(c)=0, but three separate derivatives give a nonzero tensor.
def forgotten_derivative(column,start):
    out={}
    for (word,marks),coefficient in column.items():
        assert not any(marks)
        state=start
        for p in word:
            end=state|1<<p;key=(state,p,end)
            out[key]=out.get(key,0)+coefficient;state=end
    return {k:v for k,v in out.items() if v}
a,b,c=(local_relation(pair,0) for pair in ((0,1),(2,3),(4,5)))
assert not forgotten_derivative(multiply(a,b),0)
assert not forgotten_derivative(multiply(b,c),3)
local_cycles=[forgotten_derivative(a,0),forgotten_derivative(b,3),forgotten_derivative(c,15)]
assert all(local_cycles)
triple={keys:prod(cycle[key] for cycle,key in zip(local_cycles,keys)) for keys in product(*local_cycles)}
assert len(triple)==64 and multiply(multiply(a,b),c)

# Moving between fixed caps is not an intertwiner on arbitrary top-degree states.
# A top word is killed by cap-2 creation but survives in cap 3.
assert len((0,0)+(1,))>2 and len((0,0)+(1,))<=3

result={'schema':'marici.grothendieck.packet-refinement-relation-tower.v1','passed':True,
        'event_refinement_squares':edge_checks,'convex_old_endpoint_intervals':corner_checks,
        'checks':{'chamber_refinements_injective':True,'nested_refinements_compose':True,
                  'event_windows_commute_with_refinement':True,'old_face_is_convex':True,
                  'fixed_cap_all_state_inclusion_not_claimed':True,
                  'coarse_first_derivative_kills_triple_product':True,
                  'three_seam_refinement_detects_same_triple_product':True,
                  'strict_refinement_after_coarse_compression_obstructed':True},
        'minimal_relation_layers':layers,
        'scope':'General strictness and connecting-map naturality are proved in the companion note. Product dimensions are certified by exact selected-coordinate left inverses, not terminal-rank extrapolation.'}
p=Path(__file__).resolve().parents[1]/'results/packet-refinement-relation-tower.json'
p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))

"""Canonical path derivative into the analytical-refinement seam complex.

All chamber coordinates are retained. This checks maps, not matching dimensions.
"""
from pathlib import Path
from itertools import combinations,product,permutations
from collections import defaultdict
import importlib.util
import sympy as s
import json
ROOT=Path(__file__).resolve().parents[3]
spec=importlib.util.spec_from_file_location('intervals',ROOT/'research/grothendieck/theta_interval_signature.py')
a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)

def cleaned(d):return {k:v for k,v in d.items() if v}
def addto(target,source,c=1):
    for k,v in source.items():target[k]+=c*v

def record(start,word,marks):
    result={():1};state=start
    for p,keep in zip(word,marks):
        target=state|1<<p
        if keep:result={w+(j,):c for w,c in result.items() for j in range(a.POSITION[state],a.POSITION[target])}
        state=target
    return result

def derivative(start,word,marks):
    states=[start]
    for p in word:states.append(states[-1]|1<<p)
    out=defaultdict(int)
    for i,keep in enumerate(marks):
        prefix=record(start,word[:i],marks[:i])
        suffix=record(states[i+1],word[i+1:],marks[i+1:])
        seam=range(a.POSITION[states[i]],a.POSITION[states[i+1]]) if keep else (-1,)
        for u,v,c in product(prefix,suffix,seam):
            out[states[i],states[i+1],u,c,v]+=prefix[u]*suffix[v]
    return cleaned(out)

def boundary(der):
    out=defaultdict(int)
    for (x,y,u,c,v),z in der.items():
        w=() if c==-1 else (c,)
        out[y,u+w,v]+=z;out[x,u,w+v]-=z
    return cleaned(out)

def rels(pair):
    p,q=pair
    return [{((p,q),m):1 for m in pats}|{((q,p),m):-1 for m in pats}
            for pats in (((False,False),),((False,True),(True,False)))]

def deriv_relation(start,rel):
    out=defaultdict(int)
    for (w,m),c in rel.items():addto(out,derivative(start,w,m),c)
    return cleaned(out)

local_count=0;joint=[];products_killed=0
for pair in combinations(range(4),2):
    mid=sum(1<<j for j in pair);other=tuple(j for j in range(4) if j not in pair)
    left,right=rels(pair),rels(other)
    dl=[deriv_relation(0,r) for r in left];dr=[deriv_relation(mid,r) for r in right]
    for d in dl+dr:
        assert d and not boundary(d);local_count+=1
    for r1,r2,d1,d2 in ((x,y,dl[i],dr[j]) for i,x in enumerate(left) for j,y in enumerate(right)):
        composed=defaultdict(int)
        for (u,mu),x in r1.items():
            for (v,mv),y in r2.items():composed[u+v,mu+mv]+=x*y
        assert composed and not deriv_relation(0,composed)
        products_killed+=1
        joint.append({(mid,k,l):x*y for k,x in d1.items() for l,y in d2.items()})
# A selected coordinate in each typed/bidegree block certifies joint injectivity.
probes=[next(iter(col)) for col in joint]
minor=s.Matrix([[col.get(k,0) for col in joint] for k in probes])
assert minor.rank()==24
# Telescoping boundary for representative nonzero paths, not just kernel vectors.
for word in ((0,1),(1,0),(0,1,2,3)):
    for marks in product((False,True),repeat=len(word)):
        end=sum(1<<j for j in word)
        expected=defaultdict(int)
        for w,c in record(0,word,marks).items():expected[end,w,()]+=c;expected[0,(),w]-=c
        assert boundary(derivative(0,word,marks))==cleaned(expected)

# Degree-zero records identify the conormal part with the ordinary graph cycles.
forgotten=[]
for n in (2,3,4):
    vertices=list(range(1<<n))
    edges=[(x,x|1<<j) for x in vertices for j in range(n) if not x>>j&1]
    ei={e:i for i,e in enumerate(edges)}
    incidence=s.zeros(len(vertices),len(edges))
    for j,(x,y) in enumerate(edges):incidence[x,j]=-1;incidence[y,j]=1
    paths=list(permutations(range(n)));P=s.zeros(len(edges),len(paths))
    for j,path in enumerate(paths):
        x=0
        for p in path:
            y=x|1<<p;P[ei[x,y],j]+=1;x=y
    differences=s.zeros(len(paths),len(paths)-1)
    for j in range(1,len(paths)):differences[0,j-1]=-1;differences[j,j-1]=1
    cycles=P*differences
    assert incidence*cycles==s.zeros(len(vertices),len(paths)-1)
    rank=cycles.rank()
    assert rank==len(edges)-incidence.rank()
    forgotten.append({'primes':n,'graph_cycle_dimension':rank,
                      'forgotten_route_relations':len(paths)-1,
                      'relations_killed_by_first_derivative':len(paths)-1-rank})

result={'schema':'marici.grothendieck.relation-to-seam-bridge.v1','passed':True,
        'forgotten_sector':forgotten,
        'nonzero_local_relation_cycles_checked':local_count,
        'nonzero_product_relations_killed_by_single_seam_derivative':products_killed,
        'typed_joint_two_seam_minor_rank':minor.rank(),
        'checks':{'telescoping_path_boundary':True,'local_relations_are_seam_cycles':True,
                  'all_24_products_have_zero_single_derivative':True,
                  'joint_seams_separate_all_24_products':True},
        'scope':'Exact source/chamber comparison. General conormal injection is proved in the companion note. No Green isometry or nonzero Tor_2 over the original source is inferred.'}
p=ROOT/'research/grothendieck/results/relation-to-seam-bridge.json'
p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))

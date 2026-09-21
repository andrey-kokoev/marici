"""Finite checks for pointed multi-input records, rejoining and dual mates.

The external perfect-module extension is proved in the companion note.
"""
from itertools import product,combinations
from pathlib import Path
from collections import Counter
import json
import sympy as s

def words(cap):
    return [w for r in range(cap+1) for w in product(range(2),repeat=r)]

def ends(cuts):return (0,)+tuple(cuts)+(3,)
def capacities(cuts):
    e=ends(cuts);return tuple(b-a for a,b in zip(e,e[1:]))
def basis(cuts):return list(product(*(words(c) for c in capacities(cuts))))
def concatenate(parts):return sum(parts,())

levels=[(),(1,),(2,),(1,2)]
bases={c:basis(c) for c in levels}
indices={c:{v:i for i,v in enumerate(bases[c])} for c in levels}

def forget(source,target,parts):
    src=ends(source);dst=ends(target)
    return tuple(concatenate(parts[src.index(a):src.index(b)]) for a,b in zip(dst,dst[1:]))
def join(source,target):
    assert set(target)<=set(source)
    out=s.zeros(len(bases[target]),len(bases[source]))
    for j,parts in enumerate(bases[source]):out[indices[target][forget(source,target,parts)],j]=1
    return out

tau=s.Integer(2)
def weight(parts):
    w=concatenate(parts)
    return tau**(2*len(w))*(-1)**sum(w)
Q={c:s.diag(*[weight(parts) for parts in bases[c]]) for c in levels}
joins={}
for source in levels:
    for target in levels:
        if set(target)<=set(source):
            J=join(source,target);joins[source,target]=J
            assert J.T*Q[target]==Q[source]*J.T
for source in levels:
    for middle in levels:
        for target in levels:
            if set(target)<=set(middle)<=set(source):
                assert joins[middle,target]*joins[source,middle]==joins[source,target]
                assert joins[source,middle].T*joins[middle,target].T==joins[source,target].T

# Each marked source event emits either vacuum or its prepared feature.
a=(s.Integer(1),s.I);b=(s.Integer(2),1-s.I);c=(-s.I,s.Integer(3))
def add(u,v):return tuple(x+y for x,y in zip(u,v))
# Two explicit chronological source decompositions; the test is not a rank test.
routes=[(a,add(b,c),a),(add(a,b),c,b)]
def multiply(left,right):
    out=Counter()
    for u,x in left.items():
        for v,y in right.items():out[u+v]+=x*y
    return dict(out)
def record(features,marks):
    out={():s.Integer(1)}
    for g,mark in zip(features,marks):
        out=multiply(out,{(j,):g[j] for j in range(2)} if mark else {():s.Integer(1)})
    return out

def observation(features,marks,cuts):
    e=ends(cuts)
    factors=[record(features[a:b],marks[a:b]) for a,b in zip(e,e[1:])]
    out=s.zeros(len(bases[cuts]),1)
    for terms in product(*(list(f.items()) for f in factors)):
        key=tuple(w for w,_ in terms)
        out[indices[cuts][key]]=s.prod(v for _,v in terms)
    return out
for features in routes:
    for marks in product((False,True),repeat=3):
        obs={cut:observation(features,marks,cut) for cut in levels}
        for (source,target),J in joins.items():
            assert (J*obs[source]-obs[target]).applyfunc(s.simplify)==s.zeros(len(bases[target]),1)

# Exact failure of naive naturality on arbitrary input memory:
# mu(c_R(a) vacuum tensor b) = a b, but c_R(a) mu(vacuum tensor b) = b a.
u1=words(1);u2=words(2)
mu=s.zeros(len(u2),len(u1)**2)
for i,x in enumerate(u1):
    for j,y in enumerate(u1):mu[u2.index(x+y),i*len(u1)+j]=1
def create(letter,cap):
    ws=words(cap);out=s.zeros(len(ws))
    for j,w in enumerate(ws):
        if len(w)<cap:out[ws.index(w+(letter,)),j]=1
    return out
state=s.zeros(len(u1)**2,1);state[u1.index(())*len(u1)+u1.index((1,))]=1
left=mu*s.kronecker_product(create(0,1),s.eye(len(u1)))*state
right=create(0,2)*mu*state
assert left!=right and left[u2.index((0,1))]==1 and right[u2.index((1,0))]==1
# Algebra multiplication cannot be an algebra map from the external tensor algebra.
# Independent actions commute externally; their target right creations need not.
assert s.kronecker_product(create(0,1),s.eye(3))*s.kronecker_product(s.eye(3),create(1,1))==s.kronecker_product(create(0,1),create(1,1))
assert create(0,2)*create(1,2)!=create(1,2)*create(0,2)

# Cochain tensor differential: the grading here is NOT feature-word degree.
d0=s.Matrix([2,3]);d1=s.Matrix([[-3,2]])
assert d1*d0==s.zeros(1)

result={'schema':'marici.grothendieck.joint-cut-multi-input-extension.v1','passed':True,
        'feature_dimension':2,'three_event_capacity_dimensions':{str(c):len(bases[c]) for c in levels},
        'checks':{'pointed_record_rejoining':True,'all_coarsening_compositions':True,
                  'unique_weighted_signed_mates':True,'contravariant_mate_composition':True,
                  'noncommutative_full_memory_naturality_hostile':True,
                  'cochain_tensor_differential_sign':True},
        'scope':'Exact record-level multi-input comparison and obstruction to a naive one-functor promotion. Not a physical cloning map or a formal proof of the external derived tensor theorem.'}
p=Path(__file__).resolve().parents[1]/'results/joint-cut-multi-input-extension.json'
p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))

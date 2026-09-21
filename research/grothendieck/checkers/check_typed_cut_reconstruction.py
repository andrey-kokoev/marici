"""General regrouping regression and explicit local-decoder certificates."""
from pathlib import Path
from itertools import permutations,product
from functools import lru_cache
from collections import Counter
import importlib.util
import sys
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
def load(name,file):
    spec=importlib.util.spec_from_file_location(name,ROOT/'research/grothendieck'/file)
    m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m);return m
h=load('typed_history','endpoint_decorated_history.py')
a=load('chambers','theta_interval_signature.py')

@lru_cache(None)
def trees(n):
    out=[None]
    for j in range(1,n):
        out += [(j,l,r) for l in trees(j) for r in trees(n-j)]
    return tuple(out)

def restrict(tree,history):
    if tree is None:return history
    j,l,r=tree;left,right=history.cut(j)
    return restrict(l,left),restrict(r,right)

def assemble(tree,record):
    if tree is None:return record
    _,l,r=tree
    return assemble(l,record[0]).join(assemble(r,record[1]))

def regroup(old,new,record):return restrict(new,assemble(old,record))

def full_column(history):
    slots=[]
    for i,kept in enumerate(history.retained):
        left,right=history.vertices[i:i+2]
        slots.append(tuple(range(a.POSITION[left],a.POSITION[right])) if kept else (-1,))
    return {(history.vertices,tuple(coords)):1 for coords in product(*slots)}

def probe(history):
    return history.vertices,tuple(a.POSITION[history.vertices[i]] if keep else -1
                                 for i,keep in enumerate(history.retained))

def coarse(column,boundaries):
    out=Counter()
    for (vertices,slots),c in column.items():
        ends=(0,)+tuple(boundaries)+(len(slots),)
        key=(tuple(vertices[j] for j in ends),
             tuple(tuple(x for x in slots[left:right] if x!=-1) for left,right in zip(ends,ends[1:])))
        out[key]+=c
    return dict(out)

def matrix(columns):
    keys=sorted(set().union(*(set(c) for c in columns)))
    return s.Matrix([[c.get(k,0) for c in columns] for k in keys])

histories=[];tree_checks=0;pair_checks=0
for start in range(16):
    remaining=[j for j in range(4) if not start>>j&1]
    for n in range(len(remaining)+1):
        for word in permutations(remaining,n):
            for x in h.marked_lift(start,word):
                histories.append(x)
                ts=trees(n)
                for tree in ts:
                    assert assemble(tree,restrict(tree,x))==x;tree_checks+=1
                    for new in ts:
                        assert regroup(tree,new,restrict(tree,x))==restrict(new,x);pair_checks+=1
                # Explicit coherence triangle, in addition to the Agda theorem.
                for tree in ts:
                    rec=restrict(tree,x)
                    assert regroup(ts[-1],ts[0],regroup(tree,ts[-1],rec))==regroup(tree,ts[0],rec)
columns=[full_column(x) for x in histories]
# Selected coordinates give a left inverse on every marked source basis vector.
# Endpoints and slot-vacuum patterns distinguish all probes without dense matrices.
lookup={probe(x):i for i,x in enumerate(histories)}
assert len(lookup)==len(histories)
for i,c in enumerate(columns):
    selected={lookup[k]:v for k,v in c.items() if k in lookup}
    assert selected=={i:1}

fixtures=[]
for indices in ((0,1),(0,1,2)):
    routes=list(permutations(indices));n=len(indices)
    xs=[x for route in routes for x in h.marked_lift(0,route)]
    cs=[full_column(x) for x in xs]
    terminal=matrix([coarse(c,()) for c in cs])
    single_matrices=[matrix([coarse(c,(j,)) for c in cs]) for j in range(1,n)]
    stacked=s.Matrix.vstack(*single_matrices)
    fullrank=len(xs) # certified by the explicit selected-coordinate left inverse above
    assert fullrank==len(routes)*2**n
    fixture={'primes':[h.PRIMES[j] for j in indices], 'full_event_cut_rank':fullrank,
             'terminal_rank':terminal.rank(),'single_cut_ranks':[m.rank() for m in single_matrices],
             'all_single_cut_observations_stacked_rank':stacked.rank()}
    if n==2:
        assert fullrank==8 and fixture['terminal_rank']==6
    else:
        # Distinct three-route-order marginals can collide even with both cut charts.
        # Alternating all-forgotten route combination is the explicit witness.
        witness=s.zeros(len(xs),1)
        for r,route in enumerate(routes):
            inversions=sum(route[i]>route[j] for i in range(n) for j in range(i+1,n))
            witness[r*2**n]=(-1)**inversions
        assert witness!=s.zeros(len(xs),1) and stacked*witness==s.zeros(stacked.rows,1)
        witness1=s.zeros(len(xs),1)
        for r,route in enumerate(routes):
            inversions=sum(route[i]>route[j] for i in range(n) for j in range(i+1,n))
            for marking in (1,2,4):witness1[r*2**n+marking]=(-1)**inversions
        assert stacked*witness1==s.zeros(stacked.rows,1)
        assert s.Matrix.hstack(witness,witness1).rank()==2
        assert len(xs)-fixture['all_single_cut_observations_stacked_rank']==2
        for v in (witness,witness1):
            plus=s.ones(len(xs),1)/48+v/96
            minus=s.ones(len(xs),1)/48-v/96
            assert all(c>0 for c in plus) and all(c>0 for c in minus)
            assert sum(plus)==sum(minus)==1 and stacked*plus==stacked*minus
        fixture['joint_single_cut_kernel']='Exactly alternating all-forgotten routes and alternating sums of one-retained-event routes'
        fixture['strictly_positive_mixture_collisions']=True
    fixtures.append(fixture)
result={'schema':'marici.grothendieck.typed-cut-reconstruction.v1','passed':True,
        'marked_source_histories':len(histories),'tree_roundtrips':tree_checks,
        'regrouping_pairs':pair_checks,'full_cut_left_inverse_verified':True,'fixtures':fixtures,
        'scope':'Typed source regrouping and exact coefficient receiver with vacuum/letter separation. Analytical receivers need the stated local embedding hypothesis.'}
p=ROOT/'research/grothendieck/results/typed-cut-reconstruction.json'
p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))

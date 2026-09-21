"""Finite all-state correction: collisions plus explicit capacity loss.

The signed word fixtures test the universal construction, not spectral ranks.
"""
from pathlib import Path
from itertools import product
from collections import defaultdict
import sympy as s
import json
ROOT=Path(__file__).resolve().parents[3]
small=((),('a',),('b',));small_basis=list(product(small,repeat=3))
def shape(u):return tuple(map(len,u))
def pairing(u,v):
    if u is None or v is None or shape(u)!=shape(v):return s.Integer(0)
    a,b=sum(u,()),sum(v,())
    return s.prod(s.Symbol(f'N{k}_{i}_{j}')/s.Symbol(f'D{k}') for k,(i,j) in enumerate(zip(a,b)))
def merge(u,mode,cap):
    if u is None:return None
    if mode=='left':out=(u[0]+u[1],u[2])
    elif mode=='right':out=(u[0],u[1]+u[2])
    else:out=(sum(u,()),)
    return None if any(len(w)>cap for w in out) else out

def current(u,v,mode,cap):
    if u is None or v is None:return s.Integer(0)
    mu,mv=merge(u,mode,cap),merge(v,mode,cap)
    # Loss is a source-cutoff operation; do not reconstruct it from a metric.
    if mu is None or mv is None:return -pairing(u,v)
    if shape(mu)==shape(mv) and shape(u)!=shape(v):return pairing(mu,mv)
    return s.Integer(0)

nested=0
for cap in (1,2):
    for u,v in product(small_basis,repeat=2):
        for mode in ('left','right'):
            mu,mv=merge(u,mode,cap),merge(v,mode,cap)
            assert s.expand(pairing(mu,mv)-pairing(u,v)-current(u,v,mode,cap))==0
            assert s.expand(current(u,v,mode,cap)+current(mu,mv,'all',cap)-current(u,v,'all',cap))==0
            nested+=1

# Complete finite word spaces at cap 2: R has dimension 7, R^tensor3 dimension343.
words=tuple(w for n in range(3) for w in product(('a','b'),repeat=n))
basis=list(product(words,repeat=3));row={w:i for i,w in enumerate(words)}
def sign(word):return (-1)**word.count('b')
raw_sign=[sign(sum(u,())) for u in basis]
Graw=s.SparseMatrix.diag(*raw_sign);Gbal=s.SparseMatrix.diag(*(sign(w) for w in words))
entries={};fibers=defaultdict(list);lost=[]
for j,u in enumerate(basis):
    out=merge(u,'all',2)
    if out is None:lost.append(j)
    else:
        entries[row[out[0]],j]=1;fibers[out[0]].append(j)
M=s.SparseMatrix(len(words),len(basis),entries)
# Construct the current independently from lost states and newly equal word shapes.
t_entries={(j,j):-raw_sign[j] for j in lost}
for word,indices in fibers.items():
    for i,j in product(indices,repeat=2):
        if shape(basis[i])!=shape(basis[j]):t_entries[i,j]=sign(word)
T=s.SparseMatrix(len(basis),len(basis),t_entries)
corrected=Graw+T
assert corrected==M.H*Gbal*M
assert M.rank()==corrected.rank()==7
assert len(basis)-corrected.rank()==336
# The raw form does not descend; an overflowing diagonal already refutes it.
j=basis.index((('a','a'),('a',),()))
assert M[:,j]==s.zeros(7,1) and Graw[j,j]==1 and T[j,j]==-1 and corrected[j,j]==0
# Green mate uses the original nondegenerate forms, not the degenerate correction.
Msharp=Graw*M.H*Gbal  # Graw^{-1}=Graw in this exact fixture.
assert Graw*Msharp==M.H*Gbal
assert Msharp.rank()==7
assert M*Msharp==s.diag(*(len(fibers[w]) for w in words))
assert M*Msharp!=s.eye(7)
# Composition of the two finite multiplication maps reverses under taking mates.
pairs=list(product(words,repeat=2));pair_index={u:i for i,u in enumerate(pairs)}
e1={};e2={}
for j,u in enumerate(basis):
    out=merge(u,'left',2)
    if out is not None:e1[pair_index[out],j]=1
for j,u in enumerate(pairs):
    out=merge(u,'all',2)
    if out is not None:e2[row[out[0]],j]=1
M1=s.SparseMatrix(49,343,e1);M2=s.SparseMatrix(7,49,e2)
Gmid=s.SparseMatrix.diag(*(sign(u+v) for u,v in pairs))
assert M2*M1==M
assert (Graw*M1.H*Gmid)*(Gmid*M2.H*Gbal)==Msharp
result={'schema':'marici.grothendieck.balanced-green-capacity-descent.v1','passed':True,
        'nested_pair_checks':nested,'raw_fixture_dimension':343,'balanced_fixture_dimension':7,
        'lost_basis_states':len(lost),'corrected_form_rank':7,'ambient_radical_dimension':336,
        'checks':{'collision_and_capacity_loss_constructor':True,'nested_currents_with_overflow':True,
                  'corrected_form_equals_normal_form_pullback':True,'raw_descent_hostile':True,
                  'green_mate_square':True,'mate_composition':True,'mate_is_not_inverse':True},
        'scope':'Exact finite word-algebra and formal spectral-pair fixtures. General complex-level radical/descent statements are proved in the companion note. These ranks are NOT seven-event relation dimensions.'}
p=ROOT/'research/grothendieck/results/balanced-green-capacity-descent.json'
p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))

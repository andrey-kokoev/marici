"""Audit what retained grouping plus reference residuals determines.

Two recursive endpoint policies obey the same retention and residual equations,
but have different successors. All-pairs construction has a separate object
signature from one-fresh-label-per-family promotion.
"""
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
from biclique_complex import rank


@dataclass(frozen=True)
class Row:
    source: object
    target: object
    value: F
    mass: int
    members: tuple
    leaves: frozenset
    reference: F
    residual: F


V=range(4)
E=[edge for edge in product(V,repeat=2) if edge[0]!=edge[1] and edge!=(0,1)]
slots=[('arrow',a,b) for a,b in product(E,repeat=2)]
slots += [('state',a,b) for a,b in product(V,repeat=2)]
d=F(7,5)
base={}
for i,(kind,a,b) in enumerate(slots):
    s=(kind,a[0],b[0]) if kind=='arrow' else (kind,a,b)
    t=(kind,a[1],b[1]) if kind=='arrow' else (kind,a,b)
    value=F((i*i+3*i)%31,11)
    base[(0,i)]=Row(s,t,value,1,(),frozenset({(0,i)}),d,value-d)


def promote(rows,depth,policy):
    groups=defaultdict(list)
    for rid,row in rows.items(): groups[row.target].append(rid)
    out={}
    for i,(key,members) in enumerate(groups.items()):
        mass=sum(rows[m].mass for m in members)
        value=sum((rows[m].mass*rows[m].value for m in members),F(0))/mass
        # Results have a common declared scalar carrier, as a simple channel of
        # Hom(A,B). These are record endpoint policies, not higher-cell fillers.
        target=('reference','d') if policy=='reference-target' else ('retained-key',depth,key)
        out[(depth,i)]=Row(('assembly',depth,i),target,value,mass,tuple(members),
                          frozenset().union(*(rows[m].leaves for m in members)),d,value-d)
    assert len(out)==len(groups)  # exactly one fresh label per retained family
    return out


def recover(levels,depth,rid):
    row=levels[depth][rid]
    if depth==0: return {rid:row}
    out={}
    for member in row.members:
        lower=recover(levels,depth-1,member)
        assert not out.keys()&lower.keys()
        out.update(lower)
    return out


initial_mean=sum((row.value for row in base.values()),F(0))/137
profiles={}
for policy in ('reference-target','inherited-key'):
    levels=[base]
    for depth in (1,2):
        current=promote(levels[-1],depth,policy); levels.append(current)
        recovered={}
        for rid,row in current.items():
            recovered.update(recover(levels,depth,rid))
            assert row.value==row.reference+row.residual
            assert row.mass==len(row.leaves)
        assert recovered==base
        assert sum((row.mass*row.value for row in current.values()),F(0))/137==initial_mean
        assert sum((row.mass*row.residual for row in current.values()),F(0))/137==initial_mean-d
    profiles[policy]=list(map(len,levels))
assert profiles=={'reference-target':[137,32,1],'inherited-key':[137,32,32]}

# Two independent2x2 matrices C,d have8 scalar parameters. Adding the residual
# C-d adds four coordinates but zero independent parameters.
columns=[]
for j in range(8):
    column={j:F(1),8+j%4:F(1 if j<4 else -1)}
    columns.append(column)
assert rank(columns)==8
# Repeated deterministic residual bookkeeping still has the same parameter rank.
for depth in (1,2,4):
    extended=[]
    for j,column in enumerate(columns):
        decorated=dict(column)
        for step in range(depth): decorated[12+4*step+j%4]=F(1 if j<4 else -1)
        extended.append(decorated)
    assert rank(extended)==8
# Fixed reference leaves only the four aggregate matrix parameters.
assert rank([{j:F(1),4+j:F(1)} for j in range(4)])==4

# Literal promotion and independent family pairing have different object types.
first=promote(base,1,'inherited-key')
family_labels=tuple(first)
pairs=tuple(product(family_labels,repeat=2))
assert len(first)==32 and len(pairs)==1024
assert len(pairs)!=len(first)
# Existing primitive arrow relations are endpoint-unique. Parallel-arrow pairing
# respects both endpoints and therefore reduces to their diagonal, not E x E.
parallel=[(a,b) for a,b in product(E,repeat=2) if a==b]
assert len(parallel)==11 and len(E)**2==121
print('Residual-enriched promotion applied twice:')
for policy,counts in profiles.items(): print(f'  {policy}: {counts}; full recovery and weighted reference/residual equations pass.')
print('C,d,C-d retain8 independent scalar parameters, or4 with fixed d; repeated residual decoration adds no independent operand.')
print('One-label-per-family gives32 successors; independent ordered family pairs give1024 objects and require an added constructor.')
print('Endpoint-unique primitive arrows give11 parallel pairs versus121 independent pairs; the comparison type must be specified.')
print('Retention plus a residual equation does not determine successor endpoints or derive independent squaring.')

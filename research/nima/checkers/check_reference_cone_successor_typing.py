"""Type the literal retained-family successor and its reference comparisons.

Common-target comparisons need not be parallel higher cells. Additive reference
connectors provide a constructive control, but their data are determined by the
retained spokes rather than by new independent operands.
"""
from dataclasses import dataclass
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from biclique_complex import rank


@dataclass(frozen=True)
class Cell:
    name: object
    degree: int
    source: object = None
    target: object = None


def between(name,source,target):
    if source.degree!=target.degree: raise ValueError('endpoint degree mismatch')
    if source.degree and (source.source,source.target)!=(target.source,target.target):
        raise ValueError('higher endpoints are not parallel')
    return Cell(name,source.degree+1,source,target)


def compose(name,first,second):
    if first.degree!=second.degree or first.target!=second.source:
        raise ValueError('noncomposable cells')
    return between(name,first.source,second.target)


@dataclass(frozen=True)
class FamilyRecord:
    label: object
    members: tuple
    assembly: Cell
    reference: Cell
    comparison: Cell
    residual: F


primitive=[e for e in product(range(4),repeat=2) if e[0]!=e[1] and e!=(0,1)]
slots=[('arrow',a,b) for a,b in product(primitive,repeat=2)]
slots += [('state',a,b) for a,b in product(range(4),repeat=2)]
groups=defaultdict(list)
for i,(kind,a,b) in enumerate(slots):
    target=(kind,a[1],b[1]) if kind=='arrow' else (kind,a,b)
    groups[target].append(i)
assert len(groups)==32
A=Cell('A',0); B=Cell('B',0)
d=between('direct-reference',A,B)
records=[]; potentials={d:F(0)}
leaf_values={}
for i,(key,members) in enumerate(groups.items()):
    C=between(('assembly',i),A,B)
    for member in members: leaf_values[member]=F(i+1)
    value=sum((leaf_values[m] for m in members),F(0))/len(members)
    potentials[C]=value
    sigma=between(('comparison',i),C,d)
    records.append(FamilyRecord(('family',i),tuple(members),C,d,sigma,value-potentials[d]))
assert {m for r in records for m in r.members}==set(range(137))
assert len({r.label for r in records})==32
# Retaining these comparison records as one incoming family remains legal;
# it does not make arbitrary members parallel or increase their cell degree.
assert len({r.comparison.target for r in records})==1
assert len({r.comparison.source for r in records})==32
rejected=0
for left,right in product(records,repeat=2):
    try: higher=between(('raw-next',left.label,right.label),left.comparison,right.comparison)
    except ValueError as error:
        assert str(error)=='higher endpoints are not parallel'
        rejected+=1
    else:
        assert left==right and higher.degree==3
assert rejected==32*31

# Supply source connectors explicitly. Their additive boundary values are
# determined by the same33 object potentials, including the retained reference.
objects=tuple(potentials)
connectors={(u,v):between(('connector',u.name,v.name),u,v) for u,v in product(objects,repeat=2)}
values={(u,v):potentials[u]-potentials[v] for u,v in connectors}
for u,v,w in product(objects,repeat=3):
    assert values[u,v]+values[v,w]==values[u,w]
for left,right in product(records,repeat=2):
    connector=connectors[left.assembly,right.assembly]
    via=compose(('via',left.label,right.label),connector,right.comparison)
    witness=between(('aligned-next',left.label,right.label),left.comparison,via)
    assert witness.degree==3
    assert left.residual==values[left.assembly,right.assembly]+right.residual
    # The additive boundary discrepancy vanishes. 'witness' above declares a
    # formal cell of that boundary type; its physical realization is extra data.

# All directed connector values have rank32, not33^2 independent coordinates.
pairs=list(connectors)
columns=[]
for vertex in objects:
    column={i:F((u==vertex)-(v==vertex)) for i,(u,v) in enumerate(pairs) if (u==vertex)!=(v==vertex)}
    columns.append(column)
assert rank(columns)==32
# Constant shifts of all potentials are invisible; fixing d removes that freedom.
assert all((potentials[u]+7)-(potentials[v]+7)==values[u,v] for u,v in pairs)
assert rank(columns[1:])==32
print('Literal promotion produces32 retained family records covering137 slots, each with a typed assembly->reference comparison.')
print('All32 comparisons share a target, but992 off-diagonal pairs fail the parallel-endpoint condition for a next higher cell.')
print('Explicit source connectors make all1024 pairs typeable after alignment; every additive discrepancy then telescopes to zero.')
print('The1089 ordered connectors on33 endpoint maps depend on only32 scalar differences; they add no independent comparison factor.')
print('A formal aligned higher-cell boundary is available. A realized filler and its admissible degrees of freedom need their own constructor.')

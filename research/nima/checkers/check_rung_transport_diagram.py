"""The clarified 12--9-->6,11--8-->5,10--7-->4 transport diagram.

Vertical maps retain all rows. Two explicit horizontal grouping candidates are
checked, without claiming that diagram coherence uniquely selects either one.
The rung4 reference is fixed; local reference offsets are retained.
"""
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import runpy

m=runpy.run_path(str(Path(__file__).with_name('check_shared_leg_dg_realization.py')))
I,H=m['I'],m['H']; add,scale,mul=m['add'],m['scale'],m['mul']


def mean(rows):
    total=scale(F(0), rows[0].value); mass=sum(row.mass for row in rows)
    for row in rows: total=add(total,scale(F(row.mass,mass),row.value))
    return total


@dataclass(frozen=True)
class Row:
    label: tuple
    source: tuple
    target: tuple
    value: tuple
    mass: int = 1
    members: tuple = ()


def indexed(rows,field):
    groups=defaultdict(list)
    for row in rows: groups[getattr(row,field)].append(row)
    return {key:tuple(members) for key,members in groups.items()}


def unindex(view):
    rows=tuple(sorted((r for members in view.values() for r in members),key=lambda r:r.label))
    assert len({r.label for r in rows})==len(rows)
    return rows


def incoming_promotion(rows,depth,policy):
    output=[]
    for i,(key,members) in enumerate(indexed(rows,'target').items()):
        target=('retained-key',depth,key) if policy=='inherited' else ('common-target',depth)
        output.append(Row((f'family:{depth}',i),('assembly',depth,i),target,
                          mean(members),sum(r.mass for r in members),members))
    return tuple(output)


def leaves(rows):
    result=[]
    for row in rows:
        result.extend(leaves(row.members) if row.members else (row,))
    return tuple(sorted(result,key=lambda r:r.label))


E=[e for e in product(range(4),repeat=2) if e[0]!=e[1] and e!=(0,1)]
source=[]
for tag,size in (('a',11),('s',4)):
    for i,j in product(range(size),repeat=2):
        s=(tag,E[i][0],E[j][0]) if tag=='a' else (tag,i,j)
        t=(tag,E[i][1],E[j][1]) if tag=='a' else (tag,i,j)
        value=mul(m['values'][f'{tag}y{j}'],m['values'][f'{tag}x{i}'])
        source.append(Row(('leaf',len(source)),s,t,value))
source=tuple(source)
assert len(source)==137


@dataclass(frozen=True)
class Reference:
    rung: int
    value: tuple


physical_reference=Reference(4,scale(2,I))  # fixture value, not a derived normalization


def read_at_four(view, reference=None):
    rows=unindex(view)
    reference = physical_reference if reference is None else reference
    assert reference.rung == 4
    return add(mean(rows),scale(-1,reference.value))


profiles={}
for policy in ('inherited','common'):
    # The horizontal candidate is two retained incoming-family promotions.
    # Its intermediate family records are retained as transport provenance.
    def T9(rows):
        middle=incoming_promotion(rows,1,policy)
        return incoming_promotion(middle,2,policy)
    def T8(view11): return indexed(T9(unindex(view11)),'source')
    def T7(view10): return indexed(T9(unindex(view10)),'target')
    def P1211(rows): return indexed(rows,'source')
    def P1110(view): return indexed(unindex(view),'target')
    def P65(rows): return indexed(rows,'source')
    def P54(view): return indexed(unindex(view),'target')

    left11=P1211(source); left10=P1110(left11)
    right6=T9(source); right5=P65(right6); right4=P54(right5)
    assert unindex(left11)==unindex(left10)==source
    assert T8(left11)==right5                   # upper square
    assert T7(left10)==P54(T8(left11))          # lower square
    upper_route=P54(P65(T9(source)))
    lower_route=T7(P1110(P1211(source)))
    assert upper_route==lower_route==right4
    assert leaves(unindex(right4))==source
    assert sum(row.mass for row in right6)==137
    expected=add(mean(source),scale(-1,physical_reference.value))
    assert read_at_four(upper_route)==read_at_four(lower_route)==expected
    profiles[policy]=(len(incoming_promotion(source,1,policy)),len(right6))
    # A local change of comparison coordinates cannot replace the rung4 reference.
    C=mean(right6)
    for local_reference in (I,C,add(C,H)):
        local_residual=add(C,scale(-1,local_reference))
        offset_to_four=add(local_reference,scale(-1,physical_reference.value))
        assert add(local_residual,offset_to_four)==expected
    assert C!=physical_reference.value
    assert add(C,scale(-1,C))==m['Z'] and expected!=m['Z']
    # Fresh-label unit weights are a different observation policy.
    if policy=='inherited':
        naive=m['Z']
        for row in right6: naive=add(naive,scale(F(1,len(right6)),row.value))
        assert naive!=C
        assert add(naive,scale(-1,physical_reference.value))!=expected
    # A corrupted middle transport is detected by the square, not hidden by
    # reconstructing endpoints along an independent route.
    bad_rows=list(unindex(T8(left11)))
    old=bad_rows[0]
    bad_rows[0]=Row(old.label,old.source,old.target,add(old.value,H),old.mass,old.members)
    bad5=indexed(tuple(bad_rows),'source')
    assert bad5!=P65(T9(source))
    assert read_at_four(P54(bad5))!=expected
assert profiles=={'inherited':(32,32),'common':(32,1)}
print('Both clarified squares and both complete routes to rung4 commute exactly for each declared retained-transport candidate.')
print('All137 original rows and their weights reconstruct; the same fixed rung4 residual is recovered on both routes.')
print('Setting the local mean residual to zero retains its nonzero offset to rung4; the physical-reference readout is unchanged.')
print('Wrong family weights and a corrupted middle transport are detected.')
print('Two horizontal candidates pass with different target row counts32 versus1: presentation coherence does not select the generator.')

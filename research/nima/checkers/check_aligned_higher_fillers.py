# /// script
# dependencies = ["numpy>=2,<3"]
# ///
"""Two type-ascending filler steps in the retained biclique chain model.

An exact labelled column section supplies one filler; kernel records retain all
other choices. The section is deterministic, not asserted to minimize norm.
Unit higher-cell coefficient costs are a declared test metric.
"""
from fractions import Fraction as F
from pathlib import Path
from dataclasses import dataclass
import runpy
from biclique_complex import apply, add_scaled

model=runpy.run_path(str(Path(__file__).with_name('check_two_factor_weighted_chain_transport.py')))
d=model['bd']


class Section:
    def __init__(self,columns):
        self.columns=columns; self.pivots={}; self.independent=set()
        for label,column in enumerate(columns):
            vector=dict(column); used=[]
            while vector:
                p=min(vector)
                if p in self.pivots:
                    row,_=self.pivots[p]; factor=vector[p]
                    add_scaled(vector,row,-factor); used.append((p,factor))
                else:
                    factor=vector[p]; expression={label:F(1)}
                    for q,c in used: add_scaled(expression,self.pivots[q][1],-c)
                    self.pivots[p]=({i:v/factor for i,v in vector.items()},
                                    {i:v/factor for i,v in expression.items()})
                    self.independent.add(label)
                    break
        self.rank=len(self.pivots)
        self.dependent=tuple(i for i in range(len(columns)) if i not in self.independent)

    def fill(self,boundary):
        remaining={i:F(v) for i,v in boundary.items() if v}; answer={}
        while remaining:
            p=min(remaining)
            if p not in self.pivots: return None
            row,expression=self.pivots[p]; factor=remaining[p]
            add_scaled(remaining,row,-factor); add_scaled(answer,expression,factor)
        assert apply(self.columns,answer)=={i:F(v) for i,v in boundary.items() if v}
        return answer

    def kernel(self,label):
        assert label in self.dependent
        out={label:F(1)}
        add_scaled(out,self.fill(self.columns[label]),F(-1))
        assert not apply(self.columns,out)
        return out

    def return_boundary(self,current,boundary):
        change=dict(boundary)
        add_scaled(change,apply(self.columns,current),F(-1))
        lifted=self.fill(change)
        if lifted is None: return None
        result=dict(current); add_scaled(result,lifted,F(1))
        assert apply(self.columns,result)==boundary
        return result


sections={}
for degree in (3,4,5):
    sections[degree]=Section(d[degree])
    print(f'd{degree}: {len(d[degree])} candidate cells, image rank{sections[degree].rank}, filler ambiguity dimension{len(sections[degree].dependent)}.',flush=True)
assert [sections[k].rank for k in (3,4,5)]==[1037,1459,732]
assert [len(sections[k].dependent) for k in (3,4,5)]==[1459,733,132]


@dataclass(frozen=True)
class FillerRecord:
    degree: int
    source: tuple
    target: tuple
    coefficients: tuple
    cost: F


def difference(a,b):
    out=dict(a); add_scaled(out,b,F(-1)); return out


def record(degree,source,target,kernel=None):
    boundary=difference(source,target)
    if apply(d[degree-1],boundary): return None
    filler=sections[degree].fill(boundary)
    if filler is None: return None
    if kernel:
        if apply(d[degree],kernel): return None
        add_scaled(filler,kernel,F(1))
    assert apply(d[degree],filler)==boundary
    return FillerRecord(degree,tuple(sorted(source.items())),tuple(sorted(target.items())),
                        tuple(sorted(filler.items())),sum((v*v for v in filler.values()),F(0)))


# The additive reference-cone discrepancy is zero. A fresh section selects zero;
# an existing closed filler is preserved by boundary-return rather than erased.
fresh=record(3,{},{}); assert fresh.coefficients==() and fresh.cost==0
k3=sections[3].kernel(sections[3].dependent[0])
retained=record(3,{}, {}, k3)
assert retained.cost>0 and sections[3].return_boundary(k3,{})==k3
# A nonzero admissible boundary also receives an explicit filler.
nonzero=record(3,d[3][0],{})
assert nonzero is not None and nonzero.coefficients
# A closed nonzero sphere class is an obstruction to a3-filler.
for sphere in model['Z']:
    assert not apply(d[2],sphere)
    assert record(3,sphere,{}) is None

# Compare the two3-fillers of the same boundary: their difference has a4-filler.
next_record=record(4,dict(retained.coefficients),dict(fresh.coefficients))
assert next_record is not None
j4=dict(next_record.coefficients)
assert apply(d[4],j4)==k3
k4=sections[4].kernel(sections[4].dependent[0])
alternative=record(4,k3,{},k4)
assert alternative is not None and alternative.coefficients!=next_record.coefficients
assert apply(d[4],dict(alternative.coefficients))==k3
# Every3-kernel basis vector fills at degree4: a constructive H3=0 check.
for label in sections[3].dependent:
    assert sections[4].fill(sections[3].kernel(label)) is not None
# At the next step some closed4-data cannot fill, matching the nonzero H4.
obstruction=None
for label in sections[4].dependent:
    candidate=sections[4].kernel(label)
    if sections[5].fill(candidate) is None:
        obstruction=candidate; break
assert obstruction is not None and not apply(d[4],obstruction)
assert record(5,obstruction,{}) is None
assert len(sections[4].dependent)-sections[5].rank==1
# One fixed support frame can deny a boundary that is fillable in the full frame.
restricted=Section([d[3][0]])
assert any(restricted.fill(column) is None for column in d[3])
print('Fresh zero discrepancy selects zero; a retained nonzero closed3-filler keeps its coefficients and positive cost.')
print('Two successive filler records carry explicit boundaries, coefficients and costs; nonzero admissible2-boundaries fill.')
print('All1459 independent3-cycles have4-fillers, with733 independent choices for each fixed4-boundary.')
print('Two H2 classes obstruct3-fillers; a nonzero H4 class obstructs a subsequent5-filler.')
print('Restricted support can reject globally fillable data. The labelled section is a chosen selector, not a minimum-cost theorem.')

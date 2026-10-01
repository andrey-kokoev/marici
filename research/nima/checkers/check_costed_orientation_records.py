# /// script
# dependencies = ["numpy>=2,<3"]
# ///
"""Costed records in the harmonic orientation sector at ranks1 and2.

Chosen budget law: independent class costs add, with primitive scale6.
All source rectangle cells, target views and closure residuals are retained.
Versioned updates are serialized. Other closed cell modes are outside this
sector prototype; parent links identify snapshots rather than live subscriptions.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from copy import deepcopy
import runpy
from uuid import uuid4
from biclique_complex import apply

here=Path(__file__).parent
primitive=runpy.run_path(str(here/'check_weighted_rectangle_triangle_transport.py'))
paired=runpy.run_path(str(here/'check_two_factor_weighted_chain_transport.py'))


def sparse(column): return {i:row[0] for i,row in enumerate(column) if row[0]}


models={
    1:dict(size=6,basis=[sparse(primitive['z'])],
           visible=[sparse(primitive['image'])],lifts=[sparse(primitive['lift'])],
           residuals=[sparse(primitive['residual'])],boundary=primitive['bdiffs'][2],
           map=primitive['columns']),
    2:dict(size=paired['bdims'][2],basis=paired['Z'],visible=paired['Y'],
           lifts=paired['L'],residuals=paired['residuals'],boundary=paired['bd'][2],map=paired['T2']),
}


def combine(columns,coefficients):
    result={}
    for column,c in zip(columns,coefficients):
        for i,v in column.items(): result[i]=result.get(i,F(0))+c*v
    return {i:v for i,v in result.items() if v}


def sqnorm(values): return sum((v*v for v in values.values()),F(0))


@dataclass(frozen=True)
class Cell:
    value: F
    weight: F
    revision: int


@dataclass(frozen=True)
class Request:
    owner: str
    revision: int
    increment: tuple


class CostedStore:
    def __init__(self, coordinates, parents=()):
        self.owner=str(uuid4()); self.revision=0
        self.coordinates=tuple(map(F,coordinates))
        self.model=models[len(coordinates)]
        self.weight=F(84**(len(coordinates)-1))
        self.parents=parents; self.events=[]; self.active=[]
        self.rebuild()

    def rebuild(self):
        source=combine(self.model['basis'],self.coordinates)
        self.cells={('rectangle',len(self.coordinates),i):Cell(source.get(i,F(0)),self.weight,self.revision)
                    for i in range(self.model['size'])}
        self.target=combine(self.model['visible'],self.coordinates)
        self.lift=combine(self.model['lifts'],self.coordinates)
        self.residual=combine(self.model['residuals'],self.coordinates)
        assert not apply(self.model['boundary'],source)
        assert apply(self.model['map'],source)==self.target
        assert combine((self.lift,self.residual),(F(1),F(1)))==source
        assert self.cost()==6*sum(v*v for v in self.coordinates)
        assert self.cost()==self.weight*(sqnorm(self.lift)+sqnorm(self.residual))

    def cost(self): return sum((cell.weight*cell.value**2 for cell in self.cells.values()),F(0))
    def snapshot(self, increment): return Request(self.owner,self.revision,tuple(map(F,increment)))

    def commit(self, request):
        if request.owner!=self.owner or request.revision!=self.revision:
            return False
        if len(request.increment)!=len(self.coordinates): return False
        delta=tuple(map(F,request.increment))
        change=combine(self.model['basis'],delta)
        if apply(self.model['boundary'],change): return False
        before=self.coordinates
        self.coordinates=tuple(a+b for a,b in zip(before,delta))
        self.revision+=1
        self.rebuild()
        edit_cost=self.weight*sqnorm(change)
        assert edit_cost==6*sum(v*v for v in delta)
        self.events.append(('edit',before,self.coordinates,edit_cost))
        self.active.append(len(self.events)-1)
        return True

    def undo(self):
        if not self.active: return False
        event=self.active.pop(); _,before,after,_=self.events[event]
        assert self.coordinates==after
        old=self.coordinates; self.coordinates=before; self.revision+=1
        self.rebuild()
        self.events.append((f'compensate:{event}',old,before,6*sum((a-b)**2 for a,b in zip(old,before))))
        return True


def compare_snapshots(left,right):
    assert len(left.coordinates)==len(right.coordinates)==1
    result=CostedStore(left.coordinates+right.coordinates,
                       ((left.owner,left.revision),(right.owner,right.revision)))
    assert result.cost()==left.cost()+right.cost()
    return result


left=CostedStore((2,)); right=CostedStore((-3,))
parent=compare_snapshots(left,right)
assert parent.cost()==78 and len(parent.cells)==1152
# One class covector return, directly at rank2 versus independent factor edits.
a=(F(1),F(2)); requested=F(1,3)
delta=tuple(requested*v/sum(w*w for w in a) for v in a)
assert sum(a[i]*delta[i] for i in range(2))==requested
stale=parent.snapshot(delta)
assert parent.commit(stale)
assert left.commit(left.snapshot((delta[0],)))
assert right.commit(right.snapshot((delta[1],)))
recomposed=compare_snapshots(left,right)
assert parent.coordinates==recomposed.coordinates
assert {i:(r.value,r.weight) for i,r in parent.cells.items()}=={
    i:(r.value,r.weight) for i,r in recomposed.cells.items()}
assert parent.target==recomposed.target and parent.residual==recomposed.residual
assert parent.events[-1][3]==left.events[-1][3]+right.events[-1][3]==F(2,15)
before=deepcopy(parent.__dict__)
assert not parent.commit(stale) and parent.__dict__==before
assert not parent.commit(left.snapshot((1,))) and parent.__dict__==before
assert parent.undo() and parent.coordinates==(F(2),F(-3))
assert parent.cost()==78 and parent.revision==2
assert not parent.commit(stale)
# Multiple updates and reverse replay restore content, not prior revisions.
for delta in product((F(-1,5),F(0),F(2,7)),repeat=2):
    assert parent.commit(parent.snapshot(delta))
while parent.undo(): pass
assert parent.coordinates==(F(2),F(-3)) and parent.cost()==78
assert parent.events and parent.revision>2
print('Costed harmonic-sector records retain source cells, target view, closure residual, cell weights and versions.')
print('Chosen additive budget: rectangle weight1 at rank1 and84 at rank2; class metric6*I at both ranks.')
print('Direct rank2 return equals factor returns followed by snapshot comparison in cells, views, residuals and edit cost2/15.')
print('Stale/foreign requests leave the entire store unchanged; compensation restores content and budget with fresh revisions.')
print('Parent links bind snapshots. Live propagation, nonharmonic closed modes and durable storage are outside this prototype.')

# /// script
# dependencies = ["numpy>=2,<3", "python-flint>=0.8,<1"]
# ///
"""Live two-factor costed cells with all zero-class closed modes admissible.

Parents carry primitive orientation coordinates. The derived record retains
an independent closed, zero-class cell vector, its exact cost and transport
residual. Serialized revision validation precedes all mutation.
"""
from copy import deepcopy
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
from uuid import uuid4
import runpy
import numpy as np
from biclique_complex import apply

model=runpy.run_path(str(Path(__file__).with_name('check_two_factor_weighted_chain_transport.py')))
Z=model['Z']; T=model['T2']; B2=model['bd'][2]; B3=model['bd'][3]
add=model['add']; dot=model['dot']; A=model['A']
# Cache a numerical proposal operator. Every use is certified over Q below.
proposal=np.linalg.pinv(A@A.T,rcond=1e-12)
exact_lift_solver=None


def scale(vector,c): return {i:c*v for i,v in vector.items() if c*v}


def source(h,b): return add(add(scale(Z[0],h[0]),Z[1],h[1]),b)


def certified_lift(y):
    values=proposal@np.array([float(y.get(i,F(0))) for i in range(A.shape[0])])
    for bound in (1000,10000,100000,1000000,10000000,1000000000):
        p={i:F(float(v)).limit_denominator(bound) for i,v in enumerate(values) if abs(v)>1e-13}
        lifted={j:dot(column,p) for j,column in enumerate(T)}
        lifted={j:v for j,v in lifted.items() if v}
        if apply(T,lifted)==y: return lifted
    # General requests can have denominators too large for float recovery.
    # Fall back to exact normal equations, retaining the same acceptance law.
    global exact_lift_solver
    if exact_lift_solver is None:
        from exact_minimum_lift import ExactMinimumLift
        exact_lift_solver=ExactMinimumLift(T,A.shape[0])
    result=exact_lift_solver.solve(y)
    if result is None: raise ArithmeticError('target outside the source image')
    return result


def valid_mode(b):
    return (set(b)<=set(range(len(B2))) and not apply(B2,b)
            and all(dot(z,b)==0 for z in Z))


@dataclass(frozen=True)
class Request:
    owner: str
    revision: int
    parent_versions: tuple
    dh: tuple
    db: tuple


class LiveStore:
    def __init__(self,h):
        self.owner=str(uuid4()); self.revision=0; self.parent_versions=(0,0)
        self.h=tuple(map(F,h)); self.b={}; self.events=[]; self.active=[]
        self.install(self.prepare(self.h,self.b))

    def prepare(self,h,b):
        assert valid_mode(b)
        x=source(h,b); y=apply(T,x); lifted=certified_lift(y); residual=add(x,lifted,F(-1))
        assert not apply(B2,x) and not apply(T,residual)
        assert tuple(14*dot(z,x) for z in Z)==h
        assert dot(lifted,residual)==0
        cost=84*dot(x,x)
        assert cost==6*sum(v*v for v in h)+84*dot(b,b)
        assert cost==84*(dot(lifted,lifted)+dot(residual,residual))
        return x,y,lifted,residual,cost

    def install(self,prepared):
        self.cells,self.target,self.lift,self.residual,self.cost=prepared
        self.parent_links=tuple((i,v) for i,v in enumerate(self.parent_versions))

    def snapshot(self,dh=(0,0),db=None):
        return Request(self.owner,self.revision,self.parent_versions,tuple(map(F,dh)),
                       tuple(sorted((i,F(v)) for i,v in (db or {}).items() if v)))

    def commit(self,request):
        if (request.owner,request.revision,request.parent_versions)!=(self.owner,self.revision,self.parent_versions):
            return False
        if len(request.dh)!=2 or len(dict(request.db))!=len(request.db): return False
        db=dict(request.db)
        if not valid_mode(db): return False
        h=tuple(a+b for a,b in zip(self.h,request.dh)); b=add(self.b,db)
        prepared=self.prepare(h,b)  # all expensive checks before mutation
        before=(self.h,dict(self.b))
        increment=source(request.dh,db)
        edit_cost=84*dot(increment,increment)
        assert edit_cost==6*sum(v*v for v in request.dh)+84*dot(db,db)
        self.parent_versions=tuple(v+int(d!=0) for v,d in zip(self.parent_versions,request.dh))
        self.h=h; self.b=b; self.revision+=1; self.install(prepared)
        self.events.append(('edit',before,(h,dict(b)),edit_cost))
        self.active.append(len(self.events)-1)
        return True

    def parent_edit(self,index,expected,delta):
        if index not in (0,1) or self.parent_versions[index]!=expected: return False
        dh=[F(0),F(0)]; dh[index]=F(delta)
        return self.commit(self.snapshot(dh))

    def undo(self):
        if not self.active: return False
        index=self.active[-1]; _,before,after,cost=self.events[index]
        assert (self.h,self.b)==after
        h,b=before; prepared=self.prepare(h,b)
        old=(self.h,dict(self.b))
        self.parent_versions=tuple(v+int(a!=c) for v,a,c in zip(self.parent_versions,self.h,h))
        self.h=h; self.b=dict(b); self.revision+=1; self.install(prepared)
        self.active.pop(); self.events.append((f'compensate:{index}',old,(h,dict(b)),cost))
        return True


store=LiveStore((2,-3))
initial=deepcopy((store.h,store.b,store.cells,store.target,store.residual,store.cost))
mode=B3[0]
assert valid_mode(mode) and dot(mode,mode)==3
old_h=store.h
assert store.commit(store.snapshot(db=mode))
assert store.h==old_h and store.cost==78+252
assert store.parent_versions==(0,0)
# All2496 local3-boundaries are admitted modes, spanning the previously verified
# 1037-dimensional boundary subspace. Arbitrary rational combinations are valid.
assert len(B3)==2496
assert all(valid_mode(column) for column in B3)
assert valid_mode(add(B3[0],B3[1],F(2,7)))
# A parent update immediately rebuilds cells/views while retaining internal mode.
stale=store.snapshot(dh=(1,1))
old_mode=dict(store.b); old_revision=store.revision
assert store.parent_edit(0,0,F(1,5))
assert store.b==old_mode and store.revision==old_revision+1
assert store.parent_links==((0,1),(1,0))
assert store.cost==6*sum(v*v for v in store.h)+252
before=deepcopy(store.__dict__)
assert not store.commit(stale) and store.__dict__==before
assert not store.parent_edit(0,0,1) and store.__dict__==before
# Source closure and zero-class constraints have distinct negative controls.
invalid_closed={0:F(1)}
assert apply(B2,invalid_closed)
assert not store.commit(store.snapshot(db=invalid_closed)) and store.__dict__==before
assert not store.commit(store.snapshot(db=Z[0])) and store.__dict__==before
assert store.commit(store.snapshot(dh=(F(1,7),F(-2,7)),db=scale(B3[1],F(1,3))))
# Materialized rebuild equals the live derived view at the same semantic state.
rebuilt=store.prepare(store.h,store.b)
assert rebuilt==(store.cells,store.target,store.lift,store.residual,store.cost)
# Reverse all accepted events. Values and budget return, version authority does not.
while store.undo(): pass
assert (store.h,store.b,store.cells,store.target,store.residual,store.cost)==initial
assert store.revision>0 and store.parent_versions[0]>1
assert not store.commit(stale)
print('All2496 local3-boundaries pass closure and zero-class checks; the full1037-dimensional boundary-mode space is admissible.')
print('A three-cell boundary mode preserves orientation coordinates and adds exact cost252 under weight84.')
print('Live parent edits rebuild source cells, target view and residual, preserving independent internal modes and current links.')
print('Stale roots/parents, nonclosed modes and class-changing disguised modes leave the complete store unchanged.')
print('Full rebuild and live derived records agree; compensation restores initial content and budget with fresh versions.')
print('Execution is serialized and in-memory; the prototype has two primitive parents and one rank2 derived node.')

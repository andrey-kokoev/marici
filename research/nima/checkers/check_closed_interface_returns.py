# /// script
# dependencies = ["numpy>=2,<3", "python-flint>=0.8,<1"]
# ///
"""Closure-constrained partial and complete returns, committed as live edits."""
from copy import deepcopy
from fractions import Fraction as F
from pathlib import Path
import runpy
from biclique_complex import apply
from exact_minimum_lift import ExactMinimumLift

here=Path(__file__).parent
obs=runpy.run_path(str(here/'check_closed_cell_observability.py'))
model=obs['model']; T=model['T2']; B2=model['bd'][2]; B3=model['bd'][3]; Z=model['Z']
add=model['add']; dot=model['dot']; chosen=obs['chosen']; basis=obs['basis']
target_size=model['ddims'][2]
constraints=[dict(column) for column in T]
for j,boundary in enumerate(B2):
    constraints[j].update({target_size+i:v for i,v in boundary.items()})
solver=ExactMinimumLift(constraints,target_size+model['bdims'][1])
assert solver.rank==392  # 279 visible closed directions +113 closure constraints
print('Exact partial-return solver initialized:392 independent constraints,760 free closed directions.',flush=True)


def partial_return(dy): return solver.solve(dy)  # all source-boundary entries default to zero


# A fresh exact decoder for a complete request. Incompatible observations are
# detected while eliminating redundant rows; no state is mutated here.
view_rows=obs['rows'](obs['images'],target_size)
source_rows=obs['rows'](basis,len(B2))

def complete_return(dy,extra):
    if set(extra)!=set(chosen) or not set(dy)<=set(range(target_size)): return None
    equations=[(row,dy.get(i,F(0))) for i,row in enumerate(view_rows)]
    equations.extend((source_rows[i],F(extra[i])) for i in chosen)
    pivots={}
    for row,value in equations:
        vector=dict(row)
        while vector:
            p=min(vector)
            if p in pivots:
                pr,pv=pivots[p]; factor=vector[p]
                vector=add(vector,pr,-factor); value-=factor*pv
            else:
                factor=vector[p]; pivots[p]=({i:v/factor for i,v in vector.items()},value/factor)
                break
        else:
            if value: return None
    coefficients={}
    for p in reversed(range(len(basis))):
        row,value=pivots[p]
        coefficients[p]=value-sum((v*coefficients[i] for i,v in row.items() if i!=p),F(0))
    x=apply(basis,coefficients)
    assert apply(T,x)=={i:F(v) for i,v in dy.items() if v} and not apply(B2,x)
    return x


hidden=obs['zero_images'][0]
visible=next(column for column in B3 if apply(T,column))
requested=add(add({i:v/3 for i,v in Z[0].items()},visible,F(1,5)),hidden)
dy=apply(T,requested)
minimum=partial_return(dy)
assert minimum is not None and not apply(B2,minimum) and apply(T,minimum)==dy
free=add(requested,minimum,F(-1))
assert not apply(B2,free) and not apply(T,free)
assert dot(minimum,free)==0
assert dot(requested,requested)==dot(minimum,minimum)+dot(free,free)
assert dot(free,free)>0
assert dot(minimum,hidden)==0
assert partial_return({})=={}
assert partial_return({i:2*v for i,v in dy.items()})=={i:2*v for i,v in minimum.items()}
# Fixed-topology absolute-view replacement has the content lens laws: no change
# at the current view, exact requested readback, and telescoping replacements.
start=add(Z[1],hidden)
first=add(start,minimum)
second=add(first,minimum)
direct=add(start,minimum,F(2))
assert second==direct
assert apply(T,first)==add(apply(T,start),dy)
extra={i:requested.get(i,F(0)) for i in chosen}
complete=complete_return(dy,extra)
assert complete==requested
# Supplying the selected readings of the partial optimum makes both interfaces agree.
assert complete_return(dy,{i:minimum.get(i,F(0)) for i in chosen})==minimum

# Reject even a CLOSED target cycle when it lies outside this view's image.
incompatible=None
for column in model['dd'].get(3,[]):
    test=deepcopy(obs['image_pivots'])
    if obs['admit'](test,column): incompatible=column; break
assert incompatible is not None and not apply(model['dd'][2],incompatible)
assert partial_return(incompatible) is None
assert complete_return(incompatible,{i:F(0) for i in chosen}) is None
print('Partial/complete returns and closed-but-incompatible target rejection passed.',flush=True)

live=runpy.run_path(str(here/'check_live_costed_cell_records.py'))
store=live['LiveStore']((1,-2))
assert store.commit(store.snapshot(db=hidden))


def request_for_change(store,change):
    dh=tuple(14*dot(z,change) for z in Z)
    db=dict(change)
    for z,value in zip(Z,dh): db=add(db,z,-value)
    assert live['valid_mode'](db)
    return store.snapshot(dh=dh,db=db)


before=dict(store.cells)
request=request_for_change(store,minimum)
assert store.commit(request)
assert store.cells==add(before,minimum)
assert apply(T,add(store.cells,before,F(-1)))==dy
assert store.events[-1][3]==84*dot(minimum,minimum)
assert store.commit(request_for_change(store,free))
assert store.cells==add(before,requested)
assert apply(T,store.cells)==apply(T,add(before,minimum))
# Hidden completion costs exactly the extra amount and has no triangle effect.
assert store.events[-1][3]==84*dot(free,free)
stale=request_for_change(store,minimum)
assert store.parent_edit(0,store.parent_versions[0],F(1,7))
snapshot=deepcopy(store.__dict__)
assert not store.commit(stale) and store.__dict__==snapshot
assert store.undo() and store.undo() and store.undo()
assert store.cells==before
print('Minimum closed partial return commits with exact cost; hidden completion reaches the unique complete request without changing its triangle view.')
print('Pythagorean edit-cost split, live version checks and compensation passed.')
print('Complete constraints determine one source edit; partial returns choose the orthogonal minimum while preserving pre-existing hidden components.')

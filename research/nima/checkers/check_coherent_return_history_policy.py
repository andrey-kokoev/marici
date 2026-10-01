"""Protected-history policy for coherent weak reference returns.

Parents remain immutable. A declared positive metric selects a least-change
version subject to unit equations, a triangle filler, and protected readouts.
All matrices, constraints and optimality checks use rational arithmetic.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
import runpy

m=runpy.run_path(str(Path(__file__).with_name('check_witnessed_reference_return.py')))
Map,add,mul,delta,spaces=m['Map'],m['add'],m['mul'],m['delta'],m['spaces']


def independent_constraints(rows,n):
    rows=[[F(v) for v in row] for row in rows]
    pivot_row=0
    for col in range(n):
        pivot=next((i for i in range(pivot_row,len(rows)) if rows[i][col]),None)
        if pivot is None: continue
        rows[pivot_row],rows[pivot]=rows[pivot],rows[pivot_row]
        a=rows[pivot_row][col]; rows[pivot_row]=[v/a for v in rows[pivot_row]]
        for i in range(len(rows)):
            if i!=pivot_row and rows[i][col]:
                a=rows[i][col]; rows[i]=[x-a*y for x,y in zip(rows[i],rows[pivot_row])]
        pivot_row+=1
    if any(not any(row[:n]) and row[n] for row in rows): return None
    return rows[:pivot_row]


def solve_square(matrix,rhs):
    n=len(rhs)
    reduced=independent_constraints([row+[b] for row,b in zip(matrix,rhs)],n)
    assert reduced is not None and len(reduced)==n
    return [row[-1] for row in reduced]


def nearest(rows,old,weights):
    assert all(w>0 for w in weights)
    n=len(old); independent=independent_constraints(rows,n)
    if independent is None: return None
    A=[row[:n] for row in independent]; b=[row[n] for row in independent]
    G=[[sum((a[k]*c[k]/weights[k] for k in range(n)),F(0)) for c in A] for a in A]
    defect=[sum((a[k]*old[k] for k in range(n)),F(0))-target for a,target in zip(A,b)]
    lam=solve_square(G,defect)
    result=[old[k]-sum((A[i][k]*lam[i] for i in range(len(A))),F(0))/weights[k] for k in range(n)]
    assert all(sum((row[k]*result[k] for k in range(n)),F(0))==row[n] for row in rows)
    # Exact stationarity: weighted edit is in the constraint row span. Together
    # with feasibility and a positive metric this proves the unique minimum.
    assert all(weights[k]*(result[k]-old[k])+sum((A[i][k]*lam[i] for i in range(len(A))),F(0))==0 for k in range(n))
    cost=sum((weights[k]*(result[k]-old[k])**2 for k in range(n)),F(0))
    return result,cost


def basis(s,t,degree):
    return [Map(s,t,degree,{(i,j):F(1)}) for i,g in enumerate(spaces[t])
            for j,h in enumerate(spaces[s]) if g-h==degree]


def coordinates(a,bs): return [a.entries.get(next(iter(b.entries)),F(0)) for b in bs]
def reconstruct(template,bs,values):
    entries={}
    for b,value in zip(bs,values):
        if value: entries[next(iter(b.entries))]=value
    return Map(template.source,template.target,template.degree,entries)


@dataclass(frozen=True)
class Version:
    parents: tuple
    u: Map
    v: Map
    triangle: Map
    edits: tuple
    edit_cost: F
    changed_readouts: tuple


def select(d,r,u,v,protect=('u','v'),weights=(F(1),F(1),F(1)),extra_readouts=(),old_triangle=None):
    A,B=d.source,d.target
    ub,vb,wb=basis(A,A,1),basis(B,B,1),basis(A,B,2)
    sizes=list(map(len,(ub,vb,wb))); nu,nv,nw=sizes; n=sum(sizes)
    previous=Map(A,B,2,{}) if old_triangle is None else old_triangle
    assert (previous.source,previous.target,previous.degree)==(A,B,2)
    old=coordinates(u,ub)+coordinates(v,vb)+coordinates(previous,wb)
    columns=[]
    # Constraint coordinates are tagged by equation and matrix entry.
    for group,bs in enumerate((ub,vb,wb)):
        for b in bs:
            col={}
            if group<2:
                for key,value in delta(b).entries.items(): col[(group,key)]=value
                triangle=mul(d,b) if group==0 else mul(b,d)
                for key,value in triangle.entries.items(): col[(2,key)]=value*(1 if group==0 else -1)
            else:
                for key,value in delta(b).entries.items(): col[(2,key)]=-value
            columns.append(col)
    target={}
    for group,a in enumerate((add(mul(r,d),m['identity'](A),-1),add(mul(d,r),m['identity'](B),-1))):
        for key,value in a.entries.items(): target[group,key]=value
    keys=set(target).union(*(set(c) for c in columns))
    rows=[[c.get(key,F(0)) for c in columns]+[target.get(key,F(0))] for key in sorted(keys)]
    for group,start,length in (('u',0,nu),('v',nu,nv)):
        if group in protect:
            for i in range(start,start+length): rows.append([F(j==i) for j in range(n)]+[old[i]])
    for coefficients in extra_readouts:
        assert len(coefficients)==n
        rows.append(list(coefficients)+[sum((a*b for a,b in zip(coefficients,old)),F(0))])
    metric=[w for w,size in zip(weights,sizes) for _ in range(size)]
    result=nearest(rows,old,metric)
    if result is None: return None
    values,cost=result
    new_u=reconstruct(u,ub,values[:nu]); new_v=reconstruct(v,vb,values[nu:nu+nv])
    W=reconstruct(Map(A,B,2,{}),wb,values[nu+nv:])
    edits=(add(new_u,u,-1),add(new_v,v,-1))
    assert not delta(edits[0]).entries and not delta(edits[1]).entries
    assert delta(new_u)==delta(u) and delta(new_v)==delta(v)
    assert delta(W)==add(mul(d,new_u),mul(new_v,d),-1)
    changed=tuple((i,a,b) for i,(a,b) in enumerate(zip(old,values)) if a!=b)
    assert delta(mul(d,new_u))==add(mul(mul(d,r),d),d,-1)
    parents=(u,v) if old_triangle is None else (u,v,old_triangle)
    return Version(parents,new_u,new_v,W,edits,cost,changed)


# The singular weak-reference example fills the triangle with histories locked.
u,v,d,r=m['u'],m['v'],m['d'],m['r']
snapshots=(dict(u.entries),dict(v.entries))
fixed=select(d,r,u,v)
assert fixed is not None and fixed.u==u and fixed.v==v and fixed.triangle.entries
assert fixed.edit_cost>0 and not any(e.entries for e in fixed.edits)
# Reusing a complete coherent version is a zero-cost no-op, retaining its filler.
reused=select(d,r,fixed.u,fixed.v,old_triangle=fixed.triangle)
assert reused.triangle==fixed.triangle and reused.edit_cost==0
assert not reused.changed_readouts

# In the zero-differential counterexample, no triangle exists with both histories
# protected. Policy must explicitly permit a change to the observed unit data.
x=m['ix']; ux,vx=m['ux'],m['vx']
assert select(x,x,ux,vx) is None
right_only=select(x,x,ux,vx,protect=('u',),weights=(F(2),F(3),F(1)))
assert right_only.u==ux and right_only.v==ux and right_only.edit_cost==3
both=select(x,x,ux,vx,protect=(),weights=(F(2),F(3),F(1)))
assert both.u.entries==both.v.entries=={(1,0):F(2,5)}
assert both.edit_cost==F(6,5)
# Keeping both unit-coordinate readouts fixed has the same obstruction as locks.
assert select(x,x,ux,vx,protect=(),extra_readouts=((F(1),F(0)),(F(0),F(1)))) is None
# A common weighted readout can be preserved while reconciling the histories.
observed=select(x,x,ux,vx,protect=(),weights=(F(2),F(3),F(1)),extra_readouts=((F(2),F(3)),))
assert observed.u==both.u and observed.v==both.v
assert 2*observed.u.entries[1,0]+3*observed.v.entries[1,0]==2
# Equal weights share the adjustment equally; metric choice is visible.
equal=select(x,x,ux,vx,protect=())
assert equal.u.entries==equal.v.entries=={(1,0):F(1,2)} and equal.edit_cost==F(1,2)
assert (u.entries,v.entries)==snapshots
assert ux.entries=={(1,0):F(1)} and vx.entries=={}
assert both.parents==(ux,vx) and both.changed_readouts

# Feed each accepted policy into the same fixed-reference recursion. Adjusting
# unit history changes its correction witness, while preserving the drift law.
for ref,ret,version in ((d,r,fixed),(x,x,both),(x,x,right_only),(x,x,equal)):
    e=mul(ref,version.u)
    def prod(*items):
        out=items[0]
        for item in items[1:]: out=mul(out,item)
        return out
    def combine(left,right):
        C1,h1=left; C2,h2=right
        C=prod(C2,ret,C1)
        h=add(add(prod(h2,ret,C1),prod(ref,ret,h1)),e)
        assert delta(h)==add(C,ref,-1)
        return C,h
    seed=(add(ref,delta(e)),e)
    twice=combine(combine(seed,seed),combine(seed,seed))
    assert delta(twice[1])==add(twice[0],ref,-1)
    left=combine(combine(seed,seed),seed)
    right=combine(seed,combine(seed,seed))
    associator=add(prod(ref,version.u,version.u),prod(e,ret,seed[1]))
    assert left[0]==right[0] and delta(associator)==add(left[1],right[1],-1)
print('Protected histories: singular-reference example has an exact minimum-cost triangle with unchanged unit witnesses.')
print('Fixed-history obstruction rejects; permitted one-sided edit costs3, while weights2:3 select u=v=2/5 at cost6/5.')
print('Protecting both readouts rejects; protecting their weighted total accepts the same coherent update.')
print('Every accepted version satisfies unit and triangle equations; closed edits, original parents, changed coordinates and costs are retained.')
print('Rational feasibility and stationarity certify the declared minima. Weights, protected observables and edit permission are policy inputs.')

"""Can current response data determine the coherent-history metric?

Build the exact tangent space of admissible unit/triangle history changes and
pull back the boundary-response readout. Compare its degeneracy with the
strictly positive coefficient metric used by the selection prototype.
"""
from fractions import Fraction as F
from pathlib import Path
import runpy
from biclique_complex import rank

policy=runpy.run_path(str(Path(__file__).with_name('check_coherent_return_history_policy.py')))
basis,delta,add,mul=policy['basis'],policy['delta'],policy['add'],policy['mul']
d,r=policy['d'],policy['r']
ub,vb,wb=basis('A','A',1),basis('B','B',1),basis('A','B',2)
nu,nv,nw=map(len,(ub,vb,wb)); n=nu+nv+nw
assert (nu,nv,nw)==(14,14,10)
constraints=[]; readouts=[]
for group,bs in enumerate((ub,vb,wb)):
    for element in bs:
        c={}; observed={}
        if group<2:
            for key,value in delta(element).entries.items():
                c[group,key]=value; observed[group,key]=value
            triangle=mul(d,element) if group==0 else mul(element,d)
            for key,value in triangle.entries.items(): c[2,key]=value*(1 if group==0 else -1)
        else:
            for key,value in delta(element).entries.items(): c[2,key]=-value
            # A boundary-response observation of a triangle's boundary factors
            # through delta^2. It does not specify an independent filler readout.
            assert not delta(delta(element)).entries
        constraints.append(c); readouts.append(observed)
assert rank(readouts)==20
keys=sorted(set().union(*(set(c) for c in constraints)))
rows=[[c.get(key,F(0)) for c in constraints]+[F(0)] for key in keys]
reduced=policy['independent_constraints'](rows,n)
pivots=[next(i for i,v in enumerate(row[:n]) if v) for row in reduced]
free=[j for j in range(n) if j not in pivots]
assert len(pivots)==24 and len(free)==14


def apply(columns,vector):
    result={}
    for j,c in enumerate(vector):
        if c:
            for key,v in columns[j].items():
                result[key]=result.get(key,F(0))+c*v
                if not result[key]: del result[key]
    return result


hidden=[]
for j in free:
    vector=[F(0)]*n; vector[j]=F(1)
    for pivot,row in zip(pivots,reduced): vector[pivot]=-row[j]
    assert not apply(constraints,vector)
    assert not apply(readouts,vector)
    # A coefficient metric charges a strictly positive cost where the full
    # current boundary-response pullback charges exactly zero.
    assert sum(v*v for v in vector)>0
    hidden.append(vector)
assert len(hidden)==14
# With both unit histories fixed, six triangle-kernel directions still remain.
assert nw-rank([{key:v for key,v in delta(b).entries.items()} for b in wb])==6

# Distinct coherent versions from the prior exact selector have identical unit
# response data; the declared coefficient metric nevertheless distinguishes them.
left,right=policy['both'],policy['right_only']
assert left.u!=right.u and left.edit_cost!=right.edit_cost
assert delta(left.u)==delta(right.u) and delta(left.v)==delta(right.v)
assert delta(left.triangle)==delta(right.triangle)

# Actual matrix slot/mixed readouts depend on maps and reference, not on a
# closed-history coordinate. Hold those retained inputs fixed across versions.
assembly=runpy.run_path(str(Path(__file__).with_name('check_shared_leg_dg_realization.py')))
values=assembly['values']; mm,ma,ms=assembly['mul'],assembly['add'],assembly['scale']
slot_values=[]; mixed_values=[]
for tag,size in (('a',11),('s',4)):
    for i in range(size):
        for j in range(size):
            slot_values.append(ma(mm(values[f'{tag}y{j}'],values[f'{tag}x{i}']),ms(-1,values['d'])))
            if i and j:
                dx=ma(values[f'{tag}x{i}'],ms(-1,values[f'{tag}x0']))
                dy=ma(values[f'{tag}y{j}'],ms(-1,values[f'{tag}y0']))
                mixed_values.append(mm(dy,dx))
assert len(slot_values)==137 and len(mixed_values)==109
assert any(value!=assembly['Z'] for value in mixed_values)
# These tuples are functions only of the fixed maps; adding them to a history
# observer contributes zero columns to its derivative. This is a dependency
# statement, not an identification of the two fixtures' chain complexes.
assert len(hidden)==14

# Carrier relabelling preserves comparison kind. Independent positive block
# weights therefore remain admissible under that symmetry.
permutation=list(range(120,-1,-1))+list(range(136,120,-1))
for a,b in ((F(1),F(1)),(F(1),F(2))):
    weights=[a]*121+[b]*16
    assert [weights[i] for i in permutation]==weights
assert 121+16==137 and 121+2*16==153
print('Unit/triangle coefficient space:38 dimensions; coherent-history tangent:14 dimensions.')
print('Boundary-response pullback has rank20 overall and is identically zero on every one of those14 admissible history directions.')
print('Six invisible triangle directions remain even with both unit histories locked.')
print('Distinct selected histories have equal boundary responses but different declared coefficient costs.')
print('All137 slot responses and109 mixed readouts depend only on retained maps; they supply no sensitivity to independent closed-history edits.')
print('Kind-preserving symmetry permits different arrow/state metric weights; it does not determine their ratio.')
print('Current response data do not derive a strictly positive history metric. A new history-sensitive observable or a declared quotient is required.')

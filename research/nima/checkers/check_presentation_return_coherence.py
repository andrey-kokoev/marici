# /// script
# dependencies = ["numpy>=2,<3", "python-flint>=0.8,<1"]
# ///
"""Return coherence across anchor maps, with source constraints made explicit."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import runpy
from biclique_complex import apply
from exact_minimum_lift import ExactMinimumLift

obs=runpy.run_path(str(Path(__file__).with_name('check_closed_cell_observability.py')))
m=obs['model']; B2=m['bd'][2]; B3=m['bd'][3]; Z=m['Z']; cells=m['bc']; dc=m['dc']; dd=m['dd']
add=m['add']; dot=m['dot']; basis=obs['basis']; target_size=m['ddims'][2]
labels={d:{face:i for i,face in enumerate(rows)} for d,rows in dc.items()}


def parity(order): return (-1)**sum(order[i]>order[j] for i in range(len(order)) for j in range(i+1,len(order)))
def oriented(face):
    if len(set(face))!=len(face): return {}
    ordered=tuple(sorted(face,key=repr))
    return {labels[len(face)-1][ordered]:F(parity([ordered.index(v) for v in face]))}


def maps(left,right):
    def anchor(t): return ('s',(left[t[1][0]],right[t[1][1]]))
    edge_map=[oriented((anchor(t),s)) for s,t in m['ends']]
    cell_map=[add(oriented((anchor(v),u,w)),oriented((anchor(t),u,w)),F(-1))
              for (u,w),(v,t) in cells[2]]
    for j,column in enumerate(B2): assert apply(edge_map,column)==apply(dd[2],cell_map[j])
    return cell_map


def periods(T):
    result=[]
    for k in range(2):
        row={}
        for j,column in enumerate(T):
            value=sum((m['period'](dc[2][i],k)*v for i,v in column.items()),F(0))
            if value: row[j]=value
        result.append(row)
    return result


def closed_solver(T):
    columns=[dict(c) for c in T]
    for j,column in enumerate(B2): columns[j].update({target_size+i:v for i,v in column.items()})
    return ExactMinimumLift(columns,target_size+m['bdims'][1])


choices=((1,2,3,0),(1,0,0,0),(1,0,3,2))
reference_periods=periods(m['T2'])
records=[]
for left,right in product(choices,repeat=2):
    T=maps(left,right); p=periods(T)
    for row,reference in zip(p,reference_periods):
        difference=add(row,reference,F(-1))
        assert all(sum((difference.get(i,F(0))*v for i,v in col.items()),F(0))==0 for col in basis)
    pivots={}
    for col in basis: obs['admit'](pivots,apply(T,col))
    records.append((T,len(pivots)))
print(f'Nine product-anchor maps agree on the two class constraints; their closed-view ranks are {[r for _,r in records]}.',flush=True)

# Solve identical class constraints through two different presentations.
class_change=(F(2,3),F(-1,5))
expected=add({i:class_change[0]*v for i,v in Z[0].items()},Z[1],class_change[1])
for T,_ in (records[0],records[-1]):
    p=periods(T)
    columns=[]
    for j,column in enumerate(B2):
        combined={k:row[j] for k,row in enumerate(p) if j in row}
        combined.update({2+i:v for i,v in column.items()})
        columns.append(combined)
    solver=ExactMinimumLift(columns,2+m['bdims'][1])
    assert solver.rank==115
    target={k:sum((row.get(i,F(0))*v for i,v in expected.items()),F(0)) for k,row in enumerate(p)}
    assert solver.solve(target)==expected

# Full retained cell views transport the SAME source and cost, even when
# their visible ranks differ. Keep orthogonal complements, not just classes.
TA=records[0][0]
TB=records[-1][0]
witness=next(col for col in B3 if not apply(TB,col) and apply(TA,col))
x=add(expected,witness,F(1,7))
packages=[]
for T in (TA,TB):
    solver=ExactMinimumLift(T,target_size)
    y=apply(T,x); lifted=solver.solve(y)
    assert lifted is not None
    residual=add(x,lifted,F(-1))
    assert not apply(T,residual) and dot(lifted,residual)==0
    assert add(lifted,residual)==x
    assert not apply(B2,add(lifted,residual))
    assert 84*(dot(lifted,lifted)+dot(residual,residual))==84*dot(x,x)
    packages.append((solver,y,lifted,residual))
# Roundtrip via reconstructed source recovers the original complete package.
reconstructed=add(packages[1][2],packages[1][3])
assert apply(TA,reconstructed)==packages[0][1]
assert add(reconstructed,packages[0][0].solve(apply(TA,reconstructed)),F(-1))==packages[0][3]

# This zero-class edit is invisible in one map but visible in the other.
# The corresponding PARTIAL view requests therefore impose different constraints.
assert all(sum((row.get(i,F(0))*v for i,v in witness.items()),F(0))==0 for row in reference_periods)
optimum=closed_solver(TA).solve(apply(TA,witness))
assert optimum and not apply(B2,optimum)
assert apply(TA,optimum)==apply(TA,witness)
assert closed_solver(TB).solve({})=={}
assert dot(optimum,optimum)>0
# Same partial source constraint, expressed in invertibly rescaled coordinates.
# Transform the request along with the readout; retain the source metric.
scales=[F(i%3+1) for i in range(target_size)]
rescaled=[{i:scales[i]*v for i,v in column.items()} for column in TA]
request={i:scales[i]*v for i,v in apply(TA,witness).items()}
assert closed_solver(rescaled).solve(request)==optimum
print('Equivalent class requests yield the identical harmonic source return and cost through distinct anchors.')
print('Complete target-plus-residual packages roundtrip exactly with closure and source metric retained.')
print('A zero-class mode is hidden by one map and visible in another: partial returns differ because the constraints differ.')
print('Invertible target rescaling with the request transported leaves the constrained minimum return unchanged.')

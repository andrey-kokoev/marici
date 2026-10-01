"""Boundary adapter from the actual137-slot typed matrix assembly.

Retain11+11 arrow legs,4+4 state legs and the direct reference. Composite slots
are paths, not independent primitive arrows. Compute the reference-comparison
chain space and evaluate its rectangle relations as exact matrix responses.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import runpy
from biclique_complex import apply, rank, add_scaled

assembly=runpy.run_path(str(Path(__file__).with_name('check_comparison_slot_reference_assembly.py')))
I,H=assembly['I'],assembly['H']; ZERO=assembly['ZERO']
add,scale,mul,assemble=assembly['add'],assembly['scale'],assembly['mul'],assembly['assemble']
objects={'A':0,'U':1,'V':2,'B':3}
legs=[(f'x{i}','A','U') for i in range(11)]+[(f'y{j}','U','B') for j in range(11)]
legs += [(f's{i}','A','V') for i in range(4)]+[(f't{j}','V','B') for j in range(4)]
legs += [('d','A','B')]
leg_id={name:i for i,(name,_,_) in enumerate(legs)}
B1=[{objects[a]:F(1),objects[b]:F(-1)} for _,a,b in legs]
slots=[('arrow',i,j) for i,j in product(range(11),repeat=2)]
slots += [('state',i,j) for i,j in product(range(4),repeat=2)]
slot_id={slot:i for i,slot in enumerate(slots)}
paths=[]
for kind,i,j in slots:
    left,right=(f'x{i}',f'y{j}') if kind=='arrow' else (f's{i}',f't{j}')
    paths.append({leg_id[left]:F(1),leg_id[right]:F(1)})
B2=[]
for path in paths:
    column=dict(path); column[leg_id['d']]=F(-1)
    B2.append(column)
assert len(legs)==31 and len(slots)==137
assert rank(B1)==3 and rank(B2)==28
assert all(not apply(B1,column) for column in B2)
assert 137-rank(B2)==109

# Retain explicit composite names and composition witnesses, then eliminate
# these auxiliary pairs by a checked chain retraction.
E1=B1+[{objects['A']:F(1),objects['B']:F(-1)} for _ in slots]
E2=[]
for i,path in enumerate(paths):
    column=dict(path); column[len(legs)+i]=F(-1); E2.append(column)  # tau_i: path-p_i
E2 += [{len(legs)+i:F(1),leg_id['d']:F(-1)} for i in range(137)]  # sigma_i: p_i-d
assert rank(E2)==165 and 274-rank(E2)==109
assert all(not apply(E1,column) for column in E2)
P1=[{i:F(1)} for i in range(31)]+paths
P2=[{} for _ in slots]+[{i:F(1)} for i in range(137)]
J2=[{i:F(1),137+i:F(1)} for i in range(137)]
for i,column in enumerate(E2): assert apply(P1,column)==apply(B2,P2[i])
for i,column in enumerate(J2):
    assert apply(P2,column)=={i:F(1)}
    assert apply(E2,column)==B2[i]
# The alternative that forgets leg factorization has138 independent parallel
# paths/reference and137 independent comparison boundaries.
collapsed=[{i:F(1),137:F(-1)} for i in range(137)]
assert rank(collapsed)==137

# A full kernel basis of rooted rectangle relations:100 arrow and9 state modes.
rectangles=[]; distinguished=[]
for kind,size in (('arrow',11),('state',4)):
    for i,j in product(range(1,size),repeat=2):
        rectangle={slot_id[kind,i,j]:F(1),slot_id[kind,i,0]:F(-1),
                   slot_id[kind,0,j]:F(-1),slot_id[kind,0,0]:F(1)}
        assert not apply(B2,rectangle)
        rectangles.append(rectangle); distinguished.append(slot_id[kind,i,j])
assert len(rectangles)==109
assert all(rectangle.get(label,F(0))==F(i==j)
           for i,rectangle in enumerate(rectangles) for j,label in enumerate(distinguished))


def residuals(x,y,s,t,reference):
    out=[]
    for kind,i,j in slots:
        composite=mul(y[j],x[i]) if kind=='arrow' else mul(t[j],s[i])
        out.append(add(composite,scale(-1,reference)))
    return out


def evaluate(chain,values):
    result=ZERO
    for i,c in chain.items(): result=add(result,scale(c,values[i]))
    return result


x,y,s,t=[I]*11,[I]*11,[I]*4,[I]*4
assert all(evaluate(r,residuals(x,y,s,t,I))==ZERO for r in rectangles)
K=((F(0),F(0)),(F(1),F(0)))
x[1]=add(I,scale(F(2,3),H)); y[1]=add(I,scale(F(3,5),K))
values=residuals(x,y,s,t,I)
for rectangle,(kind,i,j) in zip(rectangles,
    [(kind,i,j) for kind,size in (('arrow',11),('state',4)) for i,j in product(range(1,size),repeat=2)]):
    dx=add(x[i],scale(-1,x[0])) if kind=='arrow' else add(s[i],scale(-1,s[0]))
    dy=add(y[j],scale(-1,y[0])) if kind=='arrow' else add(t[j],scale(-1,t[0]))
    assert evaluate(rectangle,values)==mul(dy,dx)
assert evaluate(rectangles[0],values)==scale(F(2,5),mul(K,H))!=ZERO
# First-order controls: perturbing only one leg family leaves this rectangle0.
assert evaluate(rectangles[0],residuals(x,[I]*11,s,t,I))==ZERO
assert evaluate(rectangles[0],residuals([I]*11,y,s,t,I))==ZERO
# The normalized total recovers the existing finite matrix assembly exactly.
mean=evaluate({i:F(1,137) for i in range(137)},values)
assert mean==add(assemble(x,y,s,t),scale(-1,I))
# Changing the direct reference cancels from every rectangle relation.
shifted=residuals(x,y,s,t,add(I,H))
assert all(evaluate(r,values)==evaluate(r,shifted) for r in rectangles)
print('Actual typed assembly:4 objects,31 primitive/reference legs,137 path-reference2-cells; boundary rank28 and109 independent closed2-relations.')
print('Keeping137 composite names plus137 composition witnesses gives the same109 relations by an exact chain retraction.')
print('Forgetting leg sharing instead gives137 independent boundaries and no2-kernel.')
print('The109 closed relations split into100 arrow rectangles and9 state rectangles.')
print('Their exact matrix readouts are (right_j-right_0)*(left_i-left_0); a two-leg perturbation gives a nonzero2/5*K*H defect.')
print('Single-leg perturbations and reference changes do not create these rectangle defects; weighted total reproduces the137-slot assembly.')

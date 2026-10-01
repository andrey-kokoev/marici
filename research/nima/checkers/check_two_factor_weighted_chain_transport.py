# /// script
# dependencies = ["numpy>=2,<3"]
# ///
"""Exact two-factor class metrics and certified quotient/residual transport.

NumPy proposes multipliers for a least-norm lift. Rationalized multipliers must
satisfy the entire normal equation exactly before any metric claim is accepted.
"""
from fractions import Fraction as F
from itertools import product
import numpy as np
from biclique_complex import apply, biclique, dowker


def sign(values): return (-1)**sum(values[i]>values[j] for i in range(len(values)) for j in range(i+1,len(values)))
def dot(x,y): return sum((x.get(i,F(0))*y.get(i,F(0)) for i in set(x)|set(y)),F(0))
def add(x,y,scale=F(1)):
    out=dict(x)
    for i,v in y.items(): out[i]=out.get(i,F(0))+scale*v
    return {i:v for i,v in out.items() if v}


def relation(n):
    vertices=list(product(range(4),repeat=n))
    return [(('s',a),('t',b)) for a,b in product(vertices,repeat=2) if all(i!=j for i,j in zip(a,b))]


_,pd,pc,_=biclique(relation(1))
primitive_cycle=next(dict(enumerate(map(F,(1,)+tail))) for tail in product((-1,1),repeat=5)
                     if not apply(pd[2],dict(enumerate(map(F,(1,)+tail)))))
primitive_labels={(tuple(v[1][0] for v in left),tuple(v[1][0] for v in right)):i
                  for i,(left,right) in enumerate(pc[2])}

ends=relation(2)
bdims,bd,bc,_=biclique(ends)
ddims,dd,dc=dowker(ends,include_cells=True)
dl={degree:{face:i for i,face in enumerate(rows)} for degree,rows in dc.items()}


def rect_projection(cell,k):
    left,right=cell
    a=[v[1][k] for v in left]; b=[v[1][k] for v in right]
    if len(set(a))<2 or len(set(b))<2: return None,0
    return primitive_labels[(tuple(sorted(a)),tuple(sorted(b)))],sign(a)*sign(b)


Z=[]
for k in range(2):
    column={}
    for j,cell in enumerate(bc[2]):
        label,orientation=rect_projection(cell,k)
        if label is not None: column[j]=primitive_cycle[label]*orientation/F(84)
    assert len(column)==504
    assert not apply(bd[2],column)
    assert all(dot(column,boundary)==0 for boundary in bd[3])
    Z.append(column)
assert [[dot(a,b) for b in Z] for a in Z]==[[F(1,14),F(0)],[F(0),F(1,14)]]

# Product anchors give a concrete map to the Dowker triangles.
def anchor(t): return ('s',tuple((v+1)%4 for v in t[1]))
def oriented(face):
    if len(set(face))!=len(face): return {}
    ordered=tuple(sorted(face,key=repr))
    return {dl[len(face)-1][ordered]:F(sign([ordered.index(v) for v in face]))}

T2=[add(oriented((anchor(right[0]),*left)),oriented((anchor(right[1]),*left)),F(-1))
    for left,right in bc[2]]
T1=[oriented((anchor(t),s)) for s,t in ends]
vertices=sorted({v for edge in ends for v in edge},key=repr)
T0=[{dl[0][(v if v[0]=='s' else anchor(v),)]:F(1)} for v in vertices]
for j,column in enumerate(bd[1]): assert apply(T0,column)==apply(dd[1],T1[j])
for j,column in enumerate(bd[2]): assert apply(T1,column)==apply(dd[2],T2[j])
Y=[apply(T2,z) for z in Z]


def period(face,k):
    labels=[v[1][k] for v in face]
    return sign(labels) if sorted(labels)==[0,1,2] else 0


period_matrix=[[sum((period(dc[2][j],k)*v for j,v in y.items()),F(0)) for y in Y] for k in range(2)]
assert period_matrix[0][1]==period_matrix[1][0]==0
assert abs(period_matrix[0][0])==abs(period_matrix[1][1])==1
assert all(not apply(dd[2],y) for y in Y)
print(f'Exact source harmonic Gram=(1/14)*I; mapped period matrix={period_matrix}.',flush=True)

# Solve T2*T2^T p=Y numerically, then validate a rational certificate exactly.
A=np.zeros((ddims[2],bdims[2]))
for j,column in enumerate(T2):
    for i,v in column.items(): A[i,j]=float(v)
array_y=np.array([[float(y.get(i,F(0))) for y in Y] for i in range(ddims[2])])
multipliers=np.linalg.lstsq(A@A.T,array_y,rcond=1e-12)[0]
L=[]; residuals=[]
for k in range(2):
    p={i:F(float(value)).limit_denominator(10**9) for i,value in enumerate(multipliers[:,k]) if abs(value)>1e-13}
    lifted={j:dot(column,p) for j,column in enumerate(T2)}
    lifted={j:v for j,v in lifted.items() if v}
    assert apply(T2,lifted)==Y[k], 'rational normal-equation certificate failed'
    residual=add(Z[k],lifted,F(-1))
    assert not apply(T2,residual)
    assert dot(lifted,residual)==0
    assert apply(bd[2],lifted), 'negative control must have a nonclosed unconstrained lift'
    assert not apply(bd[2],add(lifted,residual))
    L.append(lifted); residuals.append(residual)

source_gram=[[dot(a,b) for b in Z] for a in Z]
quotient_gram=[[dot(a,b) for b in L] for a in L]
residual_gram=[[dot(a,b) for b in residuals] for a in residuals]
assert all(source_gram[i][j]==quotient_gram[i][j]+residual_gram[i][j] for i,j in product(range(2),repeat=2))
for a,b in product((F(-2),F(0),F(3,7)),repeat=2):
    original=add({i:a*v for i,v in Z[0].items()},Z[1],b)
    reconstructed=add(add({i:a*v for i,v in L[0].items()},L[1],b),
                      add({i:a*v for i,v in residuals[0].items()},residuals[1],b))
    assert original==reconstructed
    assert dot(original,original)==F(1,14)*(a*a+b*b)
assert F(1,14)/F(1,16)==F(8,7)
assert F(8,7)!=F(6,4)
# Product-count source of the metric scaling: each additional primitive factor
# supplies84 admissible labelled K(2,2) assignments (repetition within a shore
# is allowed), versus64 label assignments for a Dowker triangle.
assignments=[(a,c,b,d) for a,c,b,d in product(range(4),repeat=4)
             if a!=b and a!=d and c!=b and c!=d]
assert len(assignments)==84
assert sum(a==c for a,c,b,d in assignments)==36
assert sum(a!=c for a,c,b,d in assignments)==48
assert F(6,84)==F(1,14)
print('Product-count prediction at rank4: rectangle class scale=6/84^3=1/98784; triangle scale=1/65536; conversion=2048/3087.')
assert F(6,84**3)==F(1,98784)
assert F(6,84**3)/F(4,64**3)==F(2048,3087)
print(f'Certified unconstrained quotient Gram={quotient_gram}',flush=True)
print(f'Retained residual Gram={residual_gram}',flush=True)
print('Their sum is exactly(1/14)*I, with both closed orientation classes and all tested mixed returns reconstructed.')
print('Relative to fresh unit triangle class cost1/16, transported closed cost has factor8/7; the primitive factor was3/2.')
print('The numerical solve is only a proposal: rational normal equations, orthogonality, chain identities, and costs all passed exactly.')

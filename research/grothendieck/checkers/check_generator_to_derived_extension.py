"""Exact algebraic regressions for mate extension, complexes and retracts.

This finite two-sheet record fixture is not a sampled analytical Clark source.
"""
from pathlib import Path
from itertools import product
import json
import sympy as s
I=s.I
tau=s.Integer(2)
words=[()]+[(j,) for j in range(2)]+list(product(range(2),repeat=2))
index={w:i for i,w in enumerate(words)}
J=s.diag(1,-1)
Q=s.diag(*[tau**(2*len(w))*s.prod(J[j,j] for j in w) for w in words])

def creation(g):
    out=s.zeros(len(words))
    for w,k in index.items():
        if len(w)<2:
            for j in range(2):out[index[w+(j,)],k]=g[j]
    return out

def annihilation(g):
    out=s.zeros(len(words))
    for w,k in index.items():
        if w:out[index[w[:-1]],k]=s.conjugate(g[w[-1]])
    return out

def clean(M):return M.applyfunc(s.simplify)
def eq(A,B):assert clean(A-B)==s.zeros(A.rows,A.cols)
def mate(A,Qsrc=Q,Qtgt=Q):return clean(Qsrc.inv()*A.H*Qtgt)

# Typed diamond; reassembly phases depend only on endpoints.
phase={2:s.Integer(1),4:I,6:-s.Integer(1),12:-I}
a=s.Matrix([1,I]);b=s.Matrix([2,-1+I]);c=s.Matrix([-I,3])
edges={(2,4):a,(4,12):b+c,(2,6):a+b,(6,12):c}
arrows={};mates={}
for (x,y),g in edges.items():
    T=phase[x]/phase[y]
    arrows[x,y,0]=T*s.eye(7);arrows[x,y,1]=T*creation(g)
    mates[x,y,0]=s.conjugate(T)*s.eye(7)
    mates[x,y,1]=s.conjugate(T)*tau**2*annihilation(J*g)
    for mark in (0,1):
        A=arrows[x,y,mark];B=mates[x,y,mark]
        eq(Q*B,A.H*Q)
        eq(B,mate(A));eq(mate(B),A)
        # The dagger is conjugate-linear on source coefficients.
        eq(mate((2+3*I)*A),(2-3*I)*B)
for middle in (4,6):
    for first,last in product((0,1),repeat=2):
        A=arrows[2,middle,first];B=arrows[middle,12,last]
        eq(mate(B*A),mates[2,middle,first]*mates[middle,12,last])
    # The unmarked derived restriction uses sums, not sums of cofibers.
    U=arrows[2,middle,0]+arrows[2,middle,1]
    V=arrows[middle,12,0]+arrows[middle,12,1]
    eq(V*U,sum((arrows[middle,12,j]*arrows[2,middle,i] for i,j in product((0,1),repeat=2)),s.zeros(7)))

A=arrows[2,4,1]
# Cone(A): X in degree -1, Y in degree 0. Dual differential is -A^vee.
eq(Q*(-mate(A)),(-A.H)*Q)
# A nontrivial three-term complex X -> X+Y -> Y, with d1*d0=0.
id7=s.eye(7)
d0=id7.col_join(A);d1=(-A).row_join(id7)
eq(d1*d0,s.zeros(7))
# Dual degrees -2,-1,0 give -d1^vee and +d0^vee.
eq(d0.H*(-d1.H),s.zeros(7))
Qsum=s.diag(Q,Q)
dual0=mate(d1,Qsum,Q);dual1=mate(d0,Q,Qsum)
eq(dual1*(-dual0),s.zeros(7))
eq(Qsum*(-dual0),(-d1.H)*Q)
eq(Q*dual1,d0.H*Qsum)

# Retracts require DIFFERENT primal/dual images, not a nondegenerate restriction
# of one signed form to every image.
q=s.diag(1,-1)
p=s.Matrix([[1,0],[1,0]])
ps=mate(p,q,q)
eq(p*p,p);eq(ps*ps,ps)
u=s.Matrix([1,1]);v=s.Matrix([1,0])
eq(p*u,u);eq(ps*v,v)
assert (u.H*q*u)[0]==0 and (u.H*q*v)[0]==1

result={'schema':'marici.grothendieck.generator-to-derived-extension.v1','passed':True,
        'fixture':'finite two-sheet record through degree two, tau=2; independent complex features',
        'checks':{'generator_pairing_squares':True,'mate_composition':True,
                  'conjugate_linearity':True,'unmarked_lift_restriction':True,
                  'cone_fiber_sign':True,'dual_three_term_differential_squares_zero':True,
                  'dual_idempotent_retract_pairing':True,
                  'isotropic_primal_retract_hostile':True},
        'scope':'Exact finite algebraic regressions. The universal perfect-module extension is proved in the companion theorem; no analytical sampling or physical admission is inferred.'}
pth=Path(__file__).resolve().parents[1]/'results/generator-to-derived-extension.json'
pth.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))

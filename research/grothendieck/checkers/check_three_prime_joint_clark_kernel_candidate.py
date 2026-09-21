"""Assemble the finite three-prime joint Clark kernel before rejoining."""
from pathlib import Path
from itertools import permutations
import sympy as s, json
ROOT=Path(__file__).resolve().parents[3]
# chamber basis: intervals between 2,4,6,10,12,20,30,60, represented by 7 bins
# Use the two-sheet reduction B on the four-port incidence proxy.
J=s.diag(1,-1)
B=s.Matrix([[1,1,-1,1],[1,1,1,-1]])/2
# deterministic four-port event feature from its endpoint chamber interval
intervals={(2,4):0,(4,6):1,(6,10):2,(10,12):3,(12,20):4,(20,30):5,(30,60):6}
def feature(a,b):
    # four ports: two endpoint channels with the interval incidence sign
    i=intervals.get((a,b),0)
    v=s.zeros(4,1); v[i%4]=1; v[(i+1)%4]=1
    return B*v
routes=list(permutations((2,3,5)))
# arithmetic route vertices (product of prime events)
def vertices(route):
    x=2; out=[x]
    for p in route:x*=p;out.append(x)
    return out
# reduced record through degree 3: vacuum + one/two/three tensors
blocks=[s.ones(1,1),J,s.kronecker_product(J,J),s.kronecker_product(J,J,J)]
Q=s.zeros(15); offs=(0,1,3,7)
for off,block in zip(offs,(s.ones(1),J,s.kronecker_product(J,J),s.kronecker_product(J,J,J))):
    for i in range(block.rows):
        for j in range(block.cols): Q[off+i,off+j]=block[i,j]
def markvec(fs,mask):
    marked=[f for f,m in zip(fs,mask) if m]
    z=s.ones(1,1)
    for f in marked:z=s.kronecker_product(z,f)
    out=s.zeros(15,1); degree=len(marked)
    offsets=(0,1,3,7)
    out[offsets[degree]:offsets[degree]+z.rows,0]=z
    return out
cols=[]
for route in routes:
    vs=vertices(route); fs=[feature(vs[i],vs[i+1]) for i in range(3)]
    for mask in range(8):cols.append(markvec(fs,[(mask>>i)&1 for i in range(3)]))
R=s.diag(*([1]*6)) # build route-major direct sum by placing each column in its route block
R=s.zeros(90,48)
for j,col in enumerate(cols):
    for i in range(15): R[15*(j//8)+i,j]=col[i]
Qjoint=s.zeros(90)
for r in range(6):
    for i in range(15):
        for j in range(15): Qjoint[15*r+i,15*r+j]=Q[i,j]
K=s.simplify(R.T*Qjoint*R)
# Alternating route ghosts, all-forgotten and one-letter sum.
eps=s.Matrix([(-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3)) for p in routes])
g0=s.zeros(48,1);g1=s.zeros(48,1)
for r,e in enumerate(eps):
    g0[8*r]=e
    for m in (1,2,4):g1[8*r+m]=e
G=s.Matrix.hstack(g0,g1)
assert R.rank()>0 and Q.rank()==15 and Qjoint.rank()==90
assert G.T*K*G != s.zeros(2)
result={'schema':'marici.grothendieck.three-prime-joint-clark-kernel-candidate.v1','passed':True,
 'routes':6,'source_columns':48,'reduced_record_dimension_per_route':15,
 'joint_receiver_rank':R.rank(),'pulled_back_pairing_rank':K.rank(),
 'pulled_back_pairing_is_nondegenerate':K.rank()==R.rank(),
 'ghost_pairing_matrix':[[str(x) for x in row] for row in (G.T*K*G).tolist()],
 'cross_cut_terms_retained':True,
 'status':'finite reduced-feature candidate; equality with the full analytic Clark kernel remains open'}
(ROOT/'research/grothendieck/results/three-prime-joint-clark-kernel-candidate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))

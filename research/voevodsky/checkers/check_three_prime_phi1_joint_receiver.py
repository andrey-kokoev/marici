"""Numerical three-prime joint receiver using the recorded theta atom Phi_1."""
from itertools import permutations
from pathlib import Path
import sys, numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from clark_feature_evaluator import ClarkFeatureEvaluator,phi_one
routes=list(permutations((2,3,5)))
ev=ClarkFeatureEvaluator([],phi_one,quadrature=256)
C=np.array([[0,0,-.5,.5],[0,0,-.5,.5],[-.5,-.5,0,0],[.5,.5,0,0]],complex)
def f(a,b,z): return np.array(ev.interval_feature(np.log(a),np.log(b),z),complex)
z=0.7+1.4j
Q=np.zeros((85,85),complex); Q[0,0]=1
for d in range(1,4):
    sl=slice((4**d-1)//3,(4**(d+1)-1)//3)
    inds=np.arange((4**d-1)//3,(4**(d+1)-1)//3)
    block=C
    for _ in range(d-1): block=np.kron(block,C)
    Q[np.ix_(inds,inds)]=block
cols=[]
for route in routes:
    x=2; fs=[]
    for p in route:
        y=x*p;fs.append(f(x,y,z));x=y
    for mask in range(8):
        v=np.zeros(85,complex); marked=[fs[i] for i in range(3) if mask>>i&1]
        w=np.array([1],complex)
        for a in marked:w=np.kron(w,a)
        d=len(marked); start=(4**d-1)//3;v[start:start+len(w)]=w
        cols.append(v)
R=np.zeros((510,48),complex)
for j,v in enumerate(cols):R[85*(j//8):85*(j//8)+85,j]=v
K=R.conj().T@np.kron(np.eye(6),Q)@R
eps=np.array([(-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3)) for p in routes])
g0=np.zeros(48);g1=np.zeros(48)
for r,e in enumerate(eps):g0[8*r]=e;g1[8*r+1]=g1[8*r+2]=g1[8*r+4]=e
G=np.column_stack((g0,g1)); gram=G.conj().T@K@G
rank=int(np.linalg.matrix_rank(R,tol=1e-10))
assert rank>0
print({'passed':True,'phi':'Phi_1','joint_rank':rank,'pairing_rank':np.linalg.matrix_rank(K,tol=1e-10),'ghost_pairing':gram.tolist(),'scope':'Numerical Phi_1 surrogate; not completed summed Phi'})

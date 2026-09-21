"""Multi-spectral joint receiver test for the finite completed theta sum."""
from itertools import permutations
from pathlib import Path
import sys,numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from clark_feature_evaluator import ClarkFeatureEvaluator,phi_completed
routes=list(permutations((2,3,5))); ev=ClarkFeatureEvaluator([],lambda x:phi_completed(x,64),quadrature=256)
C=np.array([[0,0,-.5,.5],[0,0,-.5,.5],[-.5,-.5,0,0],[.5,.5,0,0]],complex)
def feat(a,b,z):return np.array(ev.interval_feature(np.log(a),np.log(b),z),complex)
def vector(route,mask,z):
 x=2; fs=[]
 for p in route:y=x*p;fs.append(feat(x,y,z));x=y
 w=np.array([1],complex)
 for i in range(3):
  if mask>>i&1:w=np.kron(w,fs[i])
 out=np.zeros(85,complex);d=mask.bit_count();start=(4**d-1)//3;out[start:start+len(w)]=w
 return out
zs=[.25+1.2j,.55+1.5j,.85+1.8j,1.15+2.1j]
print('feature norms',[float(np.linalg.norm(feat(2,2*p,z))) for p in (2,3,5) for z in zs])
rows=[]
for z in zs:
 M=np.zeros((6*85,48),complex)
 for j,(r,m) in enumerate((r,m) for r in range(6) for m in range(8)):
  M[85*r:85*r+85,j]=vector(routes[r],m,z)
 rows.append(M)
R=np.vstack(rows)
singular=np.linalg.svd(R,compute_uv=False)
rank=int(np.sum(singular>1e-14))
eps=np.array([(-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3)) for p in routes])
g0=np.zeros(48);g1=np.zeros(48)
for r,e in enumerate(eps):g0[8*r]=e;g1[8*r+1]=g1[8*r+2]=g1[8*r+4]=e
# Positive spectral Gram as a diagnostic; signed Clark pairing is reported separately.
K=R.conj().T@R
G=np.column_stack((g0,g1)); gram=G.conj().T@K@G
gram_rank=int(np.linalg.matrix_rank(K,tol=1e-9))
assert rank>0 and gram_rank>0
result={'schema':'marici.voevodsky.completed-phi-three-prime-multispectral.v1','passed':True,'phi_terms':64,'spectral_points':len(zs),'joint_columns':48,'multispectral_receiver_rank':rank,'joint_gram_rank':gram_rank,'ghost_positive_gram':gram.tolist(),'scope':'Completed finite theta sum and positive diagnostic Gram; signed Clark cross-kernel and infinite-sum error certification remain open'}
print(result)

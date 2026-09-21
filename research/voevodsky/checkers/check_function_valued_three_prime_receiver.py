"""Function-valued Clark feature probe: retain the t-dependence of k_z."""
from itertools import permutations
import sys,numpy as np
sys.path.insert(0,str(__import__('pathlib').Path(__file__).resolve().parents[1]))
from clark_feature_evaluator import ClarkFeatureEvaluator,phi_completed
routes=list(permutations((2,3,5))); T=np.array([.0,.35,.8,1.4]); zs=[.15+1.05j,.25+1.15j,.35+1.25j,.45+1.35j,.55+1.45j,.65+1.55j,.75+1.65j,.85+1.75j,.95+1.85j,1.05+1.95j,1.15+2.05j,1.25+2.15j]
ev=ClarkFeatureEvaluator([],lambda x:phi_completed(x,64),quadrature=256)
def letter(a,b,z):
 h=np.array(ev.interval_feature(np.log(a),np.log(b),z),complex)
 # Conditioning-only normalization: preserves nonzero source directions but
 # avoids double-precision loss on late theta shells.
 scale=np.linalg.norm(h)
 if scale: h=h/scale
 return np.kron(h,np.exp(1j*z*T))
L=4*len(T); offsets=[0]
for d in range(1,4):offsets.append(offsets[-1]+L**(d-1))
D=offsets[-1]+L**3
R=np.zeros((len(zs)*6*D,48),complex)
for q,z in enumerate(zs):
 for r,route in enumerate(routes):
  x=2; fs=[]
  for p in route:y=x*p;fs.append(letter(x,y,z));x=y
  for m in range(8):
   w=np.array([1],complex)
   for i in range(3):
    if m>>i&1:w=np.kron(w,fs[i])
   d=m.bit_count();R[q*6*D+r*D+offsets[d]:q*6*D+r*D+offsets[d]+len(w),r*8+m]=w
sv=np.linalg.svd(R,compute_uv=False); rank=int(np.sum(sv>1e-16)); print({'passed':rank==48,'function_valued_rank':rank,'columns':48,'z_samples':len(zs),'t_samples':len(T),'scope':'Finite quadrature probe of the L2(Omega x R+) feature, not a completion proof'})

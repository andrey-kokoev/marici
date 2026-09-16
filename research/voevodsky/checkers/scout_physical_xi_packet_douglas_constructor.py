"""Build finite Xi de Branges packets, split their inertia, and run the Douglas test."""
import json,sys
from pathlib import Path
try:
 import mpmath as mp
 import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import mpmath as mp;import numpy as np
sys.path.insert(0,str(Path(__file__).parent))
from partial_douglas_constructor import construct
mp.mp.dps=60;pi=mp.pi

def xi(s): return mp.mpf('.5')*s*(s-1)*pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
def X(z): return xi(mp.mpf('.5')+1j*z)
def E(z): return X(z)+1j*mp.diff(X,z)
def Estar(z): return X(z)-1j*mp.diff(X,z)
def kernel(z,w): return (E(z)*mp.conj(E(w))-Estar(z)*mp.conj(Estar(w)))/(2*pi*1j*(mp.conj(w)-z))

def packet(points):
 K=np.array([[complex(kernel(z,w)) for w in points] for z in points]);K=(K+K.conj().T)/2
 lam,U=np.linalg.eigh(K);scale=max(1,float(np.max(np.abs(lam))));tol=1e-10*scale
 pos=np.maximum(lam,0);neg=np.maximum(-lam,0)
 AS=(np.sqrt(pos)[:,None]*U.conj().T)
 AB=(np.sqrt(neg)[:,None]*U.conj().T)
 result=construct(AS,AB,1e-10)
 return {'points':[[float(mp.re(z)),float(mp.im(z))] for z in points],'eigenvalues':[float(x) for x in lam],'negative_eigenvalues_below_tolerance':int(np.sum(lam < -tol)),'douglas_status':result['status'],'minimum_eigenvalue':float(lam[0]),'result':result}

packets=[
 [mp.mpc(0,1),mp.mpc(5,1),mp.mpc(10,1),mp.mpc(15,1)],
 [mp.mpc(2,2),mp.mpc(8,3),mp.mpc(14,2),mp.mpc(20,4)],
 [mp.mpc(5,.25),mp.mpc(12,.5),mp.mpc(20,.75),mp.mpc(28,1)],
]
out={'packets':[packet(p) for p in packets],'method':'spectral positive/negative feature split of the physical Xi de Branges Gram matrix','scope':'finite numerical scout only','rh_proved':False}
if __name__=='__main__':
 p=Path(__file__).parents[1]/'results'/'physical-xi-packet-douglas-scout.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

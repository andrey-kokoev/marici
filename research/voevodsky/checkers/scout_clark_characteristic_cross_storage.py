"""Nystrom scout for the characteristic theta cross-storage kernel."""
import json,sys,functools
from pathlib import Path
try:
 import mpmath as mp
 import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import mpmath as mp;import numpy as np
mp.mp.dps=50;pi=mp.pi
@functools.lru_cache(maxsize=None)
def phi_text(xtext):
 u=mp.mpf(xtext);e=mp.exp(2*u);s=mp.mpf('0')
 for n in range(1,20):
  a=(4*pi*pi*n**4*mp.exp(mp.mpf('4.5')*u)-6*pi*n*n*mp.exp(mp.mpf('2.5')*u))*mp.exp(-pi*n*n*e);s+=a
  if n>3 and abs(a)<mp.mpf('1e-60'): break
 return s
def phi(x): return phi_text(mp.nstr(x,50))
def transformed_kernel(u,v,gn,gw):
 # The characteristic integral is symmetric in u,v.  Integrating only to
 # min(u,v) avoids catastrophic cancellation across its odd midpoint.
 if v>u: u,v=v,u
 total=mp.mpf('0')
 for x,w in zip(gn,gw):
  t=v*(mp.mpf(x)+1)/2
  total += mp.mpf(w)*(u+v-2*t)*phi(u+v-t)*phi(t)
 total*=v/2
 return total/(2*mp.sqrt(phi(u)*phi(v)))
def run(U,n=28,inner=32):
 x,w=np.polynomial.legendre.leggauss(n);nodes=(x+1)*U/2;weights=w*U/2
 gx,gw=np.polynomial.legendre.leggauss(inner);M=np.empty((n,n))
 for i,u in enumerate(nodes):
  for j,v in enumerate(nodes): M[i,j]=float(transformed_kernel(mp.mpf(u),mp.mpf(v),gx,gw)*mp.sqrt(weights[i]*weights[j]))
 sv=np.linalg.svd(M,compute_uv=False)
 return {'cutoff':U,'nodes':n,'inner_nodes':inner,'operator_norm_nystrom':float(sv[0]),'hilbert_schmidt_norm_nystrom':float(np.linalg.norm(M)),'smallest_singular_value':float(sv[-1])}
out={'runs':[run(U) for U in (1,2,3,4,5)],'method':'Gauss-Legendre Nystrom on the unitarily transformed kernel','certified':False,'rh_proved':False}
if __name__=='__main__':
 p=Path(__file__).parents[1]/'results'/'clark-characteristic-cross-storage-scout.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

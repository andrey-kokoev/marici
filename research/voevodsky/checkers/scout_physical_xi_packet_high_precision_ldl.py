"""High-precision LDL scout for the three physical Xi de Branges packets.

This avoids the double-precision eigensolve used by the earlier Douglas scout.
It is still not interval arithmetic, so it reports stability rather than proof.
"""
import json,sys
from pathlib import Path
try: import mpmath as mp
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import mpmath as mp

PACKETS=[[(0,1),(5,1),(10,1),(15,1)],[(2,2),(8,3),(14,2),(20,4)],[(5,.25),(12,.5),(20,.75),(28,1)]]

def evaluate(raw,dps):
 mp.mp.dps=dps;pi=mp.pi
 def xi(s): return mp.mpf('.5')*s*(s-1)*pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
 def X(z): return xi(mp.mpf('.5')+1j*z)
 def E(z): return X(z)+1j*mp.diff(X,z)
 def Es(z): return X(z)-1j*mp.diff(X,z)
 def k(z,w): return (E(z)*mp.conj(E(w))-Es(z)*mp.conj(Es(w)))/(2*pi*1j*(mp.conj(w)-z))
 pts=[mp.mpc(x,y) for x,y in raw];n=len(pts)
 K=mp.matrix(n);L=mp.eye(n);D=[]
 for i in range(n):
  for j in range(n): K[i,j]=(k(pts[i],pts[j])+mp.conj(k(pts[j],pts[i])))/2
 for j in range(n):
  dj=mp.re(K[j,j]-sum(L[j,q]*D[q]*mp.conj(L[j,q]) for q in range(j)));D.append(dj)
  for i in range(j+1,n): L[i,j]=(K[i,j]-sum(L[i,q]*D[q]*mp.conj(L[j,q]) for q in range(j)))/dj
 residual=max(abs(K[i,j]-sum(L[i,q]*D[q]*mp.conj(L[j,q]) for q in range(n))) for i in range(n) for j in range(n))
 return {'dps':dps,'ldl_pivots':[mp.nstr(x,30) for x in D],'all_pivots_positive':all(x>0 for x in D),'minimum_pivot':mp.nstr(min(D),30),'ldl_residual':mp.nstr(residual,8)}

out={'packets':[],'method':'unpivoted Hermitian LDL at 60, 100, and 160 decimal digits','interval_certified':False,'rh_proved':False}
for raw in PACKETS: out['packets'].append({'points':raw,'runs':[evaluate(raw,d) for d in (60,100,160)]})
if __name__=='__main__':
 p=Path(__file__).parents[1]/'results'/'physical-xi-packet-high-precision-ldl-scout.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

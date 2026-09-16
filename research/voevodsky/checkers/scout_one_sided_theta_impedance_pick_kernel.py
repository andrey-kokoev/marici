"""Finite-packet scout for positive-realness of m(s)=-F'(s)/F(s)."""
import json,sys
from pathlib import Path
try:
 import mpmath as mp
 import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import mpmath as mp;import numpy as np
mp.mp.dps=60;pi=mp.pi
def phi(u):
 e=mp.exp(2*u);return mp.nsum(lambda n:(4*pi*pi*n**4*mp.exp(mp.mpf('4.5')*u)-6*pi*n*n*mp.exp(mp.mpf('2.5')*u))*mp.exp(-pi*n*n*e),[1,mp.inf])
def F(s,k=0): return mp.quad(lambda u:(u**k)*phi(u)*mp.exp(-s*u),[0,1,2,4])
def m(s): return F(s,1)/F(s,0)
def run(raw):
 p=[mp.mpc(a,b) for a,b in raw];mv=[m(s) for s in p]
 K=np.array([[complex((mv[i]+mp.conj(mv[j]))/(p[i]+mp.conj(p[j]))) for j in range(len(p))] for i in range(len(p))]);K=(K+K.conj().T)/2
 lam=np.linalg.eigvalsh(K)
 return {'points':raw,'m_values':[[float(mp.re(x)),float(mp.im(x))] for x in mv],'real_parts_positive':all(mp.re(x)>0 for x in mv),'kernel_eigenvalues':[float(x) for x in lam],'kernel_positive_numerically':bool(lam[0]>-1e-12)}
packets=[[(.5,0),(.5,2),(.5,5),(.5,10)],[(1,1),(2,3),(3,7),(4,12)],[(.1,5),(.2,10),(.5,15),(1,20)]]
out={'packets':[run(p) for p in packets],'method':'60-digit quadrature followed by double Hermitian eigensolve','certified':False,'rh_proved':False}
if __name__=='__main__':
 p=Path(__file__).parents[1]/'results'/'one-sided-theta-impedance-pick-kernel-scout.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

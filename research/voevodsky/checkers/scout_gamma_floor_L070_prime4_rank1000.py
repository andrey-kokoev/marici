#!/usr/bin/env python3
"""Scout the monotone gamma-floor replacement for the frequency tail above 250."""
import json,math,sys
from pathlib import Path
try:
 import numpy as np
 from scipy.special import digamma,spherical_jn,iv
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
 from scipy.special import digamma,spherical_jn,iv
from numpy.polynomial.legendre import leggauss
L=.70;N=1000;orders=np.arange(N);norm=2*L*np.sqrt((2*orders+1)/(2*L));ph=(-1.)**(orders//2);Q=300;nodes,wts=leggauss(Q);G=np.zeros((N,N));K=np.zeros((N,N))
for aa,bb in [(0,1),(1,2),(2,4),(4,8),(8,16),(16,32),(32,64),(64,128),(128,250)]:
 u=(aa+bb)/2+(bb-aa)*nodes/2;w=(bb-aa)*wts/2;V=(norm[:,None]*ph[:,None]*spherical_jn(orders[:,None],L*u[None,:])).T;q=(digamma(.25+.5j*u).real-math.log(math.pi))/2
 for target,weight in ((G,w*q/math.pi),(K,w/math.pi)):
  B=(V.T*weight)@V;B[0::2,1::2]=0;B[1::2,0::2]=0;target+=B
# Exact spatial prime overlaps by Gauss polynomial quadrature.
xg,wg=leggauss(N);P=np.zeros((N,N))
for p,c in ((2,math.log(2)/math.sqrt(2)),(3,math.log(3)/math.sqrt(3)),(4,math.log(2)/2)):
 a=math.log(p);lo=-L;hi=L-a;t=(lo+hi)/2+(hi-lo)*xg/2;ww=(hi-lo)*wg/2
 def legvals(x):
  V=np.empty((len(x),N));V[:,0]=1;V[:,1]=x
  for n in range(1,N-1):V[:,n+1]=((2*n+1)*x*V[:,n]-n*V[:,n-1])/(n+1)
  return V*np.sqrt((2*orders+1)/(2*L))
 X=legvals(t/L);Y=legvals((t+a)/L);T=(X.T*ww)@Y;P-=c*(T+T.T)/2
x=L/2;ap=np.array([2*L*math.sqrt((2*n+1)/(2*L))*math.sqrt(math.pi/(2*x))*iv(n+.5,x) for n in orders]);am=ap*((-1.)**orders);E=(np.outer(ap,am)+np.outer(am,ap))/2
q250=(digamma(.25+125j).real-math.log(math.pi))/2;A=G+P+E+q250*(np.eye(N)-K);A=(A+A.T)/2;np.savez(Path(__file__).parents[1]/'results'/'gamma_floor_L070_prime4_rank1000_midpoint.npz',matrix=A);ev,U=np.linalg.eigh(A);np.savez(Path(__file__).parents[1]/'results'/'gamma_floor_L070_prime4_rank1000_dangerous_vectors.npz',eigenvalues=ev[:8],vectors=U[:,:8]);F=A[:670,:670];B=A[:670,670:];C=A[670:,670:];S=F-B@np.linalg.solve(C,B.T)
out={'schema':'marici.voevodsky.gamma-floor-L070-prime4-rank1000-scout.v1','cutoff':250,'gamma_floor':q250,'min_eigenvalue':float(ev[0]),'rank670_compression_min':float(np.linalg.eigvalsh(F)[0]),'finite_tail_min':float(np.linalg.eigvalsh(C)[0]),'rank670_schur_min_through_1000':float(np.linalg.eigvalsh(S)[0]),'cross_norm':float(np.linalg.svd(B,compute_uv=False)[0]),'negative_eigenvalues_below_minus_1e-10':int(np.sum(ev<-1e-10)),'smallest_ten':[float(x) for x in ev[:10]],'status':'floating scout; monotonic gamma-floor inequality not interval promoted','passed':True,'rh_proved':False};p=Path(__file__).parents[1]/'results'/'gamma_floor_L070_prime4_rank1000_scout.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

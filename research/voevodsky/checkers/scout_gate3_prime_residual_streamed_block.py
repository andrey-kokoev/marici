#!/usr/bin/env python3
"""Exact-degree streamed Gauss evaluation of one high prime residual block."""
import json,math,sys
from pathlib import Path
try:
 import numpy as np
 from scipy.special import roots_legendre,eval_legendre
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
 from scipy.special import roots_legendre,eval_legendre
from numpy.polynomial.legendre import legval
root=Path(__file__).parents[1]/'results';m=int(sys.argv[1]);extra=int(sys.argv[2]) if len(sys.argv)>2 else 0;lo=1000*m;hi=lo+1000;d=np.load(root/'regularized_union_tail_maps_L0649_L065.npz');U=d['packet']-d['tail_maps'][4];L=.6495;q=(hi+1000+2)//2+extra;xg,wg=roots_legendre(q);R=np.zeros((1000,40));k=np.arange(1000);sc=np.sqrt((2*k+1)/(2*L));fp=np.array([legval(1,U[:,j]*sc) for j in range(40)]);fm=np.array([legval(-1,U[:,j]*sc) for j in range(40)]);J=np.zeros_like(R);ns=np.arange(lo,hi)
def vals(z,maxn,keepfrom=0):
 out=np.empty((len(z),maxn-keepfrom));p0=np.ones(len(z));p1=z.copy()
 if keepfrom==0:out[:,0]=p0
 if keepfrom<=1<maxn:out[:,1-keepfrom]=p1
 for n in range(1,maxn-1):
  p2=((2*n+1)*z*p1-n*p0)/(n+1)
  if n+1>=keepfrom:out[:,n+1-keepfrom]=p2
  p0,p1=p1,p2
 return out
for p in (2,3):
 a=math.log(p);left=-L;right=L-a;t=(left+right)/2+(right-left)*xg/2;ww=(right-left)*wg/2;zx=t/L;zy=(t+a)/L;Xs=vals(zx,1000)*sc;Ys=vals(zy,1000)*sc;so=np.sqrt((2*ns+1)/(2*L));Xo=vals(zx,hi,lo)*so;Yo=vals(zy,hi,lo)*so;c=math.log(p)/math.sqrt(p);R-=.5*c*(Xo.T@(ww[:,None]*(Ys@U))+Yo.T@(ww[:,None]*(Xs@U)))
 atoms=[((L-a)/L,.5*c*fp),((-L+a)/L,-.5*c*fm)]
 for y,row in atoms:
  ker=eval_legendre(ns+1,y)-eval_legendre(ns-1,y);fac=-np.sqrt(L*(2*ns+1)/2)/(2*ns+1);J+=(fac*ker)[:,None]*row
S=R-J;op=float(np.linalg.norm(S,2));out={'schema':'marici.voevodsky.gate3-prime-residual-streamed-block.v1','m':m,'mode_range':[lo,hi-1],'gauss_nodes':q,'extra_gauss_nodes':extra,'smooth_norm':op,'m_times_smooth':m*op,'target':.02,'passed_scout':m*op<.02,'status':'floating exact-degree Gauss; gamma and endpoint exponentially small but omitted','passed':False,'rh_proved':False};p=root/f'gate3_prime_residual_streamed_block_m{m}_extra{extra}.json';p.write_text(json.dumps(out,indent=2)+'\n');np.savez_compressed(root/f'gate3_prime_residual_streamed_block_m{m}_extra{extra}.npz',smooth=S);print(json.dumps(out,indent=2));assert out['passed_scout']

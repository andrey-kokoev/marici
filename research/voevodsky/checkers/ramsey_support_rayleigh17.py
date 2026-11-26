"""Collision relaxation and spectral upper certificate for the matched cores. Cannot use quartet verdicts as input to optimization. Theta dual M=tI+Y-J, Y supported only on conflicting pairs: for a compatible panel of k distinct supports, x'Mx=k(t-k). All supports here miss at least one five, forbidding repeats. If rounded Gram bound fails, test separable first-anchor bounds."""
import json,itertools,collections,sys
from pathlib import Path
import numpy as np
import cvxpy as cp
from scipy.optimize import linprog
P=Path(__file__).resolve().parents[1]/'results';data=json.loads((P/'ramsey_frozen_gain_control.json').read_text())[1];out=[]
def theta(G):
 n=len(G);t=cp.Variable();Y=cp.Variable((n,n),symmetric=True);allowed=1-np.eye(n)-G.astype(int);M=t*np.eye(n)+cp.multiply(allowed,Y)-np.ones((n,n));prob=cp.Problem(cp.Minimize(t),[M>>0]);prob.solve(solver='SCS',eps=1e-5,max_iters=5000,verbose=False);return float(t.value),np.asarray(Y.value)*allowed
for r in data:
 if r['score']!=4:continue
 a=r['core'];I=[0]
 for j,v in enumerate(a):I.extend([s|1<<j for s in I if not s&v])
 S=[s for s in I if all(s&(v|1<<i) for i,v in enumerate(a))];Q=[q for q in I if q.bit_count()==5];B=np.array([[int(not s&q) for s in S] for q in Q]);K=B.T@B;G=(K==0);assert not np.diag(G).any();lp=linprog(-np.ones(len(S)),A_ub=B,b_ub=np.ones(len(Q)));assert lp.success
 # Exact rational relaxation witness: scaled rounded-down LP masses, rescaled to total 4. Record numerator of collision polynomial.
 y=np.floor(np.maximum(0,lp.x)*10**7).astype('int64');den=int(y.sum());m=4*(B@y);assert min(m)>=0 and max(m)<=den and 4*max(y)<=den;energy=sum(int(z)*(int(z)-den) for z in m)
 t,Y=theta(G);print('n',len(S),'degree range',np.sum(G,axis=0).min(),np.sum(G,axis=0).max(),'real energy',energy/den**2,'theta',t,flush=True)
 rec=dict(core=a,supports=S,theta_approx=t,frac_den=den,frac_num={s:4*int(v) for s,v in zip(S,y) if v},energy_num=energy);out.append(rec)
 # Robust upper bound <4? Round dual and test M by exact Sylvester pivots, if possible.
 if t<3.999:
  for scale in (4,8,16,32,64,128,256,1000):
   T=4*scale-1;Z=np.rint(scale*Y).astype(int);H=T*np.eye(len(S),dtype=int)+Z-scale
   if np.linalg.eigvalsh(H)[0]<=0:continue
   # For this fixed rounded conflict matrix find lowest positive-definite integer diagonal offset.
   while np.linalg.eigvalsh(H)[0]>1:T-=1;H-=np.eye(len(S),dtype=int)
   h=H.tolist();prev=1
   for i in range(len(h)):
    pivot=h[i][i];assert pivot>0
    for j in range(i+1,len(h)):
     for k in range(i+1,len(h)):h[j][k]=(pivot*h[j][k]-h[j][i]*h[i][k])//prev
    prev=pivot
   rec.update(scale=scale,T=T,dual=Z.tolist());print('exact theta certificate',T,scale,flush=True);break
  assert 'dual' in rec
(P/'ramsey_support_rayleigh17.json').write_text(json.dumps(out)+'\n')

from __future__ import annotations
import json,math
from pathlib import Path
import numpy as np
from scipy.linalg import eigh
from scipy.special import digamma
from numpy.polynomial.legendre import leggauss,legvander

R=100.0
LS=[0.35,0.55,0.70,0.90,1.10]

def mangoldt_terms(L):
 out=[]
 for n in range(2,int(math.exp(2*L))+1):
  p=None;m=n
  for q in range(2,int(math.sqrt(n))+2):
   if m%q==0:
    p=q
    while m%q==0:m//=q
    break
  if p is None:p=n;m=1
  if m==1:out.append((n,math.log(p)/math.sqrt(n)))
 return out

def frequency_nodes(n=120):
 edges=np.array([0.,1.,2.,4.,8.,16.,32.,64.,128.,250.]);z,w=leggauss(n);us=[];ws=[]
 for a,b in zip(edges[:-1],edges[1:]):
  q=(a+b)/2+(b-a)*z/2;v=(b-a)*w/2
  us.extend((-q[::-1]).tolist());ws.extend(v[::-1].tolist());us.extend(q.tolist());ws.extend(v.tolist())
 o=np.argsort(us);return np.asarray(us)[o],np.asarray(ws)[o]

def one(L,nx=400,degree=160):
 z,w=leggauss(nx);x=L*z;wx=L*w;sw=np.sqrt(wx)
 E=sw[:,None]*legvander(z,degree-1)*np.sqrt((2*np.arange(degree)+1)/(2*L))[None,:]
 d=x[:,None]-x[None,:];T=(sw[:,None]*sw[None,:])*(R/math.pi)*np.sinc(R*d/math.pi)
 H=(E.T@T@E);H=(H+H.T)/2;vals,V=eigh(H)
 trace=2*L*R/math.pi;K=None;res=None
 for k in range(1,degree+1):
  r=trace-float(np.sum(vals[-k:]))
  if r<1/130:K=k;res=r;break
 u,wu=frequency_nodes();symbol=(np.real(digamma(.25+.5j*u))-math.log(math.pi))/2
 terms=mangoldt_terms(L)
 for n,c in terms:symbol-=c*np.cos(u*math.log(n))
 FE=(np.exp(-1j*u[:,None]*x[None,:])*(np.sqrt(wu)[:,None]*sw[None,:]/math.sqrt(2*math.pi)))@E
 A=np.real(FE.conj().T@(symbol[:,None]*FE))
 ep=E.T@(sw*np.exp(x/2));em=E.T@(sw*np.exp(-x/2));A+=(np.outer(ep,em)+np.outer(em,ep))/2;A=(A+A.T)/2
 ans={'L':L,'support_radius_2L':2*L,'mangoldt_terms':[n for n,_ in terms],
      'trace':trace,'degree':degree,'selected_rank_for_trace_floor':K,'trace_residual':res,
      'full_degree_minimum':float(np.linalg.eigvalsh(A)[0])}
 if K is not None:
  O=np.column_stack((V[:,-K:],V[:,:-K]));AO=O.T@A@O;F=AO[:K,:K];B=AO[:K,K:];C=AO[K:,K:]
  cm=float(np.linalg.eigvalsh(C)[0]);ans.update({'tail_floor':(1-130*res)/40,
   'selected_form_minimum':float(np.linalg.eigvalsh(F)[0]),'resolved_tail_minimum':cm})
  if cm>0:
   J=F-B@np.linalg.solve(C,B.T);ans['finite_degree_schur_minimum']=float(np.linalg.eigvalsh((J+J.T)/2)[0])
 return ans

def main():
 rows=[one(L) for L in LS]
 out={'schema':'marici.voevodsky.support-window-scaling-scout.v1','R':R,'rows':rows,
      'passed':all(r.get('selected_rank_for_trace_floor') is not None for r in rows),
      'strength':'floating scaling scout; not a continuum certificate'}
 text=json.dumps(out,indent=2,sort_keys=True);Path('research/voevodsky/results/support_window_scaling_scout.json').write_text(text+'\n');print(text)
if __name__=='__main__':main()

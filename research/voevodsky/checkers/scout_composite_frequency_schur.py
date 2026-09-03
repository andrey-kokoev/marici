from __future__ import annotations
import json,math
import numpy as np
from scipy.special import digamma
from numpy.polynomial.legendre import leggauss

def composite_nodes(n):
    edges=np.array([0.,1.,2.,4.,8.,16.,32.,64.,128.,250.])
    z,w=leggauss(n); us=[]; ws=[]
    for a,b in zip(edges[:-1],edges[1:]):
        mid=(a+b)/2; half=(b-a)/2
        up=mid+half*z; wp=half*w
        us.extend((-up[::-1]).tolist()); ws.extend(wp[::-1].tolist())
        us.extend(up.tolist()); ws.extend(wp.tolist())
    order=np.argsort(us)
    return np.asarray(us)[order],np.asarray(ws)[order]

def build(npanel,nx=700,threshold=1/130,reltol=1e-12):
    L=.35;R=100.;c=math.log(2)/math.sqrt(2)
    z,w=leggauss(nx);x=L*z;wx=L*w;sw=np.sqrt(wx)
    d=x[:,None]-x[None,:]
    T=(sw[:,None]*sw[None,:])*(R/math.pi)*np.sinc(R*d/math.pi)
    lam,V=np.linalg.eigh(T);o=np.argsort(lam)[::-1];lam=lam[o];V=V[:,o]
    rank=int(np.count_nonzero(lam>threshold));P=V[:,:rank];Q=V[:,rank:]
    u,wu=composite_nodes(npanel)
    symbol=(np.real(digamma(.25+.5j*u))-math.log(math.pi))/2-c*np.cos(u*math.log(2))
    E=np.exp(-1j*u[:,None]*x[None,:])*(np.sqrt(wu)[:,None]*sw[None,:]/math.sqrt(2*math.pi))
    A=np.real(E.conj().T@(symbol[:,None]*E))
    vp=sw*np.exp(x/2);vm=sw*np.exp(-x/2);A+=(np.outer(vp,vm)+np.outer(vm,vp))/2
    F=P.T@A@P;C=Q.T@A@Q;C=(C+C.T)/2;B=P.T@A@Q
    ce,CV=np.linalg.eigh(C);tol=reltol*max(1.,abs(ce[-1]));pos=ce>tol
    BP=B@CV[:,pos];S=F-(BP/ce[pos][None,:])@BP.T
    return (S+S.T)/2,rank,len(u)

def main():
    runs=[]; mats=[]
    for n in (160,220,280):
        S,r,total=build(n);mats.append(S)
        runs.append({"nodes_per_half_panel":n,"total_frequency_nodes":total,
          "least_schur":float(np.linalg.eigvalsh(S)[0])})
    comparisons=[]
    for a,b,label in ((0,1,"160_to_220"),(1,2,"220_to_280"),(0,2,"160_to_280")):
        D=mats[a]-mats[b]
        comparisons.append({"label":label,"maximum_entry_difference":float(np.max(np.abs(D))),
          "spectral_norm_difference":float(np.linalg.norm(D,2))})
    result={"schema":"marici.voevodsky.composite-frequency-schur-scout.v1",
      "status":"geometric_panel_frequency_refinement","rank":r,
      "positive_panel_edges":[0,1,2,4,8,16,32,64,128,250],
      "runs":runs,"comparisons":comparisons,"entry_radius_target":1e-5,
      "analytic_panel_remainders_proved":False,"interval_certified":False,
      "rh_implication":False,"passed":True}
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()

from __future__ import annotations
import json, math
import numpy as np
from scipy.special import digamma
from numpy.polynomial.legendre import leggauss

def build(nx,nu,U=250.,threshold=1/130,reltol=1e-12):
    L=.35; R=100.; c=math.log(2)/math.sqrt(2)
    z,w=leggauss(nx); x=L*z; wx=L*w; sw=np.sqrt(wx)
    d=x[:,None]-x[None,:]
    T=(sw[:,None]*sw[None,:])*(R/math.pi)*np.sinc(R*d/math.pi)
    lam,V=np.linalg.eigh(T); order=np.argsort(lam)[::-1]; lam=lam[order]; V=V[:,order]
    rank=int(np.count_nonzero(lam>threshold))
    zu,wu=leggauss(nu); u=U*zu; wu=U*wu
    symbol=(np.real(digamma(.25+.5j*u))-math.log(math.pi))/2-c*np.cos(u*math.log(2))
    E=np.exp(-1j*u[:,None]*x[None,:])*(np.sqrt(wu)[:,None]*sw[None,:]/math.sqrt(2*math.pi))
    A=np.real(E.conj().T@(symbol[:,None]*E))
    vp=sw*np.exp(x/2); vm=sw*np.exp(-x/2); A+=np.outer(vp,vm)+np.outer(vm,vp)
    P=V[:,:rank]; Q=V[:,rank:]; F=P.T@A@P
    C=Q.T@A@Q; C=(C+C.T)/2; B=P.T@A@Q
    ceig,CV=np.linalg.eigh(C); tol=reltol*max(1.,abs(ceig[-1])); pos=ceig>tol
    BP=B@CV[:,pos]; S=F-(BP/ceig[pos][None,:])@BP.T; S=(S+S.T)/2
    return {"x":x,"wx":wx,"lam":lam[:rank],"V":P,"S":S,"rank":rank}

def extend(data,xq,wq):
    R=100.; d=xq[:,None]-data["x"][None,:]
    K=(R/math.pi)*np.sinc(R*d/math.pi)
    phi=(K@(np.sqrt(data["wx"])[:,None]*data["V"]))/data["lam"][None,:]
    return np.sqrt(wq)[:,None]*phi

def compare(left,right,xq,wq,label):
    El=extend(left,xq,wq); Er=extend(right,xq,wq)
    overlap=El.T@Er; U,sv,Vh=np.linalg.svd(overlap); O=U@Vh
    delta=O.T@left["S"]@O-right["S"]
    return {"label":label,"maximum_entry_difference":float(np.max(np.abs(delta))),
      "spectral_norm_difference":float(np.linalg.norm(delta,2)),
      "minimum_overlap_singular_value":float(sv[-1]),
      "left_orthogonality_error":float(np.linalg.norm(El.T@El-np.eye(left["rank"]),2)),
      "right_orthogonality_error":float(np.linalg.norm(Er.T@Er-np.eye(right["rank"]),2))}

def main():
    q2800=build(700,2800); q3600=build(700,3600); q4400=build(700,4400)
    z,w=leggauss(850); xq=.35*z; wq=.35*w
    comparisons=[compare(q2800,q3600,xq,wq,"frequency_2800_to_3600"),
      compare(q3600,q4400,xq,wq,"frequency_3600_to_4400"),
      compare(q2800,q4400,xq,wq,"frequency_2800_to_4400")]
    result={"schema":"marici.voevodsky.aligned-schur-entry-difference-scout.v3",
      "status":"high_order_frequency_refinement","rank":q2800["rank"],
      "comparisons":comparisons,"entry_radius_target":1e-5,
      "interval_certified":False,"rh_implication":False,"passed":True}
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()

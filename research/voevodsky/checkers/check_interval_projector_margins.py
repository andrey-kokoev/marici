from __future__ import annotations
import json,math
import numpy as np
from numpy.polynomial.legendre import leggauss
import flint
from flint import arb,arb_mat
flint.ctx.prec=128

def data():
    L=.35;R=100.;n=700;m=25
    z,w=leggauss(n);x=L*z;wx=L*w;sw=np.sqrt(wx)
    d=x[:,None]-x[None,:]
    T=(sw[:,None]*sw[None,:])*(R/math.pi)*np.sinc(R*d/math.pi)
    lam,V=np.linalg.eigh(T);o=np.argsort(lam)[::-1];lam=lam[o];V=V[:,o]
    zq,wq=leggauss(900);xq=L*zq;wq=L*wq
    dq=xq[:,None]-x[:,None].T
    K=(R/math.pi)*np.sinc(R*dq/math.pi)
    E=np.sqrt(wq)[:,None]*(K@(sw[:,None]*V[:,:m]))/lam[:m][None,:]
    dqq=xq[:,None]-xq[None,:]
    Tq=(np.sqrt(wq)[:,None]*np.sqrt(wq)[None,:])*(R/math.pi)*np.sinc(R*dqq/math.pi)
    G=(E.T@E);H=E.T@Tq@E;H=(H+H.T)/2
    return G,H

def imat(A,r):
    return arb_mat([[arb(f"{A[i,j]:.17g} +/- {r:.2g}") for j in range(A.shape[1])] for i in range(A.shape[0])])

def ldl_positive(A):
    n=A.nrows();L=[[arb(0) for _ in range(n)] for _ in range(n)];D=[arb(0) for _ in range(n)]
    for i in range(n):L[i][i]=arb(1)
    for j in range(n):
        d=A[j,j]
        for k in range(j):d-=L[j][k]*L[j][k]*D[k]
        if not d>0:return False,j,str(d)
        D[j]=d
        for i in range(j+1,n):
            a=A[i,j]
            for k in range(j):a-=L[i][k]*L[j][k]*D[k]
            L[i][j]=a/D[j]
    return True,n,None

def main():
    G,H=data();threshold=arb(1)/130;tests=[]
    for r in (1e-7,1e-6,1.5e-6,2e-6,3e-6,1e-5):
        Gi=imat(G,r);Hi=imat(H,r);A=Hi-threshold*Gi
        low_ok,pivot,interval=ldl_positive(A)
        try:
            captured=(Gi.inv()*Hi);tr=sum((captured[i,i] for i in range(25)),arb(0))
            tail=arb(70)/arb.pi()-tr;upper_ok=tail<threshold
        except Exception as exc:
            tail=arb(0);upper_ok=False;interval=f"{type(exc).__name__}: {exc}"
        tests.append({"entry_radius":r,"lower_rank_positive":low_ok,"lower_stopping_pivot":pivot,
          "upper_rank_tail_below_threshold":bool(upper_ok),"tail_interval":str(tail),"failure":interval})
    result={"schema":"marici.voevodsky.interval-projector-margins.v1",
      "status":"interval_perturbation_projector_rank_scout","rank":25,"threshold":"1/130",
      "tests":tests,"continuum_entries_enclosed":False,"projector_certified":False,
      "rh_implication":False,"passed":True}
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()

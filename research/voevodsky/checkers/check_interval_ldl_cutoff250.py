from __future__ import annotations
import json, math
import numpy as np
from scipy.special import digamma
from numpy.polynomial.legendre import leggauss
import flint
from flint import arb

flint.ctx.prec = 128

def schur_matrix(nx=560, nu=2200, U=250., threshold=1/130, reltol=1e-12):
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
    vp=sw*np.exp(x/2); vm=sw*np.exp(-x/2)
    A += np.outer(vp,vm)+np.outer(vm,vp)
    P=V[:,:rank]; Q=V[:,rank:]
    F=P.T@A@P; C=Q.T@A@Q; C=(C+C.T)/2; B=P.T@A@Q
    ceig,CV=np.linalg.eigh(C); tol=reltol*max(1.,abs(ceig[-1])); pos=ceig>tol
    BP=B@CV[:,pos]
    S=F-(BP/ceig[pos][None,:])@BP.T
    return (S+S.T)/2, rank

def interval_ldl_positive(A, radius):
    n=A.shape[0]; L=[[arb(0) for _ in range(n)] for _ in range(n)]; D=[arb(0) for _ in range(n)]
    for i in range(n): L[i][i]=arb(1)
    min_lower=None
    for j in range(n):
        dj=arb(f"{A[j,j]:.17g} +/- {radius:.2g}")
        for k in range(j): dj -= L[j][k]*L[j][k]*D[k]
        if not (dj>0): return False,j,str(dj),min_lower
        D[j]=dj; lo=float(dj.lower()); min_lower=lo if min_lower is None else min(min_lower,lo)
        for i in range(j+1,n):
            aij=arb(f"{A[i,j]:.17g} +/- {radius:.2g}")
            for k in range(j): aij -= L[i][k]*L[j][k]*D[k]
            L[i][j]=aij/D[j]
    return True,n,None,min_lower

def main():
    S,rank=schur_matrix(); target=.001; A=S-target*np.eye(rank)
    tests=[]
    for radius in (1e-8,1e-6,1e-5,3e-5,1e-4,3e-4,1e-3):
        ok,pivot,interval,min_lower=interval_ldl_positive(A,radius)
        tests.append({"entry_radius":radius,"positive":ok,"stopping_pivot":pivot,
                      "failed_pivot_interval":interval,"minimum_pivot_lower":min_lower})
    result={"schema":"marici.voevodsky.interval-ldl-cutoff250.v1",
      "status":"interval_perturbation_radius_scout","rank":rank,"target_margin":target,
      "tests":tests,"matrix_entries_continuum_enclosed":False,
      "rh_implication":False,"passed":True}
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()

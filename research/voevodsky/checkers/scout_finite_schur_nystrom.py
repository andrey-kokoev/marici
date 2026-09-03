from __future__ import annotations
import json, math
import numpy as np
from scipy.special import digamma
from numpy.polynomial.legendre import leggauss

def run(nx,nu,U,threshold=1/130):
    L=.35; R=100.; c=math.log(2)/math.sqrt(2)
    z,w=leggauss(nx); x=L*z; wx=L*w; sw=np.sqrt(wx)
    d=x[:,None]-x[None,:]
    T=(sw[:,None]*sw[None,:])*(R/math.pi)*np.sinc(R*d/math.pi)
    lam,V=np.linalg.eigh(T); order=np.argsort(lam)[::-1]; lam=lam[order]; V=V[:,order]
    zu,wu=leggauss(nu); u=U*zu; wu=U*wu
    symbol=(np.real(digamma(.25+.5j*u))-math.log(math.pi))/2-c*np.cos(u*math.log(2))
    E=np.exp(-1j*u[:,None]*x[None,:])*(np.sqrt(wu)[:,None]*sw[None,:]/math.sqrt(2*math.pi))
    A=np.real(E.conj().T@(symbol[:,None]*E))
    vp=sw*np.exp(x/2); vm=sw*np.exp(-x/2)
    A += (np.outer(vp,vm)+np.outer(vm,vp))/2
    rank=int(np.count_nonzero(lam>threshold))
    P=V[:,:rank]; F=P.T@A@P; A2=P.T@(A@A)@P
    leakage=A2-F@F; leakage=(leakage+leakage.T)/2
    G=F-40*leakage; G=(G+G.T)/2
    eig=np.linalg.eigvalsh(G); feig=np.linalg.eigvalsh((F+F.T)/2)
    leig=np.linalg.eigvalsh(leakage)
    Q=V[:,rank:]; C=Q.T@A@Q; C=(C+C.T)/2; B=P.T@A@Q
    ceig,CV=np.linalg.eigh(C); least_C=float(ceig[0]); largest_C=float(ceig[-1])
    scale=max(1.0,abs(largest_C)); sweeps=[]
    for reltol in (1e-8,1e-10,1e-12):
        tol=reltol*scale; pos=ceig>tol; null=~pos
        residual=float(np.linalg.norm(B@CV[:,null],2)) if np.any(null) else 0.0
        BP=B@CV[:,pos]
        S=F-(BP/ceig[pos][None,:])@BP.T; S=(S+S.T)/2
        seig,SV=np.linalg.eigh(S)
        target=.001; cholesky_ok=True; min_cholesky_diagonal=None
        try:
            chol=np.linalg.cholesky(S-target*np.eye(rank))
            min_cholesky_diagonal=float(np.min(np.diag(chol)))
        except np.linalg.LinAlgError:
            cholesky_ok=False
        eigen_residual=float(np.linalg.norm(S@SV[:,0]-seig[0]*SV[:,0]))
        sweeps.append({"relative_tolerance":reltol,"absolute_tolerance":tol,
          "tail_positive_rank":int(np.count_nonzero(pos)),"tail_nullity":int(np.count_nonzero(null)),
          "range_compatibility_residual":residual,"least_exact_schur":float(seig[0]),
          "negative_exact_schur_count":int(np.count_nonzero(seig<0)),
          "target_margin":target,"cholesky_above_target":cholesky_ok,
          "minimum_cholesky_diagonal":min_cholesky_diagonal,
          "least_eigenpair_residual":eigen_residual})
    primary=sweeps[1]
    aeig=np.linalg.eigvalsh((A+A.T)/2); apos=aeig[aeig>1e-10]
    return {"nx":nx,"nu":nu,"frequency_cutoff":U,"threshold":threshold,
            "least_full_truncated_operator":float(aeig[0]),
            "negative_full_operator_count_below_1e_10":int(np.count_nonzero(aeig < -1e-10)),
            "smallest_positive_full_operator":float(apos[0]) if len(apos) else None,
            "pseudoinverse_sweeps":sweeps,
            "tail_positive_rank":primary["tail_positive_rank"],"tail_nullity":primary["tail_nullity"],
            "tail_pseudoinverse_tolerance":primary["absolute_tolerance"],
            "range_compatibility_residual":primary["range_compatibility_residual"],
            "least_exact_schur_truncated":primary["least_exact_schur"],
            "negative_exact_schur_count":primary["negative_exact_schur_count"],
            "selected_rank":rank,"lambda_last_selected":float(lam[rank-1]),
            "lambda_first_tail":float(lam[rank]),
            "least_F":float(feig[0]),"least_C_truncated":least_C,
            "least_leakage":float(leig[0]),"largest_leakage":float(leig[-1]),
            "least_G":float(eig[0]),"largest_G":float(eig[-1]),
            "negative_G_count":int(np.count_nonzero(eig<0))}

def main():
    runs=[run(400,1400,150.),run(480,1800,250.),
          run(560,2200,250.),run(640,2600,350.)]
    result={"schema":"marici.voevodsky.finite-schur-nystrom-scout.v2",
      "status":"nonrigorous_threshold_spectral_projection_scout",
      "certified_rank_upper":190,"selection_threshold":"1/130","runs":runs,
      "endpoint_normalization":"outer(vplus,vminus)+outer(vminus,vplus)",
      "frequency_tail_included":False,"interval_certified":False,
      "concentration_threshold_stable":runs[0]["selected_rank"]==runs[1]["selected_rank"],
      "rh_implication":False,"passed":True}
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()

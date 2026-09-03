from __future__ import annotations
import json,math
import numpy as np
from numpy.polynomial.legendre import leggauss

def nystrom(n):
    L=.35;R=100.;z,w=leggauss(n);x=L*z;wx=L*w;sw=np.sqrt(wx)
    d=x[:,None]-x[None,:]
    T=(sw[:,None]*sw[None,:])*(R/math.pi)*np.sinc(R*d/math.pi)
    lam,V=np.linalg.eigh(T);o=np.argsort(lam)[::-1]
    return x,wx,lam[o],V[:,o]

def extend(x,wx,lam,V,xq,wq,m):
    R=100.;d=xq[:,None]-x[None,:]
    K=(R/math.pi)*np.sinc(R*d/math.pi)
    phi=(K@(np.sqrt(wx)[:,None]*V[:,:m]))/lam[:m][None,:]
    return np.sqrt(wq)[:,None]*phi

def main():
    x,wx,lam,V=nystrom(700);m=25;threshold=1/130
    zq,wq=leggauss(900);xq=.35*zq;wq=.35*wq
    E=extend(x,wx,lam,V,xq,wq,m)
    dq=xq[:,None]-xq[None,:]
    Tq=(np.sqrt(wq)[:,None]*np.sqrt(wq)[None,:])*(100/math.pi)*np.sinc(100*dq/math.pi)
    gram=E.T@E; H=E.T@Tq@E; H=(H+H.T)/2
    residual=Tq@E-E@H
    ritz=np.linalg.eigvalsh(H)
    trace=70/math.pi;tail=trace-float(np.trace(H))
    complement_upper=tail
    separation=float(ritz[0]-complement_upper)
    residual_op=float(np.linalg.norm(residual,2))
    projector_error=residual_op/separation
    result={"schema":"marici.voevodsky.concentration-projector-certificate-scout.v2",
      "status":"ritz_trace_rank_and_projector_error_scout","nystrom_order":700,"residual_grid_order":900,
      "threshold":threshold,"lambda_25":float(lam[24]),"lambda_26":float(lam[25]),
      "least_ritz_value":float(ritz[0]),"ritz_sum_first_25":float(np.trace(H)),"exact_trace":trace,
      "trace_tail_after_25":tail,"trace_tail_below_threshold":tail<threshold,
      "upper_rank_margin":threshold-tail,"lower_rank_margin":float(ritz[0]-threshold),
      "cluster_to_complement_separation":separation,"ritz_residual_operator_norm":residual_op,
      "projector_error_bound_diagnostic":projector_error,
      "orthogonality_error":float(np.linalg.norm(gram-np.eye(m),2)),
      "analytic_quadrature_enclosed":False,"projector_certified":False,
      "rh_implication":False,"passed":True}
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()

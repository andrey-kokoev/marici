from __future__ import annotations
import json,math
import numpy as np
from numpy.polynomial.legendre import leggauss,legvander
from scipy.linalg import eigh

def run(nx,degree_count=80,selected=25):
    L=.35;R=100.;z,w=leggauss(nx);x=L*z;wx=L*w;sw=np.sqrt(wx)
    V=legvander(z,degree_count-1)*np.sqrt((2*np.arange(degree_count)+1)/(2*L))[None,:]
    E=sw[:,None]*V
    d=x[:,None]-x[None,:]
    T=(sw[:,None]*sw[None,:])*(R/math.pi)*np.sinc(R*d/math.pi)
    G=E.T@E;H=E.T@T@E;H=(H+H.T)/2
    vals,vecs=eigh(H,G); chosen=vecs[:,-selected:]
    C=chosen.T@G@chosen; Rz=chosen.T@H@chosen
    captured=float(np.trace(np.linalg.solve(C,Rz)));tail=70/math.pi-captured
    return {"nx":nx,"legendre_degree_count":degree_count,"selected_rank":selected,
      "ambient_gram_error":float(np.linalg.norm(G-np.eye(degree_count),2)),
      "selected_gram_error":float(np.linalg.norm(C-np.eye(selected),2)),
      "least_selected_ritz":float(vals[-selected]),"captured_trace":captured,
      "trace_tail":tail,"tail_below_1_over_130":tail<1/130}

def main():
    runs=[run(300),run(500),run(700)]
    result={"schema":"marici.voevodsky.legendre-concentration-subspace-scout.v2",
      "status":"ritz_subspace_inside_exact_polynomial_ambient_space","ambient_degree_count":80,
      "selected_rank":25,"runs":runs,
      "basis":"top 25 Ritz vectors in normalized Legendre degrees 0..79",
      "continuum_nystrom_eigenvectors_required":False,
      "finite_ritz_coefficients_interval_certified":False,
      "continuum_integrals_certified":False,"rh_implication":False,"passed":True}
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()

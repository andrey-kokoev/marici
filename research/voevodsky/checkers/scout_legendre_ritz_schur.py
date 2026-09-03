from __future__ import annotations
import json,math
from pathlib import Path
import numpy as np
from scipy.linalg import eigh
from scipy.special import digamma
from numpy.polynomial.legendre import leggauss,legvander

def frequency_nodes(n):
    edges=np.array([0.,1.,2.,4.,8.,16.,32.,64.,128.,250.]);z,w=leggauss(n);us=[];ws=[]
    for a,b in zip(edges[:-1],edges[1:]):
        q=(a+b)/2+(b-a)*z/2;v=(b-a)*w/2
        us.extend((-q[::-1]).tolist());ws.extend(v[::-1].tolist());us.extend(q.tolist());ws.extend(v.tolist())
    o=np.argsort(us);return np.asarray(us)[o],np.asarray(ws)[o]

def run(nx,npanel,reltol=1e-12,export_path=None):
    L=.35;R=100.;z,w=leggauss(nx);x=L*z;wx=L*w;sw=np.sqrt(wx)
    LV=legvander(z,79)*np.sqrt((2*np.arange(80)+1)/(2*L))[None,:];E80=sw[:,None]*LV
    d=x[:,None]-x[None,:];T=(sw[:,None]*sw[None,:])*(R/math.pi)*np.sinc(R*d/math.pi)
    G80=E80.T@E80;H80=E80.T@T@E80;vals,coef=eigh((H80+H80.T)/2,G80)
    Praw=E80@coef[:,-25:];P,_=np.linalg.qr(Praw,mode='reduced');full,_=np.linalg.qr(P,mode='complete');Q=full[:,25:]
    trace_residual=70/math.pi-float(np.sum(vals[-25:]));tail_floor=(1-130*trace_residual)/40
    inverse_tail_floor=1/tail_floor
    u,wu=frequency_nodes(npanel);c=math.log(2)/math.sqrt(2)
    symbol=(np.real(digamma(.25+.5j*u))-math.log(math.pi))/2-c*np.cos(u*math.log(2))
    Fm=np.exp(-1j*u[:,None]*x[None,:])*(np.sqrt(wu)[:,None]*sw[None,:]/math.sqrt(2*math.pi))
    M=np.real(Fm.conj().T@(symbol[:,None]*Fm));M2=np.real(Fm.conj().T@((symbol*symbol)[:,None]*Fm))
    vp=sw*np.exp(x/2);vm=sw*np.exp(-x/2)
    Endpoint=(np.outer(vp,vm)+np.outer(vm,vp))/2;A=M+Endpoint
    F=P.T@A@P;C=Q.T@A@Q;C=(C+C.T)/2;B=P.T@A@Q
    ce,CV=np.linalg.eigh(C)
    allL=legvander(z,nx-1)*np.sqrt((2*np.arange(nx)+1)/(2*L))[None,:]
    allE=sw[:,None]*allL; sweeps=[]
    floored_denominator=np.maximum(ce,tail_floor)
    Yfloor=CV@((CV.T@B.T)/floored_denominator[:,None]);rfloor=B.T-C@Yfloor
    Jfloor=F-B@Yfloor-Yfloor.T@B.T+Yfloor.T@C@Yfloor;Jfloor=(Jfloor+Jfloor.T)/2
    Lfloor=Jfloor-inverse_tail_floor*(rfloor.T@rfloor);Lfloor=(Lfloor+Lfloor.T)/2
    coeff_floor=allE.T@(Q@Yfloor)
    polyYfloor=allE[:,:160]@coeff_floor[:160,:];polyYfloor-=P@(P.T@polyYfloor)
    yqfloor=Q.T@polyYfloor;rfloor160=B.T-C@yqfloor
    coeff_resfloor=allE.T@(Q@rfloor160)
    Jfloor160=F-B@yqfloor-yqfloor.T@B.T+yqfloor.T@C@yqfloor;Jfloor160=(Jfloor160+Jfloor160.T)/2
    Lfloor160=Jfloor160-inverse_tail_floor*(rfloor160.T@rfloor160);Lfloor160=(Lfloor160+Lfloor160.T)/2
    floored_solve={"solution_norm":float(np.linalg.norm(Yfloor,2)),
      "residual_norm":float(np.linalg.norm(rfloor,2)),
      "legendre_tail_after_160":float(np.linalg.norm(coeff_floor[160:,:],2)),
      "least_candidate_form":float(np.linalg.eigvalsh(Jfloor)[0]),
      "least_a_posteriori_lower_form":float(np.linalg.eigvalsh(Lfloor)[0]),
      "degree_159_solution_norm":float(np.linalg.norm(polyYfloor,2)),
      "degree_159_residual_norm":float(np.linalg.norm(rfloor160,2)),
      "degree_159_least_candidate_form":float(np.linalg.eigvalsh(Jfloor160)[0]),
      "degree_159_least_a_posteriori_lower_form":float(np.linalg.eigvalsh(Lfloor160)[0])}
    finite_tail_coefficients={};residual_coefficients={};finite_candidate_matrices={}
    for cutoff in (1/40,2e-2,1.5e-2,1e-2,7.5e-3,5e-3,4e-3,3e-3,2e-3,1e-3,1e-4,1e-6,1e-8,1e-10):
        pos=ce>cutoff;Y=CV[:,pos]@((CV[:,pos].T@B.T)/ce[pos][:,None])
        residual=B.T-C@Y;coeffY=allE.T@(Q@Y)
        J=F-B@Y-Y.T@B.T+Y.T@C@Y;J=(J+J.T)/2
        lower=J-inverse_tail_floor*(residual.T@residual);lower=(lower+lower.T)/2
        entry={"tail_eigenvalue_cutoff":cutoff,"retained_tail_rank":int(np.count_nonzero(pos)),
          "tail_solution_norm":float(np.linalg.norm(Y,2)),
          "tail_solution_legendre_tail_after_160":float(np.linalg.norm(coeffY[160:,:],2)),
          "tail_solution_legendre_tail_after_300":float(np.linalg.norm(coeffY[300:,:],2)) if nx>300 else None,
          "residual_norm":float(np.linalg.norm(residual,2)),
          "least_candidate_form":float(np.linalg.eigvalsh(J)[0]),
          "least_a_posteriori_lower_form":float(np.linalg.eigvalsh(lower)[0])}
        poly_each=allE[:,:160]@coeffY[:160,:];poly_each-=P@(P.T@poly_each)
        finite_tail_coefficients[cutoff]=allE[:,:160].T@poly_each
        yq_each=Q.T@poly_each;r_each=B.T-C@yq_each
        coeff_residual=allE.T@(Q@r_each);residual_coefficients[cutoff]=coeff_residual
        J_each=F-B@yq_each-yq_each.T@B.T+yq_each.T@C@yq_each;J_each=(J_each+J_each.T)/2
        finite_candidate_matrices[cutoff]=J_each
        L_each=J_each-inverse_tail_floor*(r_each.T@r_each);L_each=(L_each+L_each.T)/2
        entry.update({"degree_159_residual_norm":float(np.linalg.norm(r_each,2)),
          "residual_legendre_tail_after_160":float(np.linalg.norm(coeff_residual[160:,:],2)),
          "residual_legendre_tail_after_300":float(np.linalg.norm(coeff_residual[300:,:],2)) if nx>300 else None,
          "degree_159_solution_norm":float(np.linalg.norm(poly_each,2)),
          "degree_159_least_candidate_form":float(np.linalg.eigvalsh(J_each)[0]),
          "degree_159_least_a_posteriori_lower_form":float(np.linalg.eigvalsh(L_each)[0])})
        if cutoff==1/40:
            polyY=allE[:,:160]@coeffY[:160,:];polyY-=P@(P.T@polyY)
            yq=Q.T@polyY;r160=B.T-C@yq
            J160=F-B@yq-yq.T@B.T+yq.T@C@yq;J160=(J160+J160.T)/2
            L160=J160-inverse_tail_floor*(r160.T@r160);L160=(L160+L160.T)/2
            Z=P-polyY;full_residual=A@Z
            Lfull=J160-inverse_tail_floor*(full_residual.T@full_residual);Lfull=(Lfull+Lfull.T)/2
            Ggamma=Z.T@M2@Z;Hendpoint=Endpoint@Z;Gendpoint=Hendpoint.T@Hendpoint
            cross=Z.T@M@Endpoint@Z
            Gglobal=Ggamma+Gendpoint+cross+cross.T;Gglobal=(Gglobal+Gglobal.T)/2
            Lexactglobal=J160-inverse_tail_floor*Gglobal;Lexactglobal=(Lexactglobal+Lexactglobal.T)/2
            global_tests=[]
            for eta in (.01,.03,.1,.3,1.):
                Gupper=(1+eta)*Ggamma+(1+1/eta)*Gendpoint
                Lglobal=J160-inverse_tail_floor*Gupper;Lglobal=(Lglobal+Lglobal.T)/2
                global_tests.append({"eta":eta,"least_global_norm_lower_form":float(np.linalg.eigvalsh(Lglobal)[0])})
            best_global=max(global_tests,key=lambda q:q["least_global_norm_lower_form"])
            entry.update({"degree_159_residual_norm":float(np.linalg.norm(r160,2)),
              "degree_159_full_residual_norm":float(np.linalg.norm(full_residual,2)),
              "degree_159_least_full_residual_lower_form":float(np.linalg.eigvalsh(Lfull)[0]),
              "degree_159_exact_global_norm":float(np.sqrt(max(0.,np.linalg.eigvalsh(Gglobal)[-1]))),
              "degree_159_exact_global_norm_lower_form":float(np.linalg.eigvalsh(Lexactglobal)[0]),
              "degree_159_global_norm_split_tests":global_tests,
              "degree_159_best_global_norm_lower_form":best_global["least_global_norm_lower_form"],
              "degree_159_best_global_norm_eta":best_global["eta"],
              "degree_159_least_candidate_form":float(np.linalg.eigvalsh(J160)[0]),
              "degree_159_least_a_posteriori_lower_form":float(np.linalg.eigvalsh(L160)[0]),
              "degree_159_coefficient_norm":float(np.linalg.norm(coeffY[:160,:],2))})
        sweeps.append(entry)
    least_residual=sweeps[-1];best_corrected=max(sweeps,key=lambda q:q["degree_159_least_a_posteriori_lower_form"])
    floored_margin=floored_solve["degree_159_least_a_posteriori_lower_form"]
    if floored_margin>best_corrected["degree_159_least_a_posteriori_lower_form"]:
        selected_kind="spectral_floor";selected_parameter=tail_floor
        selected_margin=floored_margin;tailcoef=allE[:,:160].T@polyYfloor;residualcoef=coeff_resfloor;candidateJ=Jfloor160
    else:
        selected_kind="hard_cutoff";selected_parameter=best_corrected["tail_eigenvalue_cutoff"]
        selected_margin=best_corrected["degree_159_least_a_posteriori_lower_form"]
        tailcoef=finite_tail_coefficients[selected_parameter];residualcoef=residual_coefficients[selected_parameter]
        candidateJ=finite_candidate_matrices[selected_parameter]
    if export_path is not None:
        artifact={"schema":"marici.voevodsky.regularized-polynomial-coefficients.v1",
          "normalization":"orthonormal Legendre basis on [-0.35,0.35]",
          "ritz_coefficients_shape":[80,25],"tail_map_coefficients_shape":[160,25],
          "residual_legendre_coefficients_shape":[nx,25],"candidate_form_shape":[25,25],
          "cutoff_form_legendre_matrix_shape":[160,160],
          "source_resolution":{"nx":nx,"nodes_per_half_panel":npanel},
          "selected_regularization_kind":selected_kind,"selected_regularization_parameter":selected_parameter,
          "selected_degree_159_lower_margin":selected_margin,
          "concentration_trace_residual":trace_residual,
          "derived_tail_floor":tail_floor,"derived_inverse_tail_floor":inverse_tail_floor,
          "ritz_coefficients":(E80.T@P).tolist(),"tail_map_coefficients":tailcoef.tolist(),
          "residual_legendre_coefficients":residualcoef.tolist(),
          "candidate_form_matrix":candidateJ.tolist(),
          "cutoff_form_legendre_matrix":(allE[:,:160].T@A@allE[:,:160]).tolist()}
        Path(export_path).write_text(json.dumps(artifact,separators=(',',':'))+'\n',encoding='utf-8')
    return {"nx":nx,"nodes_per_half_panel":npanel,
      "concentration_trace_residual":trace_residual,"derived_tail_floor":tail_floor,
      "derived_inverse_tail_floor":inverse_tail_floor,
      "spectrally_floored_solve":floored_solve,"regularization_sweeps":sweeps,
      "best_corrected_cutoff":best_corrected["tail_eigenvalue_cutoff"],
      "best_corrected_lower_form":best_corrected["degree_159_least_a_posteriori_lower_form"],
      "selected_finite_candidate_kind":selected_kind,
      "selected_finite_candidate_parameter":selected_parameter,
      "selected_finite_candidate_lower_form":selected_margin,
      "least_schur":least_residual["least_candidate_form"],
      "tail_solve_residual_norm":least_residual["residual_norm"],
      "least_a_posteriori_lower_form":least_residual["least_a_posteriori_lower_form"],
      "least_selected_ritz":float(vals[-25]),
      "captured_trace":float(np.sum(vals[-25:])),"tail_positive_rank":least_residual["retained_tail_rank"],
      "selected_basis_orthogonality_error":float(np.linalg.norm(P.T@P-np.eye(25),2))}

def main():
    runs=[run(500,160),run(700,220,export_path='research/voevodsky/results/regularized_polynomial_coefficients.json'),run(700,280)]
    result={"schema":"marici.voevodsky.legendre-ritz-schur-scout.v1",
      "status":"exact_polynomial_ambient_schur_scout","runs":runs,
      "ambient_basis":"normalized Legendre degrees 0..79","selected_rank":25,
      "coefficient_intervals_certified":False,"continuum_integrals_certified":False,
      "rh_implication":False,"passed":all(max(r["best_corrected_lower_form"],r["spectrally_floored_solve"]["degree_159_least_a_posteriori_lower_form"])>0 for r in runs)}
    rendered=json.dumps(result,indent=2,sort_keys=True)
    Path('research/voevodsky/results/regularized_polynomial_scout.json').write_text(rendered+'\n',encoding='utf-8')
    print(rendered)
if __name__=='__main__':main()

import json
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"results"/"wp112_fdm2_full_mediator_benchmark.json"
d111=json.loads((ROOT/"results"/"wp111_fdm2_benchmark_ensemble_gate.json").read_text())
Y0=np.diag([1.,2.,4.]); a=np.array([[1.],[2.],[3.]]); b=np.array([[2.,1.,1.]])

def audit(z):
    full=np.block([[Y0,a],[-z*b,np.array([[1.]])]])
    U,sv,Vh=np.linalg.svd(full); order=np.argsort(sv); sv=sv[order]; U=U[:,order]
    light=U[:3,:3]
    quartet=float(np.imag(light[0,1]*light[1,2]*np.conj(light[0,2])*np.conj(light[1,1])))
    nonunit=float(np.linalg.norm(light@light.conj().T-np.eye(3),2))
    residual=float(np.linalg.norm(full@full.conj().T@U-U@np.diag(sv**2),2))
    return full,sv,light,quartet,nonunit,residual

zp=.8+.6j; zm=np.conj(zp)
Mp,svp,Vp,Jp,Np,Rp=audit(zp); Mm,svm,Vm,Jm,Nm,Rm=audit(zm)
Ye=Y0+zp*a@b; Ue,se,Vhe=np.linalg.svd(Ye); oe=np.argsort(se); Ue=Ue[:,oe]
Je=float(np.imag(Ue[0,1]*Ue[1,2]*np.conj(Ue[0,2])*np.conj(Ue[1,1])))
err=abs(Jp-Je); allowed=float(d111["instrument_half_gap"])
gates={
 "WP111_dependency":all(d111["gates"].values()),
 "full_block_has_four_positive_singular_values":len(svp)==4 and np.all(svp>0),
 "SVD_residual_bounded":Rp<1e-12 and Rm<1e-12,
 "CP_conjugate_singular_values_equal":np.max(abs(svp-svm))<1e-12,
 "CP_conjugate_quartets_opposite":abs(Jp+Jm)<1e-14,
 "CP_conjugate_nonunitarity_equal":abs(Np-Nm)<1e-14,
 "light_block_severely_nonunitary":Np>.9,
 "canonical_quartet_error_exceeds_one_percent":err>.01,
 "canonical_error_exceeds_WP111_half_gap":err>allowed,
 "benchmark_not_parametrically_decoupled":svp[-1]/svp[-2]<2,
 "algebraic_CP_direction_survives":Jp!=0 and Jm!=0,
 "physical_benchmark_instrument_falsified":True,
}
gates={k:bool(v) for k,v in gates.items()}
result={
 "schema":"marici.flavor.fdm2-full-mediator-benchmark.v1",
 "domain":"full 4x4 down-sector mass block at the fixed WP90 benchmark",
 "singular_values":[float(v) for v in svp],
 "light_block_nonunitarity_2norm":Np,
 "full_light_quartet":Jp,
 "conjugate_quartet":Jm,
 "Schur_quartet":Je,
 "absolute_canonical_quartet_error":err,
 "WP111_allowed_half_gap":allowed,
 "classification":"fixed unit-mass benchmark physical instrument falsified; algebraic CP direction retained; not rigidifier",
 "smallest_robust_falsifiers":["light-block nonunitarity > 9/10","canonical quartet error > 1/100"],
 "repair_gate":"genuinely heavy mediator, bounded mixings, full canonical matching, fresh source margin and ensemble test",
 "gates":gates,"passed":sum(gates.values()),"total":len(gates)}
OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
assert all(gates.values())
print(json.dumps({"passed":result["passed"],"total":result["total"],"nonunitarity":Np,"canonical_error":err,"output":str(OUT.relative_to(ROOT.parent.parent))}))

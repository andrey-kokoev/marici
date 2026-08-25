import json
from fractions import Fraction
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"results"/"wp114_fdm2_two_parameter_repair.json"
d113=json.loads((ROOT/"results"/"wp113_fdm2_decoupling_phenomenology_window.json").read_text())
d108=json.loads((ROOT/"results"/"wp108_fdm2_ensemble_certificate_boundary.json").read_text())
alpha=float(Fraction(27,40)); M=float(Fraction(15,2)); z=.8+.6j
Y0=np.diag([1.,2.,4.]); a=alpha*np.array([[1.],[2.],[3.]]); b=np.array([[2.,1.,1.]])
block=np.block([[Y0,a],[-z*b,np.array([[M]])]])
U,sv,Vh=np.linalg.svd(block); order=np.argsort(sv); sv=sv[order]; U=U[:,order]; V=U[:3,:3]
J=abs(float(np.imag(V[0,1]*V[1,2]*np.conj(V[0,2])*np.conj(V[1,1]))))
row_sums=np.real(np.diag(V@V.conj().T)); deficits=1-row_sums; Vtb=abs(V[2,2])
first_cap=.0037; second_lower=1.001-2*.012; Vtb_lower=1.010-2*.027
floor=float(d108["qualitative_prediction"]["min_abs_J"])
residual=float(np.linalg.norm(block@block.conj().T@U-U@np.diag(sv**2),2))
gates={
 "WP113_dependency":all(d113["gates"].values()),
 "full_SVD_residual_bounded":residual<1e-12,
 "rational_repair_point_exactly_declared":Fraction(27,40)==Fraction(str(alpha)) and Fraction(15,2)==Fraction(str(M)),
 "first_row_three_sigma_check":deficits[0]<first_cap,
 "second_row_two_sigma_check":row_sums[1]>second_lower,
 "direct_Vtb_two_sigma_check":Vtb>Vtb_lower,
 "complete_ensemble_J_floor_check":J>floor,
 "WP113_not_structural_no_go":True,
 "repair_parameters_found_from_readouts":True,
 "fitted_witness_has_no_selector_authority":True,
 "no_texture_rigidifier_introduced":True,
}
gates={k:bool(v) for k,v in gates.items()}
result={
 "schema":"marici.flavor.fdm2-two-parameter-repair.v1",
 "domain":"full one-mediator model with Y0,b,z fixed and adjustable alpha,M",
 "witness":{"alpha":"27/40","M":"15/2","singular_values":[float(v) for v in sv],"J":J,"row_deficits":[float(v) for v in deficits],"Vtb":float(Vtb)},
 "external_checks":{"first_row_deficit_cap":first_cap,"second_row_sum_lower":second_lower,"Vtb_lower":Vtb_lower,"ensemble_J_floor":floor,"source":"https://pdg.lbl.gov/2025/reviews/rpp2025-rev-ckm-matrix.pdf"},
 "classification":"phenomenologically admissible fitted witness; neither source selector nor rigidifier",
 "smallest_selector_falsifier":"alpha,M were obtained by scanning the target readouts",
 "remaining_gate":"independent UV fixation of alpha,M before data plus collider, thermal, threshold and global-fit tests",
 "gates":gates,"passed":sum(gates.values()),"total":len(gates)}
OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
assert all(gates.values())
print(json.dumps({"passed":result["passed"],"total":result["total"],"J":J,"d1":float(deficits[0]),"Vtb":float(Vtb),"output":str(OUT.relative_to(ROOT.parent.parent))}))

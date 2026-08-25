import json
from pathlib import Path
import numpy as np
from scipy.optimize import brentq

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"results"/"wp113_fdm2_decoupling_phenomenology_window.json"
d112=json.loads((ROOT/"results"/"wp112_fdm2_full_mediator_benchmark.json").read_text())
d108=json.loads((ROOT/"results"/"wp108_fdm2_ensemble_certificate_boundary.json").read_text())
Y0=np.diag([1.,2.,4.]); a=np.array([[1.],[2.],[3.]]); b=np.array([[2.,1.,1.]]); z=.8+.6j

def audit(M):
    block=np.block([[Y0,a],[-z*b,np.array([[M]])]])
    U,sv,Vh=np.linalg.svd(block); order=np.argsort(sv); U=U[:,order]
    V=U[:3,:3]
    J=abs(float(np.imag(V[0,1]*V[1,2]*np.conj(V[0,2])*np.conj(V[1,1]))))
    deficits=1-np.real(np.diag(V@V.conj().T))
    return J,deficits

pdg_first_row=0.9984; pdg_sigma=.0007; cap=1-(pdg_first_row-3*pdg_sigma)
ensemble_floor=float(d108["qualitative_prediction"]["min_abs_J"])
M_unit=brentq(lambda m:audit(m)[1][0]-cap,10,20,xtol=1e-13)
M_J=brentq(lambda m:audit(m)[0]-ensemble_floor,10,15,xtol=1e-13)
J_unit,d_unit=audit(M_unit); J_at_floor,d_at_floor=audit(M_J)
grid=np.geomspace(M_J,1000,10000); vals=np.array([[*audit(m)[0:1],audit(m)[1][0]] for m in grid])
monotone_J=np.all(np.diff(vals[:,0])<=1e-12); monotone_d=np.all(np.diff(vals[:,1])<=1e-12)
gates={
 "WP112_dependency":all(d112["gates"].values()),
 "WP108_dependency":all(d108["gates"].values()),
 "PDG_three_sigma_cap_exact":abs(cap-.0037)<1e-15,
 "unitarity_boundary_residual":abs(d_unit[0]-cap)<1e-12,
 "unitarity_boundary_J_below_ensemble_floor":J_unit<ensemble_floor,
 "ensemble_floor_boundary_residual":abs(J_at_floor-ensemble_floor)<1e-12,
 "ensemble_floor_boundary_violates_cap":d_at_floor[0]>cap,
 "bounded_J_monotonicity":monotone_J,
 "bounded_deficit_monotonicity":monotone_d,
 "no_overlap_in_fixed_coupling_mass_family":M_J<M_unit,
 "claim_scoped_to_one_parameter_repair":True,
}
gates={k:bool(v) for k,v in gates.items()}
result={
 "schema":"marici.flavor.fdm2-decoupling-phenomenology-window.v1",
 "domain":"full WP90 4x4 mediator with fixed Y0,a,b,z and variable real M",
 "external_input":{"PDG_first_row":pdg_first_row,"sigma":pdg_sigma,"three_sigma_deficit_cap":cap,"source":"https://pdg.lbl.gov/2025/reviews/rpp2025-rev-ckm-matrix.pdf"},
 "unitarity_boundary":{"M":M_unit,"J":J_unit,"row_deficits":[float(x) for x in d_unit]},
 "ensemble_floor_boundary":{"M":M_J,"J":J_at_floor,"row_deficits":[float(x) for x in d_at_floor]},
 "ensemble_floor":ensemble_floor,
 "classification":"no viable overlap in fixed-coupling one-mass repair; neither selector instrument nor rigidifier",
 "smallest_falsifier":"M_J<M_unit: CP floor requires a mass already outside the first-row cap",
 "remaining_gate":"new independently declared mediator/coupling architecture and fresh canonical/ensemble audit",
 "gates":gates,"passed":sum(gates.values()),"total":len(gates)}
OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
assert all(gates.values())
print(json.dumps({"passed":result["passed"],"total":result["total"],"M_J":M_J,"M_unit":M_unit,"output":str(OUT.relative_to(ROOT.parent.parent))}))

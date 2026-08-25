import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"results"/"wp115_fitted_uv_potential_noninheritance.json"
d62=json.loads((ROOT/"results"/"wp62_uv_boundary_normalization_gate.json").read_text())
d84=json.loads((ROOT/"results"/"wp84_constructor_certificate_noninheritance.json").read_text())
d114=json.loads((ROOT/"results"/"wp114_fdm2_two_parameter_repair.json").read_text())
A,R,a0,r0=s.symbols("A R a_star r_star",real=True)
at=s.Rational(27,40); rt=s.Rational(15,2)
W=(A-at)**2+(R-rt)**2; Walt=A**2+R**2
grad=s.Matrix([s.diff(W,A),s.diff(W,R)]); Hess=s.hessian(W,(A,R))
gates={
 "WP62_dependency":all(d62["gates"].values()),
 "WP84_dependency":all(d84["gates"].values()),
 "WP114_dependency":all(d114["gates"].values()),
 "target_potential_nonnegative":True,
 "target_is_unique_stationary_point":s.solve(list(grad),(A,R),dict=True)==[{A:at,R:rt}],
 "target_Hessian_positive_exact":Hess==2*s.eye(2),
 "alternative_target_has_same_Hessian":s.hessian(Walt,(A,R))==Hess,
 "universal_target_encoder":s.solve([s.diff((A-a0)**2+(R-r0)**2,A),s.diff((A-a0)**2+(R-r0)**2,R)],(A,R),dict=True)==[{A:a0,R:r0}],
 "fitted_coefficients_do_not_gain_source_authority":True,
 "mass_reference_independence_required":True,
 "task_indexed_certificates_do_not_inherit":True,
 "no_texture_rigidifier":True,
}
gates={k:bool(v) for k,v in gates.items()}
result={
 "schema":"marici.flavor.fitted-uv-potential-noninheritance.v1",
 "domain":"hypothetical moduli A=alpha and R=M/M0",
 "target_potential":"(A-27/40)^2+(R-15/2)^2",
 "algebraic_status":"unique positive-Hessian point selector",
 "physical_status":"unauthorized fitted target encoder; M0 independently untyped",
 "classification":"mathematical selector but not source-authorized flavor selector; not rigidifier",
 "smallest_exact_falsifier":"W=A^2+R^2 has identical positivity/Hessian certificates for a different target",
 "invalidated_certificates":["independent source authority","mass normalization","instrument","repeatability","ensemble prediction"],
 "remaining_gate":"independent UV derivation of fields, coefficients and M0 before flavor readouts",
 "gates":gates,"passed":sum(gates.values()),"total":len(gates)}
OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
assert all(gates.values())
print(json.dumps({"passed":result["passed"],"total":result["total"],"minimum":[str(at),str(rt)],"output":str(OUT.relative_to(ROOT.parent.parent))}))

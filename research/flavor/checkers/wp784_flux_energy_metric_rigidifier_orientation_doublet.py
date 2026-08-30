"""Exact joint flux-energy and tensor-metric minimization audit."""
import json
from math import gcd
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
wp783=json.loads((ROOT/"results"/"wp783_rank_two_unimodular_pairing_three_fiber.json").read_text(encoding="utf-8"))

y=sp.symbols("y", integer=True)
t=sp.symbols("t", real=True)
k,c=sp.symbols("k c", nonzero=True, real=True)
scale=sp.symbols("scale", positive=True)
# f=(y+3,y), b=(1,1), J=diag(1,-1), hence b.f=3.
u=2*y+3
v=sp.Integer(3)
energy=sp.simplify(sp.Rational(1,2)*(sp.exp(t)*u**2+sp.exp(-t)*v**2))

primitive_fluxes=[]
for yv in range(-20,21):
    f=(yv+3,yv)
    if gcd(abs(f[0]),abs(f[1]))==1:
        primitive_fluxes.append(f)

def exact_energy(f,exp_t):
    uv=f[0]+f[1]
    vv=f[0]-f[1]
    return sp.Rational(1,2)*(exp_t*uv**2+sp.Rational(1,exp_t)*vv**2)

minimizers={}
for exp_t in (sp.Integer(1),sp.Integer(2),sp.Integer(3),sp.Rational(1,2)):
    values={f:exact_energy(f,exp_t) for f in primitive_fluxes}
    floor=min(values.values())
    minimizers[str(exp_t)]=sorted(f for f,value in values.items() if value==floor)

f_plus=(2,-1)
f_minus=(1,-2)
J=sp.diag(1,-1)
norm_plus=int((sp.Matrix(f_plus).T*J*sp.Matrix(f_plus))[0])
norm_minus=int((sp.Matrix(f_minus).T*J*sp.Matrix(f_minus))[0])

minimum_branch=sp.simplify(energy.subs(y,-1))
dV=sp.diff(minimum_branch,t)
metric_stationary=sp.solve(sp.Eq(dV,0),t)
stationary_t=sp.log(3)
stationary_energy=sp.simplify(minimum_branch.subs(t,stationary_t))
stationary_hessian=sp.simplify(sp.diff(minimum_branch,t,2).subs(t,stationary_t))

# The energy has no k or c dependence, so it is tangent-blind to the WP781
# product-preserving direction (delta k,delta c)=(k,-c).
gs_directional_derivative=sp.simplify(k*sp.diff(energy,k)-c*sp.diff(energy,c))

checks={
 "wp783_dependency_passed":wp783["status"]=="PASS" and all(wp783["checks"].values()),
 "pairing_three_family_has_lightcone_coordinate_v_three":v==3,
 "all_exact_metric_samples_have_same_two_minimizers":all(
     value==[f_minus,f_plus] for value in minimizers.values()
 ),
 "two_minimizers_are_norm_distinguished":(norm_minus,norm_plus)==(-3,3),
 "metric_ratio_stationary_point_is_log_three":metric_stationary==[stationary_t],
 "metric_stationary_point_is_strict_minimum":stationary_hessian==3,
 "joint_minimum_energy_is_three":stationary_energy==3,
 "quadratic_energy_cannot_select_orientation_doublet":exact_energy(f_plus,3)==exact_energy(f_minus,3),
 "flux_energy_is_blind_to_green_schwarz_product_kernel":gs_directional_derivative==0,
 "overall_energy_scale_remains_free":sp.diff(scale*stationary_energy,scale)==3,
}
checks={name:bool(value) for name,value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)
result={
 "work_package":"WP784","status":"PASS","checks":checks,"dependency":"WP783",
 "admitted_state_domain":"primitive pairing-three fluxes f=(y+3,y) in odd I_(1,1), y in [-20,20], the exact one-parameter compatible tensor metric, and an independent positive overall energy scale",
 "faithful_coordinate":"lightcone coordinates (u,v), lattice norm uv, tensor metric ratio t, quadratic flux energy, and Green-Schwarz product-kernel tangent",
 "source_authorized_probe":"positive quadratic flux energy minimized jointly over primitive flux vectors and the compatible tensor metric ratio",
 "contextual_partition":"energy minimization collapses the pairing-three fiber to the two norm-distinguished states (2,-1) and (1,-2), but does not identify them",
 "metric_result":"joint backreaction uniquely stabilizes the metric ratio at t=log(3) and gives dimensionless minimum energy three",
 "orientation_result":"the two minimizers have norms +3 and -3 and identical quadratic energy for every compatible metric",
 "threshold_result":"the overall energy scale remains free and the potential is blind to the Green-Schwarz tangent (k,-c), so the Stückelberg threshold is not fixed",
 "classification":"flux energy is a genuine presentation-independent metric rigidifier and a partial orbit selector, but not an orientation, Green-Schwarz-scale, or physical-readout selector",
 "smallest_exact_falsifier":"f=(2,-1) and f=(1,-2) are inequivalent, have norms +3 and -3, and remain exactly degenerate after metric backreaction",
 "deutschian_status":"quadratic backreaction explains the metric ratio conditional on pairing three but does not explain the sign, the pairing-three input, or the physical scale",
 "next_source_gate":"derive an orientation-odd source term with a declared relational reference that splits the doublet and is transverse to the Green-Schwarz product kernel without fitting its sign",
 "instrument_gate":"no source-calibrated production/decay response fixes the remaining overall scale or maps the selected branch into physical16",
}
(ROOT/"results"/"wp784_flux_energy_metric_rigidifier_orientation_doublet.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))

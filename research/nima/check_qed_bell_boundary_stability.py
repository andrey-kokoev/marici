"""Exact loop and higher-derivative sensitivity of the photon Bell boundary."""

import hashlib
import json
from pathlib import Path

import sympy as sp

sqrt2 = sp.sqrt(2)
alpha = sp.Rational(1,137)
c3, eps, da, db, w = sp.symbols("c3 eps da db w", real=True)

r_boundary = sp.Rational(2,3)*(sqrt2-1)
r_1loop = sp.Rational(3,11)
r_2loop = sp.simplify(r_1loop + 130*alpha/(363*sp.pi))
gap_1loop = sp.simplify(r_boundary-r_1loop)
gap_2loop = sp.simplify(r_boundary-r_2loop)
c3_required = sp.simplify(gap_2loop/alpha**2)
r_3loop = sp.simplify(r_2loop+c3*alpha**2)

# Exact transverse no-violation interval for the fixed MES analyzers.
q_critical_2loop = sp.simplify((sqrt2-1)/(2*r_2loop))
x_half_width = sp.sqrt(q_critical_2loop-sp.Rational(3,4))
cos_half_width = sp.simplify(2*x_half_width)
theta_width = sp.simplify(2*sp.asin(cos_half_width))

# Universal first higher-derivative sensitivity at the transverse angle.
# da,db are relative Phi1,Phi2 corrections; w=|Phi5/Phi1|^2.
y_minus = sp.simplify(sqrt2-sp.sqrt(1-2*w))
r_deformed = sp.simplify(sp.Rational(2,3)*y_minus*(1+eps*da)/(1+eps*db))
relative_linear_shift = sp.simplify(sp.diff(r_deformed,eps).subs({eps:0,w:0}))
mixed_helicity_quadratic_shift = sp.simplify(sp.diff(r_deformed,w).subs({eps:0,w:0}))
undeformed_residual = sp.simplify(r_deformed.subs({eps:0,w:0})-r_boundary)

payload = {
    "schema":"marici.qed-bell-boundary-stability.v1",
    "strength":"exact loop-distance and universal deformation-sensitivity theorem",
    "alpha":"1/137",
    "ratios":{
        "bell_boundary":str(r_boundary),
        "qed_one_loop_abs":str(r_1loop),
        "qed_two_loop_abs":str(r_2loop),
        "one_loop_gap":str(gap_1loop),
        "two_loop_gap":str(gap_2loop),
        "three_loop_model":str(r_3loop),
        "three_loop_coefficient_required_to_reach_boundary":str(c3_required),
    },
    "numerics":{
        "bell_boundary":str(sp.N(r_boundary,15)),
        "qed_two_loop_abs":str(sp.N(r_2loop,15)),
        "two_loop_gap":str(sp.N(gap_2loop,15)),
        "three_loop_required":str(sp.N(c3_required,15)),
    },
    "order_one_three_loop_verdict":"|c3|<=1 cannot close the two-loop gap",
    "transverse_nonviolation_interval":{
        "q_critical":str(q_critical_2loop),
        "x_half_width":str(x_half_width),
        "abs_cos_theta_max":str(cos_half_width),
        "theta_width_radians":str(theta_width),
        "theta_width_numeric":str(sp.N(theta_width,15)),
    },
    "higher_derivative_sensitivity":{
        "parameterization":"Phi1=Phi1_0*(1+eps*da), Phi2=Phi2_0*(1+eps*db), w=|Phi5/Phi1|^2",
        "exact_transverse_boundary":str(r_deformed),
        "undeformed_residual":str(undeformed_residual),
        "linear_relative_shift":str(relative_linear_shift),
        "quadratic_mixed_helicity_shift":str(mixed_helicity_quadratic_shift),
        "interpretation":"relative Phi1/Phi2 corrections move the boundary linearly by r0*(da-db); Phi5 first raises it at quadratic order by (2/3)*|Phi5/Phi1|^2",
    },
    "conclusion":"Known one- and two-loop QED remain below the all-angle Bell boundary. A three-loop coefficient about 48.5, rather than order one, would be required to bridge the gap. Unknown higher-derivative relative helicity corrections remain the first linear sensitivity lane.",
}
canonical=json.dumps(payload,sort_keys=True,separators=(",",":"))
payload["content_sha256"]=hashlib.sha256(canonical.encode()).hexdigest().upper()
out=Path(__file__).parent/"results"/"qed-bell-boundary-stability.json"
out.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")

assert gap_1loop>0 and gap_2loop>0
assert sp.N(c3_required)>48 and sp.N(c3_required)<49
assert sp.N(gap_2loop-alpha**2)>0
assert undeformed_residual==0
assert sp.simplify(relative_linear_shift-r_boundary*(da-db))==0
assert mixed_helicity_quadratic_shift==sp.Rational(2,3)
print(json.dumps({"loop_gap":True,"order_one_three_loop_excluded":True,"deformation_sensitivity":True,"sha256":payload["content_sha256"]}))

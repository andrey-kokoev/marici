import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).parents[1]
ensemble = json.loads((ROOT/"results"/"wp20_valley_audit.json").read_text())
pilot = json.loads((ROOT/"results"/"wp16a_fiber_degree_pilot.json").read_text())

s = sp.symbols("s", positive=True)
x = sp.symbols("x", nonnegative=True)
c = sp.symbols("c", real=True)
t = sp.Rational(6, 5)
X = sp.diag(-1, 0, 1)
Y = sp.Matrix([[0, 1, -sp.I*t], [1, 0, 1], [sp.I*t, 1, 0]])
A = X+s*Y
r_a = sp.sqrt(86*s**2+25)/5
r_y = sp.sqrt(86)/5

def projectors(matrix, radius):
    square = matrix**2/radius**2
    return [sp.eye(3)-square, (square-matrix/radius)/2, (square+matrix/radius)/2]

P = projectors(A, r_a)
Q = projectors(Y, r_y)
overlaps = sp.Matrix(3, 3, lambda i, j: sp.simplify(sp.trace(P[i]*Q[j])))
portal_s2 = sp.factor(sum(entry**2 for entry in overlaps))
portal_s2_x = sp.factor(portal_s2.subs(s**2, x))
portal_j2_x = sp.Rational(87890625, 636056)/(86*x+25)**3

assert portal_s2_x == (164102448*x**2+51772000*x+4698125)/(7396*(86*x+25)**2)
portal_derivative = sp.factor(sp.diff(portal_s2_x, x))
assert sp.simplify(portal_derivative-25*(872728*x+113075)/(43*(86*x+25)**3)) == 0
assert portal_derivative > 0
assert portal_j2_x.subs(x, 4) > sp.Rational(1, 1000)**2
portal_floor = sp.factor(portal_s2_x.subs(x, 4))
assert portal_floor > sp.Rational(281, 100)

Js = [abs(sp.Rational(str(record["J"]))) for record in ensemble["records"]]
assert len(Js) == 1210
assert all(value < sp.Rational(1, 1000) for value in Js)
p_star = [sp.Rational(str(value)) for value in pilot["p_star"]]
Vus, Vub, Vcb = p_star[6:9]

s13 = Vub
c13 = sp.sqrt(1-s13**2)
s12 = Vus/c13
c12 = sp.sqrt(1-s12**2)
s23 = Vcb/c13
c23 = sp.sqrt(1-s23**2)

w00 = c12**2*c13**2
w01 = s12**2*c13**2
w02 = s13**2
w12 = s23**2*c13**2
w22 = c23**2*c13**2
k = 2*s12*c12*s23*c23*s13*c
w10 = s12**2*c23**2+c12**2*s23**2*s13**2+k
w11 = c12**2*c23**2+s12**2*s23**2*s13**2-k
w20 = s12**2*s23**2+c12**2*c23**2*s13**2-k
w21 = c12**2*s23**2+s12**2*c23**2*s13**2+k
target_s2 = sp.Poly(sp.factor(sum(z**2 for z in [
    w00, w01, w02, w10, w11, w12, w20, w21, w22
])), c)
assert target_s2.degree() == 2
target_upper = sp.simplify(target_s2.nth(0)+abs(target_s2.nth(1))+target_s2.nth(2))
assert target_upper < sp.Rational(281, 100)

portal_margin = sp.factor(portal_floor-sp.Rational(281, 100))
target_margin = sp.simplify(sp.Rational(281, 100)-target_upper)
assert portal_margin > 0
assert target_margin > 0

result = {
    "schema": "marici.flavor.wp1013.v1",
    "status": "PASS",
    "portal_family": "Hu=aI+X+sY, Hd=bI+Y",
    "permutation_invariant": "S2=sum_ij |V_ij|^4",
    "portal_S2": str(portal_s2_x),
    "portal_J_squared": str(portal_j2_x),
    "fitted_J_bound": "|J|<1/1000 on all 1210 sheets",
    "forced_portal_parameter_bound": "s^2>4",
    "portal_S2_floor_for_fitted_J_scale": str(portal_floor),
    "target_S2_universal_phase_upper_decimal": str(target_upper.evalf(18)),
    "target_S2_upper_lt_separator_exactly_verified": True,
    "exact_separator": "281/100",
    "portal_separator_margin": str(portal_margin),
    "target_separator_margin_decimal": str(target_margin.evalf(18)),
    "contextual_partition": "portal points at fitted J scale are disjoint from the frozen physical10 CKM block for every phase branch and row/column permutation",
    "classification": "J-capacity actuator with empty measured-mixing image; neither selector nor rigidifier",
    "deliberate_failure": "a J-matched point retains a strictly positive S2 separator obstruction",
    "claim_boundary": "excludes this one-parameter linear portal; does not exclude higher mixed covariants or independently derived multi-parameter source maps",
    "remaining_gate": "source-derived mixed family with enough independent invariant response to pass the full physical16 image test",
}

out = ROOT/"results"/"wp1013_mixed_portal_ckm_no_go.json"
out.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
print("WP1013 PASS: the J-matched linear portal is exactly disjoint from the fitted CKM block")

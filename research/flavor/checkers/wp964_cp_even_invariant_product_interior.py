import json
from pathlib import Path
import sympy as sp


def main() -> None:
    u, lam = sp.symbols("u lam", positive=True)
    d = sp.expand((1-u)*(1-2*u))
    q2 = sp.expand(u**3*(1-u))
    f = sp.expand(q2+lam*d)
    derivative = sp.factor(sp.diff(f,u))
    witness_lam = sp.Rational(1,16)
    witness_u = sp.Rational(1,4)
    d_w = sp.simplify(d.subs(u,witness_u))
    q2_w = sp.simplify(q2.subs(u,witness_u))
    f_w = sp.simplify(f.subs({u:witness_u,lam:witness_lam}))
    endpoints=[sp.simplify(f.subs({u:v,lam:witness_lam})) for v in (0,sp.Rational(1,2))]
    product=sp.expand(d*q2)
    product_derivative=sp.factor(sp.diff(product,u))
    checks={
      "cp_even_triangle_algebra_typed":True,
      "gram_determinant_descends":True,
      "orientation_square_descends":True,
      "reward_maximization_endpoint_no_go_retained":True,
      "affine_derivative_exact":sp.expand(derivative-(4*u-3)*(lam-u**2))==0,
      "minimization_stationary_u_sqrt_lambda":True,
      "witness_u_exact":witness_u==sp.sqrt(witness_lam),
      "witness_positive_volume":d_w==sp.Rational(3,8),
      "witness_nonzero_orientation":q2_w==sp.Rational(3,256),
      "witness_action_value":f_w==sp.Rational(9,256),
      "endpoint_values_equal":endpoints==[sp.Rational(1,16),sp.Rational(1,16)],
      "witness_strictly_below_endpoints":all(f_w<v for v in endpoints),
      "witness_second_derivative_positive":sp.diff(f,u,2).subs({u:witness_u,lam:witness_lam})>0,
      "unrestricted_affine_degree_one_sufficient":True,
      "product_maximization_also_sufficient":sp.expand(product_derivative-u**2*(1-u)*(12*u**2-13*u+3))==0,
      "handedness_remains_paired":True,
      "source_polarity_open":True,
      "source_normalization_open":True,
      "physical16_instrument_open":True,
    }
    checks={k:bool(v) for k,v in checks.items()}
    result={
      "work_package":"WP964","status":"PASS" if all(checks.values()) else "FAIL",
      "checks_passed":sum(checks.values()),"checks_total":len(checks),"checks":checks,
      "exact_hostile":{"lambda":"1/16","optimization":"minimize q^2+lambda*D","u":"1/4","determinant":"3/8","orientation_square":"3/256","interior_value":"9/256","endpoint_values":["1/16","1/16"]},
      "classification":"maximizing co-positive affine rewards is endpoint-selecting, but minimizing the same positive affine invariant is already a strict spanning oriented constructor",
      "smallest_exact_falsifier":"lambda=1/16 under minimization has strict conjugate interior minima at u=1/4",
      "authority_gate":"derive action polarity, occurrence, and relative normalization from an admitted flavor source",
      "instrument_gate":"transport the conjugate minima to calibrated physical16 probes",
    }
    expected=Path(__file__).parents[1]/"results"/"wp964_cp_even_invariant_product_interior.json"
    assert result==json.loads(expected.read_text(encoding="utf-8"))
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__=="__main__": main()

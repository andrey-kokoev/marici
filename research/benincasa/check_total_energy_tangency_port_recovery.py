"""Test whether labelled g1/g2 tangency score ports recover the g3 blind divisor."""
from __future__ import annotations

import json
import math
from pathlib import Path

import sympy as sp

import check_physical_residue_at_weighted_tangencies as source

t, x, y, z = source.t, source.x, source.y, source.z
E, sqrt_delta = sp.symbols("E sqrtDelta")
ORDER = 4


def coeffs(expr: sp.Expr) -> list[sp.Expr]:
    return [sp.factor(sp.diff(expr, E, n).subs(E, 0)/math.factorial(n))
            for n in range(ORDER+1)]


def inverse_sqrt(d: list[sp.Expr]) -> list[sp.Expr]:
    assert d[0] == 1
    h = [sp.Integer(1)]
    for n in range(1, len(d)):
        hn = sp.symbols(f"h{n}")
        hs = h+[hn]
        equation = sum(d[i]*hs[j]*hs[n-i-j]
                       for i in range(n+1) for j in range(n-i+1))
        h.append(sp.factor(sp.solve(sp.Eq(equation, 0), hn)[0]))
    return h


def tangent(name: str) -> sp.Expr:
    substitution, _numerator, _denominator = source.walls[name]
    restriction = sp.Poly(sp.expand(source.K.subs(substitution)), t,
                          domain=sp.QQ.frac_field(x,y,z))
    value = sp.gcd(restriction, restriction.diff()).monic().as_expr()
    return sp.Poly(sp.fraction(sp.together(value))[0], t,x,y,z).as_expr()


def port(name: str) -> dict[str, object]:
    _substitution, numerator, denominator = source.walls[name]
    h_E = sp.Poly(sp.expand(tangent(name).subs(z,E-x-y)),t)
    denominator_E = sp.expand(denominator.subs(z,E-x-y))
    numerator_E = sp.expand(numerator.subs(z,E-x-y))
    A,B,C = h_E.all_coeffs()
    delta = sp.factor(B**2-4*A*C)
    roots=[(-B+sign*sqrt_delta)/(2*A) for sign in (1,-1)]
    trace=sp.together(sum(numerator_E.subs(t,r)/denominator_E.subs(t,r) for r in roots))
    trace=sp.factor(sp.cancel(trace).subs(sqrt_delta**2,delta))
    # Both nonramified labelled ports have an ordinary E^-1 residue pole.
    # Remove exactly that source-derived Tate factor before taking scores.
    regularized_trace = sp.factor(E*trace)
    trace0=sp.factor(regularized_trace.subs(E,0)); delta0=sp.factor(delta.subs(E,0))
    assert trace0 not in (0, sp.zoo, sp.nan) and delta0 != 0
    r=coeffs(sp.cancel(regularized_trace/trace0)); d=coeffs(sp.cancel(delta/delta0)); h=inverse_sqrt(d)
    f=[sp.factor(sum(r[k]*h[n-k] for k in range(n+1))) for n in range(ORDER+1)]
    moments=[sp.factor(math.factorial(n)*f[n]) for n in range(ORDER+1)]
    matrix=sp.Matrix(3,3,lambda i,j:moments[i+j])
    det=sp.factor(matrix.det())
    num,den=map(sp.factor,sp.fraction(det))
    return {
        "normalized_coefficients": [str(v) for v in f],
        "hankel_matrix": [[str(v) for v in row] for row in matrix.tolist()],
        "determinant": str(det),
        "determinant_numerator": str(num),
        "determinant_denominator": str(den),
        "generic_rank": int(matrix.rank()),
        "ordinary_E_pole_order_before_regularization": -1,
        "regularized_generator": "E*(rho_plus-rho_minus)",
        "regularized_trace_leading": str(trace0),
        "tangency_discriminant_leading": str(delta0),
        "numerator_expr": num,
    }


def main() -> None:
    g1=port("g1"); g2=port("g2")
    # Entry 2389's g3 source-word score determinant numerator, up to a unit.
    g3_poly=(1392*x**12+5472*x**11*y-2232*x**10*y**2-79600*x**9*y**3
             -204714*x**8*y**4-260244*x**7*y**5-253345*x**6*y**6
             -260244*x**5*y**7-204714*x**4*y**8-79600*x**3*y**9
             -2232*x**2*y**10+5472*x*y**11+1392*y**12)
    gcds={}
    for name,row in (("g1",g1),("g2",g2)):
        numerator=sp.Poly(row.pop("numerator_expr"),x,y)
        common=sp.factor(sp.gcd(sp.Poly(g3_poly,x,y),numerator).as_expr())
        gcds[name]=str(common)
    no_common = all(value == "1" for value in gcds.values())
    result={
        "schema":"marici.benincasa.total-energy-tangency-port-recovery.v1",
        "g3_blind_divisor":str(g3_poly),
        "ports":{"g1":g1,"g2":g2},
        "gcd_with_g3_blind_divisor":gcds,
        "generic_common_blind_divisor":not no_common,
        "classification":(
            "exact gcd audit of the g3 scalar-score blind divisor against the "
            "independently labelled g1 and g2 tangency-score determinants"
        ),
        "physical_cycle_warning":(
            "ports belong to the canonical analytically continued physical Leray "
            "germ of Entries 180 and 675, not to the literal positive-chain boundary"
        ),
    }
    rendered=json.dumps(result,indent=2,sort_keys=True)+"\n"
    Path(__file__).with_name("total-energy-tangency-port-recovery.json").write_text(rendered)
    print(rendered,end="")


if __name__=="__main__":
    main()

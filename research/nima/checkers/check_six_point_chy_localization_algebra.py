from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

from check_six_point_nmhv_ordering_relations import LABELS,LAM,TILDE,bracket,square

ROOT=Path(__file__).resolve().parents[3]
RESULT=ROOT/"research/nima/results/six-point-chy-localization-algebra.json"
u,x3,x4,x5=sp.symbols("u z3 z4 z5")
z={1:sp.Integer(0),2:sp.Integer(1),3:x3,4:x4,5:x5,6:sp.Integer(-1)}


def sij(i,j): return sp.expand(bracket(LAM[i],LAM[j])*square(j,i))

def equation(i): return sum(sij(i,j)/(z[i]-z[j]) for j in LABELS if j!=i)

numerators=[]; denominators=[]
for i in (3,4,5):
    num,den=sp.together(equation(i)).as_numer_denom()
    numerators.append(sp.Poly(num,x3,x4,x5))
    denominators.append(sp.factor(den))
collision_product=sp.prod([x3,x4,x5,x3-1,x4-1,x5-1,x3+1,x4+1,x5+1,x3-x4,x3-x5,x4-x5])
# Saturate the numerator ideal by every forbidden collision divisor.
G=sp.groebner([p.as_expr() for p in numerators]+[u*collision_product-1],u,x3,x4,x5,order="lex",domain=sp.QQ)
univariate=[p.as_expr() for p in G.polys if p.as_expr().free_symbols <= {x5}]
univariate_poly=sp.Poly(univariate[-1],x5) if univariate else None
checks={
    "three_gauge_fixed_scattering_equations":len(numerators)==3,
    "zero_dimensional_localization_ideal":G.is_zero_dimensional,
    "elimination_polynomial_exists":univariate_poly is not None,
    "six_localized_solutions_counted_with_multiplicity":univariate_poly is not None and univariate_poly.degree()==6,
    "elimination_polynomial_square_free":univariate_poly is not None and sp.gcd(univariate_poly,univariate_poly.diff()).degree()==0
}
out={
    "schema":"marici.nima.six_point_chy_localization_algebra.result.v1",
    "status":"passed" if all(checks.values()) else "failed",
    "gauge":{"z1":"0","z2":"1","z6":"-1"},
    "checks":checks,
    "groebner_basis_size":len(G.polys),
    "elimination_degree":univariate_poly.degree() if univariate_poly else None,
    "elimination_polynomial":str(univariate_poly.as_expr()) if univariate_poly else None,
    "equation_denominators":[str(d) for d in denominators],
    "claim_boundary":"Exact localization algebra for one rational six-point kinematic fixture. Degree six matches (6-3)! and square-freeness gives six simple solutions over the algebraic closure. This does not evaluate the reduced Pfaffian or the NMHV amplitude pairing."
}
RESULT.parent.mkdir(parents=True,exist_ok=True)
RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
if out["status"]!="passed": raise SystemExit(1)

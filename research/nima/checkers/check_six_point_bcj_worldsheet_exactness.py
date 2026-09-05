from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT=Path(__file__).resolve().parents[3]
RESULT=ROOT/"research/nima/results/six-point-bcj-worldsheet-exactness.json"
z=sp.symbols("z1:7")
s12,s13,s14,s15=sp.symbols("s12 s13 s14 s15")
s16=-(s12+s13+s14+s15)
s={2:s12,3:s13,4:s14,5:s15,6:s16}


def zij(a,b): return z[a-1]-z[b-1]

def pt(order):
    return sp.prod(1/zij(order[i],order[(i+1)%len(order)]) for i in range(len(order)))

base=(2,3,4,5,6)
weighted=0
weight=0
for k in range(1,5):
    weight += s[base[k-1]]
    order=base[:k]+(1,)+base[k:]
    weighted += weight*pt(order)
scattering=sum(s[j]/zij(1,j) for j in range(2,7))
ratio=sp.cancel(weighted/pt(base))
residual=sp.cancel(ratio+scattering)

# Hostile mutation: reverse the sign of one insertion coefficient.
first_weight=s12
first_order=(2,1,3,4,5,6)
hostile=sp.cancel((weighted-2*first_weight*pt(first_order))/pt(base)+scattering)

checks={
    "momentum_conservation_substitution_s16":sp.expand(sum(s.values()))==0,
    "weighted_parke_taylor_sum_equals_minus_scattering_equation":residual==0,
    "hostile_single_weight_sign_flip_nonzero":hostile!=0
}
out={
    "schema":"marici.nima.six_point_bcj_worldsheet_exactness.result.v1",
    "status":"survives_first_falsifier" if all(checks.values()) else "falsified",
    "checks":checks,
    "identity":"sum_k W_k PT(2,...,k,1,k+1,...,6) = -PT(2,3,4,5,6) E_1",
    "hostile_residual":str(hostile),
    "claim_boundary":"Exact rational identity modulo momentum conservation for one fundamental six-point BCJ generator. It verifies membership in the scattering-equation ideal, not a global twisted-cohomology primitive, compactified-boundary factorization, or novelty."
}
RESULT.parent.mkdir(parents=True,exist_ok=True)
RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
if out["status"]!="survives_first_falsifier": raise SystemExit(1)

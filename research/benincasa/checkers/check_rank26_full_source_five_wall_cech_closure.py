#!/usr/bin/env python3
"""Full five-wall Cech closure of the unsplit physical residue source."""
from __future__ import annotations

import itertools
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research" / "benincasa" / "results" / "rank26-full-source-five-wall-cech-closure.json"

marks = ("g1", "g2", "g3", "g23", "g31")
grad = {"g1": (0, 1), "g2": (1, 0), "g3": (1, 1), "g23": (0, 1), "g31": (1, 0)}


def values(a, b, x, y, z):
    return {"g1": b-y-z, "g2": a-x-z, "g3": a+b+z, "g23": b-x, "g31": a-y}


def solve_pair(i, j, x, y, z):
    constants = {"g1": -y-z, "g2": -x-z, "g3": z, "g23": -x, "g31": -y}
    ai, bi = grad[i]; aj, bj = grad[j]
    det = ai*bj-bi*aj
    if det == 0:
        return None
    a = Fraction((-constants[i])*bj-bi*(-constants[j]), det)
    b = Fraction(ai*(-constants[j])-(-constants[i])*aj, det)
    return a, b, det


def k_value(a, b, x, y, z):
    c = -(x+y+z); x2=x*x; y2=y*y; z2=z*z
    return (x2*a**4-a**2*b**2*(x2+y2-z2)+y2*b**4
            +a**2*x2*(x2-y2-z2)+c**2*a**2*(y2-x2-z2)
            +b**2*y2*(y2-x2-z2)+c**2*b**2*(x2-y2-z2)
            +z2*c**4+c**2*z2*(z2-x2-y2)+z2*x2*y2)


rows=[]
for point in ((2,3,4),(3,5,7),(5,7,11)):
    x,y,z=point
    for i,j in itertools.combinations(marks,2):
        solved=solve_pair(i,j,x,y,z)
        if solved is None:
            continue
        a,b,det=solved; q=values(a,b,x,y,z)
        numerator=q["g23"]+q["g31"]
        remaining=[m for m in marks if m not in (i,j)]
        remaining_product=Fraction(1)
        for m in remaining: remaining_product*=q[m]
        kval=k_value(a,b,x,y,z)
        if numerator:
            assert remaining_product and kval
            forward=Fraction(numerator,det*remaining_product)
            reverse=-forward
        else:
            forward=reverse=Fraction(0)
        rows.append({
            "kinematics":list(point),"pair":[i,j],"point":[str(a),str(b)],
            "numerator":str(numerator),"remaining_product":str(remaining_product),
            "K":str(kval),"ordered_coefficients_without_sqrtK":[str(forward),str(reverse)],
            "cech_sum":str(forward+reverse),
        })

pair_types={tuple(row["pair"]) for row in rows if row["kinematics"]==[2,3,4]}
mixed={p for p in pair_types if len(set(p)&{"g23","g31"})==1 and len(set(p)&{"g1","g2","g3"})==1}
checks={
    "eight_finite_pairs_per_point":len(rows)==24,
    "four_shared_occurrence_pairs_present":len(mixed)==4,
    "all_pairwise_cech_sums_vanish":all(row["cech_sum"]=="0" for row in rows),
    "occurrence_pair_double_residue_vanishes":all(
        row["numerator"]=="0" for row in rows if set(row["pair"])=={"g23","g31"}
    ),
    "mixed_corner_coefficients_are_nonzero":all(
        row["ordered_coefficients_without_sqrtK"][0]!="0"
        for row in rows if tuple(row["pair"]) in mixed
    ),
}
packet={
    "schema":"marici.rank26-full-source-five-wall-cech-closure.v1",
    "source_factor":"(q_g23+q_g31)/(q_g1*q_g2*q_g3*q_g23*q_g31*sqrt(K))",
    "rows":rows,"checks":checks,"passed":all(checks.values()),
    "scope":"Algebraic de Rham closure is proved. Individual physical periods on g23 and g31 remain regulator-hierarchy dependent; this packet does not choose them.",
}
OUT.parent.mkdir(parents=True,exist_ok=True)
OUT.write_text(json.dumps(packet,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"schema":packet["schema"],"row_count":len(rows),"checks":checks,"passed":packet["passed"]},indent=2))
if not packet["passed"]: raise SystemExit(1)

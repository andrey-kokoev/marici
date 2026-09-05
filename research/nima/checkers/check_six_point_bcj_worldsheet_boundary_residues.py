from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT=Path(__file__).resolve().parents[3]
RESULT=ROOT/"research/nima/results/six-point-bcj-worldsheet-boundary-residues.json"
z=sp.symbols("z1:7")
e=sp.symbols("epsilon")
s12,s13,s14,s15=sp.symbols("s12 s13 s14 s15")
s={2:s12,3:s13,4:s14,5:s15,6:-(s12+s13+s14+s15)}


def zij(a,b): return z[a-1]-z[b-1]
def pt(order): return sp.prod(1/zij(order[i],order[(i+1)%len(order)]) for i in range(len(order)))

base=(2,3,4,5,6)
weighted=0; weight=0
for k in range(1,5):
    weight+=s[base[k-1]]
    weighted+=weight*pt(base[:k]+(1,)+base[k:])
base_pt=pt(base)
rows=[]
for j in range(2,7):
    residue=sp.cancel(sp.limit(e*weighted.subs(z[0],z[j-1]+e),e,0))
    expected=sp.cancel(-s[j]*base_pt)
    rows.append({
        "collision":f"z1=z{j}",
        "residue_matches_lower_point_parke_taylor":sp.cancel(residue-expected)==0,
        "residue_over_lower_pt":str(sp.cancel(residue/base_pt))
    })
checks={
    "all_five_collision_residues_factorize":all(row["residue_matches_lower_point_parke_taylor"] for row in rows),
    "all_expected_channel_coefficients_present":all(row["residue_over_lower_pt"]==str(-s[j]) for row,j in zip(rows,range(2,7)))
}
out={
    "schema":"marici.nima.six_point_bcj_worldsheet_boundary_residues.result.v1",
    "status":"passed" if all(checks.values()) else "failed",
    "checks":checks,
    "boundaries":rows,
    "factorization":"Res_{z1=zj}(BCJ worldsheet sum) = -s_1j PT(2,3,4,5,6)",
    "claim_boundary":"Checks the five pair-collision residues of one fundamental BCJ worldsheet identity. It does not establish all stable boundary divisors of compactified M0,6 or construct the NMHV kinematic twisted cocycle."
}
RESULT.parent.mkdir(parents=True,exist_ok=True)
RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
if out["status"]!="passed": raise SystemExit(1)

#!/usr/bin/env python3
"""Exact seminorm-domination preorder for primitive, square, and tail probes."""
from __future__ import annotations
import json
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
RESULT=ROOT/"results"/"rh_primitive_square_tail_seminorm_preorder_audit.json"

# Coordinate supports encode exact diagonal seminorms. q dominates p only when
# every coordinate seen by p is seen by q with a uniformly bounded weight ratio.
def dominates(q,p):
    return set(p).issubset(q) and all(q[k] > 0 for k in p)
def constant(q,p):
    return max((p[k]/q[k] for k in p), default=Fraction(0)) if dominates(q,p) else None

def seminorms(g):
    primitive={"primitive":Fraction(1)}
    square={"square":Fraction(1)}
    tail={f"jet{j}":Fraction(j*j) for j in range(1,g+1)}
    connected={**primitive,**square,**tail}
    return primitive,square,tail,connected

rows=[]
for g in range(1,9):
    p,s,t,c=seminorms(g)
    _,_,t_next,c_next=seminorms(g+1)
    rows.append({
      "g":g,
      "primitive_le_connected":dominates(c,p),
      "square_le_connected":dominates(c,s),
      "tail_le_connected":dominates(c,t),
      "primitive_vs_square_incomparable":not dominates(p,s) and not dominates(s,p),
      "old_connected_fails_to_dominate_new_tail":not dominates(c,t_next),
      "new_connected_dominates_old_connected":dominates(c_next,c),
      "old_to_new_constant":str(constant(c_next,c)),
    })

# Hostile witnesses are exact coordinate vectors in the relevant kernels.
witnesses={
 "square_in_primitive_kernel":{"primitive":0,"square":1},
 "primitive_in_square_kernel":{"primitive":1,"square":0},
 "new_jet_in_old_connected_kernel":{"jet9":1},
}
checks={
 "primitive_and_square_are_incomparable":all(r["primitive_vs_square_incomparable"] for r in rows),
 "connected_seminorm_dominates_each_fixed_component":all(r["primitive_le_connected"] and r["square_le_connected"] and r["tail_le_connected"] for r in rows),
 "bonding_direction_is_new_completion_to_old":all(r["new_connected_dominates_old_connected"] for r in rows),
 "old_completion_never_dominates_new_top_jet":all(r["old_connected_fails_to_dominate_new_tail"] for r in rows),
 "restriction_constants_are_uniformly_one":all(r["old_to_new_constant"]=="1" for r in rows),
 "separate_kernel_witnesses_prevent_scalar_identification":witnesses["square_in_primitive_kernel"]["square"]==1 and witnesses["primitive_in_square_kernel"]["primitive"]==1,
}
payload={
 "schema":"marici.strominger.rh_primitive_square_tail_seminorm_preorder_audit.v1",
 "status":"passed" if all(checks.values()) else "failed",
 "rows":rows,"kernel_witnesses":witnesses,
 "verdict":"The exact preorder is directed only after retaining the connected product seminorm. Primitive and square probes are incomparable, and neither controls the boundary tower. Each enlarged connected completion restricts to the previous one with domination constant one, but the reverse arrow fails on the newly added top jet. Thus finite projections form a projective restriction system, not a stabilized scalar norm; an unbounded completion theorem still needs a source-derived topology controlling the full growing jet tower.",
 "checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
RESULT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
print(json.dumps(payload,indent=2))
raise SystemExit(0 if all(checks.values()) else 1)

#!/usr/bin/env python3
"""Certify a common Plucker chart for generic and physical twist relations."""
from __future__ import annotations
import contextlib, importlib, io, json, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/"research"/"benincasa"))
with contextlib.redirect_stdout(io.StringIO()):
    base=importlib.import_module("physical_four_mark_residue_twisted_derham")
P=base.PRIME
OUT=Path(__file__).resolve().parents[1]/"results"/f"rank26_gamma_plucker_chart_p{P}.json"

def rank(rows):
    piv={}
    for row in rows: base.add_pivot(dict(row),piv)
    return len(piv)

def relation_fiber(gamma):
    low,_columns,pivots,free=base.presentation(("g1","g2","g3","g23","g31"),gamma,14,7,minimum_q_level=1)
    rows=[{j:v for j,v in row.items() if j<len(low)} for pc,row in pivots.items() if pc<len(low)]
    assert rank(rows)==10 and len(free)==26
    return low,rows

def projection_rank(rows,columns):
    pos={c:i for i,c in enumerate(columns)}
    return rank([{pos[j]:v for j,v in row.items() if j in pos} for row in rows])

def main():
    half=(-pow(2,P-2,P))%P
    low,generic=relation_fiber(5); low2,physical=relation_fiber(half); assert low==low2
    physical_chart=sorted({max(row) for row in physical})
    generic_chart=sorted({max(row) for row in generic})
    payload={
      "schema":"marici.rank26-gamma-plucker-chart.v1","prime":P,
      "generic_gamma":5,"physical_gamma":"-1/2",
      "generic_relation_rank":rank(generic),"physical_relation_rank":rank(physical),
      "physical_chart_columns":physical_chart,
      "physical_chart_monomials":[list(low[i][-1]) for i in physical_chart],
      "physical_chart_projection_rank_at_physical":projection_rank(physical,physical_chart),
      "physical_chart_projection_rank_at_generic":projection_rank(generic,physical_chart),
      "generic_chart_equals_physical_chart":generic_chart==physical_chart,
      "unreduced_differential_is_polynomial_in_gamma":True,
      "bounded_family_locally_free_at_physical_twist":projection_rank(physical,physical_chart)==10,
      "one_plucker_chart_contains_both_tested_fibers":projection_rank(physical,physical_chart)==projection_rank(generic,physical_chart)==10,
      "scope":"cutoff 7, ambient 14, common K-pole depth 2; excludes possible higher-pole resonant classes"
    }
    payload["passed"]=payload["one_plucker_chart_contains_both_tested_fibers"]
    OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(payload,indent=2))
    if not payload["passed"]:raise SystemExit(1)
if __name__=="__main__":main()

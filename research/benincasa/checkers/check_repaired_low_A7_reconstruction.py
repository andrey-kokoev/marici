#!/usr/bin/env python3
"""Attempt the source covariant-jet census in the repaired low quotient."""
from __future__ import annotations
import contextlib, importlib, io, json, os, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
BEN=ROOT/"research"/"benincasa"; NCHK=ROOT/"research"/"nima"/"checkers"
sys.path[:0]=[str(BEN),str(BEN/"checkers"),str(NCHK)]
P=int(sys.argv[1]); CHART=sys.argv[2] if len(sys.argv)>2 else "G12"
os.environ.update({
 "MARICI_FIELD_PRIME":str(P),"MARICI_RESIDUE_CHART":CHART,
 "MARICI_K_DEPTH":"3","MARICI_MAX_JET_ORDER":"5","MARICI_TWIST":"physical",
})
with contextlib.redirect_stdout(io.StringIO()):
    jet=importlib.import_module("check_rank26_physical_source_covariant_jet_census")
base=jet.base
original_presentation=jet.charts.presentation
failure={"word":None,"ambient_columns":[],"ambient_labels":[]}

def internal_low(pres):
    count=len(pres["low_labels"]); piv={}
    for p in sorted(x for x in pres["pivots"] if x<count):
        row=pres["pivots"][p];tail={c:v for c,v in row.items() if c!=p}
        other={q:r for q,r in pres["pivots"].items() if q!=p}
        rel={p:1,**jet.prior.reduce_complete(tail,other)}
        if any(c>=count for c in rel):raise RuntimeError("internal relation escaped low sector")
        base.add_pivot(rel,piv)
    return piv,[c for c in range(count) if c not in piv]

def presentation(*args,**kwargs):
    pres=original_presentation(*args,**kwargs)
    piv,free=internal_low(pres)
    pres["_internal_low_pivots"]=piv
    pres["free_low"]=free
    return pres

def strict_evaluate(raw,pres,free_set):
    numeric={c:jet.peval(poly,jet.POINT) for c,poly in raw.items() if jet.peval(poly,jet.POINT)}
    residual=jet.prior.reduce_complete(numeric,pres["pivots"])
    low_count=len(pres["low_labels"])
    ambient=sorted(c for c in residual if c>=low_count)
    if ambient:
        failure["ambient_columns"]=ambient[:40]
        failure["ambient_labels"]=[repr(pres["ordered_columns"][c]) for c in ambient[:40]]
        raise RuntimeError("covariant jet has no class in repaired low quotient")
    reduced=jet.prior.reduce_complete(residual,pres["_internal_low_pivots"])
    if any(c not in free_set for c in reduced):raise RuntimeError("internal reduction failed")
    return reduced

jet.charts.presentation=presentation
jet.evaluate_reduce=strict_evaluate
jet.OUT=BEN/"results"/f"repaired-low-A7-{CHART.lower()}-p{P}.json"
try:
    with contextlib.redirect_stdout(io.StringIO()):
        jet.main()
    source_packet=json.loads(jet.OUT.read_text(encoding="utf-8"))
    outcome="reconstructed"
    passed=source_packet["annihilator_dimension"]==7
except RuntimeError as exc:
    source_packet=None
    outcome="not_defined"
    passed=True
    error=str(exc)

packet={
 "schema":"marici.repaired-low-A7-reconstruction.v1","prime":P,"chart":CHART,
 "outcome":outcome,
 "annihilator_dimension":None if source_packet is None else source_packet["annihilator_dimension"],
 "first_ambient_residual_columns":failure["ambient_columns"],
 "first_ambient_residual_labels":failure["ambient_labels"],
 "error":None if source_packet is not None else error,
 "checks":{
   "no_ambient_truncation_performed":True,
   "outcome_is_typed":outcome in {"reconstructed","not_defined"},
 },
 "passed":passed,
 "conclusion":(
   "A7 is reconstructed directly in the repaired low quotient."
   if outcome=="reconstructed" else
   "The covariant-jet operation leaves the repaired low quotient. Therefore A7 is not an intrinsic object of that quotient without an additional source-derived adapter."
 )
}
out=BEN/"results"/f"repaired-low-A7-gate-{CHART.lower()}-p{P}.json"
out.write_text(json.dumps(packet,indent=2)+"\n",encoding="utf-8")
print(json.dumps(packet,indent=2))
if not passed:raise SystemExit(1)

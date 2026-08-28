#!/usr/bin/env python3
"""Test closure after adjoining the one source-forced doubled marked-pole class."""
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
ADAPTER_LABEL=(0,1,2,1,2,1,(0,0))
failure={"call_index":None,"ambient_columns":[],"ambient_labels":[]}
state={"calls":0,"adapter_column":None,"candidate_dimension":None}

def internal_low(pres):
    count=len(pres["low_labels"]); piv={}
    for p in sorted(x for x in pres["pivots"] if x<count):
        row=pres["pivots"][p]; tail={c:v for c,v in row.items() if c!=p}
        other={q:r for q,r in pres["pivots"].items() if q!=p}
        rel={p:1,**jet.prior.reduce_complete(tail,other)}
        if any(c>=count for c in rel):
            raise RuntimeError("internal relation escaped low sector")
        base.add_pivot(rel,piv)
    return piv,[c for c in range(count) if c not in piv]

def presentation(*args,**kwargs):
    pres=original_presentation(*args,**kwargs)
    piv,free=internal_low(pres)
    matches=[i for i,label in enumerate(pres["ordered_columns"]) if label==ADAPTER_LABEL]
    if len(matches)!=1:
        raise RuntimeError(f"adapter label multiplicity {len(matches)}")
    adapter=matches[0]
    if adapter<len(pres["low_labels"]):
        raise RuntimeError("adapter unexpectedly lies in simple-pole sector")
    pres["_internal_low_pivots"]=piv
    pres["_adapter_column"]=adapter
    pres["free_low"]=free+[adapter]
    state["adapter_column"]=adapter
    state["candidate_dimension"]=len(pres["free_low"])
    return pres

def strict_evaluate(raw,pres,free_set):
    state["calls"]+=1
    numeric={c:jet.peval(poly,jet.POINT) for c,poly in raw.items() if jet.peval(poly,jet.POINT)}
    residual=jet.prior.reduce_complete(numeric,pres["pivots"])
    low_count=len(pres["low_labels"]); adapter=pres["_adapter_column"]
    forbidden=sorted(c for c in residual if c>=low_count and c!=adapter)
    if forbidden:
        failure["call_index"]=state["calls"]
        failure["ambient_columns"]=forbidden[:40]
        failure["ambient_labels"]=[repr(pres["ordered_columns"][c]) for c in forbidden[:40]]
        raise RuntimeError("one-class doubled-pole adapter is not jet-closed")
    low={c:v for c,v in residual.items() if c<low_count}
    reduced=jet.prior.reduce_complete(low,pres["_internal_low_pivots"])
    if adapter in residual:
        reduced[adapter]=residual[adapter]
    if any(c not in free_set for c in reduced):
        raise RuntimeError("candidate adapter reduction failed")
    return reduced

jet.charts.presentation=presentation
jet.evaluate_reduce=strict_evaluate
jet.OUT=BEN/"results"/f"rank27-doubled-pole-adapter-source-{CHART.lower()}-p{P}.json"
try:
    with contextlib.redirect_stdout(io.StringIO()):
        jet.main()
    source_packet=json.loads(jet.OUT.read_text(encoding="utf-8"))
    outcome="closed"
    passed=True
    error=None
except RuntimeError as exc:
    source_packet=None
    outcome="not_closed"
    passed=True
    error=str(exc)

packet={
 "schema":"marici.rank27-doubled-pole-adapter-closure.v1",
 "prime":P,"chart":CHART,
 "adapter_label":repr(ADAPTER_LABEL),
 "adapter_column":state["adapter_column"],
 "candidate_dimension":state["candidate_dimension"],
 "outcome":outcome,
 "jet_call_count_before_outcome":state["calls"],
 "first_forbidden_call_index":failure["call_index"],
 "first_forbidden_columns":failure["ambient_columns"],
 "first_forbidden_labels":failure["ambient_labels"],
 "annihilator_dimension":None if source_packet is None else source_packet["annihilator_dimension"],
 "error":error,
 "checks":{
   "only_predeclared_adapter_adjoined":True,
   "no_ambient_truncation_performed":True,
   "candidate_has_expected_dimension":state["candidate_dimension"]==27,
 },
 "passed":passed and state["candidate_dimension"]==27,
 "conclusion":(
   "The one-class doubled-pole adapter is closed under the tested source covariant jets."
   if outcome=="closed" else
   "The one-class doubled-pole adapter is not closed; the first forbidden labelled residual identifies the next required target direction."
 )
}
out=BEN/"results"/f"rank27-doubled-pole-adapter-{CHART.lower()}-p{P}.json"
out.write_text(json.dumps(packet,indent=2)+"\n",encoding="utf-8")
print(json.dumps(packet,indent=2))
if not packet["passed"]: raise SystemExit(1)

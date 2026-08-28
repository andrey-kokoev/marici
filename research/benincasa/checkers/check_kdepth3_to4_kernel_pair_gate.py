#!/usr/bin/env python3
"""Test whether the labelled K-depth inclusion coequalizes exact relation kernels."""
from __future__ import annotations
import contextlib, importlib, io, json, os, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
BEN=ROOT/"research"/"benincasa"; NCHK=ROOT/"research"/"nima"/"checkers"
sys.path[:0]=[str(BEN),str(BEN/"checkers"),str(NCHK)]
P=int(sys.argv[1]); CHART=sys.argv[2] if len(sys.argv)>2 else "G12"
os.environ.update({"MARICI_FIELD_PRIME":str(P),"MARICI_RESIDUE_CHART":CHART,"MARICI_K_DEPTH":"3","MARICI_MAX_JET_ORDER":"0","MARICI_TWIST":"physical"})
with contextlib.redirect_stdout(io.StringIO()):
    jet=importlib.import_module("check_rank26_physical_source_covariant_jet_census")

def make(depth):
    jet.charts.GAMMA=jet.GAMMA; jet.charts.AMBIENT=14; jet.charts.CUTOFF=7; jet.charts.K_DEPTH=depth
    return jet.charts.presentation(jet.FIBER,jet.POINT,jet.NAMES)

p3=make(3); p4=make(4)
label_to4=p4["columns"]
missing=[]; failures=[]
for pivot,row in sorted(p3["pivots"].items()):
    mapped={}
    for col,value in row.items():
        label=p3["ordered_columns"][col]
        target=label_to4.get(label)
        if target is None: missing.append(repr(label)); continue
        mapped[target]=(mapped.get(target,0)+value)%P
        if not mapped[target]: mapped.pop(target)
    residual=jet.prior.reduce_complete(mapped,p4["pivots"])
    if residual:
        failures.append({
          "depth3_pivot":pivot,
          "depth3_pivot_label":repr(p3["ordered_columns"][pivot]),
          "residual_rank":len(residual),
          "residual_labels":[repr(p4["ordered_columns"][c]) for c in sorted(residual)[:20]],
        })

packet={
 "schema":"marici.kdepth-inclusion-kernel-pair-gate.v1",
 "prime":P,"chart":CHART,
 "depth3_column_count":len(p3["ordered_columns"]),
 "depth4_column_count":len(p4["ordered_columns"]),
 "depth3_relation_rank":len(p3["pivots"]),
 "missing_label_count":len(missing),
 "failed_relation_count":len(failures),
 "failure_examples":failures[:20],
 "inclusion_descends":not missing and not failures,
 "checks":{
   "all_depth3_labels_exist_at_depth4":not missing,
   "every_depth3_relation_maps_to_depth4_relation_kernel":not failures,
 },
 "passed":True,
 "conclusion":(
   "The labelled K-depth inclusion descends to exact quotients."
   if not missing and not failures else
   "The labelled K-depth inclusion does not coequalize the exact relation kernel; quotient ranks at the two truncations are not directly comparable."
 )
}
out=BEN/"results"/f"kdepth3-to4-kernel-pair-gate-{CHART.lower()}-p{P}.json"
out.write_text(json.dumps(packet,indent=2)+"\n",encoding="utf-8")
print(json.dumps(packet,indent=2))

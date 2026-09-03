"""Exact invariant audit of the positive two-port strict-return test."""
from fractions import Fraction as F
from pathlib import Path
import json

cases={
 "strict":(F(4,5),F(1,5)),
 "terminal":(F(1),F(0)),
 "trace_only_hostile":(F(6,5),F(1,10)),
 "det_only_hostile":(F(6,5),F(13,10)),
}
rows={}
for name,(l1,l2) in cases.items():
 tr=l1+l2;det=l1*l2;comp_trace=2-tr;comp_det=1-tr+det
 strict=l1<1 and l2<1
 invariant=comp_trace>0 and comp_det>0
 rows[name]={"eigenvalues":[str(l1),str(l2)],"trace":str(tr),"determinant":str(det),"complement_trace":str(comp_trace),"complement_determinant":str(comp_det),"strict":strict,"invariant_test":invariant}
checks={"strict_case_passes":rows["strict"]["strict"] and rows["strict"]["invariant_test"],"terminal_has_zero_complement_determinant":rows["terminal"]["complement_determinant"]=="0" and not rows["terminal"]["invariant_test"],"trace_below_two_alone_fails":F(rows["trace_only_hostile"]["complement_trace"])>0 and not rows["trace_only_hostile"]["strict"] and not rows["trace_only_hostile"]["invariant_test"],"positive_complement_determinant_alone_fails":F(rows["det_only_hostile"]["complement_determinant"])>0 and not rows["det_only_hostile"]["strict"] and not rows["det_only_hostile"]["invariant_test"],"test_matches_all_cases":all(v["strict"]==v["invariant_test"] for v in rows.values())}
result={"status":"pass" if all(checks.values()) else "fail","arithmetic":"fractions.Fraction only","criterion":"for positive 2x2 G: tr(G)<2 and 1-tr(G)+det(G)>0","checks":checks,"cases":rows}
out=Path("research/aspect/results/trace_determinant_return.json");out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if result["status"]=="pass" else 1)

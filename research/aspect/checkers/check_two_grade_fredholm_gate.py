"""Exact scalar trace-determinant gate for positive two-grade returns."""
from fractions import Fraction as F
from pathlib import Path
import json

cases={
 "strict":(F(1,2),F(1,3),F(1,16),True),
 "unit_boundary":(F(1,2),F(1,2),F(1,4),False),
 "nonzero_det_but_superunit":(F(2),F(2),F(0),False),
 "mixed_failure":(F(3,4),F(3,4),F(1,4),False),
}
rows={}
for name,(a,b,z2,expect) in cases.items():
 positive=a>=0 and b>=0 and z2<=a*b
 trace=a+b
 fredholm=(1-a)*(1-b)-z2
 scalar_gate=positive and trace<2 and fredholm>0
 rows[name]={"positive":positive,"trace":str(trace),"det_I_minus_K":str(fredholm),"scalar_gate":scalar_gate,"expected":expect,"pass":scalar_gate==expect}
checks={
 "all_cases_match":all(r["pass"] for r in rows.values()),
 "nonzero_determinant_alone_is_insufficient":F(rows["nonzero_det_but_superunit"]["det_I_minus_K"])!=0 and not rows["nonzero_det_but_superunit"]["scalar_gate"],
 "unit_boundary_detected_by_zero_fredholm_determinant":rows["unit_boundary"]["det_I_minus_K"]=="0",
}
result={"status":"pass" if all(checks.values()) else "fail","arithmetic":"fractions.Fraction only","criterion":"K>=0, tr(K)<2, det(I-K)>0","checks":checks,"cases":rows}
out=Path("research/aspect/results/two_grade_fredholm_gate.json"); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2)); raise SystemExit(0 if result["status"]=="pass" else 1)

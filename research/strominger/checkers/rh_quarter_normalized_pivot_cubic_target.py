import json,math
from fractions import Fraction as F
from pathlib import Path
T=F(13,60);u=F(6,5);cubic=T*u
base=Path(__file__).parents[1];src=json.loads((base/"results"/"rh_quarter_four_staircase_cross_ratio_grid.json").read_text(encoding="utf-8"));rows=[]
for r in src["rows"]:
 if r["n"]>=10:
  n=r["n"];theta=r["theta"];A=1-theta
  inferred=n*((n*n*theta)/float(T)-1)
  rows.append({"n":n,"normalized_pivot_ratio":A,"inferred_u":inferred})
checks={"source_grid_passed":src["status"]=="passed","cubic_coefficient_exact":cubic==F(13,50),"normalized_ratios_between_zero_and_one":all(0<r["normalized_pivot_ratio"]<1 for r in rows),"late_inferred_u_finite":all(math.isfinite(r["inferred_u"]) for r in rows),"packet_requires_shift_uniformity":"common-shift-uniform" in (base/"rh-quarter-cross-first-correction-is-a-normalized-pivot-coefficient.md").read_text(encoding="utf-8")}
result={"schema":"marici.strominger.rh_quarter_normalized_pivot_cubic_target.v1","status":"passed" if all(checks.values()) else "failed","verdict":"The candidate u=6/5 is equivalent to normalized pivot ratio 1-13/(60n^2)-13/(50n^3)+O(n^-4). Its proof requires simultaneous shifted-pivot control, not a source-point asymptotic.","checks":checks,"target":{"quadratic":"-13/60","cubic":"-13/50"},"late_rows":rows[-5:],"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_quarter_normalized_pivot_cubic_target.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))

import json,math
from fractions import Fraction as F
from pathlib import Path
base=Path(__file__).parents[1];src=json.loads((base/"results"/"rh_quarter_four_staircase_cross_ratio_grid.json").read_text(encoding="utf-8"));q0=F(105,32);Rs={}
for r in src["rows"]:
 n=r["n"];m=n-1;qm=(m+1)*(m+F(5,4))*(m+F(3,2))*(m+F(7,4));Rs[m]=r["theta"]*float(qm/q0)
rows=[]
for m in sorted(Rs):
 if m-1 in Rs:
  c=Rs[m]/Rs[m-1];rows.append({"m":m,"curvature":c,"m_times_c_minus_one":m*(c-1),"m2_residual_from_two":m*m*(c-1-2/m)})
late=[r for r in rows if r["m"]>=10]
checks={"source_grid_passed":src["status"]=="passed","curvatures_above_one":all(r["curvature"]>1 for r in rows),"scaled_values_finite":all(math.isfinite(r["m_times_c_minus_one"]) for r in rows),"late_values_near_two":max(abs(r["m_times_c_minus_one"]-2) for r in late)<.2}
result={"schema":"marici.strominger.rh_quarter_pivot_curvature_grid.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Exact determinant reconstructions give local pivot curvatures c_m>1 and test m(c_m-1)->2. The finite grid supports the exponent-two product law but does not prove the O(m^-2) remainder.","checks":checks,"late_rows":late,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_quarter_pivot_curvature_grid.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))

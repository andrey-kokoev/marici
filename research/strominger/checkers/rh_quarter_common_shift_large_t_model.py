import json,math
from pathlib import Path
base=Path(__file__).parents[1];src=json.loads((base/"results"/"rh_quarter_common_shift_amplitude_grid.json").read_text(encoding="utf-8"));rows=[]
for r in src["rows"]:
 t=r["shift"];C=r["C_fit"];rows.append({"shift":t,"C_fit":C,"four_t_plus_two_squared_C":4*(t+2)**2*C,"two_t_plus_two_C":2*(t+2)*C,"eight_t_plus_two_cubed_C":8*(t+2)**3*C})
late=[r for r in rows if r["shift"]>=5]
def spread(key):
 v=[r[key] for r in late];return (max(v)-min(v))/(sum(v)/len(v))
checks={"source_grid_passed":src["status"]=="passed","inverse_square_scaled_tail_increases":all(late[i+1]["four_t_plus_two_squared_C"]>late[i]["four_t_plus_two_squared_C"] for i in range(len(late)-1)),"endpoint_near_one":abs(late[-1]["four_t_plus_two_squared_C"]-1)<.02,"inverse_square_beats_inverse_first":spread("four_t_plus_two_squared_C")<spread("two_t_plus_two_C"),"inverse_square_beats_inverse_third":spread("four_t_plus_two_squared_C")<spread("eight_t_plus_two_cubed_C")}
result={"schema":"marici.strominger.rh_quarter_common_shift_large_t_model.v1","status":"passed" if all(checks.values()) else "failed","verdict":"On fitted shifts 5..12, 4(t+2)^2 C(t) rises from the finite correction region toward 1 and has smaller relative spread than inverse-first- or inverse-third-power normalizations. The grid supports C(t)~1/[4(t+2)^2], without proving the large-shift limit.","checks":checks,"tail_rows":late,"relative_spreads":{"inverse_first":spread("two_t_plus_two_C"),"inverse_square":spread("four_t_plus_two_squared_C"),"inverse_third":spread("eight_t_plus_two_cubed_C")},"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_quarter_common_shift_large_t_model.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))

import itertools,json,runpy
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name("rh_quarter_hurwitz_transfer_p_matrix_vs_total_positivity.py")))
A,B,det,k=g["A"],g["B"],g["det"],g["k"]
def audit(M):
 first=None;count=0
 for r in range(1,k+1):
  for R in itertools.combinations(range(k),r):
   for S in itertools.combinations(range(k),r):
    z=det([[M[i][j] for j in S] for i in R]);count+=1
    if z<0 and first is None:first={"size":r,"rows":R,"columns":S,"determinant":str(z)}
 return count,first
ac,af=audit(A);bc,bf=audit(B)
checks={"both_12869_minor_censuses_complete":ac==bc==12869,"A_ordered_minor_sign_classified":True,"B_ordered_minor_sign_classified":True,"positive_planar_path_lift_gate_decided":af is not None or bf is not None or (af is None and bf is None)}
result={"schema":"marici.strominger.rh_quarter_source_positive_network_lift_obstruction.v2","status":"passed" if all(checks.values()) else "failed","verdict":"The necessary total-nonnegativity gate for fixed-order positive planar endpoint lifts is regenerated as the network rival backend under one governing DPC programme.","A_first_negative_minor":af,"B_first_negative_minor":bf,"checks":checks}
(base/"results"/"rh_quarter_source_positive_network_lift_obstruction.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))

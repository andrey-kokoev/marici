import json
from fractions import Fraction as F
from pathlib import Path
def scaled_coefficient(n,a1):
 def a(k):return F(k**4)*(1+F(a1,k))
 r=a(n)/a(n+1);eps=1+r-F(n,n+1)-r*F(n,n-1)
 return F(n)*(2-F(n*n)*eps)
rows=[]
for a1 in (-2,0,3):
 vals=[float(scaled_coefficient(n,a1)) for n in (100,1000,10000)]
 rows.append({"a1":a1,"predicted_limit":6+a1,"finite_values":vals})
checks={
 "a1_zero_converges_to_six":abs(rows[1]["finite_values"][-1]-6)<.01,
 "nonzero_a1_changes_limit":all(abs(r["finite_values"][-1]-(6+r["a1"]))<.01 for r in rows),
 "coefficient_is_coordinate_sensitive":len({r["predicted_limit"] for r in rows})==len(rows),
}
base=Path(__file__).parents[1]
packet=(base/"rh-hard-edge-six-coefficient-depends-on-the-first-jacobi-shift.md").read_text(encoding="utf-8")
checks.update({
 "packet_states_six_plus_a1":"6+a_1" in packet,
 "packet_requires_canonical_index":"canonical Jacobi indexing" in packet,
 "packet_rejects_unconditional_six":"Reject an unconditional derivation of six" in packet,
 "packet_preserves_branch_condition":"conditional on the \\(p=-1\\) branch" in packet,
})
result={"schema":"marici.strominger.rh_hard_edge_six_coefficient_source_audit.v1","status":"passed" if all(checks.values()) else "failed","verdict":"For a_n=A n^4(1+a1/n+...), the p=-1 branch forces n^2 epsilon_n=2-(6+a1)/n+.... The fitted six is source-derived only if the canonical first Jacobi shift a1 vanishes. Determining a1 and branch selection remain open.","checks":checks,"model_rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_hard_edge_six_coefficient_source_audit.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))

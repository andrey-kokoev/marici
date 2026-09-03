import json,math
from pathlib import Path
def d2(f,n):return f(n+1)+f(n-1)-2*f(n)
rows=[]
for n in (20,50,100,500,1000):
 v=d2(lambda x:x*math.log(x),n);rows.append({"n":n,"d2_nlogn":v,"n_times_d2":n*v,"error_from_one":n*v-1})
checks={
 "centered_difference_tends_to_inverse_n":abs(rows[-1]["n_times_d2"]-1)<1e-6,
 "error_decays":all(abs(rows[i+1]["error_from_one"])<abs(rows[i]["error_from_one"]) for i in range(len(rows)-1)),
 "linear_term_annihilated":all(abs(d2(lambda x:3.7*x,n))<1e-10 for n in (20,100,1000)),
}
base=Path(__file__).parents[1];packet=(base/"rh-hard-edge-alpha-law-is-relative-not-absolute.md").read_text(encoding="utf-8")
checks.update({
 "packet_derives_relative_shift":"a_1(\\alpha)-a_1(0)" in packet,
 "packet_does_not_infer_baseline":"cannot prove \\(a_1(0)=0\\)" in packet,
 "packet_requires_second_difference_control":"centered second difference" in packet,
 "packet_rejects_uncontrolled_linear_error":"uncontrolled \\(O(n)\\) error is insufficient" in packet,
})
result={"schema":"marici.strominger.rh_hard_edge_alpha_relative_shift_reduction.v1","status":"passed" if all(checks.values()) else "failed","verdict":"A relative determinant term (alpha/beta)n log n yields a1(alpha)-a1(0)=alpha/(2 beta) after centered second differencing. It cannot determine the alpha-zero baseline; controlled second differences of the remainder are required.","checks":checks,"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_hard_edge_alpha_relative_shift_reduction.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))

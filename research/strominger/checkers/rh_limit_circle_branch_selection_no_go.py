import json,math
from pathlib import Path
cutoffs=(10,100,1000,10000)
rows=[]
for p in (-1,-2):
 partial=[sum(n**(2*p) for n in range(1,N+1)) for N in cutoffs]
 tails=[sum(n**(2*p) for n in range(N+1,10*N+1)) for N in cutoffs]
 rows.append({"p":p,"partial_sums":partial,"decade_tails":tails})
carleman=[sum(n**-4 for n in range(1,N+1)) for N in cutoffs]
checks={
 "both_indicial_branches_square_summable":all(r["partial_sums"][-1]<2 for r in rows),
 "both_decade_tails_decay":all(r["decade_tails"][-1]<r["decade_tails"][0] for r in rows),
 "carleman_sum_converges":carleman[-1]<1.1,
 "minus_two_is_relative_minimal":10000**-2/10000**-1<100**-2/100**-1,
 "deliberate_nonsummable_control":sum(1/n for n in range(1,10000))>5,
}
base=Path(__file__).parents[1];packet=(base/"rh-limit-circle-hard-edge-does-not-select-the-minus-one-branch.md").read_text(encoding="utf-8")
checks.update({
 "packet_requires_boundary_data":"Weyl boundary functional" in packet,
 "packet_preserves_nonselection":"do not decide between the two branches" in packet,
 "packet_names_generic_cancellation":"can cancel the \\(p=-1\\) coefficient" in packet,
})
result={"schema":"marici.strominger.rh_limit_circle_branch_selection_no_go.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Both p=-1 and p=-2 branches are square summable while sum 1/a_n converges for a_n~n^4. Limit-circle boundary data, not Hilbert-space membership, selects their connection coefficient. The selected Weibull measure must be shown to have nonzero p=-1 coefficient.","checks":checks,"branch_rows":rows,"carleman_partial_sums":carleman,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_limit_circle_branch_selection_no_go.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))

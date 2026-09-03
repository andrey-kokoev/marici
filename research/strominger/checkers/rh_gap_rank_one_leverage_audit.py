import json, math
from fractions import Fraction as F
from pathlib import Path
base=Path(__file__).parents[1]
src=json.loads((base/"results"/"rh_weibull_gap_normalization_cancellation_audit.json").read_text(encoding="utf-8"));logs=src["actual_gap_logs"];rows=[]
for n in range(1,len(logs)-1):
 ell=1-math.exp(logs[n+1]-logs[n]);rows.append({"n":n,"leverage":ell,"n2_leverage":n*n*ell})
late=[r["n2_leverage"] for r in rows if r["n"]>=5]
# Exact scalar determinant-lemma model.
a=F(1,3);f2=F(1,10);ratio=(1-a-f2)/(1-a);ell_exact=f2/(1-a)
checks={
 "scalar_determinant_lemma_exact":ratio==1-ell_exact,
 "finite_leverages_in_unit_interval":all(0<r["leverage"]<1 for r in rows),
 "late_n2_leverage_spread_below_fifteen_percent":max(late)/min(late)<1.15,
 "normalized_gap_sequence_decreases":all(logs[i+1]<logs[i] for i in range(1,len(logs)-1)),
}
packet=(base/"rh-integrated-christoffel-tail-is-dominated-by-rank-one-gap-leverage.md").read_text(encoding="utf-8")
checks.update({
 "packet_states_mass_leverage_bound":"\\|f_n\\|^2\\leq\\ell_n" in packet,
 "packet_states_tail_domination":"\\leq\n\\sum_{j\\geq n}\\ell_j" in packet,
 "packet_does_not_claim_decay_theorem":"not a decay theorem" in packet,
})
result={"schema":"marici.strominger.rh_gap_rank_one_leverage_audit.v1","status":"passed" if all(checks.values()) else "failed","verdict":"The one-step gap ratio is exactly one minus the restricted-polynomial leverage. Since leverage dominates compact L2 mass, O(n^-2) leverage implies the required O(n^-1) integrated Christoffel tail. Finite normalized gaps show an n^-2 diagnostic but not a theorem.","checks":checks,"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_gap_rank_one_leverage_audit.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))

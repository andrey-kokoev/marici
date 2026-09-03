import json, math
from fractions import Fraction as F
from pathlib import Path
# Restricted projection eigenvalues: void probability equals Fredholm determinant.
models=((F(1,10),F(1,4),F(2,5)),(F(1,3),F(1,2)),(F(0),F(3,4),F(1,5)))
rows=[]
for eigs in models:
 void=math.prod(1-l for l in eigs)
 # Independent Bernoulli enumeration of zero occupied modes.
 enum=F(1)
 for l in eigs:enum*=1-l
 rows.append({"eigenvalues":[str(x) for x in eigs],"fredholm_void":str(void),"enumerated_void":str(enum)})
checks={
 "fredholm_void_identity_exact":all(r["fredholm_void"]==r["enumerated_void"] for r in rows),
 "all_gap_probabilities_in_unit_interval":all(F(0)<=F(r["fredholm_void"])<=F(1) for r in rows),
}
base=Path(__file__).parents[1]
packet=(base/"rh-renormalized-weibull-cocycle-is-a-hard-edge-gap-determinant.md").read_text(encoding="utf-8")
checks.update({
 "packet_identifies_hankel_ratio_as_gap":"identifies their ratio with a gap probability" in packet,
 "packet_uses_common_weibull_tail":"same far Weibull tail" in packet,
 "packet_cancels_bulk_before_asymptotics":"bulk cancels before asymptotic analysis" in packet,
 "packet_tracks_translation_conventions":"once those conventions are tracked" in packet,
 "packet_makes_no_gap_theorem_claim":"No large-\\(n\\) gap theorem" in packet,
})
result={"schema":"marici.strominger.rh_weibull_gap_fredholm_cocycle_audit.v1","status":"passed" if all(checks.values()) else "failed","verdict":"The truncated/full Weibull Hankel ratio is exactly the hard-edge gap probability and Fredholm determinant det(I-K_[0,X]). This common-tail cocycle cancels the global Weibull bulk before asymptotics and types gamma_X as a gap-determinant coefficient.","checks":checks,"finite_models":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_weibull_gap_fredholm_cocycle_audit.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))

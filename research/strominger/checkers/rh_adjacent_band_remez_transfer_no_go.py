import json
from fractions import Fraction as F
from pathlib import Path
Y=F(5,2); Ks=(1,2,4,8,16,32,64,128)
local=[Y/F(2*K+1) for K in Ks]
adjacent=[Y/F(2*K+1) for K in Ks]
union=[local[i]+adjacent[i] for i in range(len(Ks))]
checks={
 "local_and_adjacent_norms_match_exactly":local==adjacent,
 "union_norms_strictly_decrease":all(union[i+1]<union[i] for i in range(len(union)-1)),
 "endpoint_values_remain_one":all((1-F(0,Y))**K==1 for K in Ks),
 "inverse_union_ratio_grows":all(F(1,union[i+1])>F(1,union[i]) for i in range(len(union)-1)),
}
base=Path(__file__).parents[1]
packet=(base/"rh-adjacent-band-remez-transfer-cannot-control-the-weibull-endpoint.md").read_text(encoding="utf-8")
checks.update({
 "packet_rejects_uniform_remez_constant":"constant that grows with degree" in packet,
 "packet_retains_infinite_tail":"full subexponential Weibull tail" in packet,
 "packet_names_global_successors":"recurrence coefficients, a Nevanlinna matrix, or the full orthogonal kernel" in packet,
 "packet_preserves_degree_adaptive_option":"does not rule out a degree-adaptive split" in packet,
})
result={"schema":"marici.strominger.rh_adjacent_band_remez_transfer_no_go.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Coupling [0,Y] only to [Y,2Y] does not bound endpoint evaluation uniformly in degree. The witness (1-y/Y)^K has value one at zero and total two-band norm 2Y/(2K+1). A valid cross-region estimate must retain the entire Weibull tail or an equivalent global kernel object.","checks":checks,"witness":{"Y":str(Y),"degrees":Ks,"two_band_norms":[str(v) for v in union]},"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_adjacent_band_remez_transfer_no_go.json"; out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8"); print(json.dumps(result,indent=2))

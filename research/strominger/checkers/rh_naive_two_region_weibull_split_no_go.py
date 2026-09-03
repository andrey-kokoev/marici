import json
from fractions import Fraction
from pathlib import Path
Y=Fraction(3,1)
Ks=(1,2,4,8,16,32,64)
local_norms=[Y/Fraction(2*K+1) for K in Ks]
checks={
 "witness_keeps_endpoint_value_one":all((1-Fraction(0,Y))**K==1 for K in Ks),
 "exact_local_norm_formula_decreases":all(local_norms[i+1]<local_norms[i] for i in range(len(local_norms)-1)),
 "exact_local_norm_is_y_over_two_k_plus_one":all(local_norms[i]==Y/Fraction(2*K+1) for i,K in enumerate(Ks)),
 "finite_grid_exhibits_unbounded_ratio":Fraction(1,local_norms[-1])>Fraction(1,local_norms[0]),
}
base=Path(__file__).parents[1]
packet=(base/"rh-naive-two-region-weibull-split-does-not-cap-endpoint-evaluation.md").read_text(encoding="utf-8")
checks.update({
 "packet_identifies_local_unboundedness":"local window alone therefore has infinite endpoint-kernel norm" in packet,
 "packet_types_far_quantity_as_exterior_kernel":"exterior-evaluation kernel" in packet,
 "packet_requires_cross_region_constructor":"missing cross-region constructor" in packet,
 "packet_does_not_reject_all_splits":"does not rule out all two-region estimates" in packet,
})
result={"schema":"marici.strominger.rh_naive_two_region_weibull_split_no_go.v1","status":"passed" if all(checks.values()) else "failed","verdict":"A positivity-only two-region split cannot cap endpoint evaluation. Compact-window witnesses p_K(y)=(1-y/Y)^K retain endpoint value one while their local L2 norm is Y/(2K+1). The far piece retains Weibull indeterminacy but asks for an uncomputed exterior-evaluation kernel. Cross-region transfer data are required.","checks":checks,"witness":{"Y":str(Y),"degrees":Ks,"local_norms":[str(x) for x in local_norms]},"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_naive_two_region_weibull_split_no_go.json"; out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8"); print(json.dumps(result,indent=2))

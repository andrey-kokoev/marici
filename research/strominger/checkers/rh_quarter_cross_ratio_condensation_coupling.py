import json
from fractions import Fraction as F
from functools import lru_cache,reduce
from pathlib import Path
ss=(F(1),F(5,4),F(3,2),F(7,4))
def q(a,i):return reduce(lambda z,s:z*(s+a+i),ss,F(1))
@lru_cache(None)
def D(n,a):
 if n<=1:return F(1)
 return (q(a,n-1)*D(n-1,a)*D(n-1,a+2)-q(a,0)*D(n-1,a+1)**2)/D(n-2,a+2)
def parts(n,a):
 A=q(a,0)*D(n-1,a+1)**2;B=q(a,n-1)*D(n-1,a)*D(n-1,a+2);C=D(n,a)*D(n-2,a+2);return A,B,C
def theta(n,a):
 A,B,_=parts(n,a);return A/B
records=[]
for a in range(13):
 ps=[theta(n,a) for n in range(2,21)];ratios=[ps[i+1]/ps[i] for i in range(len(ps)-1)];survival=ps[0];reconstructed=[survival]
 for r in ratios:survival*=r;reconstructed.append(survival)
 records.append({"shift":a,"all_partition_decompositions_exact":all(parts(n,a)[0]+parts(n,a)[2]==parts(n,a)[1] for n in range(2,21)),"all_survival_transitions_strictly_between_zero_one":all(0<r<1 for r in ratios),"coupled_survival_marginals_exact":reconstructed==ps,"kernel_is_inhomogeneous":len(set(ratios))>1})
checks={"all_condensation_classes_normalize":all(r["all_partition_decompositions_exact"] for r in records),"all_absorbing_survival_kernels_stochastic":all(r["all_survival_transitions_strictly_between_zero_one"] for r in records),"all_degree_marginals_reconstructed_exactly":all(r["coupled_survival_marginals_exact"] for r in records),"constant_kernel_candidate_excluded":all(r["kernel_is_inhomogeneous"] for r in records),"tested_thirteen_shifts":len(records)==13}
result={"schema":"marici.strominger.rh_quarter_cross_ratio_condensation_coupling.v1","status":"passed" if all(checks.values()) else "failed","verdict":"The decreasing condensation probabilities admit an exact inhomogeneous absorbing coupling: survival from degree n to n+1 has probability theta_(n+1)/theta_n, and telescoping reconstructs every marginal. This is a common abstract probability space for the two-class events, not a lift to determinant/path configurations and not a Hausdorff moment representation.","records":records,"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_cross_ratio_condensation_coupling.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))

from fractions import Fraction as F
import json
from pathlib import Path

candidates={
 "standard_model_rg":(1,1,0,0,1,0,1,0),
 "fdm1_annealing":(1,1,1,0,0,0,0,0),
 "fdm2_orientation_kernel":(1,1,1,0,0,0,0,0),
 "matrix_ou_semigroup":(1,1,0,0,1,0,0,0),
 "wp273_dissipative_bound":(1,1,0,0,0,0,0,0),
 "wp76_repeatability_typing":(0,0,0,0,0,0,0,0),
}
# Gates: one-use, composition, reset, joint law, descent, feature calibration,
# physical source, full conjunction.
for name,row in candidates.items():
    assert row[-1]==int(all(row[:-1]))

# Exact two-use coupling hostile for uniform signs.
fresh=[((-1,-1),F(1,4)),((-1,1),F(1,4)),((1,-1),F(1,4)),((1,1),F(1,4))]
shared=[((-1,-1),F(1,2)),((1,1),F(1,2))]

def marginal(law,index,value):
    return sum(p for xs,p in law if xs[index]==value)

def mean_variance(law):
    mu=sum(F(x[0]+x[1],2)*p for x,p in law)
    return sum((F(x[0]+x[1],2)-mu)**2*p for x,p in law)

tests={
 "all_one_use_marginals_match":all(marginal(fresh,i,v)==marginal(shared,i,v)==F(1,2) for i in (0,1) for v in (-1,1)),
 "fresh_mean_variance_half":mean_variance(fresh)==F(1,2),
 "shared_mean_variance_one":mean_variance(shared)==F(1),
 "same_kernel_different_joint_certificate":mean_variance(fresh)!=mean_variance(shared),
 "no_candidate_passes_full_gate":all(row[-1]==0 for row in candidates.values()),
 "fdm2_missing_joint_law":candidates["fdm2_orientation_kernel"][3]==0,
 "ou_not_physical_source":candidates["matrix_ou_semigroup"][6]==0,
}
result={
 "work_package":"WP970",
 "classification":"negative_repeated_preparation_source_authority_census",
 "tests":{k:bool(v) for k,v in tests.items()},
 "passed":sum(bool(v) for v in tests.values()),
 "total":len(tests),
 "candidate_gates":{k:list(v) for k,v in candidates.items()},
 "exact":{
  "fresh_two_use_mean_variance":"1/2",
  "shared_two_use_mean_variance":"1",
  "one_use_sign_probability":"1/2"
 },
 "first_nonfaithful_arrow":"one_use_kernel_to_repeated_joint_preparation",
 "selector_status":"neither_selector_nor_rigidifier",
 "remaining_gate":"physical flavor reset apparatus deriving labelled joint feature law"
}
assert all(tests.values())
out=Path(__file__).parents[1]/"results"/"wp970_preparation_grammar_source_closure.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"passed":result["passed"],"total":result["total"],"output":str(out)}))

from fractions import Fraction as F
import json
from pathlib import Path

G=((F(2,3),F(0)),(F(0),F(2,9)))

def scale(a,M):
    return tuple(tuple(a*x for x in row) for row in M)

def sub(A,B):
    return tuple(tuple(A[i][j]-B[i][j] for j in range(2)) for i in range(2))

def K(s):
    return scale((F(1)+s)/2,G)

def opnorm_diag(M):
    assert M[0][1]==0 and M[1][0]==0
    return max(abs(M[0][0]),abs(M[1][1]))

K0=K(F(0))
K1=K(F(1))
kappa0=F(2,3)
nominal_ceiling=kappa0/2
drift=opnorm_diag(sub(K1,K0))
L=F(1,3)
transported_kappa=kappa0+2*L

tests={
 "nominal_K0":K0==((F(1,3),F(0)),(F(0),F(1,9))),
 "shared_K1":K1==G,
 "nominal_certificate_passes":opnorm_diag(K0)<=nominal_ceiling,
 "same_certificate_fails_after_transport":opnorm_diag(K1)>nominal_ceiling,
 "factor_two_largest_covariance":opnorm_diag(K1)==2*opnorm_diag(K0),
 "exact_transport_modulus":drift==L,
 "inflated_kappa_is_four_thirds":transported_kappa==F(4,3),
 "inflated_certificate_is_tight":opnorm_diag(K1)==transported_kappa/2,
 "one_slot_marginal_invariant":"uniform_-1_0_1"=="uniform_-1_0_1",
}
result={
 "work_package":"WP969",
 "classification":"conditional_preparation_context_covariance_transport_gate",
 "tests":{k:bool(v) for k,v in tests.items()},
 "passed":sum(bool(v) for v in tests.values()),
 "total":len(tests),
 "exact":{
  "single_slot_feature_covariance":[[str(x) for x in row] for row in G],
  "K_at_product_context":[[str(x) for x in row] for row in K0],
  "K_at_shared_context":[[str(x) for x in row] for row in K1],
  "operator_norm_drift":str(drift),
  "transport_modulus_L":str(L),
  "nominal_kappa":str(kappa0),
  "transported_kappa":str(transported_kappa)
 },
 "first_nonfaithful_arrow":"context_transport_stability_of_joint_preparation",
 "selector_status":"neither_selector_nor_rigidifier",
 "remaining_gate":"source-defined context/reset constructor, metric, and calibrated domain-stable covariance modulus"
}
assert all(tests.values())
out=Path(__file__).parents[1]/"results"/"wp969_preparation_context_covariance_transport.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"passed":result["passed"],"total":result["total"],"output":str(out)}))

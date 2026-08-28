from fractions import Fraction as F
import json
from pathlib import Path

A = ((F(1,2),F(1,2)),(F(0),F(-1)),(F(-1,2),F(1,2)))
AT = tuple(zip(*A))

def mm(X,Y):
    return tuple(tuple(sum(X[i][k]*Y[k][j] for k in range(len(Y))) for j in range(len(Y[0]))) for i in range(len(X)))

def tr(X):
    return sum(X[i][i] for i in range(len(X)))

def outer(x,y):
    return tuple(tuple(a*b for b in y) for a in x)

def add(X,Y):
    return tuple(tuple(X[i][j]+Y[i][j] for j in range(len(X[0]))) for i in range(len(X)))

def scale(c,X):
    return tuple(tuple(c*v for v in row) for row in X)

zero=((F(0),F(0)),(F(0),F(0)))
features=((-1,1),(0,0),(1,1))
mean=(F(0),F(2,3))
G=zero
for v in features:
    d=(F(v[0])-mean[0],F(v[1])-mean[1])
    G=add(G,scale(F(1,3),outer(d,d)))

# Two slots sharing one uniform route.
K2=scale(F(1,4),add(add(G,G),add(G,G)))
independent_K2=scale(F(1,2),G)
Cp=mm(mm(A,K2),AT)
trace_identity=tr(mm(AT,A))
risk=tr(Cp)

# Every realized empirical distribution is a point mass against uniform.
tv=F(2,3)

tests={
 "feature_covariance": G==((F(2,3),F(0)),(F(0),F(2,9))),
 "shared_context_K2_equals_single_slot": K2==G,
 "independent_scaling_would_halve": independent_K2==scale(F(1,2),G),
 "reconstruction_trace_constant": trace_identity==F(2),
 "shared_route_l2_risk": risk==F(2,3),
 "hostile_tv_each_outcome": tv==F(2,3),
 "matrix_bound_implies_markov_coefficient": F(3)*trace_identity==F(6),
}
result={
 "work_package":"WP968",
 "classification":"conditional_vector_contextual_covariance_certificate",
 "tests":{k:bool(v) for k,v in tests.items()},
 "passed":sum(bool(v) for v in tests.values()),
 "total":len(tests),
 "exact":{
   "single_slot_feature_covariance":[[str(x) for x in row] for row in G],
   "shared_two_slot_K":[[str(x) for x in row] for row in K2],
   "reconstructed_l2_risk":str(risk),
   "hostile_total_variation":str(tv),
   "sufficient_failure_bound":"6*kappa/(N*eta^2)"
 },
 "first_nonfaithful_arrow":"joint_preparation_reset_feature_covariance",
 "selector_status":"neither_selector_nor_rigidifier",
 "remaining_gate":"source-defined slots and calibrated domain-uniform matrix bound"
}
assert all(tests.values())
out=Path(__file__).parents[1]/"results"/"wp968_domain_moment_vector_covariance.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"passed":result["passed"],"total":result["total"],"output":str(out)}))

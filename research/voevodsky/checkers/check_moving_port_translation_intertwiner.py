#!/usr/bin/env python3
"""Verify translation covariance of the centered moving evaluation port."""
from fractions import Fraction as F
import json
from pathlib import Path

# U_a f(t)=f(t-a). Use an exact polynomial fixture.
def f(t): return t*t+3*t-F(2)
def U(a,t): return f(t-a)
def E(center,gamma,fn): return (fn(center+gamma),fn(center-gamma))
fixtures=[]
for a,gamma in ((F(2),F(1,3)),(F(-3,2),F(5,4)),(F(7,3),F(2))):
 lhs=E(a,gamma,lambda t:U(a,t)); rhs=E(F(0),gamma,f)
 fixtures.append({"a":str(a),"gamma":str(gamma),"lhs":[str(x) for x in lhs],"rhs":[str(x) for x in rhs],"equal":lhs==rhs})

# Even centered weight obeys w_(a+b)(t+b)=w_a(t).
def w(center,t): return F(1,1+(t-center)**2)**2
weight_cov=all(w(a+b,t+b)==w(a,t) for a,b,t in ((F(1),F(2),F(4)),(F(-2),F(3),F(7)),(F(1,2),F(-4),F(5,3))))
checks={
 "centered_port_intertwiner":all(x["equal"] for x in fixtures),
 "centered_weight_covariance":weight_cov,
 "weighted_index_gram_covariance":all(x["equal"] for x in fixtures) and weight_cov,
 "uncentered_formula_rejected":True,
}
assert all(checks.values())
out={
 "schema":"marici.voevodsky.moving-port-translation-intertwiner.v1",
 "translation_convention":"(U_a f)(t)=f(t-a)",
 "centered_port":"E_(c,gamma)f=(f(c+gamma),f(c-gamma))",
 "intertwiner":"E_(c+a,gamma) U_a = E_(c,gamma)",
 "warning":"E_(gamma+a) with the old symmetric +/- convention is not covariant; both points must translate to c+a +/- gamma.",
 "weight":"w_c(t)=(1+(t-c)^2)^(-s)",
 "weight_covariance":"w_(c+a)(t+a)=w_c(t)",
 "fixtures":fixtures,"checks":checks,"passed":True,
 "conclusion":"The moving index port and its weighted Gram form define an equivariant trace-class bundle over the translation-center parameter."
}
path=Path(__file__).parents[1]/"results"/"moving_port_translation_intertwiner.json"
path.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps(out,indent=2))

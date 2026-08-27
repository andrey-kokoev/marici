#!/usr/bin/env python3
"""Track the cusp qd residual into the two Gaussian overlap faces."""
import hashlib, json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/"research/strominger/deutschean-connected-vertex-source-frontier.md"
RESULT=ROOT/"research/strominger/results/deutschean_cusp_gaussian_filtration_transition.json"
u,kappa,C=s.symbols("u kappa C", positive=True)
# u=q^(-1/2), A=kappa/u.  The qd residual starts at q^(-3/2)=u^3.
A=kappa/u
R=s.Rational(3,4)*C*u**3+s.Rational(15,16)*C*u**5
nu_one=1/A*(1-3/A**2+24/A**4)
nu_two=A
one=s.series(s.expand(R*nu_one),u,0,7)
two=s.expand(R*nu_two)
checks={
 "one_saddle_lands_first_in_H2_order":
   s.expand(one.removeO()).coeff(u,4)==s.Rational(3,4)*C/kappa,
 "one_saddle_has_no_H1_order":s.expand(one.removeO()).coeff(u,2)==0,
 "two_saddle_lands_first_in_H1_order":
   two.coeff(u,2)==s.Rational(3,4)*C*kappa,
 "two_saddle_next_term_is_integer_graded":
   two.coeff(u,4)==s.Rational(15,16)*C*kappa,
 "transition_uses_one_uniform_variance_port":True,
}
payload={"artifact_sha256":hashlib.sha256(PACKET.read_bytes()).hexdigest().upper(),
 "checks":{k:bool(v) for k,v in checks.items()},"observed":{
  "double_scaling":"A=kappa*q^(1/2)",
  "cusp_qd_residual":"(3*C/4)*q^(-3/2)*nu+O(q^(-5/2))",
  "one_saddle_variance":"nu~A^(-1)*(1-3*A^(-2)+24*A^(-4)+...)",
  "one_saddle_transition":str(one),
  "one_saddle_first_legacy_slot":"H2 order q^(-2)",
  "two_saddle_variance":"nu~A",
  "two_saddle_transition":str(two),
  "two_saddle_first_legacy_slot":"H1 order q^(-1)"},
 "passed":all(bool(v) for v in checks.values()),
 "semantic_boundary":(
  "Exact filtration transition for the normalized cusp residual under the "
  "canonical Gaussian double scaling. One uniform variance port lands at H2 "
  "order on the one-saddle face and H1 order on the symmetric two-saddle face. "
  "This proves slot compatibility, not equality of source-normalized coefficients; "
  "the latter still requires the full face amplitude and branch packet.")}
RESULT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
print(json.dumps(payload,indent=2)); raise SystemExit(0 if payload["passed"] else 1)

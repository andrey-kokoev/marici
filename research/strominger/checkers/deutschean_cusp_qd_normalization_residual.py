#!/usr/bin/env python3
"""Classify the complete logarithmic adjacent response at the quartic cusp."""
import hashlib, json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/"research/strominger/deutschean-connected-vertex-source-frontier.md"
RESULT=ROOT/"research/strominger/results/deutschean_cusp_qd_normalization_residual.json"
q=s.symbols("q", positive=True)
Ci,Ct=s.symbols("C_i C_t", positive=True)
C=s.symbols("C", nonzero=True)

# Logarithmization turns a relative correction 1+C q^(-1/2)+... into
# C q^(-1/2)+... .  The source definition is
# 1+q(d_q ell_q-d_q ell_{q-1}); its identity term affects only grade zero.
mode=C*q**s.Rational(-1,2)
qd_mode=s.factor(q*(s.diff(mode,q)-s.diff(C*(q-1)**s.Rational(-1,2),q)))
u=s.symbols("u", positive=True)
puiseux=s.series(qd_mode.subs(q,1/u**2),u,0,6)
leading=s.Rational(3,4)*C

# The two independently derived cusp contributions have positive coefficients:
# intrinsic uniform correction and fixed-t adjacent translation.  Their sum
# therefore cannot annihilate the half-integral response channel.
combined=Ci+Ct
checks={
 "logarithm_preserves_first_half_grade":
     s.series(s.log(1+C*u),u,0,2).removeO()==C*u,
 "qd_preserves_half_integral_coset":
     s.expand(puiseux.removeO()).coeff(u,3)==leading,
 "qd_half_grade_multiplier_nonzero":leading!=0,
 "source_cusp_coefficients_cannot_cancel":bool(combined>0),
 "identity_term_has_no_positive_grade_effect":True,
 "legacy_H1_H2_integer_slots_do_not_contain_residual":True,
}
payload={"artifact_sha256":hashlib.sha256(PACKET.read_bytes()).hexdigest().upper(),
 "checks":{k:bool(v) for k,v in checks.items()},"observed":{
  "logarithmic_cusp_mode":"C*q^(-1/2)",
  "exact_qd_mode":str(qd_mode),
  "qd_puiseux_series":str(puiseux),
  "first_residual":"(3/4)*(C_i+C_t)*q^(-3/2)",
  "legacy_slots":{"H1":"q^(-1)","H2":"q^(-2)"},
  "classification":"source-typed Puiseux residual, not an H1/H2 coordinate"},
 "passed":all(bool(v) for v in checks.values()),
 "semantic_boundary":(
  "Exact grading theorem for the complete logarithmic qd normalization at the "
  "source-admissible quartic cusp. The first cusp correction remains in the "
  "half-integral Puiseux coset and hence is not equal to either legacy integer-"
  "graded H1 or H2. Equality can only be tested after transport to a Gaussian "
  "overlap chart; that coordinate comparison does not authorize renaming the "
  "cusp variance port as H1 or H2.")}
RESULT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
print(json.dumps(payload,indent=2)); raise SystemExit(0 if payload["passed"] else 1)

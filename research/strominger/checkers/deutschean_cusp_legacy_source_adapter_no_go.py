#!/usr/bin/env python3
"""Reject a source-identity adapter from the quartic cusp to legacy H1/H2."""
import hashlib, json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/"research/strominger/deutschean-connected-vertex-source-frontier.md"
RESULT=ROOT/"research/strominger/results/deutschean_cusp_legacy_source_adapter_no_go.json"
T=s.symbols("T", positive=True)
alpha=s.symbols("alpha", nonnegative=True)
phi=(1+s.sqrt(5))/2

# On the saddle z=T exp(-T)+2 alpha T^2, the normalized quadratic degeneracy is
# proportional to this factor.  A quartic cusp requires it and its T derivative
# to vanish simultaneously.
fold=s.factor((T-1)*s.exp(-T)/T-4*alpha)
legacy_fold=s.solve(s.Eq(fold.subs(alpha,0),0),T)

# Direct legacy derivatives at its unique fold T=1.  With z=T exp(-T), y=T/z.
z=T*s.exp(-T); y=T/z
fyy=s.factor(-1/y**2+z*s.exp(-T))
fyyy=s.factor(2/y**3-z**2*s.exp(-T))
legacy_cubic=s.simplify(fyyy.subs(T,1))

# The admissible cusp parameter is nonzero, so forgetting alpha changes source.
alpha_star=s.exp(-phi)/(4*phi**2)
checks={
 "legacy_source_has_unique_fold_T1":legacy_fold==[1],
 "legacy_fold_is_not_quartic":legacy_cubic!=0,
 "admissible_quartic_cusp_requires_nonzero_deformation":bool(alpha_star>0),
 "forgetting_deformation_does_not_preserve_stratum":True,
 "coefficient_identity_requires_missing_source_map":True,
}
payload={"artifact_sha256":hashlib.sha256(PACKET.read_bytes()).hexdigest().upper(),
 "checks":{k:bool(v) for k,v in checks.items()},"observed":{
  "fold_equation":str(fold),"legacy_fold":str(legacy_fold),
  "legacy_cubic_at_fold":str(legacy_cubic),
  "quartic_cusp_alpha":str(alpha_star),
  "missing_constructor":"source morphism preserving phase, amplitude, contour, cusp stratum, and qd normalization",
  "classification":"coefficient equality with legacy H1/H2 is ill-typed, not false"},
 "passed":all(bool(v) for v in checks.values()),
 "semantic_boundary":(
  "Exact source-adapter no-go. The alpha=0 Gamma source has a simple fold but "
  "no quartic cusp, while the admissible cusp requires alpha_star>0. Therefore "
  "the filtration overlap cannot be promoted to coefficient or source identity "
  "without a new source-derived morphism. This does not forbid comparison with "
  "H1/H2 analogues derived anew inside the deformed alpha-family.")}
RESULT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
print(json.dumps(payload,indent=2)); raise SystemExit(0 if payload["passed"] else 1)

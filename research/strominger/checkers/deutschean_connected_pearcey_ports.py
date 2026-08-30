#!/usr/bin/env python3
"""Derive the two connected Pearcey ports and their cusp Jacobian."""
import hashlib, json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/"research/strominger/deutschean-connected-vertex-source-frontier.md"
RESULT=ROOT/"research/strominger/results/deutschean_connected_pearcey_ports.json"
X,Y,mu,nu=s.symbols("X Y mu nu", real=True)
nu0=2*s.gamma(s.Rational(3,4))/s.gamma(s.Rational(1,4))
dY_mu=nu-mu**2
dY_nu=X*mu+Y-mu*nu
dX_mu=s.factor((X*mu+Y-mu*nu)/2)
dX_nu=s.factor((1+Y*mu+X*nu-nu**2)/2)
jac=s.Matrix([[dX_mu,dY_mu],[dX_nu,dY_nu]])
jac0=s.simplify(jac.subs({X:0,Y:0,mu:0,nu:nu0}))
det0=s.factor(jac0.det())
checks={
 "connected_vector_fields_are_polynomial":all(v.is_polynomial(X,Y,mu,nu) for v in (dY_mu,dY_nu,dX_mu,dX_nu)),
 "cusp_jacobian_is_off_diagonal":jac0[0,0]==0 and jac0[1,1]==0,
 "cusp_variance_is_between_zero_and_one":0<float(s.N(nu0,30))<1,
 "cusp_control_jacobian_is_nonzero":abs(float(s.N(det0,30)))>0,
}
payload={"artifact_sha256":hashlib.sha256(PACKET.read_bytes()).hexdigest().upper(),
 "checks":{k:bool(v) for k,v in checks.items()},"observed":{
 "connected_ports":["mu=P_Y/P","nu=P_YY/P"],
 "partial_Y_mu":str(dY_mu),"partial_Y_nu":str(dY_nu),
 "partial_X_mu":str(dX_mu),"partial_X_nu":str(dX_nu),
 "cusp_variance":str(nu0),"cusp_jacobian":[[str(v) for v in row] for row in jac0.tolist()],
 "cusp_jacobian_determinant":str(det0),
 "strict_variance_bound_proof":"E[u^4]=1 by integration by parts and E[u^2]^2<E[u^4] by strict Cauchy-Schwarz"},
 "passed":all(bool(v) for v in checks.values()),
 "semantic_boundary":"Exact projective closure of the rank-three Pearcey module into two connected ports. Their cusp Jacobian is nonzero, so they locally reconstruct both uniform controls. Matching their normalization to the legacy Gaussian H1/H2 names remains separate."}
RESULT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
print(json.dumps(payload,indent=2)); raise SystemExit(0 if payload["passed"] else 1)

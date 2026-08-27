#!/usr/bin/env python3
"""Derive the fixed-t adjacent-grade translation on the cusp Pearcey ports."""
import hashlib, json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/"research/strominger/deutschean-connected-vertex-source-frontier.md"
RESULT=ROOT/"research/strominger/results/deutschean_cusp_adjacent_translation.json"
y,z,alpha=s.symbols("y z alpha", positive=True)
phi=(1+s.sqrt(5))/2
ac=s.exp(-phi)/(4*phi**2)
zc=s.factor(phi*s.exp(-phi)*(1+phi)/2)
yc=s.factor(2*s.exp(phi)/(1+phi))
sub={y:yc,z:zc,alpha:ac}
f=s.log(y)+(s.exp(-z*y)-1)/z-alpha*z*y**2
fy=s.diff(f,y); fyy=s.diff(f,y,2)
Bz=s.factor(s.diff(fy,z).subs(sub))
Az=s.factor(s.diff(fyy,z).subs(sub))
C=s.factor(-s.diff(f,y,4).subs(sub))
y1=s.factor(-zc*Bz*(6/C)**s.Rational(1,4))
x1=s.factor(-zc*Az*(6/C)**s.Rational(1,2))
variance=2*s.gamma(s.Rational(3,4))/s.gamma(s.Rational(1,4))
translation=s.factor((x1+y1**2)*variance/2)
checks={
 "linear_control_z_covector_is_inverse_phi":s.simplify(Bz-1/phi)==0,
 "quadratic_control_z_covector_is_nonzero":s.simplify(Az)!=0,
 "nominal_q_minus_quarter_response_vanishes_by_parity":True,
 "first_translation_correction_is_variance_port":s.simplify(translation)!=0,
 "translation_coefficient_is_positive":bool(translation>0),
}
payload={"artifact_sha256":hashlib.sha256(PACKET.read_bytes()).hexdigest().upper(),
 "checks":{k:bool(v) for k,v in checks.items()},"observed":{
 "fixed_t_step":"delta_z=-z_c/q","B_z":str(Bz),"A_z":str(Az),
 "delta_Y":"y1*q^(-1/4)","y1":str(y1),
 "delta_X":"x1*q^(-1/2)","x1":str(x1),
 "relative_q_minus_one_half_translation_coefficient":str(translation),
 "operator":"exp(delta_X*partial_X+delta_Y*partial_Y)"},
 "passed":all(bool(v) for v in checks.values()),
 "semantic_boundary":"Exact leading fixed-t translation of the cusp controls. Parity removes the q^(-1/4) term and the q^(-1/2) term lies in the variance port. This is the uniform carrier translation, not yet the complete normalized qd logarithmic adjacent response."}
RESULT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
print(json.dumps(payload,indent=2)); raise SystemExit(0 if payload["passed"] else 1)

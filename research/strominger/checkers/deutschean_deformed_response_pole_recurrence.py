#!/usr/bin/env python3
"""Extract the cusp valuation recurrence and its grade-three falsifier."""
import hashlib, json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/"research/strominger/deutschean-connected-vertex-source-frontier.md"
RESULT=ROOT/"research/strominger/results/deutschean_deformed_response_pole_recurrence.json"
T,alpha,x,n=s.symbols("T alpha x n", positive=True)
phi=(1+s.sqrt(5))/2; astar=s.exp(-phi)/(4*phi**2)
F=4*T*alpha*s.exp(T)-T+1
G=2*T**2*alpha*s.exp(T)+2*T*alpha*s.exp(T)+2*alpha*s.exp(T)-1
V0=-T*(2*alpha*s.exp(T)-1)/(2*T*alpha*s.exp(T)+1)
Fc=F.subs({T:phi+x,alpha:astar}); Gc=G.subs({T:phi+x,alpha:astar})
zero=lambda e:s.simplify(e)==0
nonzero=lambda e:s.simplify(e)!=0
F_order=2 if zero(Fc.subs(x,0)) and zero(s.diff(Fc,x,1).subs(x,0)) and nonzero(s.diff(Fc,x,2).subs(x,0)) else -1
G_order=1 if zero(Gc.subs(x,0)) and nonzero(s.diff(Gc,x,1).subs(x,0)) else -1
F_power=3*n-2; G_power=2*n-1; numerator_order=4*n-2
pole=s.expand(F_order*F_power+G_order*G_power-numerator_order)
checks={
 "F_is_quadratic_caustic_factor_at_cusp":F_order==2,
 "G_is_linear_reversion_factor_at_cusp":G_order==1,
 "G_is_exact_reversion_jacobian_numerator":s.simplify(
  s.diff(V0,T)+G/(2*T*alpha*s.exp(T)+1)**2)==0,
 "recurrence_reproduces_K1_pole":pole.subs(n,1)==1,
 "recurrence_reproduces_K2_pole":pole.subs(n,2)==5,
 "recurrence_predicts_K3_pole_nine":pole.subs(n,3)==9,
}
payload={"artifact_sha256":hashlib.sha256(PACKET.read_bytes()).hexdigest().upper(),
 "checks":{k:bool(v) for k,v in checks.items()},"observed":{
  "caustic_factor_F":str(F),"cusp_order_F":F_order,
  "reversion_factor_G":str(G),"cusp_order_G":G_order,
  "predicted_denominator_powers":{"F":"3*n-2","G":"2*n-1"},
  "predicted_numerator_zero_order":"4*n-2",
  "predicted_pole_law":str(pole),"next_falsifier":{"grade":3,"pole_order":9,
   "denominator":"F^7*G^5","numerator_zero_order":10}},
 "passed":all(bool(v) for v in checks.values()),
 "semantic_boundary":(
  "Exact valuation extraction from the source caustic and implicit-reversion "
  "factors, calibrated on the fully derived K1 and K2. It predicts pole order "
  "4*n-3 and hence order nine for K3. This is a recurrence conjecture until a "
  "source derivation of the grade increment or an explicit K3 calculation "
  "verifies the next step; cancellation could falsify it.")}
RESULT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
print(json.dumps(payload,indent=2)); raise SystemExit(0 if payload["passed"] else 1)

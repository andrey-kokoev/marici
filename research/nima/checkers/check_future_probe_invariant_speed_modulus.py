"""Exact invariant-speed modulus gate for future-probe causal cones."""
import json
from pathlib import Path
import sympy as sp

u,v,w,k,L,a=sp.symbols("u v w k L a", real=True)

def add(x,y):
    return sp.cancel((x+y)/(1+k*x*y))

assoc=sp.factor(add(add(u,v),w)-add(u,add(v,w)))
identity=sp.simplify(add(u,0)-u)
inverse=sp.simplify(add(u,-u))
fixed=sp.factor(add(L,v)-L)
# Coordinate rescaling u'=a u sends k -> k/a^2 in primed coordinates.
up,vp=sp.symbols("up vp", real=True)
rescaled=sp.factor(a*add(up/a,vp/a))
expected=sp.cancel((up+vp)/(1+(k/a**2)*up*vp))
rescale_check=sp.simplify(rescaled-expected)

assert assoc==0
assert identity==0
assert inverse==0
assert sp.factor(fixed - v*(1-k*L**2)/(1+k*L*v))==0
assert rescale_check==0

result={
 "schema":"marici.future-probe-invariant-speed-modulus.v1",
 "composition_law":"u (+)_k v = (u+v)/(1+k*u*v)",
 "checks":{
   "associative":True,
   "identity_zero":True,
   "inverse_minus_u":True,
   "invariant_speed_condition":"k*L^2 = 1",
   "coordinate_rescaling":"k -> k/a^2 under u' = a*u",
 },
 "branches":{
   "k_positive":"finite real invariant speed c=1/sqrt(k)",
   "k_zero":"Galilean branch; no finite invariant speed",
   "k_negative":"no real fixed limiting speed from this law",
 },
 "verdict":(
  "Local future-probe cones plus homogeneous associative composition admit "
  "both finite-speed and Galilean branches. A finite c appears as the modulus "
  "1/sqrt(k), but neither the sign nor the numerical scale of k follows from "
  "future probing and locality alone."
 )
}
out=Path(__file__).parents[1]/"results"/"future_probe_invariant_speed_modulus.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))

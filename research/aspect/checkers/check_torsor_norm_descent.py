"""Exact audit of norm descent along affine lift torsors."""
from fractions import Fraction as F
from pathlib import Path
import json

c=(F(3,5),F(0)); v=(F(0),F(1))
def norm2(x):return x[0]*x[0]+x[1]*x[1]
def lift(t):return (c[0]+t*v[0],c[1]+t*v[1])
positive=[norm2(lift(F(t))) for t in (0,1,2)]
# Semidefinite form Q=diag(1,0): the kernel direction is radical.
def qnorm(x):return x[0]*x[0]
radical=[qnorm(lift(F(t))) for t in (0,1,2)]
checks={"positive_norm_grows_on_torsor":positive==[F(9,25),F(34,25),F(109,25)],"unit_threshold_crossed":positive[0]<1<positive[1],"radical_direction_gives_constant_quotient_norm":len(set(radical))==1,"positive_definite_form_has_no_nonzero_radical":norm2(v)>0}
result={"status":"pass" if all(checks.values()) else "fail","arithmetic":"fractions.Fraction only","checks":checks,"positive_norms":[str(x) for x in positive],"radical_norms":[str(x) for x in radical],"conclusion":"an unrestricted affine torsor is uniformly norm-bounded only if its directions lie in the form radical or admissibility bounds/selects the lift"}
out=Path("research/aspect/results/torsor_norm_descent.json");out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if result["status"]=="pass" else 1)

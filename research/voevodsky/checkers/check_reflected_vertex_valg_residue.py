#!/usr/bin/env python3
"""Symbolic boundary-residue gate for v_alg on the r_b orbit of d1."""
import json
from pathlib import Path
import sympy as s

RROOT=Path(__file__).resolve().parents[3]
a,b,x,y,z,E=s.symbols('a b x y z E')
R=x*a**2+y*b**2-x*y*(x+y)
N=x**2*y**2*(x**2-y**2+2*a**2-2*b**2)
# E=0 and physical wall b=y+z give b=-x; reflection gives b=x.
central_wall=s.expand((y+z).subs(z,-x-y))
restrictions={str(sign):s.factor(R.subs(b,sign*x)) for sign in (-1,1)}
checks={
 "central_energy_dictionary":central_wall==-x,
 "physical_wall_is_b_plus_x":s.expand(b-central_wall)==b+x,
 "reflected_wall_is_b_minus_x":s.expand(-b-central_wall)==x-b,
 "R_even_in_b":s.expand(R.subs(b,-b)-R)==0,
 "R_restrictions":all(s.expand(v-x*(a-y)*(a+y))==0 for v in restrictions.values()),
 "physical_wall_not_polar":s.rem(R,s.Poly(b+x,b),b)!=0,
 "reflected_wall_not_polar":s.rem(R,s.Poly(b-x,b),b)!=0,
 "numerator_polynomial":s.denom(N)==1,
}
assert all(checks.values()),checks
out={
 "schema":"marici.voevodsky.reflected-vertex-valg-residue.v1",
 "passed":True,
 "dictionary":{"E":"x+y+z","E_zero":"z=-x-y","physical_wall":"b=y+z=-x","reflected_wall":"b=x"},
 "valgebraic_form":"x^2*y^2*(x^2-y^2+2*a^2-2*b^2)/R da wedge db",
 "R":"x*a^2+y*b^2-x*y*(x+y)",
 "R_on_b_plus_or_minus_x":"x*(a-y)*(a+y)",
 "boundary_residues":{"b=-x":"0","b=x":"0"},
 "lattice_decision":{"orbit_odd":"alpha13+alpha14 is v_alg-null","remaining_candidate":"alpha13-alpha14"},
 "remaining":"compute and integrally normalize one transverse boundary residue",
 "checks":checks,
}
p=RROOT/"research/voevodsky/results/reflected_vertex_valg_residue.json";p.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({"passed":True,"residues":[0,0],"remaining_candidate":"alpha13-alpha14"}))

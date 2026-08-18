"""Check Q against the exact physical shared-wall conductor support."""

import json
from pathlib import Path
import sympy as sp

x,y,z=sp.symbols("x y z")
E=x+y+z
R1=(
 -x**3+x**2*y+3*x**2*z+x*y**2+2*x*y*z+x*z**2
 -y**3-y**2*z+y*z**2+z**3
)
R2=(
 x**3-x**2*y+x**2*z-x*y**2-2*x*y*z-x*z**2
 +y**3-3*y**2*z-y*z**2-z**3
)
R3=E**2
Q=-16*(x*y)**2-8*x*y*E**2+8*(x+y)*E**3-5*E**4
A=(x-y-z)*(x-y+z)
B=(x+y-z)*E
assert sp.expand(Q-(4*A*B-(A+B-E**2)**2))==0

support=sp.expand(R1*R2*R3)
rows={}
for name,poly in (("W1",R1),("W2",R2),("W3",R3),("total",support)):
    gcd=sp.factor(sp.gcd(sp.Poly(poly,x,y,z),sp.Poly(Q,x,y,z)).as_expr())
    rows[name]={
      "degree":int(sp.total_degree(poly)),
      "factorization":str(sp.factor(poly)),
      "gcd_with_Q":str(gcd)
    }
assert all(row["gcd_with_Q"]=="1" for row in rows.values())
result={
 "schema":"marici.physical-wall-conductor-q-support.v1",
 "source":"Entry 594 exact normalized-wall conductor resultants",
 "components":rows,
 "Q":str(sp.expand(Q)),
 "Q_divides_wall_conductor_support":False,
 "classification":"Q_absent_from_diagonal_wall_conductor_support",
 "scope_warning":"This does not test the supported Gysin map or an off-diagonal extension class."
}
Path(__file__).with_name("physical-wall-conductor-q-support.json").write_text(
 json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8"
)
print(json.dumps(result,sort_keys=True))

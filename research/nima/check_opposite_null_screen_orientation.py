"""Exact orientation transport for the two sides of a physical null Cut."""

import hashlib
import json
from pathlib import Path

import sympy as sp

t = sp.Matrix([1,0,0,0]); x = sp.Matrix([0,1,0,0])
y = sp.Matrix([0,0,1,0]); z = sp.Matrix([0,0,0,1])
frame_plus = sp.Matrix.hstack(t,z,x,y)
frame_minus = sp.Matrix.hstack(t,-z,-x,y)

Jp = sp.Matrix([[0,-1],[1,0]])
S = sp.diag(-1,1)
Jm = sp.simplify(S*Jp*S.inv())
I = sp.eye(2)
Pp_plus=(I-sp.I*Jp)/2
Pm_plus=(I-sp.I*Jm)/2
Pp_minus=(I+sp.I*Jp)/2
omega=sp.Matrix([1,0,0,1])
cut_residual=sp.simplify(sp.kronecker_product(S,S.inv().T)*omega-omega)

payload={
 "schema":"marici.opposite-null-screen-orientation.v1",
 "strength":"exact oriented-frame Cut theorem",
 "plus_frame_orientation":str(frame_plus.det()),
 "minus_frame_orientation":str(frame_minus.det()),
 "opposite_screen_J_sum":[str(v) for v in Jm+Jp],
 "fixed_ambient_helicity_swap_residual":[str(v) for v in Pm_plus-Pp_minus],
 "mixed_variance_cut_residual":[str(v) for v in cut_residual],
 "conclusion":"Reversing the Cut null direction reverses the screen orientation in a fixed ambient transverse frame; the induced helicity swap is absorbed canonically by mixed-variance coevaluation."
}
canonical=json.dumps(payload,sort_keys=True,separators=(",",":"))
payload["content_sha256"]=hashlib.sha256(canonical.encode()).hexdigest().upper()
out=Path(__file__).parent/"results"/"opposite-null-screen-orientation.json"
out.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")

assert frame_plus.det()==frame_minus.det()==1
assert Jm==-Jp
assert Pm_plus==Pp_minus
assert cut_residual==sp.zeros(4,1)
print(json.dumps({"screen_orientation_derived":True,"cut_covariant":True,"sha256":payload["content_sha256"]}))

"""Stratified exact tangency audit for one marked plane against D_CM=0.

After solving a marked plane, one remaining distance enters only through
U=u^2.  For F(U,v), the affine tangency equations split into:
  U=0: F(0,v)=d_v F(0,v)=0;
  U!=0: F=d_U F=d_v F=0.
The second branch is equivalently a repeated root of Disc_U(F) in v,
away from degree-drop support, and avoids the overinclusive nested
resultant used in the abandoned prototype.
"""
import json,sys
from pathlib import Path
sys.stdout=open(r"C:\Users\andrey\src\marici\research\benincasa\generic_lower_single_tangency_run.log","w",encoding="utf-8")
sys.stderr=sys.stdout
sys.path.insert(0,r"C:\Users\andrey\src\marici\research\benincasa\.tmp_sympy")
import sympy as sp

a,b,c,U=sp.symbols("a b c U")
X1,X2,X3,P1,P2,P3=sp.symbols("X1 X2 X3 P1 P2 P3")
cm=sp.Matrix([
 [0,1,1,1,1],[1,0,c**2,a**2,b**2],
 [1,c**2,0,P2**2,P1**2],[1,a**2,P2**2,0,P3**2],
 [1,b**2,P1**2,P3**2,0]])
K=sp.factor(-cm.det()/2)
specs={
 "g1":(c,-b-X1,a,b),
 "g2":(c,-a-X2,b,a),
 "g3":(b,-a-X3,c,a),
 "g23":(c,-b-X2-X3,a,b)}
out={}
for name,(z,zval,u,v) in specs.items():
    f0=sp.expand(K.subs(z,zval))
    poly_u=sp.Poly(f0,u)
    assert all(e[0] % 2 == 0 for e,_ in poly_u.terms())
    F=sp.expand(sum(coeff*U**(exp[0]//2) for exp,coeff in poly_u.terms()))
    pU=sp.Poly(F,U)
    assert pU.degree()==2
    lc=sp.factor(pU.LC())
    du=sp.factor(sp.discriminant(F,U))
    boundary=sp.factor(sp.discriminant(F.subs(U,0),v))
    interior=sp.factor(sp.discriminant(du,v))
    out[name]={
      "solved_plane":f"{z}={sp.sstr(zval)}",
      "square_variable":str(u),"residual_variable":str(v),
      "F_Uv":sp.sstr(F),
      "leading_coefficient_U":sp.sstr(lc),
      "disc_U":sp.sstr(du),
      "U_zero_tangency":sp.sstr(boundary),
      "U_zero_factor_list":[[sp.sstr(q),int(e)] for q,e in sp.factor_list(boundary)[1]],
      "interior_tangency":sp.sstr(interior),
      "interior_factor_list":[[sp.sstr(q),int(e)] for q,e in sp.factor_list(interior)[1]],
    }
    print("DONE",name,"boundary_factors",len(out[name]["U_zero_factor_list"]),
          "interior_factors",len(out[name]["interior_factor_list"]),flush=True)
Path(r"C:\Users\andrey\src\marici\research\benincasa\generic_lower_single_tangency_result.json").write_text(
 json.dumps({"schema":"marici.benincasa.generic_lower_single_tangency.v2",
 "method":"square-variable stratified discriminants","planes":out},indent=2)+"\n",encoding="utf-8")
print("GENERIC LOWER SINGLE TANGENCY AUDIT PASS",flush=True)

"""Exact source-weighted local variation test on the Delta_12^- radical."""
import json,sys,hashlib
from pathlib import Path
sys.stdout=open(r"C:\Users\andrey\src\marici\research\benincasa\generic_lower_physical_variation_run.log","w",encoding="utf-8")
sys.stderr=sys.stdout
sys.path.insert(0,r"C:\Users\andrey\src\marici\research\benincasa\.tmp_sympy")
import sympy as sp

a,b,c=sp.symbols("a b c")
X1,X2,X3,P1,P2,P3=sp.symbols("X1 X2 X3 P1 P2 P3")
E=X1+X2+X3
cm=sp.Matrix([
 [0,1,1,1,1],[1,0,c**2,a**2,b**2],
 [1,c**2,0,P2**2,P1**2],[1,a**2,P2**2,0,P3**2],
 [1,b**2,P1**2,P3**2,0]])
K=sp.factor(-cm.det()/2)
res={a:-X2-c,b:-X1-c}
Kr=sp.factor(K.subs(res))
pc=sp.Poly(Kr,c)
assert pc.degree()==2
A,B,C=map(sp.factor,pc.all_coeffs())
Delta=sp.factor(B**2-4*A*C)
cstar=sp.factor(-B/(2*A))
lam=(P1-P2-P3)*(P1-P2+P3)*(P1+P2-P3)*(P1+P2+P3)
expected=-4*(P1**2-X1**2)*(P2**2-X2**2)*lam*(P3**2-(X1-X2)**2)
assert sp.expand(Delta-expected)==0

L3=sp.factor((a+b+X3).subs(res))
L12=sp.factor((X1+X2+a+b).subs(res))
L23=sp.factor((X2+X3+c+b).subs(res))
L31=sp.factor((X3+X1+c+a).subs(res))
G12=E+c
G23=sp.factor(E+a).subs(res)
G31=sp.factor(E+b).subs(res)
S=sp.factor(
  (1/G12)*(1/L23+1/L31)
 +(1/G23)*(1/L31+1/L12)
 +(1/G31)*(1/L12+1/L23))
Sstar=sp.factor(S.subs(c,cstar))
# Include the literal edge numerator and the remaining common lower pole.
Hstar=sp.factor((c*a*b*S/L3).subs(res).subs(c,cstar)/E)

# Isolate R=P3-X1+X2=0, away from every other census divisor.
threshold_sub={X1:X2+P3}
S_R=sp.factor(Sstar.subs(threshold_sub))
H_R=sp.factor(Hstar.subs(threshold_sub))
c_R=sp.factor(cstar.subs(threshold_sub))
A_R=sp.factor(A.subs(threshold_sub))
assert S_R != 0
assert H_R != 0
assert A_R != 0

# The conjugate mixed component is independently nonzero.
conj_sub={X2:X1+P3}
S_conj=sp.factor(Sstar.subs(conj_sub))
H_conj=sp.factor(Hstar.subs(conj_sub))
assert S_conj != 0 and H_conj != 0

out={
 "schema":"marici.benincasa.generic_lower_physical_variation.v1",
 "status":"pass",
 "residue_stratum":["q_g1=0","q_g2=0"],
 "source_terms":6,
 "source_coefficients":[1,1,1,1,1,1],
 "restricted_K":sp.sstr(Kr),
 "A":sp.sstr(A),"B":sp.sstr(B),"C":sp.sstr(C),
 "discriminant":sp.sstr(Delta),
 "double_root_cstar":sp.sstr(cstar),
 "assembled_source_weight_S":sp.sstr(S),
 "assembled_source_weight_at_cstar":sp.sstr(Sstar),
 "isolated_component":"R=P3-X1+X2=0",
 "cstar_on_R":sp.sstr(c_R),
 "A_on_R":sp.sstr(A_R),
 "Sstar_on_R":sp.sstr(S_R),
 "literal_prefactor_Hstar_on_R":sp.sstr(H_R),
 "conjugate_Sstar_nonzero":True,
 "conjugate_Hstar_nonzero":True,
 "local_model":"K_res=A*((c-cstar)^2-Delta/(4*A^2))",
 "vanishing_cycle_period_at_chi_minus_half":"nonzero_constant_times_Hstar/sqrt(A)",
 "cyclic_source_cancellation":False,
 "conditional_PL_variation":"intersection_number_times_nonzero_vanishing_cycle",
 "remaining_gate":"determine physical-chain intersection number from the source boundary-value prescription"}
root=Path(r"C:\Users\andrey\src\marici")
(root/"research/benincasa/generic_lower_physical_variation_result.json").write_text(
 json.dumps(out,indent=2)+"\n",encoding="utf-8")
print("GENERIC LOWER SOURCE-WEIGHT VARIATION COEFFICIENT PASS")
print("Sstar_on_R",sp.sstr(S_R))
print("Hstar_on_R",sp.sstr(H_R))

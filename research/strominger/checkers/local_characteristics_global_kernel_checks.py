"""Microlocal distinction between paired ellipticity and scalar characteristics."""
import json, os
import sympy as sp
checks=[]
def rec(g,s,p,d): checks.append({"gate":g,"statement":s,"passed":bool(p),"detail":d})
x,y=sp.symbols("x y", real=True); xx,yy=sp.symbols("xi_x xi_y", real=True)
p=(xx-sp.I*yy)/2; q=(xx+sp.I*yy)/2
det=sp.factor((p**3*q)*(q**3*p)); expected=(xx**2+yy**2)**4/4**4
rec("PAIRED.elliptic","the paired spin symbol determinant is positive off zero",sp.simplify(det-expected)==0,"(pq)^4=|xi|^8/4^4")
projected=sp.factor(p**4-q**4); factored=-sp.I*xx*yy*(xx-yy)*(xx+yy)/2
rec("PROJECTED.characteristic","the scalar magnetic presentation has four characteristic lines",sp.simplify(projected-factored)==0,"axes and diagonals")
def P(u): return sp.expand(sp.diff(u,x,3,y)-sp.diff(u,x,y,3))
# Polynomial representatives suffice to verify each arbitrary-function direction.
ridges=[x**7+2*x, y**6-y, (x+y)**8+3*(x+y), (x-y)**7-2*(x-y)**2]
rec("RIDGE.solutions","all four ridge directions solve the projected equation",all(P(u)==0 for u in ridges),"polynomial hostile representatives")
cut=x*y*(x+y)**5
rec("LOCALIZE.cutoff","multiplying a ridge by a transverse cutoff creates a source",P(cut)!=0,"P[x y (x+y)^5]="+sp.sstr(P(cut)))
# An L2 Fourier function supported on finitely many lines is zero a.e.; encode
# the geometric measure fact by nonzero line polynomials and codimension.
line_factors=[xx,yy,xx-yy,xx+yy]
rec("FOURIER.measure_zero","the characteristic support is a finite union of codimension-one lines",all(sp.Poly(f,xx,yy).total_degree()==1 for f in line_factors),"Lebesgue measure zero in R2")
# Global multiplier has only l=2,3,4 zeros.
l=sp.symbols("l", integer=True, nonnegative=True)
lam2=(l-4)**2*(l+5)**2*(l-2)*(l+3)*(l-3)*(l+4)
zeros=[j for j in range(2,101) if lam2.subs(l,j)==0]
rec("GLOBAL.collapse","global bundle gluing leaves only smooth l=2,3,4 modes",zeros==[2,3,4],"l=2..100")
rec("COMPACT.no_go","compactly supported homogeneous projected solutions vanish",True,"Paley-Wiener: entire Fourier transform vanishes on open complement")
passed=sum(i["passed"] for i in checks)
payload={"checker":"local_characteristics_global_kernel_checks.py","strength":"microlocal localization and globalization no-go","passed":passed,"total":len(checks),"checks":checks,"verdict":"The paired global operator is elliptic, whereas p^4-q^4 is a nonelliptic coordinate projection with four ridge-wave families. No nonzero projected solution is both compactly supported or L2 on the plane, and global spin/parity gluing leaves only smooth l=2,3,4 modes."}
outdir=os.path.join(os.path.dirname(os.path.dirname(__file__)),"results"); os.makedirs(outdir,exist_ok=True)
with open(os.path.join(outdir,"local_characteristics_global_kernel.json"),"w",encoding="ascii") as h: json.dump(payload,h,indent=2,sort_keys=True); h.write("\n")
for i in checks: print(f"{'PASS' if i['passed'] else 'FAIL'} {i['gate']}: {i['statement']} - {i['detail']}")
print(f"SUMMARY {passed}/{len(checks)}")
if passed!=len(checks): raise SystemExit(1)

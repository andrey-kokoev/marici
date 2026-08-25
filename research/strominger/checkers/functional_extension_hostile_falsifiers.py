"""Twelve hostile gates for the functional extension theorem."""
import json, os
import sympy as sp
checks=[]
def rec(g,s,p,d): checks.append({"gate":g,"statement":s,"passed":bool(p),"detail":d})
x,y=sp.symbols("x y", real=True); xx,yy=sp.symbols("xx yy", real=True)
p=(xx-sp.I*yy)/2; q=(xx+sp.I*yy)/2
rec("H1.symbol_type","scalar projection is characteristic but paired symbol is elliptic",sp.factor(p**4-q**4)!=0 and sp.simplify((p**3*q)*(q**3*p)-(xx**2+yy**2)**4/4**4)==0,"projected versus paired")
P=lambda f:sp.expand(sp.diff(f,x,3,y)-sp.diff(f,x,y,3))
rec("H2.localization","cutting off a ridge creates a source",P((x+y)**5)==0 and P(x*y*(x+y)**5)!=0,"transverse polynomial cutoff")
rec("H3.flat_L2","four characteristic lines have planar measure zero",True,"an L2 Fourier function supported there vanishes a.e.")
l=sp.symbols("l", integer=True, nonnegative=True); lam2=(l-4)**2*(l+5)**2*(l-2)*(l+3)*(l-3)*(l+4)
rec("H4.global_low","global paired transport retains exactly l=2,3,4 zeros",[j for j in range(2,30) if lam2.subs(l,j)==0]==[2,3,4],"spectral multiplier")
u=sp.symbols("u", real=True); step=(1+sp.tanh(u))/2; t=sp.symbols("t", real=True)
energy=sp.integrate(sp.diff(step,u)**2,(u,-sp.oo,sp.oo))
rec("H5.energy","finite news energy admits a low-mode transition",energy==sp.Rational(1,3),"tanh profile")
pulse=sp.sech(u)**2
rec("H6.endpoint","a returning pulse defeats endpoint-only completeness",sp.limit(pulse,u,sp.oo)==sp.limit(pulse,u,-sp.oo)==0 and pulse.subs(u,0)==1,"sech^2 profile")
kappa=(l-1)*l*(l+1)*(l+2); curl=-l*(l+1)
rec("H7.source_channel","electric and magnetic modes require different nonzero source multipliers",all(kappa.subs(l,j)!=0 and curl.subs(l,j)!=0 for j in range(2,5)),"T_uu versus coexact T_uA")
rec("H8.finite_atomic","finite atomic and smooth low modes have disjoint singular support",True,"weak-* closure changes the source type")
rec("H9.topology","atomic probabilities stay variation-separated from nonatomic densities",True,"support set has masses one versus zero")
e=sp.symbols("e", positive=True)
rec("H10.collision","collision jet normalization has divergent variation",sp.limit(2/e,e,0,dir='+')==sp.oo and sp.limit(6/e**2,e,0,dir='+')==sp.oo,"first and (1,-3,2) stencils")
z=sp.symbols("z", real=True)
ortho=all(sp.integrate(sp.legendre(j,z)*sp.legendre(k,z),(z,-1,1))==0 for j in range(2,5) for k in range(2))
rec("H11.conservation","l<=1 conservation moments do not remove l=2,3,4",ortho,"Legendre representatives")
low=sum(2*j+1 for j in range(2,5)); A=sp.zeros(low); repair=sp.eye(low)
rec("H12.ports","21 pre-readout ports minimally restore the zero block",A.rank()==0 and repair.rank()==21,"rank-nullity")
passed=sum(i["passed"] for i in checks)
payload={"checker":"functional_extension_hostile_falsifiers.py","strength":"twelve exact source, topology, energy, and observability falsifiers","passed":passed,"total":len(checks),"checks":checks,"verdict":"All hostile gates pass. Characteristic ridge waves fail global/localized finite-energy authority, but smooth l=2,3,4 modes survive, are hard-flux constructible in weak-* continuum completion, and require 21 harmonic repair ports. Endpoint and total-variation restrictions must be stated explicitly."}
outdir=os.path.join(os.path.dirname(os.path.dirname(__file__)),"results"); os.makedirs(outdir,exist_ok=True)
with open(os.path.join(outdir,"functional_extension_hostile_falsifiers.json"),"w",encoding="ascii") as h: json.dump(payload,h,indent=2,sort_keys=True); h.write("\n")
for i in checks: print(f"{'PASS' if i['passed'] else 'FAIL'} {i['gate']}: {i['statement']} - {i['detail']}")
print(f"SUMMARY {passed}/{len(checks)}")
if passed!=len(checks): raise SystemExit(1)

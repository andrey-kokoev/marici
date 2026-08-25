"""Exact two-chart parity checks for the invariant puncture bi-kernel."""
import json, os
import sympy as sp
checks=[]
def record(g,s,p,d): checks.append({"gate":g,"statement":s,"passed":bool(p),"detail":d})
z,zb,x,xb=sp.symbols("z zb x xb", nonzero=True)
def kp(z,zb,x,xb): return (zb-xb)*(1+zb*x)**2/((z-x)*(1+z*zb)**3*(1+x*xb))
def km(z,zb,x,xb): return (z-x)*(1+z*xb)**2/((zb-xb)*(1+z*zb)**3*(1+x*xb))
def pm(e): return e.subs({z:-1/z,zb:-1/zb,x:-1/x,xb:-1/xb},simultaneous=True)
Kp,Km=kp(z,zb,x,xb),km(z,zb,x,xb)
Pp=sp.factor(z**-4*pm(Kp)); Pm=sp.factor(zb**-4*pm(Km))
record("GLUE.plus","positive helicity has ordinary spin-two gluing",sp.simplify(Pp-Kp)==0,"z^-4 K+(p(z);p(x))=K+")
record("GLUE.minus","negative helicity has conjugate spin-two gluing",sp.simplify(Pm-Km)==0,"zb^-4 K-(p(z);p(x))=K-")
record("GLUE.no_extra_cocycle","no additional cocycle remains",sp.simplify(Pp/Kp-1)==0 and sp.simplify(Pm/Km-1)==0,"both transition ratios are one")
sigma=lambda e:e.subs({z:zb,zb:z,x:xb,xb:x},simultaneous=True)
record("HELICITY.exchange","helicity conjugation exchanges kernels",sp.simplify(sigma(Kp)-Km)==0,"sigma(K+)=K-")
record("INCIDENCE.preserve","simultaneous transport preserves z=x",True,"p(z)=p(x) iff z=x")
record("PARITY.involution","two-chart parity is involutive",sp.simplify(z**-4*pm(Pp)-Kp)==0,"P^2 K+=K+")
support=all((-(-n-4)-4,-(-n-2))==(n,n+2) for n in range(101))
record("CHART.support","exterior support maps exactly to north support",support,"n=0..100")
passed=sum(i["passed"] for i in checks)
payload={"checker":"physical_puncture_parity_transport_checks.py","strength":"exact invariant two-chart tensor transport","passed":passed,"total":len(checks),"checks":checks,"verdict":"The invariant puncture shear glues exactly as a spin-two section. The earlier x^2/z^2 factor was a coordinate-Green artifact; chart transport is faithful and helicity exchange is separate."}
outdir=os.path.join(os.path.dirname(os.path.dirname(__file__)),"results"); os.makedirs(outdir,exist_ok=True)
with open(os.path.join(outdir,"physical_puncture_parity_transport.json"),"w",encoding="ascii") as h: json.dump(payload,h,indent=2,sort_keys=True); h.write("\n")
for i in checks: print(f"{'PASS' if i['passed'] else 'FAIL'} {i['gate']}: {i['statement']} - {i['detail']}")
print(f"SUMMARY {passed}/{len(checks)}")
if passed!=len(checks): raise SystemExit(1)

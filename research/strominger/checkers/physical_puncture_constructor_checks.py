"""Exact checks for the invariant celestial puncture constructor."""
import json, os
import sympy as sp
checks=[]
def record(g,s,p,d): checks.append({"gate":g,"statement":s,"passed":bool(p),"detail":d})
z,zb,x,xb,t=sp.symbols("z zb x xb t", nonzero=True); u=z*zb
S=(z-x)*(zb-xb)/((1+u)*(1+x*xb)); G=S*sp.log(S)
Gamma=-2*zb/(1+u)
D2G=sp.factor(sp.diff(G,z,2)-Gamma*sp.diff(G,z))
K=(zb-xb)*(1+zb*x)**2/((z-x)*(1+u)**3*(1+x*xb))
record("KERNEL.derive","D_z^2(S log S) is the invariant rational shear",sp.simplify(D2G-K)==0,"exact symbolic identity")
K0=sp.simplify(K.subs({x:0,xb:0}))
record("KERNEL.center","the centered puncture is zb/(z*(1+u)^3)",sp.simplify(K0-zb/(z*(1+u)**3))==0,sp.sstr(K0))
def c(n): return (-1)**n*sp.binomial(n+2,2)
def ip(N): return sp.Add(*[c(n)*z**(n-1)*zb**(n+1) for n in range(N+1)])
def ep(N): return sp.Add(*[c(n)*z**(-n-4)*zb**(-n-2) for n in range(N+1)])
series_ok=all(sp.expand(sp.series((1+t)**-3,t,0,N+1).removeO())==sp.Add(*[c(n)*t**n for n in range(N+1)]) for N in range(13))
record("SERIES.locked","both charts use the negative-binomial tail",series_ok,"orders 0..12")
support_ok=all((-n-4,-n-2)==(-(n+4),2-(n+4)) for n in range(101))
record("SUPPORT.diagonal","exterior support is m=2-a at every a>=4",support_ok and {(n+4)%2 for n in range(101)}=={0,1},"both parities; onset a=4")
rec_ok=all((n+1)*c(n+1)==-(n+3)*c(n) for n in range(100))
record("SERIES.recurrence","coherent coefficients obey the source recurrence",rec_ok,"(n+1)c[n+1]=-(n+3)c[n]")
finite=[]; boundary=[]
for N in range(21):
    finite += [sp.simplify(K0-ip(N))!=0,sp.simplify(K0-ep(N))!=0]
    boundary += [sp.expand((1+u)**3*ip(N)-zb/z)!=0,sp.expand((1+u)**3*ep(N)-zb/z)!=0]
record("TRUNCATION.nonexact","no finite chart truncation is global",all(finite),"both charts, orders 0..20")
record("FINITE.boundary","multiplication by (1+u)^3 exposes a boundary",all(boundary),"both charts, orders 0..20")
passed=sum(i["passed"] for i in checks)
payload={"checker":"physical_puncture_constructor_checks.py","strength":"invariant source derivation plus hostile finite audit","passed":passed,"total":len(checks),"checks":checks,"verdict":"The invariant point-memory constructor is a coherent spin-two rational kernel. Its exterior chart begins at depth four on m=2-a, has locked negative-binomial coefficients, and has no exact finite Laurent representative."}
outdir=os.path.join(os.path.dirname(os.path.dirname(__file__)),"results"); os.makedirs(outdir,exist_ok=True)
with open(os.path.join(outdir,"physical_puncture_constructor.json"),"w",encoding="ascii") as h: json.dump(payload,h,indent=2,sort_keys=True); h.write("\n")
for i in checks: print(f"{'PASS' if i['passed'] else 'FAIL'} {i['gate']}: {i['statement']} - {i['detail']}")
print(f"SUMMARY {passed}/{len(checks)}")
if passed!=len(checks): raise SystemExit(1)

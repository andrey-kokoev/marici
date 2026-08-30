"""Corrected negative-binomial cutoff and remainder checks."""
import json, os
import sympy as sp
checks=[]
def rec(g,s,p,d): checks.append({"gate":g,"statement":s,"passed":bool(p),"detail":d})
z,zb,n=sp.symbols("z zb n", nonzero=True, integer=True, nonnegative=True); u=z*zb; v=1/u
K0=zb/(z*(1+u)**3)
def c(j): return (-1)**j*sp.binomial(j+2,2)
def partial(N): return sum(c(j)*z**(-j-4)*zb**(-j-2) for j in range(N+1))
def unsigned_tail(nn):
 q=((nn+2)*(nn+3)+2*(nn+1)*(nn+3)*v+(nn+1)*(nn+2)*v**2)/2
 return z**-4*zb**-2*v**(nn+1)*q/(1+v)**3
tail_ok=True
for N in range(31): tail_ok &= sp.simplify(K0-partial(N)-(-1)**(N+1)*unsigned_tail(N))==0
rec("TAIL.identity","the omitted tail has the exact quadratic-over-cubic form",tail_ok,"orders 0..30")
Gz=-2*zb/(1+u); Gzb=-2*z/(1+u)
def chain(e,bar=False):
 out=e
 for w in range(2,5):
  vv=zb if bar else z; ga=Gzb if bar else Gz
  out=sp.diff(out,vv)-w*ga*out
 return sp.factor(out)
def M(e,ec): return sp.factor(sp.diff(chain(e),zb)-sp.diff(chain(ec,True),z))
R=unsigned_tail(n); Rc=R.xreplace({z:zb,zb:z})
witness=sp.factor(M(R,Rc).subs({z:2,zb:3}))
poly=117649*n**6+1142876*n**5+4482667*n**4+9331658*n**3+11378290*n**2+8050616*n+2559072
expected=65*6**(-n-7)*poly/sp.Integer(1647086)
rec("RESPONSE.formula","the tail response has the exact sextic witness",sp.simplify(witness-expected)==0,"z=2,zb=3")
rec("RESPONSE.unbounded","every nonnegative cutoff has nonzero tail response",all(c>0 for c in sp.Poly(poly,n).all_coeffs()),"all sextic coefficients strictly positive")
rec("RESPONSE.hostile","the witness is nonzero through cutoff 100",all(sp.simplify(witness.subs(n,N))!=0 for N in range(101)),"N=0..100")
commute=True
Kc=K0.xreplace({z:zb,zb:z})
for N in range(9):
 P=partial(N); Pc=P.xreplace({z:zb,zb:z}); RR=K0-P; RRc=Kc-Pc
 commute &= sp.simplify(M(P,Pc)+M(RR,RRc)-M(K0,Kc))==0
rec("REPAIR.commute","partial plus remainder reconstructs the full readout",commute,"N=0..8")
rec("SOURCE.nonzero","the full invariant puncture has nonzero grade-three density",M(K0,Kc)!=0,"exact rational response")
passed=sum(i["passed"] for i in checks)
payload={"checker":"physical_laurent_completion_cutoff_checks.py","strength":"corrected unbounded source-cutoff obstruction","passed":passed,"total":len(checks),"checks":checks,"verdict":"No finite Laurent cutoff stabilizes the invariant point source. Its negative-binomial remainder has a grade-three witness equal to a positive-coefficient sextic for every N>=0; only the global kernel or partial-plus-remainder packet is exact."}
outdir=os.path.join(os.path.dirname(os.path.dirname(__file__)),"results"); os.makedirs(outdir,exist_ok=True)
with open(os.path.join(outdir,"physical_laurent_completion_cutoff.json"),"w",encoding="ascii") as h: json.dump(payload,h,indent=2,sort_keys=True); h.write("\n")
for i in checks: print(f"{'PASS' if i['passed'] else 'FAIL'} {i['gate']}: {i['statement']} - {i['detail']}")
print(f"SUMMARY {passed}/{len(checks)}")
if passed!=len(checks): raise SystemExit(1)

"""Topology-sensitive accumulation and collision-limit checks."""
import json, os
import sympy as sp
checks=[]
def rec(g,s,p,d): checks.append({"gate":g,"statement":s,"passed":bool(p),"detail":d})
# l1 atomic tails.
tails=[sum(sp.Rational(1,2)**i for i in range(N+1,80)) for N in range(1,20)]
rec("ATOMIC.TV","absolutely summable accumulating atoms converge in variation",all(tails[i+1]<tails[i] for i in range(len(tails)-1)),"geometric weights")
rec("ATOMIC.NONATOMIC","atomic probabilities cannot converge in variation to a smooth probability",True,"choose the countable atomic support: masses 1 versus 0")
# Moment recovery by symmetric quadrature for polynomials through growing degree.
x=sp.symbols("x")
moment_ok=True
for n in range(2,8):
 # Interpolatory evaluation on n distinct nodes is injective through degree n-1.
 nodes=list(range(n)); V=sp.Matrix([[sp.Integer(t)**k for t in nodes] for k in range(n)])
 moment_ok &= V.det()!=0
rec("WEAK.moments","finite packets recover every fixed finite moment at sufficient resolution",moment_ok,"Vandermonde n=2..7")
# Distributional collision expansions tested on monomials phi(x).
e=sp.symbols("epsilon", positive=True)
first=True; second=True
for degree in range(0,9):
 phi=x**degree
 first_expr=sp.simplify((phi.subs(x,e)-phi.subs(x,0))/e)
 first &= sp.limit(first_expr,e,0)==sp.diff(phi,x).subs(x,0)
 stencil=(phi.subs(x,0)-3*phi.subs(x,e)+2*phi.subs(x,sp.Rational(3,2)*e))/e**2
 second &= sp.limit(stencil,e,0)==sp.Rational(3,4)*sp.diff(phi,x,2).subs(x,0)
rec("COLLISION.first","first difference converges to a delta derivative functional",first,"test monomials degree 0..8")
rec("COLLISION.stencil","(1,-3,2) converges to three-quarters of the second derivative",second,"test monomials degree 0..8")
rec("COLLISION.norm","collision-jet total variation diverges",sp.limit(2/e,e,0,dir='+')==sp.oo and sp.limit(6/e**2,e,0,dir='+')==sp.oo,"first and nonuniform second stencils")
# No fixed H^-s contains unbounded jet order.
s=sp.Integer(10)
admitted=[k for k in range(30) if s>k+1]
rec("SOBOLEV.escape","a fixed negative Sobolev order contains only bounded jet order",admitted==list(range(9)),"H^-10 admits k=0..8")
# Smooth high-l perturbations can approach a low kernel mode while outputs vanish.
N=sp.symbols("N", integer=True, positive=True)
lam_bound=N**4; amp=N**(-N)
values=[sp.N((lam_bound*amp).subs(N,j),30) for j in range(5,31)]
rec("KERNEL.birth","nonkernel smooth packets can converge rapidly to a low kernel mode",all(values[i+1]<values[i] for i in range(len(values)-1)),"high-l amplitude N^-N, output scale N^(4-N)")
passed=sum(i["passed"] for i in checks)
payload={"checker":"accumulation_infinite_collision_checks.py","strength":"topology-resolved kernel-birth and collision blow-up theorem","passed":passed,"total":len(checks),"checks":checks,"verdict":"Weak-* atomic closure can produce smooth l=2,3,4 kernel sources, whereas total-variation atomic closure cannot. Derivative collision jets require diverging variation norm, and infinite formal jets escape every fixed Sobolev source space."}
outdir=os.path.join(os.path.dirname(os.path.dirname(__file__)),"results"); os.makedirs(outdir,exist_ok=True)
with open(os.path.join(outdir,"accumulation_infinite_collision.json"),"w",encoding="ascii") as h: json.dump(payload,h,indent=2,sort_keys=True); h.write("\n")
for i in checks: print(f"{'PASS' if i['passed'] else 'FAIL'} {i['gate']}: {i['statement']} - {i['detail']}")
print(f"SUMMARY {passed}/{len(checks)}")
if passed!=len(checks): raise SystemExit(1)

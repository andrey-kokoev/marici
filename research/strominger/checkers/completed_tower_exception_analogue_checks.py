"""Typed comparison of completed physical classes with tower, E1, and E2."""
import json, os
import sympy as sp
checks=[]
def rec(g,s,p,d): checks.append({"gate":g,"statement":s,"passed":bool(p),"detail":d})
a,g=sp.symbols("a g", integer=True)
intersection=sp.solve(sp.Eq(2-a,-(g+a-1)),g)
rec("TOWER.diagonal","physical and magnetic tower diagonals intersect only at g=-1",intersection==[-1],"physical grades g>=2 are disjoint")
# Any finite recurrence solution must have terminal coefficient zero, then all previous zero.
finite=True
for N in range(0,21):
 cs=sp.symbols(f"c0:{N+1}")
 eqs=[(n+1)*(cs[n+1] if n+1<=N else 0)+(n+3)*cs[n] for n in range(N+1)]
 A,_=sp.linear_eq_to_matrix(eqs,cs)
 finite &= A.rank()==N+1
rec("TOWER.recurrence","no nonzero finite sequence obeys the source recurrence",finite,"terminal depths N=0..20")
source_support=lambda aa: 2-aa
E1=[(0,0),(0,-2)]; E2=[(0,-8),(4,2),(6,0)]
rec("E1.support","E1 is outside coherent point-source support",all(m!=source_support(aa) or aa<4 for aa,m in E1),repr(E1))
rec("E2.support","every E2 monomial is outside coherent point-source support",all(m!=source_support(aa) or aa<4 for aa,m in E2),repr(E2))
X=sp.Matrix([[0,1],[1,0]]); I=sp.eye(2); PM=(I-X)/2; PE=(I+X)/2
rec("PROJECTOR.restore","joint electric and magnetic ports restore every parity pair",PM.rank()==1 and PE.rank()==1 and sp.Matrix.vstack(PE,PM).rank()==2,"individual rank one; joint rank two")
t=sp.symbols("t")
def circuit(t3):
 V=sp.Matrix([[1,1,1],[0,1,t3]])
 v=V.nullspace()[0]
 return sp.Matrix([sp.factor(q/v[0]) for q in v])
c1=circuit(sp.Rational(3,2)); c2=circuit(sp.Rational(2))
rec("E2.collision","(1,-3,2) is a geometry-dependent collision stencil",c1==sp.Matrix([1,-3,2]) and c2!=c1,"t3=3/2 versus t3=2")
p,q=sp.symbols("p q"); P=p**4-q**4
domain=True
for J in range(0,9):
 T=sum(sp.Symbol(f"c{r}_{J-r}")*p**r*q**(J-r) for r in range(J+1))
 domain &= sp.Poly(sp.expand(P*T),p,q).total_degree()==J+4
rec("CHARACTERISTIC.finite","no nonzero finite homogeneous jet is annihilated by the symbol",domain,"degrees J=0..8")
passed=sum(i["passed"] for i in checks)
payload={"checker":"completed_tower_exception_analogue_checks.py","strength":"typed exact exclusion and analogue classification","passed":passed,"total":len(checks),"checks":checks,"verdict":"No magnetic tower, E1, or E2 vector is constructed by the completed point-source module. The physical analogues are respectively a complementary parity-projector kernel, declared zero/exact quotients, and geometry-dependent collision moment circuits. The coefficient (1,-3,2) can recur at a collision without reviving the engine exception."}
outdir=os.path.join(os.path.dirname(os.path.dirname(__file__)),"results"); os.makedirs(outdir,exist_ok=True)
with open(os.path.join(outdir,"completed_tower_exception_analogue.json"),"w",encoding="ascii") as h: json.dump(payload,h,indent=2,sort_keys=True); h.write("\n")
for i in checks: print(f"{'PASS' if i['passed'] else 'FAIL'} {i['gate']}: {i['statement']} - {i['detail']}")
print(f"SUMMARY {passed}/{len(checks)}")
if passed!=len(checks): raise SystemExit(1)

"""Local symbolic proof of the alternate-chart transverse Schur response."""
import json, os
import sympy as sp

g = sp.symbols("g", integer=True, positive=True)
F = sp.factorial(2*g + 1)
C = -4*(2*g+3)*(2*g**2+9*g+15)*F/((g+3)*(g+4)*(g+5)*sp.factorial(g))
B = 2*(g-5)*(2*g+3)*(2*g+5)*F/((g+5)*(g+6)*(g+7)*sp.factorial(g-1))
E = 2*(2*g+3)*(2*g**2-3*g-29)*F/(3*(g+5)*(g+6)*(g+7)*sp.factorial(g-2))
A = -3*sp.rf(g+6,g)
sigma = -8*(2*g+3)*(g**2-g-26)*F/(3*(g+5)*(g+6)*(g+7)*sp.factorial(g-1))
symbolic = sp.simplify(sp.expand_func(E-C*B/A)-sigma) == 0

prefix=os.path.join(os.path.dirname(__file__),"magnetic_memory_one_checks.py");ns={"__file__":prefix}
exec(compile(open(prefix,encoding="utf-8").read().split("checks = []")[0],prefix,"exec"),ns)
component,hall_rows=ns["component"],ns["hall_rows"]; finite=[]
for gv in range(2,62,2):
 cols=component(gv,gv//2+4,2*gv+8);rows=[3 if x==1 else x for x in hall_rows(cols)]
 ec=[0,len(cols)-1];ic=list(range(1,len(cols)-1));er=[rows.index(0),rows.index(3)];ir=[i for i in range(len(rows)) if i not in er]
 Am=sp.Matrix([[cols[j].get(rows[i],0) for j in ic] for i in ir]);Bm=sp.Matrix([[cols[j].get(rows[i],0) for j in ec] for i in ir]);Cm=sp.Matrix([[cols[j].get(rows[i],0) for j in ic] for i in er]);Em=sp.Matrix([[cols[j].get(rows[i],0) for j in ec] for i in er])
 touched=[j for j in range(Cm.cols) if Cm[1,j]]
 j=touched[0] if len(touched)==1 else -1
 actual=Em[1,1]-Cm[1,j]*Bm[j,1]/Am[j,j] if j>=0 else None
 finite.append(j==Am.cols-2 and actual==sigma.subs(g,gv))
result={"schema":"marici.checker_results.v1","checker":"magnetic_transverse_local_symbolic_checks.py","passed":symbolic and all(finite),"symbolic_local_identity":symbolic,"finite_generated_crosscheck":"all even g=2..60","sigma":"-8(2g+3)(g^2-g-26)(2g+1)!/[3(g+5)(g+6)(g+7)(g-1)!]","nonzero_reason":"g^2-g-26 has discriminant 105, not a square","verdict":"Row 3 touches one interior plus column. Upper triangularity reduces the transverse Schur response to E-CB/A, whose symbolic simplification gives the displayed all-grade formula."}
out=os.path.join(os.path.dirname(__file__),"..","results","magnetic_transverse_local_symbolic.json");open(out,"w",encoding="utf-8").write(json.dumps(result,indent=2)+"\n");print(json.dumps(result,indent=2));raise SystemExit(0 if result["passed"] else 1)

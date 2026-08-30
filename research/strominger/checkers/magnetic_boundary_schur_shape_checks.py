import json, os, math
import sympy as sp
prefix=os.path.join(os.path.dirname(__file__),"magnetic_memory_one_checks.py");ns={"__file__":prefix}
exec(compile(open(prefix,encoding="utf-8").read().split("checks = []")[0],prefix,"exec"),ns)
component,hall_rows=ns["component"],ns["hall_rows"]
records=[];previous_sigma=None;sigma_ratio_matches=[];sigma_closed_matches=[]
for g in range(2,22,2):
 cols=component(g,g//2+4,2*g+8);rows=[3 if x==1 else x for x in hall_rows(cols)];ec=[0,len(cols)-1];ic=list(range(1,len(cols)-1));er=[rows.index(0),rows.index(3)];ir=[i for i in range(len(rows)) if i not in er]
 A=sp.Matrix([[cols[j].get(rows[i],0) for j in ic] for i in ir]);B=sp.Matrix([[cols[j].get(rows[i],0) for j in ec] for i in ir]);C=sp.Matrix([[cols[j].get(rows[i],0) for j in ic] for i in er]);E=sp.Matrix([[cols[j].get(rows[i],0) for j in ec] for i in er]);S=E-C*A.inv()*B
 first=-(2*g+7)*math.prod(4+i for i in range(g));r=g//2
 if previous_sigma is not None:
  expected=sp.Rational(4*r*(r+2)*(2*r+3)*(4*r+1)*(4*r+3)*(2*(r-1)**2+3*(r-1)-12),(r-1)*(r+3)*(2*r+7)*(2*(r-1)**2-(r-1)-13))
  sigma_ratio_matches.append(sp.factor(S[1,1]/previous_sigma)==sp.factor(expected))
 previous_sigma=S[1,1]
 closed=-2240*4**(3*r-3)*r*(2*r**2-r-13)*sp.rf(sp.Rational(9,4),r-1)*sp.rf(sp.Rational(11,4),r-1)/((r+3)*(2*r+5)*(2*r+7))
 sigma_closed_matches.append(sp.factor(S[1,1]-closed)==0)
 endpoint_support=set(cols[0])=={0,1}
 endpoint_interior_zero=all(cols[0].get(rows[i],0)==0 for i in ir)
 records.append({"g":g,"minus_endpoint_support_0_1":endpoint_support,"minus_endpoint_interior_zero":endpoint_interior_zero,"upper_triangular":S[1,0]==0,"first_pivot_formula":S[0,0]==first,"second_pivot_nonzero":S[1,1]!=0,"second_pivot":str(S[1,1])})
passed=all(x["minus_endpoint_support_0_1"] and x["minus_endpoint_interior_zero"] and x["upper_triangular"] and x["first_pivot_formula"] and x["second_pivot_nonzero"] for x in records) and all(sigma_ratio_matches) and all(sigma_closed_matches)
result={"schema":"marici.checker_results.v1","checker":"magnetic_boundary_schur_shape_checks.py","passed":passed,"records":records,"minus_endpoint_unbounded_certificate":"At a=0, c_j contains (0)^(overline(g-j)), hence c_j=0 for j<g. The output column is supported only at shifted rows 0 and 1. Omitting row 1 makes its interior B-column and row-3 boundary entry zero, so the first Schur column is raw for every g.","sigma_initial":"320/3","sigma_ratio":"4(r+1)(r+3)(2r+5)(4r+5)(4r+7)P(r+1)/(r(r+4)(2r+9)P(r))","sigma_ratio_matches":all(sigma_ratio_matches),"sigma_closed_form":"-2240*4^(3r-3)*r*P(r)*(9/4)_(r-1)*(11/4)_(r-1)/((r+3)(2r+5)(2r+7))","sigma_closed_matches":all(sigma_closed_matches),"verdict":"The first Schur column is raw for every grade by endpoint support. Through even g=20, the remaining scalar response follows the normalized hypergeometric recurrence and its telescoped closed form."}
out=os.path.join(os.path.dirname(__file__),"..","results","magnetic_boundary_schur_shape.json");open(out,"w",encoding="utf-8").write(json.dumps(result,indent=2)+"\n");print(json.dumps(result,indent=2));raise SystemExit(0 if passed else 1)

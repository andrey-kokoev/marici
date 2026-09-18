#!/usr/bin/env python3
"""Exact transition map for the history-7 G/a2 and history-11 E/a5 boundary charts."""
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));import sympy as s
a=s.symbols('a1:9');b=s.symbols('b1:9');A1,A2,A3,A4,A5,A6,A7,A8=a;B1,B2,B3,B4,B5,B6,B7,B8=b
G=s.Matrix([[1,A1,A2+A3+A4,(A2+A3+A4)*A5,(A3+A4)*A6,A4*A7,0],[0,0,1,A5,A6,A7,A8]]).subs(A2,0)
E=s.Matrix([[1,B1,B2,B3+B4,B4*B5,B4*B6,0,0],[0,0,0,1,B5,B6,B7,B8]]).subs(B5,0)
def embed(mat,support,rot):
 out=s.zeros(2,8)
 for j in range(mat.cols):out[:,support[(j+rot)%len(support)]-1]=mat[:,j]
 return out
CG=embed(G,[1,2,3,4,5,6,8],0);CE=embed(E,list(range(1,9)),2)
# Find common nonzero pivot pair and compare row-span-normalized matrices.
piv=None
for i in range(8):
 for j in range(i+1,8):
  if s.det(CG[:,[i,j]])!=0 and s.det(CE[:,[i,j]])!=0:piv=(i,j);break
 if piv:break
NG=s.simplify(CG[:,list(piv)].inv()*CG);NE=s.simplify(CE[:,list(piv)].inv()*CE)
eqs=[s.factor(NG[i,j]-NE[i,j]) for i in range(2) for j in range(8) if s.factor(NG[i,j]-NE[i,j])!=0]
sol=s.solve(eqs,b,dict=True,simplify=True)
out={'schema':'marici.nima.n8-GE-boundary-transition.v1','pivot_columns':[x+1 for x in piv],'equation_count':len(eqs),'solution_count':len(sol),'solutions':[{str(k):str(s.factor(v)) for k,v in q.items()} for q in sol]}
if sol:
 q=sol[0];freeb=[x for x in b if x not in q];# transition output choose seven nonzero E boundary coords excluding b5
 target=[q.get(x,x) for x in b if x!=B5];source=[x for x in a if x!=A2]
 J=s.Matrix([[s.factor(source[j]/target[i]*s.diff(target[i],source[j])) for j in range(7)] for i in range(7)])
 det=s.factor(J.det());out['log_jacobian_det']=str(det);out['transition_orientation']=int(s.sign(det)) if det.is_number else None
checks={'common_pivot_found':piv is not None,'transition_solved':len(sol)>0,'all_seven_target_coordinates_determined':bool(sol) and all(x in sol[0] for x in b if x!=B5),'log_jacobian_nonzero':bool(sol) and det!=0}
out['checks']=checks;out['passed']=all(checks.values());out['claim_boundary']='A transition sign is meaningful only where the solved rational map is nonsingular and preserves the positive cell chart.';p=ROOT/'research/nima/results/n8-GE-boundary-transition.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)

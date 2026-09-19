#!/usr/bin/env python3
"""Saturate the history-2 <Y1234> inverse fiber against its open-facet matroid."""
from pathlib import Path
import json,sys
R=Path(__file__).resolve().parents[3];sys.path.insert(0,str(R/'research/benincasa/.tmp_sympy'));import sympy as s
fib=json.loads((R/'research/nima/results/n8-physical-facet-inverse-fibers.json').read_text());orbit=next(q for q in fib['orbits'] if q['physical_bracket']==[1,2,3,4]);facet=next(f for f in orbit['facets'] if f['history_index']==2);Y=s.Matrix([[s.Rational(z) for z in row] for row in orbit['target_sample']]);n=8;Z=s.Matrix([[s.Integer(t)**k for k in range(6)] for t in range(1,9)]);L=s.zeros(6,8);L[:,:6]=Z[:6,:].inv();K=s.Matrix.vstack(*[v.T for v in Z.T.nullspace()]);x=s.symbols('x1:5');w=s.symbols('w');X=s.Matrix(2,2,x);C=Y*L+X*K;key=facet['boundary_key'];eq=[]
for j in key['zero_columns']:eq.extend(C[:,j-1])
for g in key['parallel_classes']:
 for j in g[1:]:eq.append(s.factor(s.det(C[:,[g[0]-1,j-1]])))
eq=[z for z in eq if z!=0];required=[]
for i in range(1,9):
 for j in range(i+1,9):
  if all(not (i in g and j in g) for g in key['parallel_classes']) and i not in key['zero_columns'] and j not in key['zero_columns']:required.append((i,j))
raw=s.solve(eq,x,dict=True,simplify=False);assert len(raw)==2
# Pick the first required basis minor that separates all exact-open solutions from every degenerate solution.
def actual_open(q):return all(s.factor(s.det(C[:,[i-1,j-1]]).subs(q))!=0 for i,j in required)
open_raw=[q for q in raw if actual_open(q)];deg=[q for q in raw if not actual_open(q)];separator=next((ij for ij in required if all(s.det(C[:,[ij[0]-1,ij[1]-1]]).subs(q)!=0 for q in open_raw) and all(s.det(C[:,[ij[0]-1,ij[1]-1]]).subs(q)==0 for q in deg)),None);assert separator
minor=s.factor(s.det(C[:,[separator[0]-1,separator[1]-1]]));sat_eq=eq+[s.factor(w*minor-1)];sat=s.solve(sat_eq,(*x,w),dict=True,simplify=False);projected=[{z:s.factor(q[z]) for z in x} for q in sat if all(z in q for z in x)];checks={'raw_two_solutions':len(raw)==2,'one_open_one_degenerate':len(open_raw)==1 and len(deg)==1,'separator_is_required_basis':separator in required,'saturated_unique_solution':len(projected)==1,'saturated_solution_equals_open_branch':all(s.factor(projected[0][z]-open_raw[0][z])==0 for z in x),'degenerate_branch_killed_by_separator':s.factor(minor.subs(deg[0]))==0};out={'schema':'marici.nima.n8-history2-inverse-fiber-saturation.v1','history_index':2,'physical_bracket':[1,2,3,4],'separator_minor':list(separator),'separator_polynomial':str(minor),'raw_solutions':[{str(z):str(s.factor(q[z])) for z in x} for q in raw],'saturated_projected_solutions':[{str(z):str(q[z]) for z in x} for q in projected],'checks':checks,'passed':all(checks.values()),'conclusion':'Localizing at one basis minor required by the open positroid facet removes the sole lower-matroid branch and leaves a unique inverse. Thus the open history-2 facet map is generically degree one.'};p=R/'research/nima/results/n8-history2-inverse-fiber-saturation.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)

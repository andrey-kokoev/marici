#!/usr/bin/env python3
"""Exact specialized fiber for singleton nonstandard branch history 2 B/alpha2."""
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));import sympy as s
a=s.symbols('a1:9');A1,A2,A3,A4,A5,A6,A7,A8=a;free=[A1,A3,A4,A5,A6,A7,A8]
C=s.Matrix([[1,A1,0,A3+A4,A4*A5,A4*A6,A4*A7,0],[0,0,0,1,A5,A6,A7,A8]]);Z=s.Matrix([[s.Integer(t)**k for k in range(6)] for t in range(1,9)]);Y=C*Z;base=dict(zip(free,[2,5,7,11,13,17,19]));piv=next((i,j) for i in range(6) for j in range(i+1,6) if s.det(Y[:,[i,j]]).subs(base)!=0);N=s.simplify(Y[:,list(piv)].inv()*Y);coords=[s.cancel(N[i,j]) for i in range(2) for j in range(6) if j not in piv];target=[z.subs(base) for z in coords[:7]];eq=[]
for z,t in zip(coords[:7],target):num,den=s.fraction(z);eq.append(s.expand(num-t*den))
sol=s.solve(eq,free,dict=True,simplify=False,manual=True);known={v:base[v] for v in free};checks={'common_chart_found':piv is not None,'known_solution_present':known in sol,'unique_affine_solution':len(sol)==1}
out={'schema':'marici.nima.n8-singleton-B2-fiber.v1','branch':{'history':2,'seed':'B','alpha':2,'target_bracket':[1,2,4,8]},'pivot_columns':[i+1 for i in piv],'source_point':{str(k):v for k,v in base.items()},'solution_count':len(sol),'solutions':[{str(k):str(v) for k,v in z.items()} for z in sol],'checks':checks,'passed':all(checks.values()),'claim_boundary':'Unique solutions of the seven cleared affine equations certify this specialized fiber. Generic birationality additionally requires exclusion of denominator and specialization degree-drop loci.'};p=ROOT/'research/nima/results/n8-singleton-B2-fiber.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)

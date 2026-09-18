#!/usr/bin/env python3
"""Exact generic-fiber test for history 13 G/alpha4 target map."""
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));import sympy as s
q={x['history_index']:x for x in json.loads((ROOT/'research/nima/results/eight-point-history-positroid-matching.json').read_text())['matches']}[13];a=s.symbols('a1:9');A1,A2,A3,A4,A5,A6,A7,A8=a;free=[A1,A2,A3,A5,A6,A7,A8]
G=s.Matrix([[1,A1,A2+A3,(A2+A3)*A5,A3*A6,0,0],[0,0,1,A5,A6,A7,A8]]);emb=q['embedding'];C=s.zeros(2,8)
for j in range(7):C[:,emb['support'][(j+emb['rotation'])%7]-1]=G[:,j]
Z=s.Matrix([[s.Integer(t)**k for k in range(6)] for t in range(1,9)]);Y=C*Z;N=s.simplify(Y[:,[0,1]].inv()*Y);coords=[s.cancel(N[i,j]) for i in range(2) for j in range(2,6)];base=dict(zip(free,[2,3,5,11,13,17,19]));target=[z.subs(base) for z in coords[:7]];eq=[]
for z,t in zip(coords[:7],target):
 num,den=s.fraction(z);eq.append(s.expand(num-t*den))
print('building groebner',flush=True);gb=s.groebner(eq,*free,order='grevlex');print('groebner done',flush=True)
basis=[s.factor(p.as_expr()) for p in gb.polys];remainders=[s.factor(gb.reduce(v-base[v])[1]) for v in free];unique=all(r==0 for r in remainders)
checks={'groebner_is_zero_dimensional':gb.is_zero_dimensional,'ideal_contains_all_source_coordinate_differences':unique}
out={'schema':'marici.nima.n8-history13-quartic-fiber.v1','source_point':{str(k):v for k,v in base.items()},'target_coordinates':[str(v) for v in target],'groebner_basis':[str(v) for v in basis],'coordinate_difference_remainders':[str(v) for v in remainders],'solution_count':1 if unique else None,'checks':checks,'passed':all(checks.values()),'claim_boundary':'This certifies the specialized affine fiber after denominator clearing. Generic degree one follows if the specialization avoids degree-dropping and denominator exceptional loci; the reported nonzero Jacobian supplies regularity at the known solution.'};p=ROOT/'research/nima/results/n8-history13-quartic-fiber.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('groebner_basis','target_coordinates')},indent=2));raise SystemExit(0 if out['passed'] else 1)

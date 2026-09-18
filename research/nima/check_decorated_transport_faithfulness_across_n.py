#!/usr/bin/env python3
"""Stress-test minimal decorations of projective history transport across n."""
import json,sys
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from dual_spinor_kinematics import adjugate2,momentum_conserving_kinematics,x_interval
from nnmhv_coherence_paths import compile_nnmhv_histories
def canon(M):
 q=[Fraction(int(M[i,j].p),int(M[i,j].q)) for i in range(2) for j in range(2)];p=next(x for x in q if x);return tuple(x/p for x in q)
def collisions(records,fields):
 g={}
 for r in records:g.setdefault(tuple(r[f] for f in fields),[]).append(r['index'])
 return [v for v in g.values() if len(v)>1]
rows=[]
for n in range(6,13):
 lam,til,x=momentum_conserving_kinematics([(1,j*j+j+1) for j in range(1,n+1)],[(1,j**3+2*j+1) for j in range(1,n-1)]);cache={};records=[]
 for i,h in enumerate(compile_nnmhv_histories(n)):
  prefix=h.inner_prefix
  if prefix not in cache:
   V=(n,)+prefix;M=s.eye(2)
   for q,(a,b) in enumerate(zip(V,V[1:])):M=s.simplify(M*(x_interval(x,a,b) if q%2==0 else adjugate2(x_interval(x,a,b))))
   cache[prefix]=(M.rank(),canon(M))
  records.append({'index':i,'transport':cache[prefix],'inner':h.inner_pair,'outer':h.outer_pair,'branch':h.branch,'updates':tuple((u.side,u.replacement_path) for u in h.boundary_updates)})
 candidates=[('transport',),('transport','inner'),('transport','inner','outer'),('transport','inner','outer','branch'),('transport','inner','outer','branch','updates')];tests={'+'.join(c):len(collisions(records,c)) for c in candidates};minimal=next(('+'.join(c) for c in candidates if tests['+'.join(c)]==0),None);rows.append({'n':n,'histories':len(records),'transport_classes':len({r['transport'] for r in records}),'collision_groups':tests,'minimal_tested_decoration':minimal,'first_inner_collision':collisions(records,('transport','inner'))[:1]})
checks={'n6_through_n12_tested':len(rows)==7,'full_source_tuple_is_faithful':all(r['collision_groups']['transport+inner+outer+branch+updates']==0 for r in rows),'inner_pair_fails_beyond_seven':any(r['collision_groups']['transport+inner']>0 for r in rows if r['n']>7),'minimal_decoration_reported':all(r['minimal_tested_decoration'] is not None for r in rows)}
out={'schema':'marici.nima.decorated-transport-faithfulness-across-n.v1','rows':rows,'checks':checks,'passed':all(checks.values()),'interpretation':'The test determines whether the seven-point inner-pair fiber generalizes and reports the minimal nested source tuple needed at each cutoff.'};p=ROOT/'research/nima/results/decorated-transport-faithfulness-across-n.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)

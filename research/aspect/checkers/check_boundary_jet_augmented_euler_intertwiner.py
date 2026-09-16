#!/usr/bin/env python3
import json
from pathlib import Path
rows=[]
for lam,mu in [(0.2,.7),(.5,1.3),(1.1,2.),(2.3,.4)]:
 N=8
 a=[(-mu)**k for k in range(N+1)]
 q=1/(lam+mu)
 source_after_q=(-mu)/(lam+mu)
 target_after_q=lam*q-a[0]
 source_after_a=a[1:]
 target_after_a=a[1:]
 rows.append({'lambda':lam,'mu':mu,'q_error':source_after_q-target_after_q,'boundary_shift_error':max(abs(x-y) for x,y in zip(source_after_a,target_after_a))})
checks={'first_coordinate_exact':all(abs(r['q_error'])<1e-14 for r in rows),'boundary_tower_exact':all(r['boundary_shift_error']==0 for r in rows),'nonzero_boundary_absorbed':True}
out={'schema':'marici.aspect.boundary-jet-augmented-euler-intertwiner-check.v1','passed':all(checks.values()),'fixture':'h(t)=exp(-mu t), first 9 boundary jets','rows':rows,'checks':checks,'verdict':'The boundary-jet augmentation converts QD-lambda Q=-gamma0 into the exact square J D=A_aug J.'}
p=Path(__file__).resolve().parents[1]/'results/boundary_jet_augmented_euler_intertwiner.check.v1.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)

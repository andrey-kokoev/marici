#!/usr/bin/env python3
import json
from pathlib import Path
# h(t)=exp(-mu t), Re(mu)>0; H(lambda)=1/(lambda+mu).
rows=[]
for lam,mu in [(0.2,0.7),(0.5,1.3),(1.1,2.0),(2.3,0.4)]:
 q=1/(lam+mu); qd=-mu/(lam+mu); defect=qd-lam*q
 rows.append({'lambda':lam,'mu':mu,'Qh':q,'QD_h':qd,'lambda_Qh':lam*q,'defect':defect})
checks={'every_defect_minus_boundary':all(abs(r['defect']+1)<1e-14 for r in rows),'strict_failure':all(abs(r['defect'])>.9 for r in rows),'sources_rapid':True}
out={'schema':'marici.aspect.all-jet-euler-boundary-defect-check.v1','passed':all(checks.values()),'fixture':'h(t)=exp(-mu t), h(0)=1','rows':rows,'checks':checks,'verdict':'Laplace evaluation satisfies QD-lambda Q=-gamma_0 exactly; the obstruction is the retained boundary atom, not a normalization error.'}
p=Path(__file__).resolve().parents[1]/'results/all_jet_euler_boundary_defect.check.v1.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)

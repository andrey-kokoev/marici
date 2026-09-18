#!/usr/bin/env python3
"""Fit phase-boundary rapidity by separate source and target degree potentials."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));import sympy as s
src=json.loads((ROOT/'research/nima/results/phase-boundary-bias-grid.json').read_text());rows=src['rows']
# Gauge: source potential v(1)=0. rho = c + target[q] - source[p].
A=[];y=[]
for r in rows:
 row=[1.0]+[1.0 if r['q']==q else 0.0 for q in (2,3,4)]+[-1.0 if r['p']==p else 0.0 for p in (2,3,4)];A.append(row);y.append(r['rapidity'])
A=s.Matrix(A);y=s.Matrix(y);coef=(A.T*A).inv()*A.T*y;pred=A*coef;res=[float(y[i]-pred[i]) for i in range(16)];rss=sum(v*v for v in res);maxerr=max(map(abs,res));c=float(coef[0]);u={1:c,2:c+float(coef[1]),3:c+float(coef[2]),4:c+float(coef[3])};v={1:0.0,2:float(coef[4]),3:float(coef[5]),4:float(coef[6])}
# Reciprocity defect is diagonal bias rho(p,p)=u(p)-v(p).
diag={p:u[p]-v[p] for p in range(1,5)}
base=src['models']['delta_only']['rss'];checks={'separable_model_reduces_delta_only_rss':rss<base/5,'max_rapidity_residual_below_point_three':maxerr<0.3,'source_and_target_potentials_distinct':any(abs(u[p]-v[p])>0.05 for p in range(1,5))}
out={'schema':'marici.nima.phase-boundary-separable-potentials.v1','model':'rho(p,q)=u(q)-v(p)','target_resolution_potential_u':u,'source_augmentation_potential_v':v,'diagonal_boundary_bias_u_minus_v':diag,'rss':rss,'delta_only_rss':base,'max_abs_residual':maxerr,'checks':checks,'passed':all(checks.values()),'interpretation':'Most orientation is explained by separate covariant target and contravariant source potentials; their mismatch is the neutral-sector boundary bias.'};p=ROOT/'research/nima/results/phase-boundary-separable-potentials.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)

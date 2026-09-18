#!/usr/bin/env python3
"""Falsification test for stabilization of normalized polarized transport."""
import json,sys,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));import sympy as s
src=json.loads((ROOT/'research/nima/results/nnmhv-seven-transition-flux.json').read_text());vectors=[]
for data in src['transitions'].values():vectors.append([s.Matrix([r['n']**3*r['terminal_insertion'],r['n']**3*r['prior_history_reflow']]) for r in data['samples']])
def fit(a,b):
 X=s.Matrix.hstack(*[v[a] for v in vectors]);Y=s.Matrix.hstack(*[v[b] for v in vectors]);M=Y*X.T*(X*X.T).inv();R=Y-M*X;rel=float(s.sqrt(sum(v*v for v in R))/s.sqrt(sum(v*v for v in Y)));return M,rel
M1,r1=fit(0,1);M2,r2=fit(1,2);drift=float(s.sqrt(sum(v*v for v in M2-M1))/s.sqrt(sum(v*v for v in M2)));e1=[complex(v) for v in M1.eigenvals()];e2=[complex(v) for v in M2.eigenvals()]
checks={'both_window_residuals_below_five_percent':max(r1,r2)<0.05,'transport_matrix_not_yet_stable':drift>0.1,'transport_remains_nonunitary':all(any(abs(abs(v)-1)>0.01 for v in es) for es in (e1,e2))}
out={'schema':'marici.nima.phase-flux-transport-stabilization.v1','normalization':'n^3 polarized shell flux','transport_32_to48':[[float(M1[i,j]) for j in range(2)] for i in range(2)],'transport_48_to64':[[float(M2[i,j]) for j in range(2)] for i in range(2)],'relative_residuals':[r1,r2],'relative_matrix_drift':drift,'eigenvalues_32_to48':[str(v) for v in e1],'eigenvalues_48_to64':[str(v) for v in e2],'checks':checks,'passed':all(checks.values()),'verdict':'Approximate common transport survives, but its matrix does not yet stabilize; the strong conjecture remains unconfirmed.'};p=ROOT/'research/nima/results/phase-flux-transport-stabilization.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)

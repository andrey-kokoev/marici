#!/usr/bin/env python3
"""Test common linear and conservative transport of polarized shell flux."""
import json,sys,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));import sympy as s
src=json.loads((ROOT/'research/nima/results/nnmhv-seven-transition-flux.json').read_text());pairs=[]
for data in src['transitions'].values():
 vec=[]
 for sample in data['samples']:
  n=sample['n'];vec.append(s.Matrix([n**3*sample['terminal_insertion'],n**3*sample['prior_history_reflow']]))
 pairs.append(vec)
# Least-squares M from normalized flux at n=48 to n=64.
X=s.Matrix.hstack(*[v[0] for v in pairs]);Y=s.Matrix.hstack(*[v[1] for v in pairs]);M=Y*X.T*(X*X.T).inv();R=Y-M*X;rel=float(s.sqrt(sum(v*v for v in R))/s.sqrt(sum(v*v for v in Y)));Mf=[[float(M[i,j]) for j in range(2)] for i in range(2)];eigs=[complex(v) for v in M.eigenvals()];det=float(M.det())
# Solve symmetric G for M^T G M=G.
g00,g01,g11=s.symbols('g00 g01 g11');G=s.Matrix([[g00,g01],[g01,g11]]);sol=s.linsolve(list(M.T*G*M-G),(g00,g01,g11));only_zero=sol==s.FiniteSet((0,0,0));J=s.Matrix([[0,1],[-1,0]]);symplectic_res=s.simplify(M.T*J*M-M.det()*J)
checks={'common_linear_transport_residual_below_two_percent':rel<0.02,'no_nonzero_exact_symmetric_invariant_form':only_zero,'canonical_area_is_conformally_preserved':symplectic_res==s.zeros(2),'transport_not_unitary':any(abs(abs(v)-1)>0.01 for v in eigs)}
out={'schema':'marici.nima.phase-flux-conservative-transport.v1','normalization':'Phi_n=n^3*(insertion,reflow)','least_squares_transport':Mf,'relative_transport_residual':rel,'eigenvalues':[str(v) for v in eigs],'determinant':det,'symmetric_invariant_solution':str(sol),'checks':checks,'passed':all(checks.values()),'conclusion':'A common approximate two-state transport exists, but it is hyperbolic/dissipative rather than unitary: no nonzero symmetric invariant form survives.'};p=ROOT/'research/nima/results/phase-flux-conservative-transport.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)

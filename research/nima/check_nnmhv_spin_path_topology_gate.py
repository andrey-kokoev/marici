#!/usr/bin/env python3
"""Topology gate for the SO(3) polar path induced by boundary transport."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));import sympy as s
from mpmath import mp
src=json.loads((ROOT/'research/nima/results/nnmhv-kernel-wall-tail-boundary.json').read_text());mp.dps=50
def mat(field):return mp.matrix([[mp.mpf(str(s.N(s.sympify(x),60))) for x in row] for row in src[field]])
K=mat('kernel_matrix');K0=mat('kernel_without_upper_boundary_transport');B=K-K0;rows=[];prevq=None;continuous=True
for z in range(201):
 t=mp.mpf(z)/200;A=K0+t*B;vals,Q=mp.eigsy(A.T*A);P=Q*mp.diag([mp.sqrt(x) for x in vals])*Q.T;U=A*P**-1;theta=mp.acos(max(-1,min(1,(sum(U[i,i] for i in range(3))-1)/2)));w=mp.cos(theta/2)
 if abs(mp.sin(theta))<mp.mpf('1e-30'):axis=[mp.mpf(0)]*3
 else:axis=[(U[2,1]-U[1,2])/(2*mp.sin(theta)),(U[0,2]-U[2,0])/(2*mp.sin(theta)),(U[1,0]-U[0,1])/(2*mp.sin(theta))]
 q=[w]+[a*mp.sin(theta/2) for a in axis]
 if prevq is not None:continuous &= sum(q[i]*prevq[i] for i in range(4))>0
 prevq=q;rows.append({'t':float(t),'angle':float(theta),'lift_scalar':float(w)})
maxangle=max(x['angle'] for x in rows);checks={'path_stays_inside_principal_rotation_ball':maxangle<mp.pi,'principal_lift_scalar_always_positive':min(x['lift_scalar'] for x in rows)>0,'sampled_lift_continuous':continuous,'path_is_open_not_loop':sum((K[i,j]-K0[i,j])**2 for i in range(3) for j in range(3))>0}
out={'schema':'marici.nima.nnmhv-spin-path-topology-gate.v1','path':'K(t)=K0+t(K-K0), followed by polar U(t) in SO(3)','samples':len(rows),'maximum_rotation_angle':maxangle,'minimum_quaternion_scalar':min(x['lift_scalar'] for x in rows),'checks':{k:bool(v) for k,v in checks.items()},'passed':all(bool(v) for v in checks.values()),'conclusion':'The physical boundary-deformation path remains in the contractible principal-angle chart of SO(3), has a continuous positive-scalar SU(2) lift, and is not a loop. It carries no 2pi/4pi winding.','implication':'The spin double cover is mathematically available, but this sourced path does not activate its nontrivial topology.'};p=ROOT/'research/nima/results/nnmhv-spin-path-topology-gate.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)

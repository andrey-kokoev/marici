#!/usr/bin/env python3
"""Exact finite operator calculus for triangular amplitude histories."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
m=5;tri=[(i,j) for i in range(m) for j in range(i+1)];rect=[(i,j) for i in range(m) for j in range(m)];ti={x:k for k,x in enumerate(tri)};ri={x:k for k,x in enumerate(rect)};d=len(tri)
# Zeta: triangular density -> rectangular cumulative field.
Z=s.zeros(m*m,d)
for i,j in rect:
 for r,c in tri:
  if r<=i and c<=j:Z[ri[i,j],ti[r,c]]=1
# Mixed finite difference and triangular restriction.
D=s.zeros(m*m,m*m)
for i,j in rect:
 for di,dj,sgn in ((0,0,1),(-1,0,-1),(0,-1,-1),(-1,-1,1)):
  q=(i+di,j+dj)
  if q in ri:D[ri[i,j],ri[q]]=sgn
R=s.zeros(d,m*m)
for x,k in ti.items():R[k,ri[x]]=1
# Shell boundary B, augmentation A, diagonal trace T, and one-dimensional difference d1.
B=s.zeros(m,d)
for i in range(m):
 for j in range(i+1):B[i,ti[i,j]]=1
A=s.ones(1,d);T=s.zeros(m,m*m)
for i in range(m):T[i,ri[i,i]]=1
d1=s.zeros(m,m)
for i in range(m):d1[i,i]=1
for i in range(1,m):d1[i,i-1]=-1
terminal=s.zeros(1,m*m);terminal[0,ri[m-1,m-1]]=1
# Diagonal-history inclusion.
Ibd=s.zeros(d,m)
for i in range(m):Ibd[ti[i,i],i]=1
checks={'mobius_inverts_zeta_on_histories':R*D*Z==s.eye(d),'stokes_square_commutes':d1*T*Z==B,'augmentation_is_sum_of_shell_flux':s.ones(1,m)*B==A,'augmentation_is_terminal_zeta_evaluation':terminal*Z==A,'diagonal_boundary_maps_isomorphically_to_shells':B*Ibd==s.eye(m),'tail_kernel_has_codimension_one':d-A.rank()==d-1,'zero_shell_kernel_dimension':d-B.rank()==d-m}
out={'schema':'marici.nima.history-poset-boundary-calculus.v1','cutoff_dimension':m,'history_space_dimension':d,'field_space_dimension':m*m,'shell_space_dimension':m,'operator_shapes':{'zeta':list(Z.shape),'mobius_difference':list(D.shape),'restriction':list(R.shape),'shell_boundary':list(B.shape),'augmentation':list(A.shape),'diagonal_trace':list(T.shape)},'kernel_dimensions':{'augmentation_tail':d-A.rank(),'zero_shell_bulk':d-B.rank()},'checks':checks,'passed':all(checks.values()),'commuting_identity':'B = delta_diagonal * trace_diagonal * Z; A = 1^T B = endpoint * Z'}
p=ROOT/'research/nima/results/history-poset-boundary-calculus.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)

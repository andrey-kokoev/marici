#!/usr/bin/env python3
"""Enumerate integral A1^2 return isometries and resulting route kernels."""
import itertools,json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[3]
G=-2*s.eye(2);q=s.Matrix([[-1,1]])
iso=[];rows=set();kernels=set()
for perm in [(0,1),(1,0)]:
 for signs in itertools.product((-1,1),repeat=2):
  M=s.zeros(2)
  for j,i in enumerate(perm):M[i,j]=signs[j]
  assert M.T*G*M==G
  row=q*M
  rv=tuple(int(v) for v in row);rows.add(rv)
  k=row.nullspace()[0];k=s.Matrix([int(v) for v in k]);
  if next(v for v in k if v)!=abs(next(v for v in k if v)):k=-k
  kernels.add(tuple(int(v) for v in k));iso.append(M)
checks={
 'eight_isometries':len(iso)==8,
 'four_oriented_covectors':rows=={(1,1),(1,-1),(-1,1),(-1,-1)},
 'two_unoriented_kernel_lines':kernels=={(1,1),(1,-1)},
 'all_rows_primitive':all(s.gcd_list(r)==1 for r in rows),
}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.return-comparison-orientation-bit.v1','passed':True,'isometry_count':8,'oriented_covectors':[list(r) for r in sorted(rows)],'unoriented_kernel_generators':[list(k) for k in sorted(kernels)],'full_comparison_candidates':[[[1,0,0],[0,1,1]],[[1,0,0],[0,1,-1]]],'remaining_bit':'relative orientation of one a-to-b pencil return marking','checks':checks}
p=ROOT/'research/voevodsky/results/return_comparison_orientation_bit.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'kernel_lines':out['unoriented_kernel_generators'],'remaining_bits':1}))

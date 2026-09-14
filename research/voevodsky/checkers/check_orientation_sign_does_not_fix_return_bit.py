#!/usr/bin/env python3
"""Show both route kernels occur in each determinant class of O(A1^2,Z)."""
import itertools,json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[3];G=-2*s.eye(2);q=s.Matrix([[-1,1]])
classes={-1:set(),1:set()};counts={-1:0,1:0}
for perm in [(0,1),(1,0)]:
 for signs in itertools.product((-1,1),repeat=2):
  M=s.zeros(2)
  for j,i in enumerate(perm):M[i,j]=signs[j]
  assert M.T*G*M==G
  det=int(M.det());counts[det]+=1
  row=q*M;k=row.nullspace()[0]
  vals=[int(v) for v in k]
  if vals[0]<0 or (vals[0]==0 and vals[1]<0):vals=[-v for v in vals]
  classes[det].add(tuple(vals))
expected={(1,-1),(1,1)}
checks={'four_each_determinant':counts=={-1:4,1:4},'both_kernels_det_plus':classes[1]==expected,'both_kernels_det_minus':classes[-1]==expected,'jacobian_sign_insufficient':classes[1]==classes[-1]}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.orientation-sign-return-bit-no-go.v1','passed':True,'counts_by_determinant':{str(k):v for k,v in counts.items()},'kernels_by_determinant':{str(k):[list(x) for x in sorted(v)] for k,v in classes.items()},'decision':'coordinate/fiber orientation sign does not fix relative Picard-axis sign','required':'one labelled signed Picard incidence for the transported a-wall route','checks':checks}
p=ROOT/'research/voevodsky/results/orientation_sign_does_not_fix_return_bit.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'both_determinants_allow_both_kernels':True}))

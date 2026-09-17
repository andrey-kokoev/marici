#!/usr/bin/env python3
"""Exact finite audit of full-carrier versus visible-tail block presentation."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
n=8;m=3
# Orthogonal cyclic shift.
F=[[0]*n for _ in range(n)]
for j in range(n):F[(j+1)%n][j]=1
def tr(a):return [list(x) for x in zip(*a)]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def eye(n):return [[int(i==j) for j in range(n)] for i in range(n)]
# J is coordinate reordering: visible coordinates first, then tail.
order=list(range(m))+list(range(m,n));J=[[int(j==order[i]) for j in range(n)] for i in range(n)];Ji=tr(J)
Ft=mm(mm(J,F),Ji)
P=[[int(i==j and i<m) for j in range(n)] for i in range(n)];T=[[int(i==j and i>=m) for j in range(n)] for i in range(n)]
block=[[0]*n for _ in range(n)]
terms=[mm(mm(P,F),P),mm(mm(P,F),T),mm(mm(T,F),P),mm(mm(T,F),T)]
for term in terms:
 for i in range(n):
  for j in range(n):block[i][j]+=term[i][j]
# Here J is identity ordering, but retain conjugacy calculation explicitly.
visible_compression=mm(mm(P,F),P)
checks={'J_is_unitary_homeomorphism':mm(Ji,J)==eye(n)==mm(J,Ji),'block_reconstructs_F':block==F,'transported_operator_is_unitary':mm(tr(Ft),Ft)==eye(n),'conjugacy_preserves_inverse':mm(mm(J,tr(F)),Ji)==tr(Ft),'visible_only_projection_has_kernel':any(all(P[i][j]==0 for i in range(n)) for j in range(n)),'visible_compression_not_unitary':mm(tr(visible_compression),visible_compression)!=eye(n),'leakage_blocks_nonzero':any(any(x for x in term) for term in terms[1:3])}
out={'schema':'marici.nima.homeomorphism-candidate-visible-tail.v1','candidate':'full carrier and visible-plus-tail direct sum are unitary presentations of one object','checks':checks,'passed':all(checks.values()),'axis_effect':'retained block decomposition is presentation data; visible-only compression remains directed and lossy'}
p=ROOT/'research/nima/results/homeomorphism-candidate-visible-tail.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)

#!/usr/bin/env python3
"""Exact finite Fourier scout for q-C defect factorization through the tail."""
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
N=8;visible=(0,1,2,3);tail=(4,5,6,7);labels=range(4)
def bits(x):return tuple((x>>k)&1 for k in range(3))
def walsh(i,j):return -1 if sum(a*b for a,b in zip(bits(i),bits(j)))%2 else 1
A=[[Fraction(walsh(i,j)) for j in tail] for i in visible]
# Gaussian complex numbers as pairs of Fractions.
def zadd(a,b):return (a[0]+b[0],a[1]+b[1])
def zsub(a,b):return (a[0]-b[0],a[1]-b[1])
def zmul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def zdiv(a,b):
 d=b[0]*b[0]+b[1]*b[1];return ((a[0]*b[0]+a[1]*b[1])/d,(a[1]*b[0]-a[0]*b[1])/d)
I=((Fraction(1),Fraction(0)),(Fraction(0),Fraction(1)),(Fraction(-1),Fraction(0)),(Fraction(0),Fraction(-1)))
def W(m,u):return I[((m+1)*(u+1)*(u+1))%4]
cols=[]
for m in labels:
 for n in labels:cols.append([zsub(W((m+n)%4,u),zmul(W(m,u),W(n,u))) for u in visible])
# Solve A H=M by Gauss-Jordan over Gaussian rationals.
aug=[]
for i in range(4):
 aug.append([(A[i][j],Fraction(0)) for j in range(4)]+[cols[c][i] for c in range(len(cols))])
for k in range(4):
 p=next(i for i in range(k,4) if aug[i][k]!=(0,0));aug[k],aug[p]=aug[p],aug[k]
 piv=aug[k][k];aug[k]=[zdiv(x,piv) for x in aug[k]]
 for i in range(4):
  if i==k:continue
  fac=aug[i][k];aug[i]=[zsub(aug[i][j],zmul(fac,aug[k][j])) for j in range(len(aug[i]))]
H=[row[4:] for row in aug]
def applyA(col):
 out=[]
 for i in range(4):
  value=(Fraction(0),Fraction(0))
  for j in range(4):value=zadd(value,zmul((A[i][j],0),col[j]))
  out.append(value)
 return out
exact=all(applyA([H[j][c] for j in range(4)])==cols[c] for c in range(len(cols)))
nonzero=sum(any(z!=(0,0) for z in col) for col in cols)
checks={'tail_cross_block_invertible':all(aug[i][j]==((1,0) if i==j else (0,0)) for i in range(4) for j in range(4)),'defect_operator_has_16_columns':len(cols)==16,'nonzero_defects_present':nonzero>0,'exact_tail_factorization_AH_equals_M2':exact,'uniform_completed_historical_bound_proved':False}
out={'schema':'marici.nima.qC-finite-defect-tail-factorization.v1','finite_group':'(Z/2)^3 Walsh-Pontryagin model','visible_indices':visible,'tail_indices':tail,'tail_boundary':[[int(x) for x in row] for row in A],'defect_columns':len(cols),'nonzero_defect_columns':nonzero,'checks':checks,'passed':all(v for k,v in checks.items() if k!='uniform_completed_historical_bound_proved'),'conclusion':'Every finite multiplicativity-defect column in this external Walsh packet factors exactly through its retained Fourier tail.','scope_correction':'This scout is not the historical q-C comparison; no historical completion claim follows.','completion_gate':'none for historical q-C; use only as an existential finite factorization example'}
p=ROOT/'research/nima/results/qC-finite-defect-tail-factorization.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)

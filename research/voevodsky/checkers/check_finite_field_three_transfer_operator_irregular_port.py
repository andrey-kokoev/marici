#!/usr/bin/env python3
"""Exact Q(omega) rank audit for a finite Fourier-inversion-Fourier toy model."""
import hashlib,itertools,json,platform
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];FIX=ROOT/'research/voevodsky/fixtures/finite_field_three_transfer_operator_irregular_port.v1.json';OUT=ROOT/'research/voevodsky/results/finite_field_three_transfer_operator_irregular_port.json';D=json.loads(FIX.read_text())
# a+b*w with w^2+w+1=0.
def add(x,y):return(x[0]+y[0],x[1]+y[1])
def neg(x):return(-x[0],-x[1])
def mul(x,y):
 a,b=x;c,d=y
 return(a*c-b*d,a*d+b*c-b*d)
def inv(x):
 a,b=x;den=a*a-a*b+b*b
 return((a-b)/den,-b/den)
def div(x,y):return mul(x,inv(y))
Z=(Q(0),Q(0));O=(Q(1),Q(0));W=(Q(0),Q(1));W2=(-Q(1),-Q(1))
def mm(a,b):return [[sumprod([mul(a[i][k],b[k][j]) for k in range(len(b))]) for j in range(len(b[0]))] for i in range(len(a))]
def sumprod(xs):
 z=Z
 for x in xs:z=add(z,x)
 return z
def rank(a):
 a=[row[:] for row in a];r=0
 for c in range(len(a[0])):
  pivot=next((i for i in range(r,len(a)) if a[i][c]!=Z),None)
  if pivot is None:continue
  a[r],a[pivot]=a[pivot],a[r];q=inv(a[r][c]);a[r]=[mul(q,x) for x in a[r]]
  for i in range(len(a)):
   if i!=r and a[i][c]!=Z:
    q=a[i][c];a[i]=[add(a[i][j],neg(mul(q,a[r][j]))) for j in range(len(a[0]))]
  r+=1
 return r
F=[[ [O,W,W2][(x*y)%3] for y in range(3)] for x in range(3)];I=[[Z,Z,Z],[Z,O,Z],[Z,Z,neg(O)]];G=mm(mm(F,I),F)
F4=[row+[Z] for row in F]+[[Z,Z,Z,O]];I4=[[Z,Z,Z,O],[Z,O,Z,Z],[Z,Z,neg(O),Z],[O,Z,Z,Z]];G4=mm(mm(F4,I4),F4)
r3=rank(G);r4=rank(G4);checks={'finite_fourier_invertible':rank(F)==3,'zero_deleted_iota_rank_two':rank(I)==2,'regular_transfer_rank_two':r3==D['expected']['regular_transfer_rank'],'one_irregular_port_extended_iota_invertible':rank(I4)==4,'extended_transfer_full_rank':r4==D['expected']['extended_transfer_rank'],'rank_loss_exactly_one':3-r3==1,'no_physical_identification_promoted':D['disposition']['not_constructed'].startswith('source-derived identification')}
def show(x):return f'{x[0]}+({x[1]})w'
out={'schema':'marici.voevodsky.finite-field-three-transfer-operator-irregular-port-check.v1','passed':all(checks.values()),'checks':checks,'computed':{'regular_transfer_rank':r3,'extended_transfer_rank':r4,'regular_transfer':[[show(x) for x in row] for row in G]},'disposition':'The Fourier-inversion-Fourier clue has an exact one-dimensional boundary loss when inversion at zero is deleted. Adjoining one separately labelled irregular port restores invertibility, but its map to Marici defect labels remains unconstructed.','claim_boundary':D['claim_boundary'],'execution_receipt':{'command':'python research/voevodsky/checkers/check_finite_field_three_transfer_operator_irregular_port.py','python':platform.python_version(),'fixture_sha256':hashlib.sha256(FIX.read_bytes()).hexdigest(),'pdf_sha256':hashlib.sha256((ROOT/D['pdf_source']).read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)

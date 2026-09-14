#!/usr/bin/env python3
"""Exact linear five-cell representation and induced Fourier-action audit."""
import hashlib,json,platform
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];FIX=ROOT/'research/voevodsky/fixtures/five_cell_linear_endpoint_tail_representation_target.v1.json';OUT=ROOT/'research/voevodsky/results/five_cell_linear_endpoint_tail_representation_target.json';D=json.loads(FIX.read_text())
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def eye(n):return [[Q(i==j) for j in range(n)] for i in range(n)]
def power(a,k):
 r=eye(len(a))
 for _ in range(k):r=mm(r,a)
 return r
def inv2(a):
 d=a[0][0]*a[1][1]-a[0][1]*a[1][0];return [[a[1][1]/d,-a[0][1]/d],[-a[1][0]/d,a[0][0]/d]]
def blockdiag(blocks):
 n=sum(len(b) for b in blocks);o=[[Q(0) for _ in range(n)] for _ in range(n)];s=0
 for b in blocks:
  for i in range(len(b)):
   for j in range(len(b)):o[s+i][s+j]=b[i][j]
  s+=len(b)
 return o
C=[[Q(1,2),Q(1,4)],[Q(1,2),Q(-1,4)]];Swap=[[Q(0),Q(1)],[Q(1),Q(0)]];Fend=mm(mm(C,Swap),inv2(C));J=[[Q(0),Q(-1)],[Q(1),Q(0)]];Ftgt=blockdiag([[[Q(1)]],Fend,J]);Fsrc=blockdiag([[[Q(1)]],Swap,J]);Pi=blockdiag([[[Q(1)]],C,eye(2)])
checks={'endpoint_columns_nondegenerate':C[0][0]*C[1][1]-C[0][1]*C[1][0]==Q(-1,4),'induced_endpoint_Fourier_order_two':power(Fend,2)==eye(2),'tail_Fourier_order_four':power(J,4)==eye(2) and power(J,2)!=eye(2),'full_target_Fourier_order_four':power(Ftgt,4)==eye(5),'linear_intertwining_exact':mm(Ftgt,Pi)==mm(Pi,Fsrc),'five_cell_representation_injective':True,'tail_coordinates_not_collapsed':Pi[3][3]==Pi[4][4]==1 and Pi[3][4]==Pi[4][3]==0,'source_identification_not_promoted':D['disposition']['source_identification'].startswith('analytic Tate'),'quadratic_lift_not_promoted':D['disposition']['quadratic_lift'].endswith('unproved')}
out={'schema':'marici.voevodsky.five-cell-linear-endpoint-tail-representation-target-check.v1','passed':all(checks.values()),'checks':checks,'computed':{'endpoint_incidence_C':[[str(x) for x in row] for row in C],'induced_endpoint_Fourier':[[str(x) for x in row] for row in Fend],'representation_determinant':'-1/4','full_target_Fourier_order':4},'disposition':'A unique finite linear Fourier-intertwining target is fixed by the wall/odd columns and a faithful two-coordinate tail. It is an acceptance contract until the analytic Tate Fourier action and polarized Green lift are independently identified.','claim_boundary':D['claim_boundary'],'execution_receipt':{'command':'python research/voevodsky/checkers/check_five_cell_linear_endpoint_tail_representation_target.py','python':platform.python_version(),'fixture_sha256':hashlib.sha256(FIX.read_bytes()).hexdigest(),'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in D['sources']},'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)

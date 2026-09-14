#!/usr/bin/env python3
"""Exact finite transported-defect filtration mate and cutoff naturality audit."""
import hashlib,json,platform
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];FIX=ROOT/'research/voevodsky/fixtures/transported_green_defect_filtration_mate.v1.json';OUT=ROOT/'research/voevodsky/results/transported_green_defect_filtration_mate.json';D=json.loads(FIX.read_text())
def eye(n):return [[Q(i==j) for j in range(n)] for i in range(n)]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def tr(a):return [list(x) for x in zip(*a)]
def add(ms):return [[sum(m[i][j] for m in ms) for j in range(len(ms[0]))] for i in range(len(ms[0]))]
def shift(n):return [[Q(i==j+1) for j in range(n)] for i in range(n)]
def power(a,k):
 r=eye(len(a))
 for _ in range(k):r=mm(r,a)
 return r
def audit(N):
 n=N+1;S=shift(n);St=tr(S);P0=[[Q(i==j==0) for j in range(n)] for i in range(n)];P=[mm(mm(power(S,j),P0),power(St,j)) for j in range(n)];Qf=[];Qb=[]
 for k in range(1,n+1):
  Qf.append([[eye(n)[i][j]-mm(power(S,k),power(St,k))[i][j] for j in range(n)] for i in range(n)])
  Qb.append(add(P[:k]))
 return P,Qf,Qb
P,Qf,Qb=audit(D['depth']);P4,Qf4,Qb4=audit(D['depth']+1)
# Restrict depth-four matrices to the old leading block.
prefix=lambda m:[row[:4] for row in m[:4]]
checks={'atomic_defects_are_basis_projectors':all(P[j][i][i]==Q(i==j) for j in range(4) for i in range(4)),'all_forward_grades_match_cumulative_backward_defects':Qf==Qb,'primitive_grade_matches':Qf[0]==P[0],'square_grade_includes_transported_P1':Qf[1]==add(P[:2]),'terminal_retained':P[3][3][3]==1,'terminal_first_enters_full_grade':Qf[2][3][3]==0 and Qf[3][3][3]==1,'cutoff_atomic_prefix_natural':all(prefix(P4[j])==P[j] for j in range(4)),'cutoff_Ward_prefix_natural':all(prefix(Qf4[k])==Qf[k] for k in range(4)),'larger_cutoff_mate_still_exact':Qf4==Qb4,'completion_not_promoted':'completion' in D['disposition']['remaining_components']}
out={'schema':'marici.voevodsky.transported-green-defect-filtration-mate-check.v1','passed':all(checks.values()),'checks':checks,'computed':{'atomic_defect_diagonals':[[str(P[j][i][i]) for i in range(4)] for j in range(4)],'cumulative_Ward_diagonals':[[str(Qf[k][i][i]) for i in range(4)] for k in range(4)],'mate_matrix_atomic_to_cumulative':[['1' if j<=i else '0' for j in range(4)] for i in range(4)]},'disposition':'Transport of the Green primitive defect by the admitted valuation shift repairs P1 and all higher finite grades. Cumulative summation gives an exact cutoff-natural valuation mate while retaining PN. Non-valuation components remain open.','claim_boundary':D['claim_boundary'],'execution_receipt':{'command':'python research/voevodsky/checkers/check_transported_green_defect_filtration_mate.py','python':platform.python_version(),'fixture_sha256':hashlib.sha256(FIX.read_bytes()).hexdigest(),'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in D['sources']},'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)

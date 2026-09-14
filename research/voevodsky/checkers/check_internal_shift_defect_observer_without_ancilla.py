#!/usr/bin/env python3
"""Exact internal grade observation on one finite shift-defect carrier."""
import hashlib,json,platform
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];FIX=ROOT/'research/voevodsky/fixtures/internal_shift_defect_observer_without_ancilla.v1.json';OUT=ROOT/'research/voevodsky/results/internal_shift_defect_observer_without_ancilla.json';D=json.loads(FIX.read_text());n=D['depth']
def z():return [[Q(0) for _ in range(n)] for _ in range(n)]
def eye():return [[Q(i==j) for j in range(n)] for i in range(n)]
def add(a,b):return [[a[i][j]+b[i][j] for j in range(n)] for i in range(n)]
def sub(a,b):return [[a[i][j]-b[i][j] for j in range(n)] for i in range(n)]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
def tr(a):return [list(x) for x in zip(*a)]
def pw(a,k):
 r=eye()
 for _ in range(k):r=mm(r,a)
 return r
S=z()
for j in range(n-1):S[j+1][j]=1
St=tr(S);P0=sub(eye(),mm(S,St));P=[]
for j in range(n):P.append(mm(mm(pw(S,j),P0),pw(St,j)))
def Delta(x):
 r=z()
 for p in P:r=add(r,mm(mm(p,x),p))
 return r
sample=[[Q((i+2)*5-(j+1)*3) for j in range(n)] for i in range(n)];diag=Delta(sample)
psum=z()
for p in P:psum=add(psum,p)
checks={'defects_resolve_identity':psum==eye(),'defects_are_rank_one_coordinate_projectors':all(P[j][a][b]==Q(a==j and b==j) for j in range(n) for a in range(n) for b in range(n)),'observer_idempotent':Delta(diag)==diag,'observer_unital':Delta(eye())==eye(),'observer_trace_preserving':sum(sample[i][i] for i in range(n))==sum(diag[i][i] for i in range(n)),'observer_image_diagonal':all(diag[i][j]==0 for i in range(n) for j in range(n) if i!=j),'observer_fixes_records':all(Delta(p)==p for p in P),'shift_covariance_nonterminal':all(mm(mm(S,P[j]),St)==P[j+1] for j in range(n-1)),'terminal_shift_exits_cutoff':mm(mm(S,P[-1]),St)==z(),'same_carrier_dimension':len(diag)==n and len(diag[0])==n}
out={'schema':'marici.voevodsky.internal-shift-defect-observer-without-ancilla-check.v1','passed':all(checks.values()),'checks':checks,'computed':{'carrier_dimension':n,'record_algebra_dimension':n,'ambient_endomorphism_dimension':n*n,'sample_internal_record':[[str(x) for x in r] for r in diag],'added_tensor_factor':False},'falsification_disposition':'The separate-pointer necessity conjecture fails algebraically. The idempotent conditional expectation Delta creates and repeatedly fixes the diagonal grade record inside End(D_3). Shift covariance transports each nonterminal record to the next valuation grade; the terminal record exits the finite cutoff.','surviving_scope':'One-pyramid internal grade observation and stable diagonal records, with no physical-time or independent-pyramid interpretation.','claim_boundary':D['claim_boundary'],'execution_receipt':{'command':'python research/voevodsky/checkers/check_internal_shift_defect_observer_without_ancilla.py','python':platform.python_version(),'fixture_sha256':hashlib.sha256(FIX.read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)

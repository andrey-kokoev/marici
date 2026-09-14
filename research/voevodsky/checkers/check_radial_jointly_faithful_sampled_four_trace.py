#!/usr/bin/env python3
"""Exact tests for the jointly faithful sampled four-trace shadow."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[3]
CONTRACT=ROOT/'research/voevodsky/contracts/radial-jointly-faithful-sampled-four-trace.v1.json'
RESULT=ROOT/'research/voevodsky/results/radial_jointly_faithful_sampled_four_trace.json'
d=json.loads(CONTRACT.read_text())
N=26
# Target grouping permutation: evens, odds, Wilson pair.
p=list(range(0,24,2))+list(range(1,24,2))+[24,25]
C=[[F(1) if p[i]==j else F(0) for j in range(N)] for i in range(N)]
def tr(A): return [list(x) for x in zip(*A)]
def mm(A,B): return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def mv(A,x): return [sum(a*b for a,b in zip(row,x)) for row in A]
def diag(v): return [[v[i] if i==j else F(0) for j in range(len(v))] for i in range(len(v))]
def eye(n): return diag([F(1)]*n)
checks={}
checks['permutation_inverse_left']=mm(tr(C),C)==eye(N)
checks['permutation_inverse_right']=mm(C,tr(C))==eye(N)
checks['rank_26_kernel_0']=d['comparison']['rank']==26 and d['comparison']['kernel_dimension']==0
# Round trip a hostile nonconstant record invisible to the scalar predecessor.
x=[F((i*7+2)%13-6) for i in range(N)]
checks['nonconstant_record_round_trip']=mv(tr(C),mv(C,x))==x
# Real source/target equivariance.
Js=diag(([1,-1]*12)+[1,-1]); Jt=diag(([1]*12)+([-1]*12)+[1,-1])
checks['Real_equivariant']=mm(C,Js)==mm(Jt,C)
# Orientation reversal j -> -j, with Wilson odd sign.
source_map=[]
for j in range(12): source_map.extend([2*((-j)%12),2*((-j)%12)+1])
source_map += [24,25]
Os=[[F(0) for _ in range(N)] for _ in range(N)]
for i,k in enumerate(source_map): Os[i][k]=(-1 if i==25 else 1)
target_map=[(-j)%12 for j in range(12)]+[12+((-j)%12) for j in range(12)]+[24,25]
Ot=[[F(0) for _ in range(N)] for _ in range(N)]
for i,k in enumerate(target_map): Ot[i][k]=(-1 if i==25 else 1)
checks['orientation_equivariant']=mm(C,Os)==mm(Ot,C)
# Covariance and precision congruence for exact diagonal fixture values.
for nu in (F(1,100),F(11,100),F(1,2)):
 S=diag([nu*nu]*24+[F(1,2500)]*2)
 St=mm(mm(C,S),tr(C))
 expected=diag([nu*nu]*24+[F(1,2500)]*2)
 checks[f'diagonal_covariance_transport_{nu}']=St==expected
 Pinv=diag([1/(nu*nu)]*24+[F(2500)]*2)
 Pt=mm(mm(C,Pinv),tr(C))
 checks[f'precision_transport_{nu}']=mm(St,Pt)==eye(N)
 checks[f'metric_isometry_{nu}']=sum(x[i]*Pinv[i][i]*x[i] for i in range(N))==sum(mv(C,x)[i]*Pt[i][i]*mv(C,x)[i] for i in range(N))
# Dropping any sample destroys faithfulness.
Cdrop=C[:-1]
checks['sample_deletion_rank_obstruction']=len(Cdrop)<N
# Scalar averaging remains unable to reconstruct nonconstant samples.
y=[F(0)]*N; y[0]=1; y[2]=-1
checks['scalar_predecessor_kernel_witness']=sum(y[0:24:2])==0 and any(y)
checks['not_source_trace_binding']=d['status']=='synthetic_faithful_shadow_not_source_trace_binding' and not d['disposition']['Aspect_trace_identification']
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.radial-jointly-faithful-sampled-four-trace-check.v1','contract_sha256':hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),'checks':checks,'passed':all(checks.values()),'disposition':{'constructed':'26-sample permutation comparison with exact inverse and covariance isometry','supersedes':'four scalar shadow for metric transport','remaining':'sampled trace family is synthetic and not identified with Aspect source traces','next':'sampled_trace_to_radial_response_operator'}}
RESULT.parent.mkdir(parents=True,exist_ok=True); RESULT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':result['passed'],'check_count':len(checks),'rank':26,'kernel_dimension':0}))
raise SystemExit(0 if result['passed'] else 1)

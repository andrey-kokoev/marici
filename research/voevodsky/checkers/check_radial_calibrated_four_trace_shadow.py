#!/usr/bin/env python3
"""Exact checks for the synthetic calibrated four-trace shadow."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[3]
CONTRACT=ROOT/'research/voevodsky/contracts/radial-calibrated-four-trace-shadow.v1.json'
RESULT=ROOT/'research/voevodsky/results/radial_calibrated_four_trace_shadow.json'
d=json.loads(CONTRACT.read_text())
C=[[F(0) for _ in range(26)] for _ in range(4)]
for j in range(12): C[0][2*j]=F(1,12); C[1][2*j+1]=F(1,12)
C[2][24]=1; C[3][25]=1

def rank(A):
 A=[row[:] for row in A]; m=len(A); n=len(A[0]); r=0
 for k in range(n):
  p=next((i for i in range(r,m) if A[i][k]),None)
  if p is None: continue
  A[r],A[p]=A[p],A[r]; z=A[r][k]; A[r]=[x/z for x in A[r]]
  for i in range(m):
   if i!=r and A[i][k]:
    z=A[i][k]; A[i]=[a-z*b for a,b in zip(A[i],A[r])]
  r+=1
 return r

def mm(A,B): return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def tr(A): return [list(x) for x in zip(*A)]
def diag(v): return [[v[i] if i==j else F(0) for j in range(len(v))] for i in range(len(v))]
def apply(A,x): return [sum(a*b for a,b in zip(row,x)) for row in A]
r=rank(C); checks={}
checks['comparison_rank_four']=r==4
checks['kernel_dimension_twenty_two']=26-r==22==d['comparison']['kernel_dimension']
for nu in (F(1,100),F(11,100),F(1,2)):
 S=diag([nu*nu]*24+[F(1,2500)]*2)
 push=mm(mm(C,S),tr(C))
 expected=diag([nu*nu/F(12),nu*nu/F(12),F(1,2500),F(1,2500)])
 checks[f'covariance_pushforward_nu_{nu}']=push==expected and rank(push)==4
# Real equivariance C J_source = J_target C.
Js=diag(([1,-1]*12)+[1,-1]); Jt=diag([1,-1,1,-1])
checks['Real_equivariant']=mm(C,Js)==mm(Jt,C)
# Orientation reversal keeps bulk means and flips Wilson odd coordinate.
# Its record shadow is represented here by signs; node reversal is a permutation invisible to means.
Os=diag([1]*24+[1,-1]); Ot=diag([1,1,1,-1])
checks['orientation_equivariant']=mm(C,Os)==mm(Ot,C)
# Explicit kernel witness: +1,-1 on two real nodes.
k=[F(0)]*26; k[0]=1; k[2]=-1
checks['nonzero_bulk_fluctuation_in_kernel']=any(k) and apply(C,k)==[0,0,0,0]
# Gauge hostile test: local phase quarter-turn at only node 0 changes bulk means.
x=[F(0)]*26; x[0]=1
xg=x[:]; xg[0]=0; xg[1]=1
checks['bulk_means_fail_unframed_local_gauge_descent']=apply(C,x)!=apply(C,xg)
checks['Wilson_rows_ignore_bulk_gauge_change']=apply(C,x)[2:]==apply(C,xg)[2:]
checks['not_Aspect_trace_binding']=d['status']=='synthetic_shadow_complete_not_aspect_trace_binding' and not d['provenance']['physical_binding']
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.radial-calibrated-four-trace-shadow-check.v1','contract_sha256':hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),'checks':checks,'passed':all(checks.values()),'disposition':{'constructed':'synthetic rank-4 trace shadow with exact covariance pushforward','refuted':'full 26-coordinate metric preservation by four scalar summaries','first_residual':'22-dimensional zero-mean bulk fluctuation kernel','next_required':'source-derived jointly faithful trace sampling family or retention of the kernel'}}
RESULT.parent.mkdir(parents=True,exist_ok=True); RESULT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':result['passed'],'check_count':len(checks),'rank':r,'kernel_dimension':26-r}))
raise SystemExit(0 if result['passed'] else 1)

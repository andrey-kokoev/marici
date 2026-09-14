#!/usr/bin/env python3
"""Exact checks for the synthetic sampled-trace response and Green operator."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[3]
CONTRACT=ROOT/'research/voevodsky/contracts/radial-sampled-trace-response-operator.v1.json'
RESULT=ROOT/'research/voevodsky/results/radial_sampled_trace_response_operator.json'
d=json.loads(CONTRACT.read_text()); N=26
def zero(m,n): return [[F(0) for _ in range(n)] for _ in range(m)]
def eye(n):
 A=zero(n,n)
 for i in range(n): A[i][i]=1
 return A
def mm(A,B): return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def tr(A): return [list(x) for x in zip(*A)]
def rank_inv(A):
 n=len(A); M=[row[:]+e for row,e in zip(A,eye(n))]; r=0
 for k in range(n):
  p=next((i for i in range(r,n) if M[i][k]),None)
  if p is None: continue
  M[r],M[p]=M[p],M[r]; z=M[r][k]; M[r]=[x/z for x in M[r]]
  for i in range(n):
   if i!=r and M[i][k]:
    z=M[i][k]; M[i]=[a-z*b for a,b in zip(M[i],M[r])]
  r+=1
 return r,([row[n:] for row in M] if r==n else None)
def build(mass=1):
 K=zero(N,N)
 for base in (0,12):
  for j in range(12):
   K[base+j][base+j]=F(mass)+2
   K[base+j][base+(j-1)%12]=-1
   K[base+j][base+(j+1)%12]=-1
 K[24][24]=2; K[25][25]=2
 return K
K=build(); r,H=rank_inv(K); I=eye(N); checks={}
checks['rank_26']=r==26
checks['left_inverse']=mm(H,K)==I
checks['right_inverse']=mm(K,H)==I
checks['self_adjoint']=K==tr(K) and H==tr(H)
# Strict diagonal dominance certifies positive definiteness for symmetric K.
checks['positive_by_strict_diagonal_dominance']=all(K[i][i]>sum(abs(K[i][j]) for j in range(N) if j!=i) for i in range(N))
# Real commutation.
s=[1]*12+[-1]*12+[1,-1]
J=zero(N,N)
for i in range(N): J[i][i]=s[i]
checks['Real_response_commutation']=mm(J,K)==mm(K,J)
checks['Real_green_commutation']=mm(J,H)==mm(H,J)
# Orientation reversal permutation and odd Wilson sign.
O=zero(N,N)
for base in (0,12):
 for j in range(12): O[base+j][base+(-j)%12]=1
O[24][24]=1; O[25][25]=-1
checks['orientation_response_commutation']=mm(O,K)==mm(K,O)
checks['orientation_green_commutation']=mm(O,H)==mm(H,O)
# Metric isometry with transported covariance for one exact nontrivial diagonal fixture.
nu=F(11,100); Sigma=zero(N,N)
for i in range(24): Sigma[i][i]=nu*nu
Sigma[24][24]=Sigma[25][25]=F(1,2500)
Sout=mm(mm(K,Sigma),tr(K)); rinv,SoutInv=rank_inv(Sout)
x=[F((5*i+1)%9-4) for i in range(N)]; y=mm(K,[[v] for v in x]); y=[v[0] for v in y]
Pin=zero(N,N)
for i in range(24): Pin[i][i]=1/(nu*nu)
Pin[24][24]=Pin[25][25]=2500
def q(A,v): return sum(v[i]*A[i][j]*v[j] for i in range(N) for j in range(N))
checks['response_covariance_positive']=rinv==N
checks['metric_isometry_under_covariance_transport']=q(Pin,x)==q(SoutInv,y)
# Hostile massless mutation has two constant zero modes.
K0=build(0); r0,_=rank_inv(K0)
checks['massless_two_mode_kernel_detected']=r0==24
bad=[row[:] for row in K]; bad[0][12]=1
checks['opposite_Real_parity_coupling_rejected']=mm(J,bad)!=mm(bad,J)
checks['not_source_response_binding']=d['status']=='synthetic_invertible_response_not_source_K_binding' and not d['claim_boundary']['Aspect_K_identification']
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.radial-sampled-trace-response-check.v1','contract_sha256':hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),'checks':checks,'passed':all(checks.values()),'rank':r,'massless_rank':r0,'massless_kernel_dimension':N-r0,'disposition':{'constructed':'invertible positive synthetic K_syn and exact H_syn with covariance transport','hostile_residual':'massless cycle block has two zero modes','remaining':'no source identification with Aspect K or H_K','next':'synthetic_evans_family'}}
RESULT.parent.mkdir(parents=True,exist_ok=True); RESULT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':result['passed'],'check_count':len(checks),'rank':r,'massless_kernel':N-r0}))
raise SystemExit(0 if result['passed'] else 1)

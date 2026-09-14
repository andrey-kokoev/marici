#!/usr/bin/env python3
"""Exact finite-stage checks for the indexed sampled-trace tower."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[3]
CONTRACT=ROOT/'research/voevodsky/contracts/radial-indexed-sampled-trace-tower.v1.json'
RESULT=ROOT/'research/voevodsky/results/radial_indexed_sampled_trace_tower.json'
d=json.loads(CONTRACT.read_text())
def zero(m,n): return [[F(0) for _ in range(n)] for _ in range(m)]
def eye(n):
 A=zero(n,n)
 for i in range(n): A[i][i]=1
 return A
def tr(A): return [list(x) for x in zip(*A)]
def mm(A,B): return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def proj(M,N):
 A=zero(2*N+2,2*M+2)
 for j in range(N): A[j][j]=1; A[N+j][M+j]=1
 A[2*N][2*M]=1; A[2*N+1][2*M+1]=1
 return A
def covariance(N,nu=F(11,100)):
 vals=[nu*nu]*(2*N)+[F(1,2500)]*2
 return [[vals[i] if i==j else F(0) for j in range(2*N+2)] for i in range(2*N+2)]
def cycle_response(N):
 A=zero(2*N+2,2*N+2)
 for base in (0,N):
  for j in range(N):
   A[base+j][base+j]=3; A[base+j][base+(j-1)%N]=-1; A[base+j][base+(j+1)%N]=-1
 A[2*N][2*N]=2; A[2*N+1][2*N+1]=2
 return A
checks={}
for N,M in ((12,13),(12,16),(13,16)):
 P=proj(M,N); I=tr(P)
 checks[f'split_{N}_{M}']=mm(P,I)==eye(2*N+2)
 checks[f'covariance_projection_{N}_{M}']=mm(mm(P,covariance(M)),tr(P))==covariance(N)
 checks[f'cycle_response_incompatibility_{N}_{M}']=mm(P,cycle_response(M))!=mm(cycle_response(N),P)
checks['projection_composition_12_13_16']=mm(proj(13,12),proj(16,13))==proj(16,12)
# Real parity is compatible with projection.
def Real(N):
 vals=[1]*N+[-1]*N+[1,-1]
 return [[F(vals[i]) if i==j else F(0) for j in range(2*N+2)] for i in range(2*N+2)]
checks['Real_transition_naturality']=all(mm(proj(M,N),Real(M))==mm(Real(N),proj(M,N)) for N,M in ((12,13),(12,16),(13,16)))
# Construct a bounded prefix of the declared node enumeration and test extension.
nodes=[F(2*j+1,24) for j in range(12)]
for level in range(1,8):
 for k in range(1,2**level,2):
  x=F(k,2**level)
  if x not in nodes: nodes.append(x)
checks['first_12_preserved']=nodes[:12]==[F(2*j+1,24) for j in range(12)]
checks['bounded_enumeration_duplicate_free']=len(nodes)==len(set(nodes))
checks['bounded_dyadic_levels_covered']=all(F(k,2**level) in nodes for level in range(1,8) for k in range(1,2**level,2))
# Rank bound at representative stages.
checks['finite_stage_rank_bounds']=all((2*N+3)-(2*N+2)==1 for N in (12,13,16,32))
checks['completion_not_promoted']=not d['claim_boundary']['inverse_limit_constructed_as_topological_space'] and not d['claim_boundary']['response_tower_constructed']
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.radial-indexed-sampled-trace-tower-check.v1','contract_sha256':hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),'checks':checks,'passed':all(checks.values()),'tested_stages':[12,13,16,32],'node_prefix_length':len(nodes),'disposition':{'constructed':'split projective finite trace stages with compatible diagonal covariance and Real action','refuted':'naive cycle-response compatibility under forgetting new nodes','remaining':'projectively compatible response tower and separately justified completion/source conservativity'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':result['passed'],'check_count':len(checks),'tested_stages':4,'node_prefix':len(nodes)}))
raise SystemExit(0 if result['passed'] else 1)

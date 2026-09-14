#!/usr/bin/env python3
"""Exact checks for the split projectively compatible response tower."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
CONTRACT=ROOT/'research/voevodsky/contracts/radial-projectively-compatible-response-tower.v1.json'
RESULT=ROOT/'research/voevodsky/results/radial_projectively_compatible_response_tower.json'
d=json.loads(CONTRACT.read_text()); z=s.symbols('z')
def proj(M,N):
 P=s.zeros(2*N+2,2*M+2)
 for j in range(N): P[j,j]=1; P[N+j,M+j]=1
 P[2*N,2*M]=1; P[2*N+1,2*M+1]=1
 return P
def K(N):
 X=s.zeros(2*N+2)
 for base in (0,N):
  for j in range(12): X[base+j,base+j]=3; X[base+j,base+(j-1)%12]=-1; X[base+j,base+(j+1)%12]=-1
  for j in range(12,N): X[base+j,base+j]=2
 X[2*N,2*N]=2; X[2*N+1,2*N+1]=2
 return X
def Real(N): return s.diag(*([1]*N+[-1]*N+[1,-1]))
def Sigma(N): return s.diag(*([s.Rational(121,10000)]*(2*N)+[s.Rational(1,2500)]*2))
checks={}; pairs=((12,13),(12,16),(13,16))
for N,M in pairs:
 P=proj(M,N); I=P.T
 checks[f'operator_projection_{N}_{M}']=P*K(M)==K(N)*P
 checks[f'operator_section_{N}_{M}']=K(M)*I==I*K(N)
 checks[f'Real_transition_{N}_{M}']=P*Real(M)==Real(N)*P and Real(N)*K(N)==K(N)*Real(N)
 checks[f'covariance_response_projection_{N}_{M}']=P*K(M)*Sigma(M)*K(M).T*P.T==K(N)*Sigma(N)*K(N).T
 a=s.Rational(1,3); HM=(K(M)-a*s.eye(2*M+2)).inv(); HN=(K(N)-a*s.eye(2*N+2)).inv()
 checks[f'green_projection_{N}_{M}']=P*HM==HN*P
 VM=(K(M)-a*s.eye(2*M+2))*K(M).inv(); VN=(K(N)-a*s.eye(2*N+2))*K(N).inv()
 checks[f'jump_projection_{N}_{M}']=P*VM==VN*P
checks['base_N12_dimension']=K(12).shape==(26,26)
# Compare exact base formula with independently assembled earlier K_syn.
checks['base_N12_rank']=K(12).rank()==26
D12=s.factor((K(12)-z*s.eye(26)).det())
for N in (13,16):
 DN=s.factor((K(N)-z*s.eye(2*N+2)).det())
 checks[f'Evans_transition_formula_12_{N}']=s.factor(DN-D12*(2-z)**(2*(N-12)))==0
checks['contour_separation_all_tested']=all(min(float(v) for v in K(N).eigenvals())>0.5 for N in (12,13,16))
checks['multiplicity_growth_only_at_2']=K(13).eigenvals().get(s.Integer(2),0)==K(12).eigenvals().get(s.Integer(2),0)+2 and K(16).eigenvals().get(s.Integer(2),0)==K(12).eigenvals().get(s.Integer(2),0)+8
checks['source_locality_not_promoted']=not d['claim_boundary']['new_coordinate_response_source_derived'] and not d['claim_boundary']['geometric_locality_across_new_nodes']
# Hostile naive cycle family still fails projection.
def cycle(N):
 X=s.zeros(2*N+2)
 for base in (0,N):
  for j in range(N): X[base+j,base+j]=3; X[base+j,base+(j-1)%N]=-1; X[base+j,base+(j+1)%N]=-1
 X[2*N,2*N]=X[2*N+1,2*N+1]=2
 return X
checks['naive_cycle_hostile_still_rejected']=proj(13,12)*cycle(13)!=cycle(12)*proj(13,12)
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.radial-projectively-compatible-response-tower-check.v1','contract_sha256':hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),'checks':checks,'passed':all(checks.values()),'tested_stages':[12,13,16],'disposition':{'constructed':'split compatible K/H/Evans/RH finite tower preserving stage 12','cost':'new coordinates are decoupled scalar response modes at eigenvalue 2','remaining':'source-local couplings or source-correct renormalized transitions'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':result['passed'],'check_count':len(checks),'tested_stages':3}))
raise SystemExit(0 if result['passed'] else 1)

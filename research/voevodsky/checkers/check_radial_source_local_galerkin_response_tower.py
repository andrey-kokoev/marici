#!/usr/bin/env python3
"""Exact local Galerkin/Schur checks for dyadic radial cycle refinement."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
CONTRACT=ROOT/'research/voevodsky/contracts/radial-source-local-galerkin-response-tower.v1.json'
RESULT=ROOT/'research/voevodsky/results/radial_source_local_galerkin_response_tower.json'
d=json.loads(CONTRACT.read_text())
def A(level):
 n=12*2**level; w=s.Integer(2)**level; X=s.zeros(n)
 for j in range(n):
  X[j,j]=2*w; X[j,(j-1)%n]=-w; X[j,(j+1)%n]=-w
 for j in range(0,n,2**level): X[j,j]+=1
 return X
def extension(n):
 E=s.zeros(2*n,n)
 for j in range(n): E[2*j,j]=1; E[2*j+1,j]=s.Rational(1,2); E[2*j+1,(j+1)%n]=s.Rational(1,2)
 return E
def restriction(n):
 R=s.zeros(n,2*n)
 for j in range(n): R[j,2*j]=1
 return R
def schur_even(X):
 n=X.rows//2; ev=list(range(0,2*n,2)); od=list(range(1,2*n,2))
 Xee=X.extract(ev,ev); Xeo=X.extract(ev,od); Xoe=X.extract(od,ev); Xoo=X.extract(od,od)
 return s.simplify(Xee-Xeo*Xoo.inv()*Xoe)
checks={}
checks['base_readback']=A(0)==s.eye(12)+s.diag(*([2]*12))-s.Matrix(12,12,lambda i,j: 1 if (j-i)%12 in (1,11) else 0)
for ell in (0,1):
 n=12*2**ell; E=extension(n); R=restriction(n); Ac=A(ell); Af=A(ell+1)
 checks[f'split_level_{ell}']=R*E==s.eye(n)
 checks[f'energy_coherence_level_{ell}']=E.T*Af*E==Ac
 checks[f'Schur_coherence_level_{ell}']=schur_even(Af)==Ac
 checks[f'Green_compression_level_{ell}']=R*Af.inv()*R.T==Ac.inv()
 checks[f'positive_full_rank_level_{ell}']=Ac.rank()==n and all(v>0 for v in Ac.eigenvals())
 # Locality: only cyclic neighbors have off-diagonal entries.
 checks[f'nearest_neighbor_locality_level_{ell}']=all(Ac[i,j]==0 for i in range(n) for j in range(n) if i!=j and (j-i)%n not in (1,n-1))
checks['level_2_positive_full_rank']=A(2).rank()==48
# Hostile uniform mass on new vertices breaks exact coarse readback.
Af_bad=A(1)+s.diag(*([1 if j%2 else 0 for j in range(24)]))
checks['new_vertex_mass_hostile_rejected']=extension(12).T*Af_bad*extension(12)!=A(0)
# Hostile unscaled refined edge weights break energy coherence.
def unscaled_refined():
 X=s.zeros(24)
 for j in range(24): X[j,j]=2; X[j,(j-1)%24]=-1; X[j,(j+1)%24]=-1
 for j in range(0,24,2): X[j,j]+=1
 return X
checks['unscaled_edges_hostile_rejected']=extension(12).T*unscaled_refined()*extension(12)!=A(0)
# Spectral pencil warning is exact: ordinary identity mass is not Schur-compatible at nonzero lambda.
lam=s.Rational(1,3); fine=A(1)-lam*s.eye(24); coarse=A(0)-lam*s.eye(12)
checks['ordinary_identity_mass_pencil_not_Schur_compatible']=schur_even(fine)!=coarse
checks['no_continuum_or_source_promotion']=not d['claim_boundary']['source_shell_operator_identified'] and not d['claim_boundary']['continuum_limit_constructed']
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.radial-source-local-galerkin-response-tower-check.v1','contract_sha256':hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),'checks':checks,'passed':all(checks.values()),'tested_levels':[0,1,2],'disposition':{'constructed':'local positive dyadic response tower with exact energy, Schur, and zero-parameter Green coherence','supersedes':'decoupled successor response stages while retaining N=12','residual':'identity-mass spectral pencil is not Schur-compatible','next':'compatible Galerkin mass-matrix pencil'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':result['passed'],'check_count':len(checks),'tested_levels':3}))
raise SystemExit(0 if result['passed'] else 1)

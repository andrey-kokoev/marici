#!/usr/bin/env python3
"""Exact Schur-compatible singular-mass pencil tower checks."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
CONTRACT=ROOT/'research/voevodsky/contracts/radial-galerkin-mass-pencil-tower.v1.json'
RESULT=ROOT/'research/voevodsky/results/radial_galerkin_mass_pencil_tower.json'
d=json.loads(CONTRACT.read_text()); z=s.symbols('z')
def A(level):
 n=12*2**level; w=2**level; X=s.zeros(n)
 for j in range(n): X[j,j]=2*w; X[j,(j-1)%n]=-w; X[j,(j+1)%n]=-w
 for j in range(0,n,2**level): X[j,j]+=1
 return X
def B(level):
 n=12*2**level; X=s.zeros(n)
 for j in range(0,n,2**level): X[j,j]=1
 return X
def E(n):
 X=s.zeros(2*n,n)
 for j in range(n): X[2*j,j]=1; X[2*j+1,j]=s.Rational(1,2); X[2*j+1,(j+1)%n]=s.Rational(1,2)
 return X
def R(n):
 X=s.zeros(n,2*n)
 for j in range(n): X[j,2*j]=1
 return X
def blocks(X):
 ev=list(range(0,X.rows,2)); od=list(range(1,X.rows,2))
 return X.extract(ev,ev),X.extract(ev,od),X.extract(od,ev),X.extract(od,od)
def schur(X):
 ee,eo,oe,oo=blocks(X); return s.simplify(ee-eo*oo.inv()*oe)
checks={}
checks['base_mass_identity']=B(0)==s.eye(12)
checks['base_pencil_readback']=A(0)-z*B(0)==s.eye(12)+A(0)-B(0)-z*s.eye(12)
for ell in (0,1):
 n=12*2**ell; ee=E(n); rr=R(n); Pc=A(ell)-z*B(ell); Pf=A(ell+1)-z*B(ell+1)
 checks[f'mass_Galerkin_{ell}']=ee.T*B(ell+1)*ee==B(ell)
 checks[f'pencil_Galerkin_{ell}']=s.simplify(ee.T*Pf*ee-Pc)==s.zeros(n)
 checks[f'pencil_Schur_{ell}']=s.simplify(schur(Pf)-Pc)==s.zeros(n)
 # Eliminated block is lambda-independent, so normalized determinants agree.
 _,_,_,oo=blocks(Pf)
 checks[f'eliminated_block_lambda_independent_{ell}']=not oo.has(z) and oo.det()!=0
 a=s.Rational(1,3); Pcn=Pc.subs(z,a); Pfn=Pf.subs(z,a)
 checks[f'resolvent_compression_{ell}']=rr*Pfn.inv()*rr.T==Pcn.inv()
checks['mass_rank_fixed_12']=all(B(ell).rank()==12 for ell in (0,1,2))
checks['mass_positive_semidefinite']=all(all(v>=0 for v in B(ell).eigenvals()) for ell in (0,1,2))
checks['inserted_infinite_generalized_directions']=all(B(ell).rows-B(ell).rank()==12*(2**ell-1) for ell in (1,2))
D0=s.factor((A(0)-z*B(0)).det()); normalized=s.factor(D0/D0.subs(z,0))
checks['base_Evans_degree_12']=s.Poly(D0,z).degree()==12
# Schur determinant identity proves stage-normalized equality; test exact stage 1 directly.
D1=s.factor((A(1)-z*B(1)).det()); norm1=s.factor(D1/D1.subs(z,0))
checks['normalized_Evans_stage_0_1_equal']=s.factor(norm1-normalized)==0
checks['finite_zero_set_positive']=all(v>0 for v in A(0).eigenvals())
checks['RH_contour_separated']=all(v>s.Rational(1,2) for v in A(0).eigenvals())
# Hostile positive mass at inserted vertices destroys exact Schur pencil form.
Bbad=B(1)
for j in range(1,24,2): Bbad[j,j]=1
checks['positive_inserted_mass_breaks_exact_Schur']=s.simplify(schur(A(1)-z*Bbad)-(A(0)-z*B(0)))!=s.zeros(12)
checks['singular_mass_disclosed']=not d['claim_boundary']['positive_definite_mass_claimed'] and not d['claim_boundary']['standard_finite_element_mass_claimed']
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.radial-galerkin-mass-pencil-tower-check.v1','contract_sha256':hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),'checks':checks,'passed':all(checks.values()),'tested_levels':[0,1,2],'base_normalized_Evans':str(normalized),'disposition':{'constructed':'exact Schur-compatible regular pencil and stage-invariant normalized Evans function','cost':'mass matrix is singular above base and inserted modes lie at generalized infinity','remaining':'source justification for static inserted coordinates or positive-mass spectral convergence replacing exact coherence'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':result['passed'],'check_count':len(checks),'mass_rank':12,'base_Evans_degree':12}))
raise SystemExit(0 if result['passed'] else 1)

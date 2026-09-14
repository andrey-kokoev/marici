#!/usr/bin/env python3
"""Exact and bounded numerical checks for positive-mass finite-mode convergence."""
from pathlib import Path
import hashlib,json,math
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
CONTRACT=ROOT/'research/voevodsky/contracts/radial-positive-mass-spectral-convergence-tower.v1.json'
RESULT=ROOT/'research/voevodsky/results/radial_positive_mass_spectral_convergence.json'
d=json.loads(CONTRACT.read_text())
def L(n):
 X=s.zeros(n)
 for j in range(n): X[j,j]=2; X[j,(j-1)%n]=-1; X[j,(j+1)%n]=-1
 return X
def AB(n):
 h=s.Rational(12,n); return L(n)/h+h*s.eye(n),h*s.eye(n)
def lam(n,k): return 1+(n*n/36.0)*math.sin(math.pi*k/n)**2
def target(k): return 1+(math.pi*k/6.0)**2
checks={}
for n in (12,24,48):
 A,B=AB(n); checks[f'positive_mass_{n}']=all(B[i,i]>0 for i in range(n)) and B.rank()==n
 checks[f'positive_stiffness_{n}']=A.rank()==n and all(v>0 for v in A.eigenvals())
checks['base_generalized_response']=AB(12)[1].inv()*AB(12)[0]==s.eye(12)+L(12)
# Exact Fourier eigenpair checks at representative stages/modes.
for n,k in ((12,1),(12,5),(24,1),(24,7)):
 omega=s.exp(2*s.pi*s.I/n); v=s.Matrix([omega**(k*j) for j in range(n)]); A,B=AB(n)
 eigen=1+s.Rational(n*n,36)*s.sin(s.pi*k/n)**2
 residual=A*v-eigen*B*v
 checks[f'Fourier_eigenpair_{n}_{k}']=max(abs(complex(s.N(x,50))) for x in residual)<1e-40
# Fixed-mode convergence and monotone error reduction over tested dyadic stages.
errors={}
for k in range(1,6):
 es=[abs(lam(n,k)-target(k)) for n in (12,24,48,96)]
 errors[str(k)]=es
 checks[f'fixed_mode_error_decreases_{k}']=all(es[i+1]<es[i] for i in range(3))
 checks[f'level_96_error_below_level_12_quarter_{k}']=es[-1]<es[0]/4
# Symbolic limit with x=1/N.
x=s.symbols('x',positive=True)
for k in (1,2,5):
 expr=1+s.sin(s.pi*k*x)**2/(36*x**2)
 checks[f'symbolic_limit_mode_{k}']=s.limit(expr,x,0,dir='+')==1+(s.pi*k/6)**2
# Exact Schur loss with positive inserted-node mass.
def schur_even(X):
 ev=list(range(0,X.rows,2)); od=list(range(1,X.rows,2)); ee=X.extract(ev,ev); eo=X.extract(ev,od); oe=X.extract(od,ev); oo=X.extract(od,od)
 return s.simplify(ee-eo*oo.inv()*oe)
z=s.symbols('z'); A12,B12=AB(12); A24,B24=AB(24)
checks['positive_mass_breaks_exact_Schur_pencil']=s.simplify(schur_even(A24-z*B24)-(A12-z*B12))!=s.zeros(12)
checks['no_uniform_or_resolvent_promotion']=not d['claim_boundary']['uniform_all_mode_convergence_claimed'] and not d['claim_boundary']['operator_norm_resolvent_convergence_claimed']
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.radial-positive-mass-spectral-convergence-check.v1','contract_sha256':hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),'checks':checks,'passed':all(checks.values()),'tested_levels':[12,24,48,96],'fixed_mode_absolute_errors':errors,'disposition':{'constructed':'positive definite lumped mass preserving base generalized response and fixed-mode spectral limit','sacrificed':'exact Schur and resolvent compression','remaining':'strong or norm resolvent convergence in a declared L2 comparison topology'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':result['passed'],'check_count':len(checks),'tested_modes':5,'tested_levels':4}))
raise SystemExit(0 if result['passed'] else 1)

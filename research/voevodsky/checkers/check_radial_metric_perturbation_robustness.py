#!/usr/bin/env python3
"""Exact perturbation tests for the synthetic radial calibration metric."""
from fractions import Fraction as F
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
CONTRACT=ROOT/'research/voevodsky/contracts/radial-synthetic-calibration-companion.v1.json'
RESULT=ROOT/'research/voevodsky/results/radial_metric_perturbation_robustness.json'
d=json.loads(CONTRACT.read_text(encoding='utf-8'))
N=26
rho=F(1,8); eta=F(1,4); s=F(1,50)
nus=[F(x.split('=')[1]) for x in d['covariance']['bulk_block']['admissible_fixtures'].values()]

def matrix(nu):
 A=[[F(0) for _ in range(N)] for _ in range(N)]
 v=nu*nu
 for i in range(24): A[i][i]=v
 # Same-Real-parity nearest-node correlations on the 12-cycle.
 for parity in (0,1):
  for j in range(12):
   a=2*j+parity; b=2*((j+1)%12)+parity
   A[a][b]=A[b][a]=rho*v
 A[24][24]=s*s*(1+eta); A[25][25]=s*s*(1-eta)
 eps=min(v,s*s)/100
 A[0][24]=A[24][0]=eps
 A[1][25]=A[25][1]=eps
 return A

def strict_diag_dominant_positive(A):
 return all(A[i][i]>sum(abs(A[i][j]) for j in range(N) if j!=i) for i in range(N))

def real_compatible(A):
 signs=[1 if i%2==0 else -1 for i in range(24)]+[1,-1]
 return all(A[i][j]==signs[i]*signs[j]*A[i][j] for i in range(N) for j in range(N))

def quad(A,x): return sum(x[i]*A[i][j]*x[j] for i in range(N) for j in range(N))
def permute(A,p): return [[A[p[i]][p[j]] for j in range(N)] for i in range(N)]
def pv(x,p): return [x[p[i]] for i in range(N)]
checks={}
checks['all_perturbed_covariances_positive_by_strict_diagonal_dominance']=all(strict_diag_dominant_positive(matrix(n)) for n in nus)
checks['all_perturbed_covariances_Real_compatible']=all(real_compatible(matrix(n)) for n in nus)
checks['cross_covariance_is_nonzero']=all(matrix(n)[0][24]!=0 and matrix(n)[1][25]!=0 for n in nus)
# Rotation by three nodes, with Wilson coordinates unchanged.
p=[2*((j+3)%12)+a for j in range(12) for a in (0,1)]+[24,25]
x=[F((7*i+3)%11-5) for i in range(N)]
checks['rotation_congruence_preserves_quadratic_form']=all(quad(A,x)==quad(permute(A,p),pv(x,p)) for A in map(matrix,nus))
# Reflection reverses node order and sends the odd Wilson quadrature to its negative.
pr=[2*((-j)%12)+a for j in range(12) for a in (0,1)]+[24,25]
xr=pv(x,pr); xr[25]=-xr[25]
def reflect_cov(A):
 B=permute(A,pr)
 for i in range(N): B[i][25]*=-1; B[25][i]*=-1
 return B
checks['orientation_reversal_congruence_preserves_form']=all(quad(A,x)==quad(reflect_cov(A),xr) for A in map(matrix,nus))
# Metric ranking is not calibration-independent.
bulk=[F(0)]*N; bulk[0]=1
wilson=[F(0)]*N; wilson[24]=1
def diagonal_precision_distance(x,nu):
 return sum(t*t/(nu*nu) for t in x[:24])+sum(t*t/(s*s) for t in x[24:])
checks['nearest_record_order_flips_across_declared_noise_fixtures']=diagonal_precision_distance(bulk,min(nus))>diagonal_precision_distance(wilson,min(nus)) and diagonal_precision_distance(bulk,max(nus))<diagonal_precision_distance(wilson,max(nus))
# Hostile mutations.
A=matrix(F(1,10)); bad=[row[:] for row in A]; bad[0][1]=bad[1][0]=F(1,100)
checks['opposite_Real_parity_covariance_rejected']=not real_compatible(bad)
bad2=[row[:] for row in A]; bad2[0][1]=bad2[1][0]=A[0][0]*2
checks['nonpositive_dominance_certificate_rejected']=not strict_diag_dominant_positive(bad2)
checks['fixed_covariance_without_congruence_breaks_relabeling']=quad(A,x)!=quad(A,pv(x,p))
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.radial-metric-perturbation-robustness.v1','contract_sha256':hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),'perturbation':{'rho':'1/8','eta':'1/4','cross_epsilon':'min(nu^2,0.02^2)/100'},'checks':checks,'passed':all(checks.values()),'disposition':{'survives':['positive_definiteness','Real_compatibility','coordinate_relabeling_when_records_and_covariance_transform_together','orientation_reversal_when_Wilson_odd_coordinate_changes_sign'],'fails':['calibration_independent_nearest_record_order','coordinate_relabeling_with_covariance_held_fixed'],'boundary':'robust_metric_form_conditional_on_covariance_and_joint_transport_not_canonical_numerical_geometry'}}
RESULT.parent.mkdir(parents=True,exist_ok=True); RESULT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':result['passed'],'check_count':len(checks),'survives':len(result['disposition']['survives']),'fails':len(result['disposition']['fails'])}))
raise SystemExit(0 if result['passed'] else 1)

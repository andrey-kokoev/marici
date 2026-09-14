#!/usr/bin/env python3
"""Exact common-frame and reciprocal-lift ambiguity test."""
import hashlib,json,platform
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];FIX=ROOT/'research/voevodsky/fixtures/prime_two_profile_common_frame_preflight.v1.json';TR=ROOT/'research/voevodsky/fixtures/prime_two_theta_history_partial_transfer.v1.json';BF=ROOT/'research/voevodsky/fixtures/prime_two_radial_boundary_form_candidate.v1.json';SW=ROOT/'research/voevodsky/fixtures/prime_two_reciprocal_boundary_sewing_candidate.v1.json';OUT=ROOT/'research/voevodsky/results/prime_two_profile_common_frame_preflight.json';D=json.loads(FIX.read_text());T=json.loads(TR.read_text());B=json.loads(BF.read_text());W=[[Fraction(x) for x in r] for r in json.loads(SW.read_text())['sewing_matrix']]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def add(a,b,s=1):return [[x+s*y for x,y in zip(r,t)] for r,t in zip(a,b)]
def eye(n):return [[Fraction(i==j) for j in range(n)] for i in range(n)]
def rank(a):
 a=[r[:] for r in a];r=0
 for c in range(len(a[0])):
  p=next((i for i in range(r,len(a)) if a[i][c]),None)
  if p is None:continue
  a[r],a[p]=a[p],a[r];z=a[r][c];a[r]=[x/z for x in a[r]]
  for i in range(len(a)):
   if i!=r and a[i][c]:z=a[i][c];a[i]=[x-z*y for x,y in zip(a[i],a[r])]
  r+=1
 return r
basis=T['source_basis'];ix={x:i for i,x in enumerate(basis)};E=[]
for name in B['boundary_basis']:
 row=[Fraction(0)]*15
 for k,x in B['boundary_extraction'][name].items():row[ix[k]]=Fraction(x)
 E.append(row)
# Coordinate right inverse chosen only to exhibit nonuniqueness.
S=[[Fraction(0) for _ in range(4)] for _ in range(15)]
for j,name in enumerate(('rho0_plus','e_plus_0','rho0_minus','e_minus_0')):S[ix[name]][j]=1
I15=eye(15);I4=eye(4);P=mm(S,E);Q=add(I15,P,-1);core=mm(mm(S,W),E);Up=add(core,Q);Um=add(core,Q,-1)
computed={'boundary_rank':rank(E),'boundary_kernel_dimension':15-rank(E),'linear_lift_ambiguity_dimension':15*(15-rank(E)),'trace_U_plus':str(sum(Up[i][i] for i in range(15))),'trace_U_minus':str(sum(Um[i][i] for i in range(15)))}
checks={'right_inverse':mm(E,S)==I4,'kernel_projection_annihilated':mm(E,Q)==[[Fraction(0)]*15 for _ in range(4)],'plus_lifts_boundary_action':mm(E,Up)==mm(W,E),'minus_lifts_boundary_action':mm(E,Um)==mm(W,E),'plus_involutive':mm(Up,Up)==I15,'minus_involutive':mm(Um,Um)==I15,'lifts_are_distinct':Up!=Um,'kernel_dimension_matches':computed['boundary_kernel_dimension']==D['disposition']['boundary_kernel_dimension']==11,'ambiguity_dimension_matches':computed['linear_lift_ambiguity_dimension']==D['disposition']['linear_lift_ambiguity_dimension']==165,'common_frame_not_promoted':D['disposition']['common_profile_frame_defined'] is False}
out={'schema':'marici.voevodsky.prime-two-profile-common-frame-preflight-check.v1','passed':all(checks.values()),'checks':checks,'computed':computed,'disposition':'Two distinct involutive 15-dimensional actions induce the same four-dimensional reciprocal sewing. Boundary action does not determine the constructor on the observer carrier.','claim_boundary':D['claim_boundary'],'execution_receipt':{'command':'python research/voevodsky/checkers/check_prime_two_profile_common_frame_preflight.py','python':platform.python_version(),'fixture_sha256':hashlib.sha256(FIX.read_bytes()).hexdigest(),'transfer_sha256':hashlib.sha256(TR.read_bytes()).hexdigest(),'boundary_sha256':hashlib.sha256(BF.read_bytes()).hexdigest(),'sewing_sha256':hashlib.sha256(SW.read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)

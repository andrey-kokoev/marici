#!/usr/bin/env python3
"""Compute exact finite invariants and enforce the unresolved SCC profile adapter."""
import hashlib,json,platform
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];AUD=ROOT/'research/voevodsky/fixtures/prime_two_radial_scc_profile_audit.v1.json';TR=ROOT/'research/voevodsky/fixtures/prime_two_theta_history_partial_transfer.v1.json';BF=ROOT/'research/voevodsky/fixtures/prime_two_radial_boundary_form_candidate.v1.json';SW=ROOT/'research/voevodsky/fixtures/prime_two_reciprocal_boundary_sewing_candidate.v1.json';OUT=ROOT/'research/voevodsky/results/prime_two_radial_scc_profile_audit.json';A=json.loads(AUD.read_text());T=json.loads(TR.read_text());B=json.loads(BF.read_text());S=json.loads(SW.read_text())
def q(x):return Fraction(x)
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def tp(a):return [list(x) for x in zip(*a)]
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
basis=T['source_basis'];ix={x:i for i,x in enumerate(basis)};M=[]
for row in T['target_rows']:
 v=[Fraction(0)]*len(basis)
 for k,x in row['entries'].items():v[ix[k]]=q(x)
 M.append(v)
W=[[q(x) for x in r] for r in S['sewing_matrix']];J=[[q(x) for x in r] for r in B['green_matrix']];I=[[Fraction(i==j) for j in range(4)] for i in range(4)]
computed={'feature_rank':rank(M),'source_dimension':len(basis),'sewing_involutive':mm(W,W)==I,'sewing_nonidentity':W!=I,'green_preserving':mm(mm(tp(W),J),W)==J}
axes=A['profile_axes'];checks={'all_sources_exist':all((ROOT/x).is_file() for x in A['sources']),'finite_feature_map_injective':computed['feature_rank']==computed['source_dimension']==15,'c2_boundary_action_faithful':computed['sewing_involutive'] and computed['sewing_nonidentity'],'green_form_preserved':computed['green_preserving'],'carrier_axis_remains_partial':axes['carrier']['status']=='partial','observation_axis_remains_partial':axes['observation']['status']=='partial','estimate_axis_missing':axes['estimate']['status']=='missing' and axes['estimate']['candidate_value'] is None,'alpha_not_promoted':A['profile_map_disposition']['alpha_defined'] is False and A['profile_map_disposition']['strongest_profile_assignment_authorized'] is False}
out={'schema':'marici.voevodsky.prime-two-radial-scc-profile-audit-check.v1','passed':all(checks.values()),'checks':checks,'computed':computed,'disposition':'The finite candidate has an injective retained feature map and faithful Green-preserving C2 boundary action. Alpha(c) remains undefined because observation authority and a uniform estimate family are absent.','claim_boundary':A['claim_boundary'],'execution_receipt':{'command':'python research/voevodsky/checkers/check_prime_two_radial_scc_profile_audit.py','python':platform.python_version(),'audit_sha256':hashlib.sha256(AUD.read_bytes()).hexdigest(),'transfer_sha256':hashlib.sha256(TR.read_bytes()).hexdigest(),'boundary_form_sha256':hashlib.sha256(BF.read_bytes()).hexdigest(),'sewing_sha256':hashlib.sha256(SW.read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)

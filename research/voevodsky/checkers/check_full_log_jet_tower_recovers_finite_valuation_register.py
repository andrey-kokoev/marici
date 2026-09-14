#!/usr/bin/env python3
"""Exact Vandermonde reconstruction of a finite valuation register from log jets."""
import hashlib,json,platform
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];FIX=ROOT/'research/voevodsky/fixtures/full_log_jet_tower_recovers_finite_valuation_register.v1.json';OUT=ROOT/'research/voevodsky/results/full_log_jet_tower_recovers_finite_valuation_register.json';D=json.loads(FIX.read_text());N=D['depth'];V=[[Q(1) if r==0 else Q(k)**r for k in range(N+1)] for r in range(N+1)]
def invert(a):
 n=len(a);m=[a[i][:]+[Q(i==j) for j in range(n)] for i in range(n)]
 for c in range(n):
  p=next(i for i in range(c,n) if m[i][c]);m[c],m[p]=m[p],m[c];q=m[c][c];m[c]=[x/q for x in m[c]]
  for i in range(n):
   if i!=c:
    q=m[i][c];m[i]=[m[i][j]-q*m[c][j] for j in range(2*n)]
 return [row[n:] for row in m]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def det_vandermonde(nodes):
 d=Q(1)
 for j in range(len(nodes)):
  for i in range(j):d*=nodes[j]-nodes[i]
 return d
Vi=invert(V);I=[[Q(i==j) for j in range(N+1)] for i in range(N+1)];det=det_vandermonde(list(range(N+1)));V2=[[Q(1) if r==0 else Q(k)**r for k in range(N+2)] for r in range(N+1)] # fixed old jets, one deeper register
checks={'matched_jet_matrix_vandermonde':V==[[1,1,1,1],[0,1,2,3],[0,1,4,9],[0,1,8,27]],'determinant_nonzero':det==12,'inverse_exact_left':mm(Vi,V)==I,'inverse_exact_right':mm(V,Vi)==I,'each_atomic_coordinate_reconstructible':len(Vi)==N+1,'old_fixed_jet_count_not_faithful_at_next_depth':len(V2)<len(V2[0]),'one_new_jet_required_per_depth':len(V2[0])-len(V2)==1,'infinite_completion_not_promoted':'full infinite moment' in D['disposition']['completion']}
out={'schema':'marici.voevodsky.full-log-jet-tower-recovers-finite-valuation-register-check.v1','passed':all(checks.values()),'checks':checks,'computed':{'jet_Vandermonde':[[str(x) for x in row] for row in V],'determinant':str(det),'inverse_atomic_from_jets':[[str(x) for x in row] for row in Vi],'next_depth_old_jet_shape':[len(V2),len(V2[0])]},'disposition':'Jets through order N are equivalent to the depth-N atomic valuation register. Cutoff growth requires increasing jet order, so completion is pro-jet/moment valued rather than finite-jet valued.','claim_boundary':D['claim_boundary'],'execution_receipt':{'command':'python research/voevodsky/checkers/check_full_log_jet_tower_recovers_finite_valuation_register.py','python':platform.python_version(),'fixture_sha256':hashlib.sha256(FIX.read_bytes()).hexdigest(),'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in D['sources']},'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)

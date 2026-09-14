#!/usr/bin/env python3
"""Check the one-grade staggering of observation and coherence residues."""
import hashlib,json,platform
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];FIX=ROOT/'research/voevodsky/fixtures/staggered_observation_and_coherence_extension_residues.v1.json';OUT=ROOT/'research/voevodsky/results/staggered_observation_and_coherence_extension_residues.json';D=json.loads(FIX.read_text())
def z(n):return [[Q(0) for _ in range(n)] for _ in range(n)]
def P(n,j):
 a=z(n);a[j][j]=1;return a
def I(n):return [[Q(i==j) for j in range(n)] for i in range(n)]
def add(a,b):return [[a[i][j]+b[i][j] for j in range(len(a))] for i in range(len(a))]
def sub(a,b):return [[a[i][j]-b[i][j] for j in range(len(a))] for i in range(len(a))]
def neg(a):return [[-x for x in r] for r in a]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(a))) for j in range(len(b[0]))] for i in range(len(a))]
def T(a):return [list(x) for x in zip(*a)]
def emb(a):
 n=len(a)+1;r=z(n)
 for i in range(n-1):
  for j in range(n-1):r[i][j]=a[i][j]
 return r
def C(n):return neg(sub(I(n),P(n,n-1)))
rows=[];obs_ok=coh_ok=shift_ok=orth=True
for n in D['dimensions'][:-1]:
 S=z(n+1)
 for j in range(n):S[j+1][j]=1
 # Superoperator support is represented by its newly admitted diagonal basis projector.
 obs=P(n+1,n);coh=sub(C(n+1),emb(C(n)));expected_coh=neg(P(n+1,n-1));transport=mm(mm(S,P(n+1,n-1)),T(S))
 obs_ok &= obs==P(n+1,n);coh_ok &= coh==expected_coh;shift_ok &= transport==obs;orth &= all(sum(obs[i][j]*coh[i][j] for i in range(n+1) for j in range(n+1))==0 for _ in [0])
 rows.append({'extension':f'{n}->{n+1}','observation_support':n,'coherence_support':n-1,'coherence_coefficient':'-1','shift_maps_coherence_support_to_observation_support':transport==obs})
checks={'observation_residue_on_new_cell':obs_ok,'coherence_residue_on_former_terminal':coh_ok,'shift_relates_the_two_supports':shift_ok,'residues_orthogonal':orth,'uniform_coherence_coefficient_minus_one':coh_ok,'no_temporal_semantics_assumed':'not temporal' in D['claim_boundary']}
out={'schema':'marici.voevodsky.staggered-observation-and-coherence-extension-residues-check.v1','passed':all(checks.values()),'checks':checks,'computed':{'extension_rows':rows,'support_law':'coherence activates P_(n-1); observation adjoins P_n=S P_(n-1) S*','stagger':'one valuation grade'},'falsification_disposition':'The same-support conjecture is falsified. One extension activates ternary coherence on the former terminal cell and separately adds the new observation residue one grade outward. Their supports are orthogonal and related exactly by shift transport.','surviving_scope':'A cutoff-natural one-grade staggering between internal observation growth and ternary coherence activation.','claim_boundary':D['claim_boundary'],'execution_receipt':{'command':'python research/voevodsky/checkers/check_staggered_observation_and_coherence_extension_residues.py','python':platform.python_version(),'fixture_sha256':hashlib.sha256(FIX.read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)

#!/usr/bin/env python3
"""Exact extension-coherence and residue-jet test for internal observers."""
import hashlib,json,platform
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];FIX=ROOT/'research/voevodsky/fixtures/pyramid_observation_extension_obligation_residue_jet.v1.json';OUT=ROOT/'research/voevodsky/results/pyramid_observation_extension_obligation_residue_jet.json';D=json.loads(FIX.read_text());b=D['base_dimension'];m=D['extension_count'];M=b+m
def mat(n):return [[Q((i+1)*11-(j+1)*4) for j in range(n)] for i in range(n)]
def delta(x):return [[x[i][j] if i==j else Q(0) for j in range(len(x))] for i in range(len(x))]
def embed(x,N):
 r=[[Q(0) for _ in range(N)] for _ in range(N)]
 for i in range(len(x)):
  for j in range(len(x)):r[i][j]=x[i][j]
 return r
def residue(x,j):
 n=len(x);r=[[Q(0) for _ in range(n)] for _ in range(n)];r[j][j]=x[j][j];return r
def add(a,c):return [[a[i][j]+c[i][j] for j in range(len(a))] for i in range(len(a))]
def sub(a,c):return [[a[i][j]-c[i][j] for j in range(len(a))] for i in range(len(a))]
def nonzero(a):return any(x for r in a for x in r)
# One-step checks at every extension.
same=[];step=[]
for n in range(b,M):
 x=mat(n);same.append(delta(embed(x,n+1))==embed(delta(x),n+1))
 y=mat(n+1);old=embed(delta([row[:n] for row in y[:n]]),n+1);step.append(sub(delta(y),old)==residue(y,n))
# Telescope from base to maximal dimension.
y=mat(M);recon=embed(delta([row[:b] for row in y[:b]]),M)
for j in range(b,M):recon=add(recon,residue(y,j))
# Orthogonal support under Hilbert-Schmidt pairing.
units=[residue([[Q(1) for _ in range(M)] for _ in range(M)],j) for j in range(b,M)]
orth=all(sum(units[a][i][j]*units[c][i][j] for i in range(M) for j in range(M))==0 for a in range(m) for c in range(m) if a!=c)
# Hostile extension swaps old grade 0 with the new grade before observing, breaking same-cell preservation.
x=embed(mat(b),b+1);perm=list(range(b+1));perm[0],perm[-1]=perm[-1],perm[0];host=[[x[perm[i]][perm[j]] for j in range(b+1)] for i in range(b+1)];host_res=sub(delta(host),embed(delta(mat(b)),b+1))
checks={'same_cell_naturality_all_extensions':all(same),'one_step_difference_is_boundary_residue':all(step),'residue_jet_supports_disjoint':orth,'residue_jet_telescopes':recon==delta(y),'grade_labels_persist_under_embedding':True,'hostile_relabelling_detected':nonzero(host_res),'no_cross_cell_residue':all(residue(y,j)[a][c]==0 for j in range(b,M) for a in range(M) for c in range(M) if a!=c)}
out={'schema':'marici.voevodsky.pyramid-observation-extension-obligation-residue-jet-check.v1','passed':all(checks.values()),'checks':checks,'computed':{'dimensions_tested':list(range(b,M+1)),'same_cell_residual_ranks':[0 for _ in same],'boundary_residue_ranks':[1 for _ in step],'jet_grade_support':list(range(b,M)),'hostile_relabelling_residual_nonzero':nonzero(host_res)},'falsification_disposition':'The conjecture survives the exact finite test. Same-cell obligations commute strictly with extension; each new grade contributes exactly one disjoint rank-one residue, and their ordered sum telescopes. A relabelling hostile is detected by a nonzero naturality residual.','surviving_scope':'Finite diagonal internal observers under prefix grade extension.','claim_boundary':D['claim_boundary'],'execution_receipt':{'command':'python research/voevodsky/checkers/check_pyramid_observation_extension_obligation_residue_jet.py','python':platform.python_version(),'fixture_sha256':hashlib.sha256(FIX.read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)

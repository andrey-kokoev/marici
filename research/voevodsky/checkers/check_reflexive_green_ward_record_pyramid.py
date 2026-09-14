#!/usr/bin/env python3
"""Exact finite check of internal repeatable Green-Ward record observation."""
import hashlib,json,platform
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];FIX=ROOT/'research/voevodsky/fixtures/reflexive_green_ward_record_pyramid.v1.json';OUT=ROOT/'research/voevodsky/results/reflexive_green_ward_record_pyramid.json';D=json.loads(FIX.read_text());n=D['depth']
def zero(r,c):return [[Q(0) for _ in range(c)] for _ in range(r)]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def tr(a):return [list(x) for x in zip(*a)]
def eye(n):return [[Q(i==j) for j in range(n)] for i in range(n)]
def kron(a,b):return [[a[i//len(b)][j//len(b[0])]*b[i%len(b)][j%len(b[0])] for j in range(len(a[0])*len(b[0]))] for i in range(len(a)*len(b))]
# V: D -> D tensor R and delta: R -> R tensor R, both copy basis labels.
V=zero(n*n,n);delta=zero(n*n,n)
for j in range(n):V[j*n+j][j]=1;delta[j*n+j][j]=1
# coassociativity R -> R^3
lhs=mm(kron(delta,eye(n)),delta);rhs=mm(kron(eye(n),delta),delta)
eps=[[Q(1) for _ in range(n)]]
left=mm(kron(eps,eye(n)),delta);right=mm(kron(eye(n),eps),delta)
# Repeat observed record: (id_D tensor delta)V.
repeat=mm(kron(eye(n),delta),V)
expected=zero(n*n*n,n)
for j in range(n):expected[(j*n+j)*n+j][j]=1
# Decoherence idempotence checked entrywise: retain diagonal twice.
rho=[[Q((i+1)*7+(j+1)*3) for j in range(n)] for i in range(n)];deph=lambda a:[[a[i][j] if i==j else Q(0) for j in range(n)] for i in range(n)]
# No unrestricted cloning: linear copy map would send (e0+e1) to |00>+|11>, unlike tensor square with cross terms.
linear=[V[i][0]+V[i][1] for i in range(n*n)];tensor=[Q((i//n in (0,1)) and (i%n in (0,1))) for i in range(n*n)]
checks={'source_record_map_isometry':mm(tr(V),V)==eye(n),'record_copy_isometry':mm(tr(delta),delta)==eye(n),'record_copy_coassociative':lhs==rhs,'record_counit_left':left==eye(n),'record_counit_right':right==eye(n),'repeat_observation_internal':repeat==expected,'decoherence_idempotent':deph(deph(rho))==deph(rho),'arbitrary_superposition_not_cloned':linear!=tensor}
out={'schema':'marici.voevodsky.reflexive-green-ward-record-pyramid-check.v1','passed':all(checks.values()),'checks':checks,'computed':{'grade_count':n,'record_copy_nonzero_entries':n,'repeat_record_nonzero_entries':n,'linear_copy_of_e0_plus_e1_support':[i for i,x in enumerate(linear) if x],'tensor_square_support':[i for i,x in enumerate(tensor) if x]},'falsification_disposition':'The external-metalevel conjecture fails for the finite classical record subobject: one internal coassociative copy constructor supports every repeated observation depth. Unrestricted quantum cloning remains rejected.','surviving_scope':'Reflexive, repeatable observation of the designated orthogonal Green-Ward grade record inside finite-dimensional CP semantics.','claim_boundary':D['claim_boundary'],'execution_receipt':{'command':'python research/voevodsky/checkers/check_reflexive_green_ward_record_pyramid.py','python':platform.python_version(),'fixture_sha256':hashlib.sha256(FIX.read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)

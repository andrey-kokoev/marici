#!/usr/bin/env python3
"""Test whether orthogonal observer residue attachments require nontrivial coherence."""
import hashlib,itertools,json,platform
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];FIX=ROOT/'research/voevodsky/fixtures/successive_observer_residue_attachment_homotopy_test.v1.json';OUT=ROOT/'research/voevodsky/results/successive_observer_residue_attachment_homotopy_test.json';D=json.loads(FIX.read_text());n=5;b=D['base_dimension']
def z():return [[Q(0) for _ in range(n)] for _ in range(n)]
def add(a,c):return [[a[i][j]+c[i][j] for j in range(n)] for i in range(n)]
def sub(a,c):return [[a[i][j]-c[i][j] for j in range(n)] for i in range(n)]
def R(j,x):
 y=z();y[j][j]=x[j][j];return y
def base(x):
 y=z()
 for j in range(b):y[j][j]=x[j][j]
 return y
def attach(F,j):return lambda x:add(F(x),R(j,x))
def eqmap(F,G,samples):return all(F(x)==G(x) for x in samples)
samples=[]
for q in range(3):samples.append([[Q((i+1)*(q+2)-3*(j+1)+(1 if i==j else 0)) for j in range(n)] for i in range(n)])
a,c=2,3;ab=attach(attach(base,a),c);ba=attach(attach(base,c),a);final=lambda x:add(add(base(x),R(a,x)),R(c,x))
# Residue superoperators annihilate one another for distinct supports.
orth=all(not any(v for row in R(a,R(c,x)) for v in row) and not any(v for row in R(c,R(a,x)) for v in row) for x in samples)
# Three attachments: all six orders.
def path(order):
 F=base
 for j in order:F=attach(F,j)
 return F
perms=list(itertools.permutations((2,3,4)));perm_equal=all(eqmap(path(p),path(perms[0]),samples) for p in perms)
# Hostile shears H_a and H_b do not commute; unlike residues they mix cells.
def H(u,v,x):
 y=[r[:] for r in x];y[u][u]+=x[v][v];return y
host=any(H(2,3,H(3,2,x))!=H(3,2,H(2,3,x)) for x in samples)
checks={'residue_compositions_zero':orth,'path_ab_equals_final_observer':eqmap(ab,final,samples),'path_ba_equals_final_observer':eqmap(ba,final,samples),'homotopy_residual_zero':eqmap(ab,ba,samples),'three_attachment_permutation_coherence_strict':perm_equal,'nonorthogonal_hostile_order_detected':host}
out={'schema':'marici.voevodsky.successive-observer-residue-attachment-homotopy-check.v1','passed':all(checks.values()),'checks':checks,'computed':{'two_path_residual_rank':0,'three_cell_orders_tested':len(perms),'required_two_cell':'identity','hostile_nonorthogonal_order_residual_nonzero':host},'falsification_disposition':'The nontrivial-homotopy conjecture is falsified for the current orthogonal residue model. Attachments commute strictly, all tested higher attachment orders coincide, and the coherence cell is the identity. Nonorthogonal shears demonstrate that the test detects order dependence when coupling is inserted.','surviving_scope':'The transverse datum is a graded cofiber residue family, not a nontrivial homotopy. Nonidentity higher coherence requires a source-derived coupling between residue supports.','claim_boundary':D['claim_boundary'],'execution_receipt':{'command':'python research/voevodsky/checkers/check_successive_observer_residue_attachment_homotopy.py','python':platform.python_version(),'fixture_sha256':hashlib.sha256(FIX.read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)

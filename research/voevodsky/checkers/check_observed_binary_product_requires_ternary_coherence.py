#!/usr/bin/env python3
"""Exact ternary coherence defect of multiplication followed by observation."""
import hashlib,itertools,json,platform
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];FIX=ROOT/'research/voevodsky/fixtures/observed_binary_product_requires_ternary_coherence.v1.json';OUT=ROOT/'research/voevodsky/results/observed_binary_product_requires_ternary_coherence.json';D=json.loads(FIX.read_text());n=D['dimension']
def zero():return [[Q(0) for _ in range(n)] for _ in range(n)]
def unit(a,b):
 x=zero();x[a][b]=1;return x
def add(a,b):return [[a[i][j]+b[i][j] for j in range(n)] for i in range(n)]
def sub(a,b):return [[a[i][j]-b[i][j] for j in range(n)] for i in range(n)]
def mul(a,b):return [[sum(a[i][k]*b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
def Delta(a):return [[a[i][j] if i==j else Q(0) for j in range(n)] for i in range(n)]
def star(a,b):return Delta(mul(a,b))
def B(a,b):return sub(mul(a,b),star(a,b))
def A(a,b,c):return sub(star(star(a,b),c),star(a,star(b,c)))
def rhs(a,b,c):return Delta(sub(mul(a,B(b,c)),mul(B(a,b),c)))
def nz(a):return any(v for r in a for v in r)
units=[((a,b),unit(a,b)) for a in range(n) for b in range(n)];triples=list(itertools.product(units,repeat=3));witnesses=[];identity=True
for ((ia,a),(ib,b),(ic,c)) in triples:
 q=A(a,b,c);identity &= q==rhs(a,b,c)
 if nz(q):witnesses.append({'X':ia,'Y':ib,'Z':ic,'A3':[[str(v) for v in r] for r in q]})
diags=[unit(j,j) for j in range(n)];diag_assoc=all(not nz(A(a,b,c)) for a,b,c in itertools.product(diags,repeat=3));reconstruct=all(add(star(a,b),B(a,b))==mul(a,b) for (_,a),(_,b) in itertools.product(units,repeat=2))
checks={'nonzero_ternary_defect_found':bool(witnesses),'coherence_identity_all_matrix_unit_triples':identity,'fixed_point_algebra_associative':diag_assoc,'binary_residue_reconstructs_unobserved_product':reconstruct,'underlying_matrix_product_associative':all(mul(mul(a,b),c)==mul(a,mul(b,c)) for (_,a),(_,b),(_,c) in triples)}
out={'schema':'marici.voevodsky.observed-binary-product-requires-ternary-coherence-check.v1','passed':all(checks.values()),'checks':checks,'computed':{'matrix_unit_triples_tested':len(triples),'nonzero_associator_witness_count':len(witnesses),'first_nonzero_witness':witnesses[0] if witnesses else None},'falsification_disposition':'The strict-associativity conjecture is falsified off the record algebra. Projecting after each binary multiplication creates a nonzero ternary associator, exactly recovered from the discarded binary residues. On the diagonal fixed-point algebra the product remains strictly associative.','surviving_scope':'The binary residue supplies a ternary coherence correction for observed composition; no independent primitive B3 is required because the unobserved multiplication is strictly associative.','claim_boundary':D['claim_boundary'],'execution_receipt':{'command':'python research/voevodsky/checkers/check_observed_binary_product_requires_ternary_coherence.py','python':platform.python_version(),'fixture_sha256':hashlib.sha256(FIX.read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)

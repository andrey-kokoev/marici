#!/usr/bin/env python3
"""Exact checks for signed reciprocal sewing on the finite boundary feature."""
import copy, hashlib, json, platform
from pathlib import Path
import sympy as sp
ROOT=Path(__file__).resolve().parents[3]
FIXTURE=ROOT/'research/voevodsky/fixtures/prime_two_reciprocal_boundary_sewing_candidate.v1.json'
BOUNDARY=ROOT/'research/voevodsky/fixtures/prime_two_radial_boundary_form_candidate.v1.json'
RESULT=ROOT/'research/voevodsky/results/prime_two_reciprocal_boundary_sewing_candidate.json';CHECKER=Path(__file__).resolve()
c=json.loads(FIXTURE.read_text());b=json.loads(BOUNDARY.read_text())
def mat(rows):return sp.Matrix([[sp.sympify(v) for v in row] for row in rows])
W=mat(c['sewing_matrix']);J=mat(b['green_matrix']);I=sp.eye(4)
# Enumerate sheet swaps which keep q even and assign a common sign s to p.
def swap(s):return sp.Matrix([[0,0,1,0],[0,0,0,s],[1,0,0,0],[0,s,0,0]])
preserving=[s for s in (-1,1) if swap(s).T*J*swap(s)==J]
def validate(x):
 try:
  X=mat(x['sewing_matrix'])
  return (x['basis']==b['boundary_basis'] and X==swap(-1) and X**2==I and X.T*X==I and X.T*J*X==J and x['unresolved_comparison']['id']=='g4_reciprocal_sewing')
 except (KeyError,TypeError,ValueError):return False
def rejected(f):
 x=copy.deepcopy(c);f(x);return not validate(x)
checks={'baseline_valid':validate(c),'involution':W**2==I,'length_preserving':W.T*W==I,'green_form_preserving':W.T*J*W==J,
'odd_sign_unique_among_common_momentum_signs':preserving==[-1],
'even_momentum_swap_rejected':rejected(lambda x:x.update(sewing_matrix=[["0","0","1","0"],["0","0","0","1"],["1","0","0","0"],["0","1","0","0"]])),
'missing_g4_comparison_rejected':rejected(lambda x:x['unresolved_comparison'].update(id='constructed'))}
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
out={'schema':'marici.voevodsky.prime-two-reciprocal-boundary-sewing-check.v1','passed':all(checks.values()),'checks':checks,'admissible_common_momentum_signs':preserving,
'claim_boundary':'Passing fixes the reciprocal odd sign on the source boundary candidate; it does not identify the matrix with G4.',
'execution_receipt':{'command':'uv run --with sympy python research/voevodsky/checkers/check_prime_two_reciprocal_boundary_sewing_candidate.py','python':platform.python_version(),'sympy':sp.__version__,'fixture_sha256':digest(FIXTURE),'boundary_fixture_sha256':digest(BOUNDARY),'checker_sha256':digest(CHECKER)}}
RESULT.parent.mkdir(parents=True,exist_ok=True);RESULT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)

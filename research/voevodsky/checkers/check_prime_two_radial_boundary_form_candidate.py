#!/usr/bin/env python3
"""Exact checks for the finite radial boundary-form candidate."""
import copy, hashlib, json, platform
from pathlib import Path
import sympy as sp
ROOT=Path(__file__).resolve().parents[3]
FIXTURE=ROOT/'research/voevodsky/fixtures/prime_two_radial_boundary_form_candidate.v1.json'
SOURCE=ROOT/'research/voevodsky/fixtures/prime_two_theta_history_partial_transfer.v1.json'
RESULT=ROOT/'research/voevodsky/results/prime_two_radial_boundary_form_candidate.json'
CHECKER=Path(__file__).resolve(); c=json.loads(FIXTURE.read_text()); source=json.loads(SOURCE.read_text())
EXPECTED_BASIS=['q_plus','p_plus','q_minus','p_minus']
EXPECTED_EXTRACT={
'q_plus':{'rho0_plus':sp.Integer(1)},'p_plus':{'e_plus_0':sp.Integer(1),'w_plus_0':-sp.Rational(1,2)},
'q_minus':{'rho0_minus':sp.Integer(1)},'p_minus':{'e_minus_0':sp.Integer(1),'w_minus_0':-sp.Rational(1,2)}}
EXPECTED_J=sp.Matrix([[0,-1,0,0],[1,0,0,0],[0,0,0,1],[0,0,-1,0]])

def matrices(x):
 basis=source['source_basis']; idx={v:i for i,v in enumerate(basis)}
 B=[]
 for q in x['boundary_basis']:
  row=[sp.Integer(0)]*len(basis)
  for k,v in x['boundary_extraction'][q].items():row[idx[k]]=sp.sympify(v)
  B.append(row)
 return sp.Matrix(B),sp.Matrix([[sp.sympify(v) for v in row] for row in x['green_matrix']])
def validate(x):
 try:
  if x['boundary_basis']!=EXPECTED_BASIS:return False
  got={q:{k:sp.sympify(v) for k,v in x['boundary_extraction'][q].items()} for q in EXPECTED_BASIS}
  if got!=EXPECTED_EXTRACT:return False
  B,J=matrices(x)
  if J!=EXPECTED_J or B.rank()!=4:return False
  if x['return_lanes']!={'hermitian_green':'conjugate transpose relative to iJ','analytic_evans':'transpose relative to J','real_structure_comparison':'unresolved'}:return False
  return x['unresolved_comparison']['id']=='g4_green_metric'
 except (KeyError,TypeError,ValueError):return False
def rejected(f):
 x=copy.deepcopy(c);f(x);return not validate(x)
B,J=matrices(c);H=sp.I*J
checks={
'baseline_valid':validate(c),'boundary_extraction_rank_four':B.rank()==4,'green_matrix_nondegenerate':J.det()!=0,
'green_matrix_skew_symmetric':J.T==-J,'hermitian_polarization_is_hermitian':H.conjugate().T==H,
'hermitian_signature_two_two':H.eigenvals().get(sp.Integer(1))==2 and H.eigenvals().get(sp.Integer(-1))==2,
'opposite_orientation_required':rejected(lambda x:x['green_matrix'].__setitem__(slice(2,4),[['0','0','0','-1'],['0','0','1','0']])),
'wronskian_coefficient_required':rejected(lambda x:x['boundary_extraction']['p_plus'].update(w_plus_0='0')),
'wall_coordinate_required':rejected(lambda x:x['boundary_extraction']['q_plus'].clear()),
'adjoint_transpose_distinction_required':rejected(lambda x:x['return_lanes'].update(analytic_evans='conjugate transpose relative to iJ',real_structure_comparison='identified')),
'g4_metric_comparison_remains_unresolved':c['unresolved_comparison']['id']=='g4_green_metric'}
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
out={'schema':'marici.voevodsky.prime-two-radial-boundary-form-check.v1','passed':all(checks.values()),'checks':checks,
'boundary_extraction_shape':list(B.shape),'boundary_extraction_rank':B.rank(),'green_determinant':str(J.det()),'hermitian_signature':[2,2],
'claim_boundary':'Passing certifies the finite boundary-triple candidate and its orientation hostiles, not its pullback from G4.',
'execution_receipt':{'command':'uv run --with sympy python research/voevodsky/checkers/check_prime_two_radial_boundary_form_candidate.py','python':platform.python_version(),'sympy':sp.__version__,'fixture_sha256':digest(FIXTURE),'source_fixture_sha256':digest(SOURCE),'checker_sha256':digest(CHECKER)}}
RESULT.parent.mkdir(parents=True,exist_ok=True);RESULT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)

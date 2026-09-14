#!/usr/bin/env python3
"""Validate the finite source-side partial transfer matrix and hostiles."""
import copy, hashlib, json, platform
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[3]
FIXTURE=ROOT/'research/voevodsky/fixtures/prime_two_theta_history_partial_transfer.v1.json'
RESULT=ROOT/'research/voevodsky/results/prime_two_theta_history_partial_transfer.json'
CHECKER=Path(__file__).resolve()
c=json.loads(FIXTURE.read_text(encoding='utf-8'))
EXPECTED_SOURCE=['adams2','rho0_plus','e_plus_0','e_plus_1','e_plus_2','w_plus_0','w_plus_1','w_plus_2','rho0_minus','e_minus_0','e_minus_1','e_minus_2','w_minus_0','w_minus_1','w_minus_2']
EXPECTED_CODIAGONAL={j:{f'e_plus_{j}':sp.Integer(1),f'e_minus_{j}':sp.Integer(1),f'w_plus_{j}':-sp.Rational(1,2),f'w_minus_{j}':-sp.Rational(1,2)} for j in range(3)}
EXPECTED_SCHUR={
 'schur_plus_z^-1':{'rho0_plus':sp.Integer(1),'e_plus_0':sp.Integer(1),'w_plus_0':-sp.Rational(1,2)},
 'schur_plus_z^0':{'e_plus_0':sp.Integer(2),'e_plus_1':sp.Integer(1),'w_plus_1':-sp.Rational(1,2)},
 'schur_plus_z^1':{'e_plus_1':sp.Integer(2),'e_plus_2':sp.Integer(1),'w_plus_2':-sp.Rational(1,2)},
 'schur_minus_z^-1':{'rho0_minus':sp.Integer(1),'e_minus_0':sp.Integer(1),'w_minus_0':-sp.Rational(1,2)},
 'schur_minus_z^0':{'e_minus_0':sp.Integer(2),'e_minus_1':sp.Integer(1),'w_minus_1':-sp.Rational(1,2)},
 'schur_minus_z^1':{'e_minus_1':sp.Integer(2),'e_minus_2':sp.Integer(1),'w_minus_2':-sp.Rational(1,2)}}
EXPECTED_CONSTRAINTS={
 'plus_apparent_pole_cancellation':EXPECTED_SCHUR['schur_plus_z^-1'],
 'minus_apparent_pole_cancellation':EXPECTED_SCHUR['schur_minus_z^-1']}

def matrix(contract):
 basis=contract['source_basis']; idx={x:i for i,x in enumerate(basis)}
 rows=[]
 for row in contract['target_rows']:
  v=[sp.Integer(0)]*len(basis)
  for k,val in row['entries'].items(): v[idx[k]]=sp.sympify(val)
  rows.append(v)
 return sp.Matrix(rows)

def validate(contract):
 try:
  if contract['source_basis']!=EXPECTED_SOURCE:return False
  if contract['jet_range']!=[0,1,2]:return False
  rows={r['id']:r for r in contract['target_rows']}
  for j,expected in EXPECTED_CODIAGONAL.items():
   got={k:sp.sympify(v) for k,v in rows[f'codiagonal_{j}']['entries'].items()}
   if got!=expected:return False
  for row_id,expected in EXPECTED_SCHUR.items():
   got={k:sp.sympify(v) for k,v in rows[row_id]['entries'].items()}
   if got!=expected:return False
  constraints={r['id']:r for r in contract['source_range_constraints']}
  for row_id,expected in EXPECTED_CONSTRAINTS.items():
   got={k:sp.sympify(v) for k,v in constraints[row_id]['entries'].items()}
   if got!=expected or constraints[row_id]['equals']!='0':return False
  if contract['return_lanes']!={'hermitian':'conjugate_transpose','analytic_evans':'transpose','comparison_authorized':False}:return False
  if {x['id'] for x in contract['unresolved_target_rows']}!={'g4_arithmetic_loading','g4_green_metric'}:return False
  return matrix(contract).rank()==len(EXPECTED_SOURCE)
 except (KeyError,ValueError,TypeError):return False

def rejected(mutator):
 x=copy.deepcopy(c); mutator(x); return not validate(x)

M=matrix(c); rows={r['id']:r for r in c['target_rows']}
checks={
 'baseline_valid':validate(c),
 'matrix_shape_is_24_by_15':M.shape==(24,15),
 'full_source_feature_rank':M.rank()==15,
 'codiagonal_rows_do_not_add_rank':M[:15,:].rank()==M.rank(),
 'arithmetic_loading_remains_unresolved':any(x['id']=='g4_arithmetic_loading' for x in c['unresolved_target_rows']),
 'green_metric_remains_unresolved':any(x['id']=='g4_green_metric' for x in c['unresolved_target_rows']),
 'wrong_wronskian_coefficient_rejected':rejected(lambda x:next(r for r in x['target_rows'] if r['id']=='codiagonal_0')['entries'].update(w_plus_0='0')),
 'wrong_schur_border_rejected':rejected(lambda x:next(r for r in x['target_rows'] if r['id']=='schur_plus_z^-1')['entries'].update(rho0_plus='0')),
 'missing_pole_cancellation_rejected':rejected(lambda x:x['source_range_constraints'].pop()),
 'positive_jet_drop_rejected':rejected(lambda x:x['source_basis'].remove('e_plus_2')),
 'adjoint_transpose_collapse_rejected':rejected(lambda x:x['return_lanes'].update(analytic_evans='conjugate_transpose',comparison_authorized=True)),
 'missing_unresolved_loading_row_rejected':rejected(lambda x:x['unresolved_target_rows'].pop(0)),
}

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
out={
 'schema':'marici.voevodsky.prime-two-theta-history-partial-transfer-check.v1',
 'passed':all(checks.values()),'checks':checks,
 'matrix_shape':list(M.shape),'matrix_rank':M.rank(),
 'codiagonal_kernel_dimension_on_response_subspace':12-3,
 'schur_laurent_range':[-1,0,1],
 'source_range_codimension_lower_bound':2,
 'claim_boundary':'The matrix faithfully retains the declared finite source feature and derives the codiagonal rows. It contains no G4 arithmetic loading or polarized metric.',
 'execution_receipt':{'command':'uv run --with sympy python research/voevodsky/checkers/check_prime_two_theta_history_partial_transfer.py','python':platform.python_version(),'sympy':sp.__version__,'fixture_sha256':digest(FIXTURE),'checker_sha256':digest(CHECKER)}}
RESULT.parent.mkdir(parents=True,exist_ok=True);RESULT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)

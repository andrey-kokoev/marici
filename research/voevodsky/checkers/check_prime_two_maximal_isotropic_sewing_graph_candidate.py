#!/usr/bin/env python3
"""Check maximal isotropy of the finite signed sewing graph."""
import copy, hashlib, json, platform
from pathlib import Path
import sympy as sp
ROOT=Path(__file__).resolve().parents[3]
FIXTURE=ROOT/'research/voevodsky/fixtures/prime_two_maximal_isotropic_sewing_graph_candidate.v1.json'
BOUNDARY=ROOT/'research/voevodsky/fixtures/prime_two_radial_boundary_form_candidate.v1.json'
SEWING=ROOT/'research/voevodsky/fixtures/prime_two_reciprocal_boundary_sewing_candidate.v1.json'
RESULT=ROOT/'research/voevodsky/results/prime_two_maximal_isotropic_sewing_graph_candidate.json';CHECKER=Path(__file__).resolve()
c=json.loads(FIXTURE.read_text());b=json.loads(BOUNDARY.read_text());s=json.loads(SEWING.read_text())
def mat(rows):return sp.Matrix([[sp.sympify(x) for x in row] for row in rows])
J=mat(b['green_matrix']);W=mat(s['sewing_matrix']);I=sp.eye(4);Z=sp.zeros(4)
Omega=(-J).row_join(Z).col_join(Z.row_join(J));G=I.col_join(W);H=sp.I*Omega
isotropic=sp.simplify(G.T*Omega*G)==sp.zeros(4)
hermitian_isotropic=sp.simplify(G.conjugate().T*H*G)==sp.zeros(4)
# A graph has dimension four in an eight-dimensional nondegenerate symplectic space.
maximal=isotropic and G.rank()==4 and Omega.rank()==8
# For real orthogonal involutive W, inverse conjugate transpose is W.
contragredient=W.inv().T

def validate(x):
 try:return (x['ambient_form']=='(-J) direct_sum J' and x['graph_map']=='column_stack(I,W)' and x['unresolved_comparison']['id']=='g4_maximal_isotropic_response_relation')
 except KeyError:return False
def rejected(f):
 x=copy.deepcopy(c);f(x);return not validate(x)
checks={'baseline_valid':validate(c),'ambient_form_nondegenerate':Omega.rank()==8,'graph_rank_four':G.rank()==4,
'graph_isotropic':isotropic,'graph_maximal_isotropic':maximal,'hermitian_polarization_isotropic':hermitian_isotropic,
'contragredient_equals_sewing':contragredient==W,
'wrong_ambient_sign_is_not_isotropic':sp.simplify(G.T*(J.row_join(Z).col_join(Z.row_join(J)))*G)!=sp.zeros(4),
'missing_g4_comparison_rejected':rejected(lambda x:x['unresolved_comparison'].update(id='constructed'))}
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
out={'schema':'marici.voevodsky.prime-two-maximal-isotropic-sewing-graph-check.v1','passed':all(checks.values()),'checks':checks,
'ambient_dimension':8,'graph_dimension':G.rank(),'claim_boundary':'Passing certifies maximal isotropy of the finite source sewing graph, not a G4 comparison.',
'execution_receipt':{'command':'uv run --with sympy python research/voevodsky/checkers/check_prime_two_maximal_isotropic_sewing_graph_candidate.py','python':platform.python_version(),'sympy':sp.__version__,'fixture_sha256':digest(FIXTURE),'boundary_fixture_sha256':digest(BOUNDARY),'sewing_fixture_sha256':digest(SEWING),'checker_sha256':digest(CHECKER)}}
RESULT.parent.mkdir(parents=True,exist_ok=True);RESULT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)
